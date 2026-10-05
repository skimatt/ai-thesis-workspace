# AI Thesis Workspace Template
### Lingkungan Kerja Penulisan Skripsi Akademik Informatika Terkontrol & Anti-Halusinasi

[![Academic Integrity](https://img.shields.io/badge/Academic%20Integrity-Permendikbudristek%2039%2F2021-0052cc.svg)](https://peraturan.go.id/id/permendikbudristek-no-39-tahun-2021)
[![University Guidelines](https://img.shields.io/badge/Standard-Universitas%20Almuslim-008080.svg)](#)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](#)
[![Document Standard](https://img.shields.io/badge/Document-A4%20%7C%204--4--3--3%20cm-success.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](#)

---

## 📌 Ringkasan

**AI Thesis Workspace Template** adalah repositori tata kelola dan lingkungan kerja komprehensif yang dirancang untuk mendampingi mahasiswa Program Studi Informatika dalam menyusun naskah skripsi akademik yang sah (*human-authored*).

Workspace ini menerapkan sistem kontrol bertingkat untuk memastikan interaksi dengan AI Coding Assistant tetap disiplin, presisi, berakar pada fakta empiris, dan sepenuhnya aman dari fabrikasi data maupun sitasi fiktif.

---

## 🛡️ 4 Pilar Anti-Halusinasi (Core Governance)

Seluruh proses komputasi dan penulisan terikat pada 4 prinsip mutlak:

1. **DO NOT INVENT** — Dilarang menciptakan fakta, teori, regulasi, atau klaim yang tidak berakar pada dokumen resmi.
2. **NO SOURCE, NO CLAIM** — Tidak ada klaim ilmiah atau sitasi tanpa sumber nyata berstatus `VERIFIED` di katalog pustaka.
3. **NO DATA, NO RESULT** — Dilarang mengarang responden, angka akurasi, matriks kebingungan (*confusion matrix*), atau hasil pengujian sebelum data riil diserahkan.
4. **NO APPROVAL, NO STRUCTURAL CHANGE** — Judul, rumusan masalah, batasan, dan metodologi yang telah dikunci pembimbing tidak boleh dirombak tanpa instruksi eksplisit.

---

## 🗂️ Struktur Direktori

```text
ai-thesis-workspace/
├── AGENTS.md                                   # Pusat kendali master governance & aturan 6-level
├── CONTEXT_SKRIPSI.txt                         # Berkas master data penelitian, metode, & status riset (LOCKED)
├── konteks.txt                                 # Pointer resmi ke CONTEXT_SKRIPSI.txt
├── CHEATSHEET_PROMPT.md                        # Repositori 25+ prompt siap pakai untuk 7 mode kerja & per-BAB
├── Chatpertama.txt                             # Prompt inisiasi sinkronisasi saat membuka sesi chat baru
│
├── AI_program/                                 # Direktori kerja internal agent
│   ├── README.md                               # Regulasi isolasi berkas kerja sementara
│   ├── scripts/                                # Skrip otomasi (pembuat dokumen, parsing, QC)
│   │   └── create_template_docx.py             # Generator template Word baku resmi Almuslim
│   └── working/                                # Draf kerja naskah
│       └── template_skripsi_almuslim.docx      # Master template Word baku (A4, 4-4-3-3 cm, Section Breaks)
│
├── ASSETS/                                     # Material visual penunjang naskah
│   ├── logo_umuslim.jpg                        # Logo resmi institusi untuk halaman judul
│   ├── DIAGRAM/                                # Berkas sumber diagram (.mmd, .puml, .svg, .png)
│   └── SCREENSHOOT/                            # Bukti tangkapan layar sistem riil dari mahasiswa
│
├── CONTOH_SKRIPSI/                             # Berkas pembanding format dan anatomi akademik
│   └── Contoh_skripsi.docx                     # Contoh skripsi metode WP (Arza Ulfa S.)
│
├── OUTPUT/                                     # Direktori khusus dokumen final yang lolos Quality Gate
│   └── README.md                               # Kriteria kelolosan dokumen siap cetak
│
├── REFERENSI/                                  # Repositori literatur ilmiah primer & sekunder
│   └── index.md                                # Master catalog pustaka terverifikasi (REF-001 dst.)
│
└── SOP/                                        # Standar Operasional Prosedur teknis
    ├── INDEX_SOP.md                            # Pemetaan direktori seluruh dokumen SOP
    ├── AI_AGENTS_SOP_PEDOMAN_SKRIPSI_ALMUSLIM.md # SOP Format, Layout, Margin, & Struktur BAB I–V
    ├── AI_AGENTS_WRITING_INTEGRITY_HUMAN_AUTHORED_SOP.md # SOP Integritas AI (Permendikbud 39/2021)
    ├── SOP_DIAGRAM.md                          # SOP Diagram-as-Code monokrom v2.0
    └── SOP_REFERENSI.md                        # SOP Tata kelola siklus hidup referensi
```

---

## ⚡ Alur Cepat Memulai (Quick Start)

### 1. Inisiasi Sesi Chat Pertama
Saat memulai percakapan baru dengan AI Assistant (Antigravity, Cursor, Claude, atau ChatGPT), salin dan kirim isi berkas:
👉 **[Chatpertama.txt](Chatpertama.txt)**  
*Agent akan menjalankan audit pasif dan mengonfirmasi kesiapan lingkungan kerja tanpa mengubah file.*

### 2. Definisikan Data Penelitian Anda
Buka dan lengkapi atribut penelitian pada:
👉 **[CONTEXT_SKRIPSI.txt](CONTEXT_SKRIPSI.txt)**  
Isi nama, judul, rumusan masalah, metode, dan objek penelitian. Bagian yang belum ditentukan akan tetap berstatus `[NEEDS USER INPUT]`.

### 3. Eksekusi Tugas Menggunakan Prompt Siap Pakai
Buka katalog prompt pada:
👉 **[CHEATSHEET_PROMPT.md](CHEATSHEET_PROMPT.md)**  
Pilih prompt sesuai mode kerja yang dibutuhkan (penulisan BAB I–V, diagram Mermaid, atau audit kualitas).

---

## 🔄 7 Mode Kerja AI Agent

| Mode | Fokus Pekerjaan | Acuan Utama |
|---|---|---|
| **`AUDIT`** | Memeriksa kelengkapan berkas, istilah, dan format naskah | [AGENTS.md](AGENTS.md) |
| **`RESEARCH`** | Mencari dan memvalidasi literatur jurnal ilmiah | [REFERENSI/index.md](REFERENSI/index.md) & [SOP_REFERENSI.md](SOP/SOP_REFERENSI.md) |
| **`WRITING`** | Menyusun draf per-subbab dengan alur deduktif/induktif formal | [SOP_PENULISAN](SOP/AI_AGENTS_SOP_PEDOMAN_SKRIPSI_ALMUSLIM.md) |
| **`DIAGRAM`** | Merancang ERD, Flowchart, dan UML monokrom (*Diagram-as-Code*) | [SOP/SOP_DIAGRAM.md](SOP/SOP_DIAGRAM.md) |
| **`DOCUMENT`** | Menata tata letak naskah ke template Word resmi | [template_skripsi_almuslim.docx](AI_program/working/template_skripsi_almuslim.docx) |
| **`QA`** | Audit 10 aspek kualitas, anti-slop, dan deteksi tag tertinggal | [AGENTS.md](AGENTS.md) (Bagian 17) |
| **`FINALIZATION`** | Ekspor naskah final siap serah ke direktori rilis | [OUTPUT/](OUTPUT/) |

---

## 📐 Standar Dokumen & Diagram

* **Tipografi & Margin**: Kertas A4 (80 gram), Margin Kiri 4 cm, Atas 4 cm, Kanan 3 cm, Bawah 3 cm. Font *Times New Roman* 12 pt, Spasi 2.0 (Double), Justified.
* **Ketebalan Halaman**: Minimal **80 halaman (lembar)** naskah utama skripsi (BAB I s.d. BAB V), maksimal fleksibel sesuai tingkat kerumitan sistem dan data.
* **Sistem Penomoran Halaman**:
  - Bagian Awal: Angka Romawi kecil (`i, ii, iii...`) di tengah bawah.
  - Bagian Utama: Angka Arab (`1, 2, 3...`) di kanan atas, kecuali halaman pertama setiap BAB berada di tengah bawah.
* **Diagram-as-Code Monokrom**: Seluruh diagram teknis diprogram dengan **Mermaid.js**, **PlantUML**, atau **Draw.io XML** dengan garis hitam tipis presisi, latar putih bersih, tanpa bayangan (*shadow*), dan bebas warna dekoratif.

---

## 📜 Kepatuhan Regulasi Akademik
Template workspace ini dirancang mematuhi:
- **Permendikbudristek No. 39 Tahun 2021** tentang Integritas Akademik dalam Menghasilkan Karya Ilmiah.
- **Pedoman Penulisan Skripsi Program Sarjana (S1)** Fakultas Ilmu Komputer, Universitas Almuslim.
- **Pedoman Umum Ejaan Bahasa Indonesia (PUEBI) / EYD Edisi V**.

---

<p align="center">
  <i>Dikembangkan untuk mewujudkan penelitian akademik yang berintegritas, terstruktur, dan akuntabel.</i>
</p>
