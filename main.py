#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : main.py
Tujuan      : Menjalankan semua modul dan mencetak satu laporan cabang gabungan.
Pembuat     : Henry Moky (NIM 2409106070)
"""

import identitas
import ssh_modul
import snmp_modul
import netconf_modul
import telemetry_modul


class LaporanCabang:
    def __init__(self, nim, nama, kode_cabang):
        self.nim = nim
        self.nama = nama
        self.kode_cabang = kode_cabang

    def tampilkan_laporan(self, hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry):
        garis = "=" * 60
        print(f"\n{garis}\nLAPORAN CABANG - {self.nama} ({self.nim})")
        print(f"ID Perangkat : {identitas.buat_id_perangkat('router', 1)}\n{garis}")

        print(f"\n[1] SSH     : {hasil_ssh['status']}")
        for cmd, out in hasil_ssh["output"].items():
            print(f"    {cmd}: {out}")

        print(f"\n[2] SNMP    : {hasil_snmp['status']} (sysName = {hasil_snmp['sysName']})")

        print("\n[3] NETCONF : pesan edit-config dibuat")
        print(pesan_netconf)

        print("\n[4] TELEMETRY:")
        for nama_sampel, (cpu, status) in hasil_telemetry.items():
            print(f"    {nama_sampel}: {cpu}% -> {status}")
        print(garis)


def main():
    hasil_ssh = ssh_modul.cek_ssh()
    hasil_snmp = snmp_modul.cek_snmp()
    pesan = netconf_modul.buat_pesan_netconf()
    print(pesan)
    hasil_tele = telemetry_modul.klasifikasi_telemetry()

    laporan = LaporanCabang(identitas.nim, identitas.nama, identitas.kode_cabang)
    laporan.tampilkan_laporan(hasil_ssh, hasil_snmp, pesan, hasil_tele)


if __name__ == "__main__":
    main()
