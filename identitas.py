#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : identitas.py
Tujuan      : Menyimpan identitas cabang virtual dan membuat ID perangkat.
Pembuat     : Henry Moky (NIM 2409106070)
"""

nim = "2409106070"
nama = "Henry Moky"
kode_cabang = nim[-3:]  # 3 digit terakhir NIM


def buat_id_perangkat(jenis, nomor):
    """Membuat ID perangkat, contoh: ROUTER-070-01."""
    return f"{jenis.upper()}-{kode_cabang}-{int(nomor):02d}"


if __name__ == "__main__":
    print(f"{nama} ({nim}) - cabang {kode_cabang}")
    print(buat_id_perangkat("router", 1))
