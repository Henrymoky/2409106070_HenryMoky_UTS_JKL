#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : ssh_modul.py
Tujuan      : Login SSH ke VM/laptop memakai Paramiko dan menjalankan perintah diagnostik.
Pembuat     : Henry Moky (NIM 2409106070)
"""

import os
import paramiko

from identitas import kode_cabang

SSH_USER = f"admin_{kode_cabang}"
# Host & password diambil dari environment variable agar tidak masuk repo.
SSH_HOST = os.environ.get("SSH_HOST", "127.0.0.1")
SSH_PORT = int(os.environ.get("SSH_PORT", "22"))
SSH_PASSWORD = os.environ.get("SSH_PASSWORD", "")

PERINTAH = ["hostname", "uname -a", "uptime"]


def _koneksi():
    """Coba login password biasa; jika ditolak, coba keyboard-interactive."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER,
                       password=SSH_PASSWORD, timeout=10,
                       look_for_keys=False, allow_agent=False)
        return client
    except paramiko.AuthenticationException:
        client.close()

    # Fallback: keyboard-interactive (dipakai macOS)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    transport = paramiko.Transport((SSH_HOST, SSH_PORT))
    transport.start_client(timeout=10)
    transport.auth_interactive(
        SSH_USER, lambda title, instr, prompts: [SSH_PASSWORD for _ in prompts])
    client._transport = transport
    return client


def cek_ssh():
    """Login SSH, jalankan perintah diagnostik, cetak & kembalikan hasilnya."""
    hasil = {"status": "GAGAL", "output": {}}
    client = None
    try:
        client = _koneksi()
        for cmd in PERINTAH:
            _, stdout, _ = client.exec_command(cmd)
            out = stdout.read().decode().strip()
            hasil["output"][cmd] = out
            print(f"[SSH] $ {cmd}\n{out}")
        hasil["status"] = "BERHASIL"
    except Exception as e:
        hasil["output"]["error"] = str(e)
        print(f"[SSH] Koneksi gagal: {e}")
    finally:
        if client:
            client.close()
    return hasil


if __name__ == "__main__":
    cek_ssh()
