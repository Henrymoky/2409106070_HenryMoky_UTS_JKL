#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : telemetry_modul.py
Tujuan      : Mengklasifikasikan sampel data telemetry cpuUsage (in-uti).
Pembuat     : Henry Moky (NIM 2409106070)
"""

# Nilai diturunkan dari digit NIM 2409106070 (pasangan digit berurutan):
# 24, 91 (digit ke-4 & 5), 60 (digit ke-7 & 8), 70 (3 digit terakhir "070" -> 70)
data_telemetry = {
    "sampel_1": {"cpuUsage": 24},
    "sampel_2": {"cpuUsage": 60},
    "sampel_3": {"cpuUsage": 91},
    "sampel_4": {"cpuUsage": 70},
}


def klasifikasi_telemetry():
    """Klasifikasi tiap sampel: >80 KRITIS, 50-80 WASPADA, <50 NORMAL."""
    hasil = {}
    for nama_sampel, data in data_telemetry.items():
        cpu = data["cpuUsage"]
        if cpu > 80:
            status = "KRITIS"
        elif cpu >= 50:
            status = "WASPADA"
        else:
            status = "NORMAL"
        hasil[nama_sampel] = (cpu, status)
        print(f"[TELEMETRY] {nama_sampel}: cpuUsage={cpu}% -> {status}")
    return hasil


if __name__ == "__main__":
    klasifikasi_telemetry()
