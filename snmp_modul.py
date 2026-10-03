#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : snmp_modul.py
Tujuan      : Mengambil sysName (OID 1.3.6.1.2.1.1.5.0) via SNMPv2c memakai PySNMP.
Pembuat     : Henry Moky (NIM 2409106070)
"""

import os

from identitas import kode_cabang

SNMP_HOST = os.environ.get("SNMP_HOST", "127.0.0.1")
SNMP_PORT = int(os.environ.get("SNMP_PORT", "161"))
COMMUNITY = f"comm_{kode_cabang}"
OID_SYSNAME = "1.3.6.1.2.1.1.5.0"


def _get_sysname():
    """Ambil sysName; mendukung PySNMP 7.x (asyncio) dan versi lama (sync)."""
    try:  # PySNMP 7.x
        import asyncio
        from pysnmp.hlapi.v3arch.asyncio import (
            SnmpEngine, CommunityData, UdpTransportTarget,
            ContextData, ObjectType, ObjectIdentity, get_cmd)

        async def _run():
            target = await UdpTransportTarget.create((SNMP_HOST, SNMP_PORT),
                                                     timeout=3, retries=1)
            return await get_cmd(
                SnmpEngine(), CommunityData(COMMUNITY, mpModel=1), target,
                ContextData(), ObjectType(ObjectIdentity(OID_SYSNAME)))

        err_ind, err_stat, err_idx, var_binds = asyncio.run(_run())
    except ImportError:  # PySNMP 4.x / 5.x / 6.x
        from pysnmp.hlapi import (
            getCmd, SnmpEngine, CommunityData, UdpTransportTarget,
            ContextData, ObjectType, ObjectIdentity)
        err_ind, err_stat, err_idx, var_binds = next(getCmd(
            SnmpEngine(), CommunityData(COMMUNITY, mpModel=1),
            UdpTransportTarget((SNMP_HOST, SNMP_PORT), timeout=3, retries=1),
            ContextData(), ObjectType(ObjectIdentity(OID_SYSNAME))))

    if err_ind:
        raise RuntimeError(str(err_ind))
    if err_stat:
        raise RuntimeError(err_stat.prettyPrint())
    return var_binds[0][1].prettyPrint()


def cek_snmp():
    """Ambil sysName, cetak & kembalikan hasilnya."""
    hasil = {"status": "GAGAL", "sysName": None}
    try:
        hasil["sysName"] = _get_sysname()
        hasil["status"] = "BERHASIL"
        print(f"[SNMP] sysName = {hasil['sysName']}")
    except Exception as e:
        hasil["sysName"] = f"error: {e}"
        print(f"[SNMP] Gagal mengambil sysName: {e}")
    return hasil


if __name__ == "__main__":
    cek_snmp()
