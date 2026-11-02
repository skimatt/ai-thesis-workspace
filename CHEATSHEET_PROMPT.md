# CHEATSHEET MASTER PROMPT SKRIPSI INFORMATIKA
## REPOSITORI PINTASAN INTERAKSI AI AGENT (UNIVERSAL INFORMATIKA ENGINE)
### FAKULTAS ILMU KOMPUTER — UNIVERSITAS ALMUSLIM

Dokumen ini adalah repositori *prompt* siap pakai (*copy-paste*) untuk memandu AI Agent di workspace ini. Seluruh *prompt* dirancang **100% GENERAL & UNIVERSAL**, berlandaskan pada **Hierarki Aturan 6-Level**, **Pedoman Resmi 6 BAB FIKOM Universitas Almuslim**, serta **4 Pilar Anti-Halusinasi** (*Do Not Invent, No Source No Claim, No Data No Result, No Approval No Structural Change*).

> [!IMPORTANT]
> **ACUAN TUNGGAL PARAMETER PENELITIAN:**  
> Seluruh prompt di bawah ini secara otomatis merujuk pada data judul, nama, objek riset, kriteria, dan metode komputasi yang telah Anda kunci di dalam:  
> 👉 **[CONTEXT_SKRIPSI.txt](file:///D:/ANTIGRAVITY-WORKSPACE/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/CONTEXT_SKRIPSI.txt)**

---

## 📌 FORMULA BAKU PROMPT AGENT (THE 5-ELEMENT FORMULA)
Untuk mendapatkan hasil penulisan akademik yang presisi, gunakan formula 5 elemen ini:
```text
[MODE KERJA] + [TARGET BAB / SUBBAB] + [ACUAN CONTEXT_SKRIPSI.txt & REFERENSI] + [BATASAN FORMAT] + [OUTPUT YANG DIHARAPKAN]
```
*Contoh:*  
`[Agent mode WRITING] [Susun subbab 1.1 Latar Belakang Masalah] [Berdasarkan masalah objek riset di CONTEXT_SKRIPSI.txt dan sitasi REF-001] [Terapkan EYD V, alur deduktif piramida terbalik, tanpa AI slop] [Tampilkan dalam 4-5 paragraf lengkap].`

---

## 1. INISIASI & PENGUNCIAN KEPUTUSAN RISET

### 1.1 Inisiasi / Pembaruan Metadata Penelitian
> **Prompt:**  
> `"Agent, saya ingin memperbarui CONTEXT_SKRIPSI.txt dengan identitas penelitian saya:  
> - Nama / NPM: [Nama Anda] / [NPM Anda]  
> - Judul Skripsi: [Judul Skripsi Lengkap]  
> - Bidang / Peminatan: [SPK / RPL / Kecerdasan Buatan / Jaringan / Citra Digital]  
> - Objek & Lokasi Riset: [Nama Instansi / Perusahaan & Alamat]  
> - Metode Komputasi / Algoritma: [Sebutkan metode, misal: WP / TOPSIS / AHP / SAW / KNN / CNN]  
> - Arsitektur Teknologi: [Bahasa Pemrograman, Framework, DBMS]  
> - Dosen Pembimbing: [Pembimbing I] & [Pembimbing II]  
> Masukkan data ini ke CONTEXT_SKRIPSI.txt dan konfirmasi bahwa status substansi ini sudah LOCKED."`

### 1.2 Mengunci Catatan Arahan / Revisi Dosen Pembimbing
> **Prompt:**  
> `"Agent, Dosen Pembimbing memberikan catatan arahan revisi berikut:  
> '[Salin catatan dosen di sini, misal: Batasi periode data tahun 2024–2025 dan tambahkan pengujian akurasi]'  
> Tolong catat arahan ini pada Bagian 8 di CONTEXT_SKRIPSI.txt. Jangan ubah keputusan lain yang telah disetujui."`

---

## 2. MODE `RESEARCH` (Pustaka, Jurnal, & Verifikasi Sitasi)
*Prinsip: No Source, No Claim. Status: DISCOVERED → DOWNLOADED → READ → VERIFIED → USED.*

### 2.1 Mencari Literatur Jurnal Terakreditasi
> **Prompt:**  
> `"Agent mode RESEARCH: Cari 3 artikel jurnal ilmiah terakreditasi nasional (SINTA) atau internasional bereputasi yang membahas penerapan [Metode di CONTEXT_SKRIPSI.txt] pada kasus yang relevan dengan topik saya.  
> Catat ke REFERENSI/index.md dengan ID REF-001, REF-002, dst. Lengkapi judul, penulis, tahun, dan DOI/URL resmi penerbit."`

### 2.2 Verifikasi Naskah Jurnal & Ekstraksi Teori
> **Prompt:**  
> `"Agent mode RESEARCH: Saya telah meletakkan berkas jurnal di folder REFERENSI/[nama_file].pdf.  
> Tolong baca naskah tersebut, ubah statusnya di REFERENSI/index.md menjadi READ lalu VERIFIED, dan ekstrak poin kuncinya:  
> 1. Masalah yang diselesaikan oleh peneliti terdahulu.  
> 2. Variabel/kriteria dan formula matematis yang digunakan.  
> 3. Hasil pengujian dan keterbatasan penelitian tersebut."`

---

## 3. MODE `WRITING` (Penyusunan Draf 6 BAB Human-Authored)

### 3.1 BAGIAN AWAL (Front Matter)
* **Menyusun Abstrak Standar Almuslim:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun draf 00_BAGIAN_AWAL.md untuk ABSTRAK (Bahasa Indonesia, 1 paragraf, 150-250 kata, spasi 1.0) dan ABSTRACT (Bahasa Inggris italic).  
  > Struktur alur: Latar belakang masalah ringkas → Tujuan penelitian → Metode komputasi & teknologi sistem → Hasil implementasi dan validasi pengujian → Kesimpulan utama.  
  > Sertakan 3–5 Kata Kunci spesifik di bawahnya."`

---

### 3.2 BAB I — PENDAHULUAN
* **Menyusun Latar Belakang Masalah (Pola Deduktif Piramida Terbalik):**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun draf drafts/01_BAB_I.md subbab 1.1 Latar Belakang Masalah (4-5 paragraf mendalam):  
  > - Paragraf 1: Kondisi ideal pentingnya teknologi informasi dan sistem terkomputasi.  
  > - Paragraf 2: Gambaran objek riset dan permasalahan nyata di lapangan sesuai CONTEXT_SKRIPSI.txt.  
  > - Paragraf 3: Dampak negatif dan inefisiensi jika masalah tersebut dibiarkan tanpa sistem.  
  > - Paragraf 4: Alasan ilmiah pemilihan [Metode di CONTEXT_SKRIPSI.txt] diperkuat sitasi dari REFERENSI/index.md.  
  > - Paragraf 5: Pernyataan tujuan penulisan skripsi ini.  
  > Terapkan kaidah EYD V, bahasa formal manusia, dan hindari kata klise (AI slop)."`

* **Menyusun Rumusan, Batasan, Tujuan, dan Sistematika Penulisan:**
  > **Prompt:**  
  > `"Agent mode WRITING: Berdasarkan parameter di CONTEXT_SKRIPSI.txt, lengkapi drafts/01_BAB_I.md untuk:  
  > 1. Subbab 1.2 Rumusan Masalah (3 butir pertanyaan penelitian terukur).  
  > 2. Subbab 1.3 Batasan Masalah (3 butir batasan data, metode, dan platform).  
  > 3. Subbab 1.4 Tujuan Penelitian (sinkron 1:1 dengan rumusan masalah).  
  > 4. Subbab 1.5 Manfaat Penelitian (praktis, akademis, dan bagi penulis).  
  > 5. Subbab 1.6 Metodologi Penelitian (observasi, wawancara, studi pustaka).  
  > 6. Subbab 1.7 Sistematika Penulisan (ringkasan alur BAB I sampai BAB VI)."`

---

### 3.3 BAB II — LANDASAN TEORI
* **Menyusun Tabel Matriks Penelitian Terdahulu (State-of-the-Art):**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 2.5 Penelitian Terkait pada drafts/02_BAB_II.md dalam bentuk narasi komparatif dan Tabel 2.1 Matriks Perbandingan Penelitian Terdahulu (minimal 3 artikel terverifikasi di REFERENSI/index.md).  
  > Kolom tabel: No, Peneliti & Tahun, Judul Penelitian, Metode, Hasil Utama, dan Posisi/Kebaruan Penelitian Ini."`

* **Menjelaskan Teori Metode Komputasi / Algoritma dengan Formula Matematis:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 2.2 Metode Komputasi pada drafts/02_BAB_II.md. Jelaskan definisi formal metode, tahapan perhitungannya langkah demi langkah, dan tuliskan rumus matematisnya lengkap dengan keterangan notasi variabel. Sitasi sumber buku/jurnal primer terverifikasi."`

---

### 3.4 BAB III — ANALISA DAN PERANCANGAN SISTEM
* **Menyusun Analisa Sistem Berjalan vs Sistem Diusulkan:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 3.1 Analisa Sistem pada drafts/03_BAB_III.md:  
  > - 3.1.1 Analisa Sistem Lama: Uraikan kelemahan alur proses bisnis saat ini.  
  > - 3.1.2 Analisa Sistem Baru: Jelaskan solusi proses bisnis dengan integrasi sistem.  
  > - 3.1.3 Analisa Kebutuhan: Rincikan kebutuhan fungsional aktor dan kebutuhan non-fungsional (hardware, software, output)."`

* **Menyusun Tabel Kriteria, Bobot, dan Skala Penilaian:**
  > **Prompt:**  
  > `"Agent mode WRITING: Berdasarkan Bagian 5 CONTEXT_SKRIPSI.txt, susun subbab 3.2 Penentuan Kriteria dan Bobot pada drafts/03_BAB_III.md lengkap dengan Tabel 3.1 (Kode, Nama Kriteria, Tipe Atribut Benefit/Cost, Bobot Awal, dan Bobot Normalisasi) serta tabel konversi nilai skala parameter."`

* **Menyusun Kamus Data Struktur Tabel Basis Data:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 3.4.2 Desain Struktur File Database pada drafts/03_BAB_III.md. Sajikan tabel kamus data untuk seluruh tabel sistem (Field, Tipe Data, Panjang Karakter, dan Keterangan Kunci PK/FK) yang sinkron dengan ERD."`

---

### 3.5 BAB IV — IMPLEMENTASI SISTEM
> [!IMPORTANT]
> **Prinsip: No Data, No Result.** Pasang tangkapan layar sistem riil Anda di folder `ASSETS/SCREENSHOOT/` sebelum meminta penulisan BAB IV!

* **Mendeskripsikan Tangkapan Layar Antarmuka Sistem Nyata:**
  > **Prompt:**  
  > `"Agent mode WRITING: Saya telah menempatkan screenshot sistem asli di folder ASSETS/SCREENSHOOT/.  
  > Tolong susun subbab 4.3 Implementasi Antarmuka Pengguna pada drafts/04_BAB_IV.md. Jelaskan fungsi form login, dashboard, input master kriteria, input data alternatif, dan laporan hasil keputusan. Hubungkan secara kontekstual dengan nomor Gambar 4.1 dst."`

* **Menjelaskan Cuplikan Kode Program Modul Algoritma:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 4.2 Implementasi Modul Komputasi pada drafts/04_BAB_IV.md. Tampilkan cuplikan fungsi kode program inti algoritma (normalisasi bobot dan kalkulasi nilai preferensi) beserta penjelasan logika perhitungannya."`

---

### 3.6 BAB V — PENGUJIAN DAN PEMBAHASAN
* **Menyusun Pengujian Perhitungan Matematis Manual vs Sistem:**
  > **Prompt:**  
  > `"Agent mode WRITING: Berikut adalah data sampel alternatif faktual dari objek riset:  
  > [Tempelkan data alternatif dan nilai kriteria di sini]  
  > Tolong susun subbab 5.1 Pengujian Model Komputasi pada drafts/05_BAB_V.md:  
  > 1. Hitung tahapan algoritma secara matematis manual sesuai rumus di BAB II.  
  > 2. Sajikan tabel perbandingan hasil perhitungan manual versus sistem untuk membuktikan akurasi 100% konsisten."`

* **Menyusun Tabel Pengujian Black Box Testing:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 5.2 Pengujian Fungsional Sistem pada drafts/05_BAB_V.md dalam bentuk Tabel 5.1 Pengujian Black Box Testing. Cantumkan minimal 8 skenario pengujian fungsionalitas (login, validasi input, simpan data, eksekusi algoritma, cetak laporan) dengan kolom: No, Komponen yang Diuji, Butir Uji, Skenario, Hasil Diharapkan, Hasil Pengamatan, Kesimpulan (Valid)."`

* **Menyusun Pembahasan Hasil Penelitian:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 5.3 Pembahasan Hasil Penelitian pada drafts/05_BAB_V.md. Ulas secara kritis interpretasi hasil perangkingan keputusan, kesesuaian rekomendasi sistem dengan kebutuhan instansi, kelebihan sistem, dan keterbatasannya."`

---

### 3.7 BAB VI — PENUTUP
* **Menyusun Kesimpulan & Saran yang Sinkron:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun drafts/06_BAB_VI.md:  
  > 1. 6.1 Kesimpulan: Jawab secara lugas rumusan masalah dan tujuan di BAB I berdasarkan bukti empiris pengujian di BAB V.  
  > 2. 6.2 Saran: Ajukan 2 butir saran teknis pengembangan perangkat lunak ke depan dan 1 butir saran operasional bagi instansi."`

---

### 3.8 BAGIAN AKHIR (Daftar Pustaka & Riwayat Hidup)
* **Menyusun Daftar Pustaka Harvard & Biodata:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun drafts/07_DAFTAR_PUSTAKA.md berdasarkan seluruh literatur yang berstatus VERIFIED di REFERENSI/index.md (format Harvard alfabetis tanpa nomor urut). Dan perbarui drafts/08_DAFTAR_RIWAYAT_HIDUP.md dengan identitas mahasiswa di CONTEXT_SKRIPSI.txt."`

---

## 4. MODE `DIAGRAM` (Standar Visual Galeri Resmi & Multi-Tooling 300 DPI)
*Acuan Visual Baku: Seluruh rancangan diagram WAJIB mencocokkan bentuk dan gayanya dengan galeri contoh di `ASSETS/DIAGRAM/STANDARD_EXAMPLES/`.*

### 4.1 Merancang Use Case Diagram (Persis Standar Gambar 1)
* **Acuan:** `ASSETS/DIAGRAM/STANDARD_EXAMPLES/01_contoh_use_case_diagram.png`
* **Format:** Subsystem boundary persegi panjang bertuliskan `«subsystem» [Nama_Sistem]`, aktor stick-figure di luar kotak (kiri & kanan), elips use case horizontal tersusun vertikal, garis asosiasi solid lurus.
> **Prompt:**  
> `"Agent mode DIAGRAM: Rancang Use Case Diagram monokrom untuk sistem saya sesuai acuan 01_contoh_use_case_diagram.png.  
> Gunakan PlantUML atau Python Generator:  
> - Boundary box bertuliskan «subsystem» [Nama Sistem di CONTEXT_SKRIPSI.txt].  
> - Aktor primer [Nama Aktor 1] di sisi kiri dan aktor sekunder [Nama Aktor 2] di sisi kanan.  
> - 6 use case fungsional riil sistem dalam bentuk elips horizontal.  
> - Simpan kode di ASSETS/DIAGRAM/use_case_sistem.puml dan render PNG 300 DPI ke ASSETS/DIAGRAM/use_case_sistem.png."`

### 4.2 Merancang ERD Notasi Peter Chen (Persis Standar Gambar 2 & 3)
* **Acuan:** `ASSETS/DIAGRAM/STANDARD_EXAMPLES/02_simbol_erd_chen_notation.png` & `03_contoh_erd_akademik.png`
* **Format:** Entitas persegi panjang, relasi belah ketupat (*diamond*), atribut elips melingkari entitas dengan tanda bintang/garis bawah untuk Primary Key (`*id_pelamar`), label kardinalitas `1` dan `N` (atau `M`) pada garis.
> **Prompt:**  
> `"Agent mode DIAGRAM: Buatkan rancangan ERD konseptual notasi Peter Chen untuk database sistem saya persis seperti standar 02_simbol_erd_chen_notation.png dan 03_contoh_erd_akademik.png.  
> Gunakan script AI_program/scripts/render_academic_diagrams.py atau Draw.io XML:  
> - Cantumkan entitas: [sebutkan entitas, misal: mahasiswa, dosen, kriteria, alternatif].  
> - Hubungkan dengan relasi belah ketupat dan kardinalitas (1:N, M:N).  
> - Pasang seluruh atribut elips beserta Primary Key (*).  
> - Simpan hasil render 300 DPI monokrom di ASSETS/DIAGRAM/erd_chen_sistem.png."`

### 4.3 Merancang DFD Level 0 / Diagram Konteks (Persis Standar Gambar 4)
* **Acuan:** `ASSETS/DIAGRAM/STANDARD_EXAMPLES/04_contoh_dfd_level_0_konteks.png`
* **Format:** Tepat 1 proses lingkaran pusat dengan nama sistem, entitas eksternal kotak persegi panjang huruf kapital di sekeliling proses, panah aliran data bolak-balik dengan teks label dokumen/informasi yang jelas.
> **Prompt:**  
> `"Agent mode DIAGRAM: Buatkan Diagram Konteks (DFD Level 0) sistem saya persis mengikuti format 04_contoh_dfd_level_0_konteks.png.  
> Gunakan Mermaid flowchart atau script render_academic_diagrams.py:  
> - Proses pusat berupa lingkaran berisi nama sistem [Nama Sistem di CONTEXT_SKRIPSI.txt].  
> - Entitas eksternal: [Sebutkan entitas luar, misal: ADMIN, PIMPINAN, PENGGUNA].  
> - Rincikan seluruh panah data input dan info output yang mengalir di antara entitas dan sistem.  
> - Simpan hasil render monokrom 300 DPI di ASSETS/DIAGRAM/dfd_konteks.png."`

### 4.4 Merancang Flowchart Algoritma ANSI/ISO (Mermaid.js)
> **Prompt:**  
> `"Agent mode DIAGRAM: Buatkan kode Mermaid.js monokrom untuk Flowchart tahapan [Metode di CONTEXT_SKRIPSI.txt] (mulai dari input data, normalisasi, perhitungan vektor, hingga perangkingan). Simpan di ASSETS/DIAGRAM/flowchart_metode.mmd, lalu render ke PNG 300 DPI menggunakan render_diagram.py."`

### 4.5 Menggunakan Plugin Draw.io untuk Desain Interaktif (.drawio)
> **Prompt:**  
> `"Agent mode DIAGRAM: Buatkan berkas rancangan Draw.io XML (.drawio) monokrom untuk [jenis diagram] agar dapat saya buka dan edit di aplikasi Draw.io Desktop. Simpan di ASSETS/DIAGRAM/[nama_diagram].drawio dan ekspor pratinjau PNG-nya."`

---

## 5. PINTASAN OTOMASI TOOLKIT LOKAL

### 5.1 Menjalankan Kompilasi Master Word Otomatis
> **Prompt:**  
> `"Agent, jalankan skrip kompilasi AI_program/scripts/build_skripsi.py untuk menyatukan seluruh draf di drafts/*.md ke dalam master template Word Almuslim. Pastikan margin 4-4-3-3, Times New Roman, dan penomoran halaman Romawi/Arab terkunci sempurna."`

### 5.2 Menjalankan Pre-Flight Quality Gate Audit
> **Prompt:**  
> `"Agent, jalankan AI_program/scripts/qa_audit.py untuk memeriksa draf skripsi saya. Laporkan apakah ada placeholder tertinggal, validitas sitasi Harvard, fisik file gambar, dan estimasi halaman menuju target minimal 80 halaman."`

---

## 6. MODE `FINALIZATION` (Rilis Naskah Siap Cetak ke OUTPUT/)

> **Prompt:**  
> `"Agent mode FINALIZATION: Seluruh draf naskah BAB I s.d. BAB VI, Bagian Awal, dan Bagian Akhir telah lolos Quality Gate.  
> Ekspor dokumen final ke folder OUTPUT/ dengan format penamaan resmi:  
> SKRIPSI_FINAL_[NAMA_MAHASISWA]_[TAHUN].docx  
> Pastikan tidak ada file sementara yang tertinggal di folder OUTPUT/."`

---

## 💡 ATURAN EMAS PENGGUNAAN PROMPT (*GOLDEN RULES*)
1. **Pola Bertahap per-Subbab**: Jangan meminta *"Tuliskan seluruh skripsi dari BAB I sampai BAB VI sekaligus"*. AI akan memberikan teks ringkas yang dangkal. Kerjakan **subbab per subbab** agar naskah mendalam, padat fakta, dan mudah mencapai syarat minimal **80 halaman**.
2. **Konteks sebagai Jangkar**: Selalu pastikan parameter objek riset, kriteria, dan data di `CONTEXT_SKRIPSI.txt` sudah lengkap sebelum menulis bab teknis (BAB III, IV, dan V).
3. **Koreksi Langsung**: Jika agen menghasilkan kalimat yang terdengar klise atau hiperbolis, instruksikan: *"Ubah paragraf tersebut menjadi lebih padat, ilmiah, dan berikan data faktual."*
