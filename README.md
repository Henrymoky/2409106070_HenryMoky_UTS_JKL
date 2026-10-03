# UTS Jaringan Komputer Lanjut - Integration Network with Python

Nama: Henry Moky | NIM: 2409106070 | Kelas B 2024 Informatika

## Struktur Project
```
.
├── .gitignore
├── README.md
├── requirements.txt
├── identitas.py        # identitas cabang & buat_id_perangkat()
├── ssh_modul.py        # cek_ssh()  - Paramiko
├── snmp_modul.py       # cek_snmp() - PySNMP (SNMPv2c)
├── netconf_modul.py    # buat_pesan_netconf() - XML edit-config
├── telemetry_modul.py  # klasifikasi_telemetry()
└── main.py             # integrasi + class LaporanCabang
```

## Cara Menjalankan
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

export SSH_HOST=<ip-vm>           # Windows: set SSH_HOST=<ip-vm>
export SSH_PASSWORD=<password>
export SNMP_HOST=<ip-vm>

python main.py
```
Jika SSH/SNMP tidak tersedia, program tetap berjalan dan melaporkan status GAGAL.

## Ringkasan Personalisasi
- Username SSH, community string SNMP, dan VLAN ID diturunkan dari 3 digit terakhir NIM.
- Sampel telemetry diturunkan dari digit-digit NIM dengan variasi KRITIS/WASPADA/NORMAL.
- Kredensial tidak disimpan di repository (dibaca dari environment variable).
