# PANDUAN INTEGRASI MCP & LOCAL TOOLKIT
## WORKSPACE SKRIPSI INFORMATIKA - UNIVERSITAS ALMUSLIM
**Document ID:** GUIDE-MCP-001  
**Version:** 1.0 (Full Dual-Engine Integration)  
**Status:** OFFICIAL WORKSPACE COMPANION  

---

## 1. PENDAHULUAN
Workspace ini dirancang dengan arsitektur **Dual-Engine (Hibrida)**:
1. **Engine A (MCP Servers)**: Protokol terbuka untuk menghubungkan AI Assistant dengan layanan eksternal (pencarian jurnal, draw.io interaktif, automasi Word langsung).
2. **Engine B (Python Toolkit Lokal)**: Skrip Python mandiri di dalam workspace yang siap dieksekusi tanpa ketergantungan jaringan (*fail-safe offline engine*).

---

## 2. REKOMENDASI & CARA MEMASANG MCP SERVERS

### 2.1 Athenaeum MCP — Riset Jurnal Ilmiah (Gratis, Tanpa API Key)
* **Kegunaan**: Mencari makalah ilmiah lintas database (Semantic Scholar, ArXiv, CrossRef), mengekstraksi metadata, mengecek jaringan sitasi, dan menemukan PDF Open Access.
* **Repositori**: [GitHub Athenaeum MCP](https://github.com/huuunleashed/athenaeum-mcp)
* **Konfigurasi Antigravity / Claude Desktop**:
  Tambahkan pada berkas konfigurasi MCP (`mcp_config.json`):
  ```json
  {
    "mcpServers": {
      "athenaeum": {
        "command": "npx",
        "args": ["-y", "athenaeum-mcp"]
      }
    }
  }
  ```

### 2.2 Zotero MCP — Pengelolaan Pustaka Lokal
* **Kegunaan**: Membaca koleksi PDF jurnal lokal yang telah diberi anotasi dan tag di Zotero, serta mengekspor sitasi berformat Harvard.
* **Repositori**: [GitHub Zotero MCP](https://github.com/drxaibi/zotero-mcp)
* **Kebutuhan**: Aplikasi Zotero terpasang dan API Key lokal aktif.

### 2.3 draw.io MCP — Diagram Interaktif (Gratis)
* **Kegunaan**: Merancang diagram UML, Flowchart, dan ERD dalam format `.drawio` yang dapat dibuka dan diedit kembali menggunakan software desktop Draw.io.
* **Repositori**: [GitHub Draw.io MCP](https://github.com/jgraph/drawio-mcp)
* **Konfigurasi**:
  ```json
  {
    "mcpServers": {
      "drawio": {
        "command": "npx",
        "args": ["-y", "@drawio/mcp-server"]
      }
    }
  }
  ```

### 2.4 Word MCP Server — Automasi Dokumen Microsoft Word
* **Kegunaan**: Berinteraksi langsung dengan aplikasi Microsoft Word yang sedang berjalan di Windows untuk formatting tingkat lanjut.
* **Repositori**: [GitHub Word MCP Server](https://github.com/HelloWorld-Open/word-mcp-server)
* **Kebutuhan**: Windows OS + Microsoft Word resmi terpasang.

---

## 3. ENGINE PYTHON LOKAL (BUILT-IN TOOLKIT)
Jika MCP belum terpasang atau sedang offline, Agent otomatis menggunakan skrip internal di folder `AI_program/scripts/`:

| Nama Skrip | Fungsi Utama | Perintah Eksekusi |
|---|---|---|
| [build_skripsi.py](file:///D:/ANTIGRAVITY-WORKSPACE/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/AI_program/scripts/build_skripsi.py) | Mengompilasi seluruh file di `drafts/*.md` ke dalam format Word baku Almuslim A4 (4-4-3-3) | `python AI_program/scripts/build_skripsi.py` |
| [table_styler.py](file:///D:/ANTIGRAVITY-WORKSPACE/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/AI_program/scripts/table_styler.py) | Menerapkan format tabel ilmiah terbuka 3 garis (open table) tanpa border vertikal | Digunakan otomatis oleh `build_skripsi.py` |
| [render_diagram.py](file:///D:/ANTIGRAVITY-WORKSPACE/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/AI_program/scripts/render_diagram.py) | Merender diagram Mermaid `.mmd` menjadi PNG 300 DPI monokrom menggunakan Playwright Edge | `python AI_program/scripts/render_diagram.py` |
| [qa_audit.py](file:///D:/ANTIGRAVITY-WORKSPACE/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/AI_program/scripts/qa_audit.py) | Menjalankan pre-flight audit untuk 10 aspek kualitas (placeholder, sitasi, gambar, tebal halaman) | `python AI_program/scripts/qa_audit.py` |

---

## 4. ALUR KERJA REKOMENDASI (BEST PRACTICE WORKFLOW)

```text
[1] MAHASISWA MENGISI PARAMETER
    Isi identitas penelitian di CONTEXT_SKRIPSI.txt.
       ↓
[2] RISET LITERATUR & PUSTAKA
    Gunakan Athenaeum MCP atau pencarian terverifikasi -> Catat di REFERENSI/index.md.
       ↓
[3] PENULISAN DRAF PER-BAB
    Tulis naskah bertahap di drafts/01_BAB_I.md s.d. drafts/05_BAB_V.md.
       ↓
[4] PEMBUATAN DIAGRAM & TABEL
    Tulis kode Mermaid di ASSETS/DIAGRAM/ -> Render ke PNG via render_diagram.py.
       ↓
[5] PRE-FLIGHT AUDIT
    Jalankan qa_audit.py untuk memastikan 0 placeholder dan sitasi cocok 100%.
       ↓
[6] KOMPILASI DOKUMEN WORD
    Jalankan build_skripsi.py -> Buka file Word di AI_program/working/ atau OUTPUT/.
```
