# CHEATSHEET MASTER PROMPT SKRIPSI INFORMATIKA
## PANDUAN PINTASAN INTERAKSI AI AGENT UNTUK MAHASISWA & PENELITI

Dokumen ini adalah repositori *prompt* siap pakai (*copy-paste*) untuk mengarahkan AI Agent di workspace ini. Seluruh *prompt* dirancang presisi mematuhi **Hierarki Aturan 6-Level**, **Pedoman Universitas Almuslim**, serta **4 Pilar Anti-Halusinasi** (*Do Not Invent, No Source No Claim, No Data No Result, No Approval No Structural Change*).

---

## 📌 FORMULA BAKU PROMPT AGENT (THE 5-ELEMENT FORMULA)
Untuk hasil terbaik, susun instruksi Anda dengan formula 5 elemen ini:
```text
[MODE KERJA] + [TARGET SUBBAB/TUGAS] + [ACUAN KONTEKS/SUMBER] + [BATASAN & ATURAN] + [OUTPUT YANG DIHARAPKAN]
```
*Contoh:*  
`[Agent mode WRITING] [Susun subbab 1.1 Latar Belakang] [Berdasarkan poin masalah di CONTEXT_SKRIPSI.txt dan sitasi REF-001] [Terapkan EYD V, alur deduktif, tanpa AI slop] [Tampilkan dalam 4 paragraf lengkap].`

---

## 1. INISIASI & PENGUNCIAN KEPUTUSAN RISET

### 1.1 Inisiasi Metadata Penelitian Baru
> **Prompt:**  
> `"Agent, saya ingin memperbarui CONTEXT_SKRIPSI.txt dengan identitas penelitian saya:  
> - Nama / NPM: [Nama Anda] / [NPM Anda]  
> - Judul: [Judul Skripsi Lengkap]  
> - Metode / Algoritma: [Metode, misal: Weighted Product / SAW / AHP / CNN]  
> - Objek & Lokasi: [Nama Instansi / Perusahaan / Lokasi Riset]  
> - Teknologi: [Bahasa Pemrograman, Framework, Database]  
> - Dosen Pembimbing: [Pembimbing I] & [Pembimbing II]  
> Masukkan data ini ke CONTEXT_SKRIPSI.txt, pertahankan tanda [NEEDS USER INPUT] pada bagian yang belum saya sebutkan, dan konfirmasi bahwa status substansi ini sudah LOCKED."`

### 1.2 Mengunci Catatan Bimbingan / Revisi Dosen
> **Prompt:**  
> `"Agent, Dosen Pembimbing I memberikan arahan revisi berikut:  
> '[Salin catatan dosen di sini, misal: Batasi kriteria penilaian hanya 5 aspek, dan gunakan data tahun 2025-2026]'  
> Tolong catat revisi ini pada bagian 13 CONTEXT_SKRIPSI.txt. Jangan ubah bagian lain yang sudah disetujui dosen."`

---

## 2. MODE `RESEARCH` (Pustaka, Jurnal, & Verifikasi Sitasi)
*Prinsip: No Source, No Claim. Status: DISCOVERED $\rightarrow$ DOWNLOADED $\rightarrow$ READ $\rightarrow$ VERIFIED $\rightarrow$ USED.*

### 2.1 Mencari Literatur Jurnal Terakreditasi
> **Prompt:**  
> `"Agent mode RESEARCH: Cari 3 artikel jurnal nasional terakreditasi SINTA (atau jurnal internasional Scopus) yang membahas penerapan [Metode Anda] dalam kasus [Topik Anda].  
> Catat ke REFERENSI/index.md dengan ID REF-001, REF-002, dst.  
> Dilarang mengarang nama penulis, tahun, nama jurnal, atau DOI. Jika tautan belum Anda verifikasi, biarkan statusnya DISCOVERED."`

### 2.2 Verifikasi Naskah Jurnal & Ekstraksi Teori
> **Prompt:**  
> `"Agent mode RESEARCH: Saya telah meletakkan berkas PDF di REFERENSI/REF-001_[nama_file].pdf.  
> Tolong baca naskah tersebut, ubah statusnya di REFERENSI/index.md menjadi READ lalu VERIFIED, dan buatkan ringkasan:  
> 1. Masalah yang diselesaikan peneliti tersebut.  
> 2. Variabel/kriteria yang digunakan.  
> 3. Formula matematis yang dipakai.  
> 4. Kelebihan dan keterbatasan penelitian tersebut."`

---

## 3. MODE `WRITING` (Penyusunan Naskah Human-Authored per BAB)

### 3.1 BAB I — Pendahuluan
* **Menyusun Latar Belakang (Pola Piramida Terbalik):**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun draf subbab 1.1 Latar Belakang (4-5 paragraf) dengan alur deduktif:  
  > - Paragraf 1: Kondisi ideal dan fenomena pentingnya [Topik Sistem Anda].  
  > - Paragraf 2: Masalah nyata di [Nama Objek Riset Anda] sesuai data CONTEXT_SKRIPSI.txt.  
  > - Paragraf 3: Dampak negatif jika masalah tidak diselesaikan dengan sistem terkomputasi.  
  > - Paragraf 4: Alasan pemilihan [Metode Anda] diperkuat sitasi dari REF-001 yang berstatus VERIFIED.  
  > - Paragraf 5: Pernyataan tujuan penulisan skripsi ini.  
  > Terapkan kaidah EYD V, bahasa formal manusia, dan hindari kata-kata klise (AI slop)."`

* **Menyusun Rumusan & Batasan Masalah:**
  > **Prompt:**  
  > `"Agent mode WRITING: Berdasarkan CONTEXT_SKRIPSI.txt, susun kalimat akademis untuk:  
  > 1. Subbab 1.2 Rumusan Masalah (buat 2-3 poin pertanyaan penelitian yang tajam dan terukur).  
  > 2. Subbab 1.3 Batasan Masalah (buat 3-4 batasan ruang lingkup teknis yang realistis agar tidak melebar saat sidang).  
  > 3. Subbab 1.4 Tujuan Penelitian (sinkronkan 1:1 dengan rumusan masalah)."`

---

### 3.2 BAB II — Landasan Teori & Tinjauan Pustaka
* **Menyusun Tabel Matriks Penelitian Terdahulu (*State-of-the-Art*):**
  > **Prompt:**  
  > `"Agent mode WRITING: Buatkan subbab 2.1 Tinjauan Pustaka dalam bentuk narasi perbandingan dan Tabel Matriks Penelitian Terdahulu (minimal 3 artikel dari REFERENSI/index.md).  
  > Kolom tabel: No, Peneliti & Tahun, Judul, Metode, Hasil Utama, dan Perbedaan/Posisi Penelitian Ini.  
  > Gunakan format tabel ilmiah (hanya garis horizontal atas, bawah, dan kepala kolom)."`

* **Menjelaskan Teori Metode / Algoritma dengan Formula:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 2.3 Teori [Metode Anda]. Jelaskan definisi formal, tahapan komputasi, dan tuliskan rumus matematisnya lengkap dengan keterangan notasi variabel. Sitasi sumber primer yang terdaftar di REFERENSI/index.md."`

---

### 3.3 BAB III — Metodologi Penelitian & Perancangan
* **Menyusun Waktu, Lokasi, dan Pengumpulan Data:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 3.1 Waktu dan Tempat Penelitian serta 3.2 Metode Pengumpulan Data (Observasi, Wawancara, Dokumentasi) sesuai parameter faktual di CONTEXT_SKRIPSI.txt. Jangan mengarang nama narasumber atau tanggal yang belum saya berikan."`

* **Menyusun Analisis Kebutuhan Sistem:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun subbab 3.4 Analisis Kebutuhan Sistem yang terbagi atas:  
  > 1. Analisis Kebutuhan Fungsional (daftar fungsi yang dapat dijalankan aktor Admin dan Pengguna).  
  > 2. Analisis Kebutuhan Non-Fungsional (aspek perangkat keras, perangkat lunak, dan keamanan).  
  > Rujuk aktor dan modul yang terdaftar di CONTEXT_SKRIPSI.txt."`

---

### 3.4 BAB IV — Hasil dan Pembahasan
> [!IMPORTANT]
> **Prinsip: No Data, No Result.** Berikan data mentah Anda sebelum meminta agen menyusun BAB IV!

* **Perhitungan Manual Algoritma Berbasis Data Nyata:**
  > **Prompt:**  
  > `"Agent mode WRITING: Berikut adalah data alternatif dan kriteria riil dari penelitian saya:  
  > [Tempelkan data tabel atau angka Anda di sini]  
  > Tolong susun subbab 4.2 Perhitungan Algoritma langkah demi langkah: pembentukan matriks keputusan, normalisasi, pembobotan, dan perangkingan akhir. Hitung secara akurat tanpa membuat data asumsi."`

* **Mendeskripsikan Tangkapan Layar Sistem (Screenshot Walkthrough):**
  > **Prompt:**  
  > `"Agent mode WRITING: Saya telah menempatkan tangkapan layar antarmuka di ASSETS/SCREENSHOOT/gambar_4_1_login.png dan gambar_4_2_dashboard.png.  
  > Susun narasi akademis untuk subbab 4.1 yang menjelaskan fungsi antarmuka tersebut, peran tombol-tombolnya, dan hubungkan dengan Gambar 4.1 dan Gambar 4.2."`

* **Menyusun Tabel Pengujian Black Box Testing:**
  > **Prompt:**  
  > `"Agent mode WRITING: Buatkan tabel Pengujian Black Box untuk subbab 4.3.  
  > Kolom tabel: No, Skenario Pengujian, Kasus Uji / Aksi, Hasil yang Diharapkan, Hasil Pengujian Aktual, dan Kesimpulan (Valid).  
  > Cantumkan minimal 6 skenario uji fungsional utama sistem."`

---

### 3.5 BAB V — Kesimpulan dan Saran
* **Menyusun Kesimpulan & Saran yang Kuat:**
  > **Prompt:**  
  > `"Agent mode WRITING: Susun BAB V Kesimpulan dan Saran:  
  > 1. Kesimpulan: Jawab secara langsung 2 rumusan masalah di BAB I dengan menyertakan bukti/hasil yang diperoleh pada BAB IV.  
  > 2. Saran: Buat 2 poin saran teknis pengembangan aplikasi ke depan dan 1 saran praktis untuk instansi terkait."`

---

### 3.6 Abstrak (Indonesia & English)
* **Menyusun Abstrak Standar Almuslim:**
  > **Prompt:**  
  > `"Agent mode WRITING: Buatkan ABSTRAK (Bahasa Indonesia, 1 paragraf, 150-200 kata, spasi tunggal) dan ABSTRACT (Bahasa Inggris italic).  
  > Struktur: Latar belakang singkat $\rightarrow$ Tujuan utama $\rightarrow$ Metode & teknologi yang dipakai $\rightarrow$ Hasil akhir/kesimpulan.  
  > Di bawahnya sertakan Kata Kunci (3-5 kata spesifik)."`

---

## 4. MODE `DIAGRAM` (Pemodelan Sistem Monokromatik)
*Prinsip: Garis hitam presisi, latar putih bersih, tanpa bayangan/warna dekoratif, sesuai SOP_DIAGRAM.md.*

* **Membuat Flowchart Alur Sistem (Mermaid.js):**
  > **Prompt:**  
  > `"Agent mode DIAGRAM: Buatkan kode Mermaid.js untuk Flowchart [Proses/Algoritma] dengan gaya monokromatik hitam-putih. Pastikan simbol terminator, proses, keputusan, dan data sesuai standar ANSI."`

* **Membuat Use Case Diagram & Deskripsi Skenario:**
  > **Prompt:**  
  > `"Agent mode DIAGRAM: Rancang Use Case Diagram untuk sistem ini berdasarkan aktor [Sebutkan aktor] dan fungsionalitas di CONTEXT_SKRIPSI.txt. Tampilkan diagram Mermaid monokrom beserta tabel Definisi Use Case (Aktor, Deskripsi, Kondisi Awal, Alur Normal)."`

* **Membuat ERD (Entity Relationship Diagram):**
  > **Prompt:**  
  > `"Agent mode DIAGRAM: Rancang ERD logis untuk database sistem. Tuliskan dalam format Mermaid `erDiagram` monokrom yang mencantumkan nama entitas, atribut kunci (PK/FK), tipe data dasar, dan kardinalitas relasi (||--o{ dsb)."`

---

## 5. MODE `DOCUMENT` (Pengelolaan File Word `.docx`)

* **Menyalin Draf ke Template Word Almuslim:**
  > **Prompt:**  
  > `"Agent mode DOCUMENT: Masukkan draf teks [Sebutkan BAB] yang sudah disetujui ke dalam berkas AI_program/working/template_skripsi_almuslim.docx.  
  > Pertahankan konfigurasi margin 4-4-3-3, font Times New Roman 12 pt spasi 2.0, Heading 1/2/3, serta section break penomoran halaman yang sudah tertanam di template tersebut."`

* **Memformat Tabel / Gambar Standar Skripsi:**
  > **Prompt:**  
  > `"Agent mode DOCUMENT: Periksa tata letak Tabel [Nomor Tabel] dan Gambar [Nomor Gambar]. Pastikan nomor dan judul tabel terletak di atas tabel (spasi 1.0, 10-11 pt), sedangkan judul gambar terletak di bawah gambar. Pastikan tidak ada tabel yang terpotong secara canggung antar halaman."`

---

## 6. MODE `QA` (Quality Assurance & Audit Anti-Halusinasi)

* **Audit 10-Poin Kualitas Sebelum Menghadap Dosen:**
  > **Prompt:**  
  > `"Agent mode QA: Jalankan audit menyeluruh terhadap draf naskah yang baru dibuat. Evaluasi 10 aspek QC:  
  > 1. Content (kesesuaian dengan rumusan masalah)  
  > 2. Source (validitas di REFERENSI/index.md)  
  > 3. Data (bebas angka palsu)  
  > 4. Citation (sinkronisasi dengan Daftar Pustaka)  
  > 5. Structure (kesesuaian subbab SOP Almuslim)  
  > 6. Format (margin 4-4-3-3, font, spasi 2.0)  
  > 7. Terminology (istilah asing dicetak miring)  
  > 8. Diagram (keterbacaan dan kesesuaian teks)  
  > 9. Document (kestabilan heading Word)  
  > 10. Output (bebas tag debug/placeholder).  
  > Tampilkan hasil audit dalam bentuk checklist tabel status [PASS / FAIL] beserta catatan perbaikan."`

* **Pemindaian Teks Debug / Placeholder:**
  > **Prompt:**  
  > `"Agent mode QA: Pindai seluruh teks naskah. Cari apakah masih ada tag [NEEDS USER INPUT], [DATA REQUIRED], [RESULT REQUIRED], TODO, atau FIXME. Laporkan lokasi barisnya jika masih ditemukan."`

---

## 7. PROMPT SIMULASI & REVIEW KRITIS

### 7.1 Simulasi Tanya-Jawab Sidang Skripsi (*Grill Me Mode*)
> **Prompt:**  
> `"Agent, bertindaklah sebagai Dosen Penguji Sidang Skripsi Informatika yang kritis dan teliti.  
> Ajukan 3 pertanyaan tersulit dan paling tajam kepada saya mengenai:  
> 1. Kelemahan metodologi/algoritma yang saya pilih dibandingkan metode sejenis.  
> 2. Validitas dan representativitas data pengujian saya.  
> 3. Kontribusi nyata sistem ini terhadap objek penelitian.  
> Uji saya satu per satu, tunggu jawaban saya, lalu beri penilaian dan saran penyempurnaan jawaban."`

### 7.2 Parafrase Akademik Anti-Plagiarisme
> **Prompt:**  
> `"Agent, tolong parafrasekan paragraf berikut agar lolos uji Turnitin/plagiarisme, namun tetap mempertahankan makna aslinya secara akurat:  
> '[Tempelkan paragraf di sini]'  
> Aturan: Gunakan struktur kalimat aktif-pasif yang bervariasi, bahasa formal EYD V, dan jangan gunakan kosakata hiperbolis (AI slop)."`

### 7.3 Pembuatan Matriks Respons Revisi Penguji
> **Prompt:**  
> `"Agent, saya baru saja selesai seminar/sidang. Berikut catatan coretan dari penguji:  
> - Penguji 1: [Tulis catatan]  
> - Penguji 2: [Tulis catatan]  
> Tolong buatkan Tabel Matriks Tindak Lanjut Revisi dengan format:  
> No | Nama Dosen Penguji | Poin Catatan/Masukan | Halaman Asal | Perubahan yang Dilakukan | Halaman Baru."`

---

## 8. MODE `FINALIZATION` (Rilis Dokumen Final ke OUTPUT/)

* **Pelepasan Naskah Final Siap Cetak:**
  > **Prompt:**  
  > `"Agent mode FINALIZATION: Seluruh isi naskah BAB I s.d. BAB V, Bagian Awal, dan Bagian Akhir telah lolos Quality Gate dan disetujui dosen.  
  > Ekspor dokumen final ke folder OUTPUT/ dengan nama file:  
  > SKRIPSI_FINAL_[NAMA_MAHASISWA]_[TAHUN].docx  
  > Pastikan tidak ada file sementara (*temporary file*) yang tertinggal di folder OUTPUT/."`

---

## 💡 ATURAN EMAS PENGGUNAAN PROMPT (*GOLDEN RULES*)
1. **Jangan Minta Menulis Sekaligus**: Jangan pernah mengetik *"Tuliskan seluruh skripsi saya dari BAB I sampai BAB V"*. AI akan memberikan teks umum yang dangkal. Kerjakan **subbab per subbab** agar mendalam dan berbobot.
2. **Berikan Fakta, Minta Narasi**: Berikan poin-poin masalah nyata di lapangan kepada agen, lalu minta agen menyusunnya ke dalam bahasa akademik formal.
3. **Koreksi Langsung**: Jika agen menggunakan kata yang terdengar terlalu generik/berbunga-bunga, katakan: *"Ubah paragraf tersebut menjadi lebih padat, ilmiah, dan hilangkan kalimat hiperbolis."*
4. **Target Ketebalan Naskah (Min 80 Halaman)**: Naskah utama skripsi (BAB I s.d. BAB V) wajib mencapai **minimal 80 halaman (lembar)**, dengan batas maksimal bebas sesuai kerumitan sistem dan data. Pastikan agen mengelaborasi rancangan sistem, tabel pengujian, diagram teknis, dan interpretasi hasil secara komprehensif, bukan membuat ringkasan singkat.

