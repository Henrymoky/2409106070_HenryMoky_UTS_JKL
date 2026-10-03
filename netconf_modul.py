#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : netconf_modul.py
Tujuan      : Membangun pesan NETCONF <rpc><edit-config> untuk membuat VLAN.
Pembuat     : Henry Moky (NIM 2409106070)
"""

import xml.etree.ElementTree as ET

from identitas import kode_cabang

NS_BASE = "urn:ietf:params:xml:ns:netconf:base:1.0"
NS_VLAN = "http://www.huawei.com/netconf/vrp/huawei-vlan"

# Transport layer: NETCONF berjalan di atas SSH (port 830), bukan dibangun
# di dalam string XML ini.


def buat_pesan_netconf():
    """Bangun XML <rpc><edit-config> pembuatan VLAN ID = kode_cabang."""
    vlan_id = int(kode_cabang)  # "070" -> 70

    # === MESSAGES LAYER: pembungkus <rpc> dengan message-id ===
    rpc = ET.Element("rpc", {"xmlns": NS_BASE, "message-id": "101"})

    # === OPERATIONS LAYER: operasi <edit-config> pada datastore running ===
    edit = ET.SubElement(rpc, "edit-config")
    target = ET.SubElement(edit, "target")
    ET.SubElement(target, "running")

    # === CONTENT LAYER: data konfigurasi VLAN yang dikirim ===
    config = ET.SubElement(edit, "config")
    vlan = ET.SubElement(config, "vlan", {"xmlns": NS_VLAN})
    vlans = ET.SubElement(vlan, "vlans")
    item = ET.SubElement(vlans, "vlan", {"operation": "create"})
    ET.SubElement(item, "vlanId").text = str(vlan_id)
    ET.SubElement(item, "vlanName").text = f"VLAN_{vlan_id}"

    ET.indent(rpc)  # Python 3.9+
    return ET.tostring(rpc, encoding="unicode")


if __name__ == "__main__":
    print(buat_pesan_netconf())
