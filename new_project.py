"""
NEW PROJECT INITIALIZER - AI THESIS WORKSPACE
Universitas Almuslim - Fakultas Ilmu Komputer - Program Studi Informatika

Skrip 1-Klik untuk menginisiasi proyek skripsi mahasiswa baru:
1. Memvalidasi environment Python & modul yang diperlukan.
2. Mengonfigurasi metadata mahasiswa pada config/thesis.yaml.
3. Menyiapkan struktur workspace (builds, reports, previews) dan direktori referensi.
4. Menjalankan audit perdana untuk memastikan kesiapan sistem.
"""

import os
import sys
import yaml
import shutil

def print_banner():
    print("=" * 72)
    print("    INISIALISASI PROYEK SKRIPSI BARU - FAKULTAS ILMU KOMPUTER")
    print("                      UNIVERSITAS ALMUSLIM                    ")
    print("=" * 72)

def check_dependencies():
    print("\n[*] Memeriksa modul Python yang diperlukan...")
    required = {
        "docx": "python-docx",
        "yaml": "pyyaml",
        "fitz": "PyMuPDF",
        "PIL": "Pillow"
    }
    missing = []
    for mod, pkg in required.items():
        try:
            __import__(mod)
            print(f"    [+] Modul '{pkg}' terinstal.")
        except ImportError:
            print(f"    [-] Modul '{pkg}' BELUM terinstal.")
            missing.append(pkg)

    if missing:
        print(f"\n[!] PERINGATAN: Pasang modul yang kurang dengan perintah:")
        print(f"    pip install {' '.join(missing)}")
    else:
        print("    [+] Seluruh dependensi utama siap digunakan!")

def init_workspace():
    print("\n[*] Menyiapkan direktori workspace dan taksonomi referensi...")
    dirs = [
        "workspace/builds",
        "workspace/reports",
        "workspace/previews",
        "REFERENSI/pdf/belum_diverifikasi",
        "REFERENSI/pdf/jurnal",
        "REFERENSI/pdf/buku",
        "REFERENSI/pdf/prosiding",
        "REFERENSI/pdf/laporan_resmi",
        "REFERENSI/pdf/skripsi_tesis",
        "ASSETS/DIAGRAM/GENERATED_TESTS",
        "ASSETS/SCREENSHOOT",
        "AI_program/working",
        "AI_program/logs",
        "OUTPUT"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("    [+] Seluruh folder staging dan taksonomi berhasil disiapkan.")

def setup_thesis_config(interactive=False):
    config_path = "config/thesis.yaml"
    if not os.path.exists(config_path):
        print(f"[-] Berkas {config_path} tidak ditemukan.")
        return

    with open(config_path, "r", encoding="utf-8") as f:
        conf = yaml.safe_load(f)

    if interactive:
        print("\n[*] Silakan masukkan metadata skripsi mahasiswa baru:")
        nama = input(f"    Nama Mahasiswa [{conf.get('student', {}).get('name', '')}]: ").strip()
        nim = input(f"    NIM Mahasiswa  [{conf.get('student', {}).get('nim', '')}]: ").strip()
        judul = input(f"    Judul Skripsi  [{conf.get('title', {}).get('main', '')}]: ").strip()

        if nama:
            conf["student"]["name"] = nama
        if nim:
            conf["student"]["nim"] = nim
        if judul:
            conf["title"]["main"] = judul

        with open(config_path, "w", encoding="utf-8") as f:
            yaml.dump(conf, f, allow_unicode=True, sort_keys=False)
        print(f"    [+] Metadata skripsi berhasil diperbarui di {config_path}!")
    else:
        print(f"    [+] Menggunakan konfigurasi yang ada di {config_path}.")

def main():
    print_banner()
    check_dependencies()
    init_workspace()
    
    # Jalankan interaktif jika argumen --interactive diberikan
    is_interactive = "--interactive" in sys.argv
    setup_thesis_config(interactive=is_interactive)

    print("\n" + "=" * 72)
    print("    PROYEK SKRIPSI BERHASIL DIINISIASI DAN SIAP DIGUNAKAN!   ")
    print("=" * 72)
    print("\nLangkah selanjutnya:")
    print("1. Salin prompt pada 'Chatpertama.txt' ke jendela chat agent baru.")
    print("2. Masukkan draf atau instruksi penulisan per BAB sesuai 'CHEATSHEET_PROMPT.md'.")
    print("3. Kompilasi naskah dengan menjalankan: python AI_program/scripts/build_skripsi.py")
    print("4. Jalankan audit mutu dengan: python AI_program/scripts/qa_audit.py\n")

if __name__ == "__main__":
    main()
