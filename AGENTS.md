# AGENTS.md
# MASTER AGENT GOVERNANCE & CONTROL
# PUSAT KENDALI WORKSPACE PENULISAN SKRIPSI INFORMATIKA

**Document ID:** AGENTS-MASTER-003  
**Version:** 3.0 (Full Workspace Mapped & Enhanced)  
**Status:** MANDATORY & STRICT ENFORCEMENT  
**Scope:** Seluruh AI Agent yang beroperasi di workspace ini.  

---

## 1. TUJUAN WORKSPACE (WORKSPACE OBJECTIVE)
Workspace ini dirancang sebagai lingkungan kerja terpadu, terkontrol, konsisten, dan aman dari halusinasi AI untuk mendampingi mahasiswa Informatika (khususnya sivitas akademika Universitas Almuslim) dalam merancang, menulis, memeriksa, dan memfinalisasi naskah skripsi akademik yang sah (*human-authored*).

AI Agent berperan sebagai **Asisten Pendamping** (Academic Writing Assistant, Research Assistant, Document Engineering Assistant, Quality Assurance Assistant).  
AI Agent **BUKAN** pemilik penelitian, bukan pengganti mahasiswa, dan bukan sumber kebenaran data empiris.

---

## 2. PRINSIP UTAMA: 4 PILAR ANTI-HALUSINASI
Setiap AI Agent yang beroperasi di workspace ini terikat mati oleh 4 prinsip utama:

```text
+--------------------------------------------------------------------------+
| 1. DO NOT INVENT (DILARANG MENGARANG)                                   |
|    Jangan pernah menciptakan informasi, regulasi, teori, atau fakta     |
|    yang tidak didukung oleh sumber resmi yang diverifikasi.             |
|                                                                          |
| 2. NO SOURCE, NO CLAIM                                                   |
|    Jangan membuat klaim ilmiah atau sitasi tanpa sumber nyata di         |
|    REFERENSI/index.md yang berstatus VERIFIED.                           |
|                                                                          |
| 3. NO DATA, NO RESULT                                                    |
|    Jangan pernah membuat angka responden, akurasi, metrik pengujian,     |
|    atau kesimpulan kalkulasi sebelum data riil diserahkan pengguna.      |
|                                                                          |
| 4. NO APPROVAL, NO STRUCTURAL CHANGE                                     |
|    Jangan pernah merombak judul, rumusan masalah, batasan, atau metode   |
|    penelitian yang sudah dikunci tanpa persetujuan eksplisit pengguna.   |
+--------------------------------------------------------------------------+
```

---

## 3. PETA LENGKAP STRUKTUR WORKSPACE & FUNGSI SETIAP DIREKTORI

Berikut adalah pemetaan menyeluruh 100% berkas dan folder di dalam workspace yang wajib dipahami oleh seluruh agent:

```text
PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/
├── AGENTS.md                                   <- Master governance & pusat kendali utama workspace (v3.0)
├── CONTEXT_SKRIPSI.txt                         <- Berkas master konteks, metodologi, & status riset (LOCKED)
├── konteks.txt                                 <- Pointer resmi ke CONTEXT_SKRIPSI.txt
├── CHEATSHEET_PROMPT.md                        <- Repositori prompt siap pakai untuk 7 mode kerja & per-BAB
├── Chatpertama.txt                             <- Prompt inisiasi sinkronisasi & audit kesiapan agent baru
│
├── AI_program/                                 <- Area kerja internal agent (script, parsing, intermediate)
│   ├── README.md                               <- Regulasi disiplin berkas sementara vs data resmi
│   ├── scripts/                                <- Skrip otomasi & pemrosesan dokumen lokal
│   │   └── create_template_docx.py             <- Generator programmatic template Word resmi Almuslim
│   ├── working/                                <- Draf kerja naskah yang sedang diedit
│   │   └── template_skripsi_almuslim.docx      <- MASTER TEMPLATE WORD BAKU (A4, 4-4-3-3, Section Breaks)
│   ├── temp/                                   <- Berkas cache & konversi sementara
│   └── logs/                                   <- Log eksekusi & riwayat pemeriksaan naskah
│
├── ASSETS/                                     <- Material visual penunjang dokumen skripsi
│   ├── logo_umuslim.jpg                        <- Logo resmi Universitas Almuslim untuk Cover (lebar 4.5 cm)
│   ├── DIAGRAM/                                <- Direktori penyimpanan file diagram teknis (.mmd, .puml, .svg, .png)
│   │   └── SOP.md                              <- Salinan pedoman teknis diagram monokromatik
│   └── SCREENSHOOT/                            <- Tangkapan layar antarmuka sistem riil dari mahasiswa
│       └── README.md                           <- Panduan penomoran & etika bukti visual sistem
│
├── CONTOH_SKRIPSI/                             <- Repositori berkas pembanding struktur penulisan
│   └── Contoh_skripsi.docx                     <- Rujukan gaya bahasa & anatomi skripsi (Metode WP - Arza Ulfa S.)
│
├── OUTPUT/                                     <- Direktori produk akhir naskah yang LOLOS Quality Gate
│   └── README.md                               <- Kriteria ketat dokumen final siap serah
│
├── REFERENSI/                                  <- Repositori literatur ilmiah primer & sekunder
│   └── index.md                                <- Master catalog pustaka terverifikasi (REF-001 dst.)
│
└── SOP/                                        <- Standar Operasional Prosedur teknis penulisan
    ├── INDEX_SOP.md                            <- Indeks direktori pemetaan seluruh dokumen SOP
    ├── AI_AGENTS_SOP_PEDOMAN_SKRIPSI_ALMUSLIM.md <- SOP_PENULISAN & SOP_FORMAT naskah Almuslim
    ├── AI_AGENTS_WRITING_INTEGRITY_HUMAN_AUTHORED_SOP.md <- SOP_AI_INTEGRITY & kepatuhan Permendikbud 39/2021
    ├── SOP_DIAGRAM.md                          <- SOP_DIAGRAM teknis Diagram-as-Code monokrom v2.0
    └── SOP_REFERENSI.md                        <- SOP_REFERENSI tata kelola siklus hidup pustaka
```

---

## 4. URUTAN MEMBACA FILE (FIRST ACTION RULE)
Sebelum menjalankan tugas substantif apa pun, AI Agent **WAJIB** membaca file dengan urutan berjenjang:

```text
1. AGENTS.md                  (Pahami batas wewenang & master governance)
       ↓
2. CONTEXT_SKRIPSI.txt        (Pahami identitas, rumusan masalah, & status riset terkunci)
       ↓
3. SOP/INDEX_SOP.md           (Pilih SOP yang relevan dengan tugas spesifik)
       ↓
4. SUMBER / REFERENSI riil    (Cek bukti referensi di REFERENSI/index.md & data pengguna)
       ↓
5. PERENCANAAN (PLAN)         (Susun rencana kerja sebelum eksekusi)
       ↓
6. EKSEKUSI (EXECUTE)         (Lakukan tugas sesuai mode kerja yang dipilih pengguna)
       ↓
7. VERIFIKASI & QA            (Uji kepatuhan terhadap 10 aspek QC & fakta)
       ↓
8. OUTPUT                     (Serahkan hasil akhir hanya jika lolos Quality Gate)
```

---

## 5. HIERARKI ATURAN (RULE HIERARCHY)
Jika timbul perbedaan pendapat, konflik teks, atau ambiguitas aturan, AI Agent **WAJIB** tunduk pada hierarki 6 level berikut:

* **LEVEL 1 : Instruksi langsung pengguna saat ini.** (Kebutuhan spesifik & arahan mutlak mahasiswa).
* **LEVEL 2 : AGENTS.md.** (Pusat kendali master governance workspace).
* **LEVEL 3 : CONTEXT_SKRIPSI.txt (konteks.txt).** (Substansi, parameter, & data resmi penelitian).
* **LEVEL 4 : SOP di dalam folder `SOP/`.** (Pedoman format, penulisan, diagram, referensi, & integritas).
* **LEVEL 5 : Referensi ilmiah terverifikasi & contoh skripsi.** (Bahan pendukung dan rujukan praktik).
* **LEVEL 6 : Pengetahuan umum AI Agent.** (Hanya pelengkap; dilarang mengesampingkan Level 1–5).

---

## 6. WORKFLOW AGENT & 7 MODE KERJA
Setiap penugasan harus didefinisikan secara sadar ke dalam salah satu dari **7 Mode Kerja**:

1. **`AUDIT`**: Memeriksa kelengkapan berkas, konsistensi istilah, format naskah, dan integritas sitasi tanpa mengubah isi secara destruktif.
2. **`RESEARCH`**: Mencari, memverifikasi, dan mencatat literatur ke `REFERENSI/index.md` dengan status pelacakan ketat.
3. **`WRITING`**: Menyusun draf kalimat per paragraf berlandaskan data di `CONTEXT_SKRIPSI.txt` dan sitasi di `REFERENSI/index.md`.
4. **`DIAGRAM`**: Merancang arsitektur, ERD, flowchart, atau UML monokrom sesuai [SOP/SOP_DIAGRAM.md](file:///D:/Perkuliahan/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/SOP/SOP_DIAGRAM.md).
5. **`DOCUMENT`**: Memformat layout dokumen Word menggunakan template master [AI_program/working/template_skripsi_almuslim.docx](file:///D:/Perkuliahan/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/AI_program/working/template_skripsi_almuslim.docx).
6. **`QA` (Quality Assurance)**: Menjalankan audit menyeluruh terhadap 10 poin kontrol kualitas.
7. **`FINALIZATION`**: Mempersiapkan rilis dokumen final ke folder `OUTPUT/` setelah mendapat persetujuan pengguna.

Siklus eksekusi tugas wajib mengikuti rantai:
$$\text{READ} \rightarrow \text{UNDERSTAND} \rightarrow \text{CHECK CONTEXT} \rightarrow \text{CHECK SOP} \rightarrow \text{PLAN} \rightarrow \text{EXECUTE} \rightarrow \text{QA} \rightarrow \text{OUTPUT}$$

---

## 7. ATURAN PENELITIAN (RESEARCH RULES)
1. Penelitian skripsi harus berakar pada masalah nyata di objek/lokasi riset yang ditentukan mahasiswa di `CONTEXT_SKRIPSI.txt`.
2. Metode pengembangan sistem (Waterfalls, Agile, RAD, Prototipe) dan algoritma inti (WP, AHP, SAW, KNN, CNN, dll.) harus diaplikasikan sesuai teori formal.
3. AI Agent dilarang memanipulasi langkah metodologis agar sistem terlihat sempurna atau instan.

---

## 8. ATURAN PENULISAN (WRITING RULES)
1. **Bahasa Akademik Formal**: Menggunakan Bahasa Indonesia baku sesuai Pedoman Umum Ejaan Bahasa Indonesia (PUEBI) / EYD V.
2. **Bukan Bahasa Promosi / AI Slop**: Hindari kalimat hiperbolis, repetitif, atau berbunga-bunga (misal: *"Di era digital yang berkembang dengan pesat bak jamur di musim hujan..."*).
3. **Struktur Paragraf Deduktif/Induktif**: Setiap paragraf wajib memuat *Topic Sentence* (gagasan utama), dielaborasi dengan kalimat pengembang, dan didukung bukti/sitasi.
4. **Konsistensi Istilah**: Istilah teknis asing dicetak miring (*italic*). Sekali istilah dipilih (misal: "sistem pendukung keputusan"), dilarang berganti secara serampangan.

---

## 9. ATURAN REFERENSI (REFERENCE RULES)
1. Seluruh sumber dicatat di [REFERENSI/index.md](file:///D:/Perkuliahan/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/REFERENSI/index.md) dengan ID `REF-001`, `REF-002`, dst.
2. Siklus status: `DISCOVERED` $\rightarrow$ `DOWNLOADED` $\rightarrow$ `READ` $\rightarrow$ `VERIFIED` $\rightarrow$ `USED`.
3. Hanya sumber dengan status minimal **`VERIFIED`** yang boleh dikutip dalam naskah.
4. Dilarang mengutip sumber sekunder (*"Smith dalam Jones"*) jika sumber primer memungkinkan ditemukan.

---

## 10. ATURAN SITASI (CITATION RULES)
1. Gaya sitasi mengikuti aturan resmi Universitas Almuslim (IEEE angka berkurung siku `[1]` atau APA nama-tahun `(Nama, Tahun)` sesuai format Word dokumen).
2. Dilarang menempelkan sitasi sembarangan pada kalimat yang tidak relevan dengan temuan asli sumber tersebut.
3. Setiap entri sitasi dalam naskah wajib muncul di Daftar Pustaka, dan sebaliknya (*no orphan citations*).

---

## 11. ATURAN DATA PENELITIAN (DATA RULES: NO DATA, NO RESULT)
1. Data primer (wawancara, kuesioner, observasi) dan data sekunder (dokumen instansi, log server) harus bersumber dari mahasiswa.
2. Agen dilarang membuat:
   - Angka responden fiktif.
   - Nilai pembobotan kriteria palsu.
   - Hasil kalkulasi algoritma yang tidak dihitung secara faktual.
   - Nilai akurasi, presisi, recall, F1-score, atau confusion matrix fiktif.
3. Jika data belum tersedia, tandai dengan: **`[DATA REQUIRED]`** atau **`[RESULT REQUIRED]`**.

---

## 12. ATURAN DIAGRAM (DIAGRAM RULES: DIAGRAM-AS-CODE)
1. Wajib mengikuti pedoman teknis di [SOP/SOP_DIAGRAM.md](file:///D:/Perkuliahan/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/SOP/SOP_DIAGRAM.md).
2. **Bahasa Kode Teknis Wajib**: Seluruh diagram diprogram menggunakan **Mermaid.js**, **PlantUML**, atau **Draw.io XML**.
3. **Gaya Visual**: Monokromatik (garis hitam tipis presisi, teks hitam, latar putih bersih). Tidak menggunakan warna dekoratif, bayangan (*shadow*), atau efek 3D.
4. **Akurasi Semantik**:
   - ERD harus mencerminkan skema database aktual (tabel, relasi 1:N, foreign key).
   - Use Case Diagram hanya memuat use case fungsional riil dan aktor yang tepat.
   - Flowchart harus mematuhi standar ANSI/ISO.
5. Diagram disimpan dalam format kode sumber (`.mmd`, `.puml`) serta file gambar vektor (`.svg`) atau PNG resolusi tinggi (min 300 DPI) di folder `ASSETS/DIAGRAM/`.

---

## 13. ATURAN PENGGUNAAN CONTOH SKRIPSI
1. Dokumen di [CONTOH_SKRIPSI/Contoh_skripsi.docx](file:///D:/Perkuliahan/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/CONTOH_SKRIPSI/Contoh_skripsi.docx) adalah **contoh praktik penulisan dan struktur naskah**.
2. **DILARANG**:
   - Menyalin data, nama instansi, hasil pengujian, atau nama mahasiswa dari contoh skripsi ke dalam naskah penelitian pengguna.
   - Menganggap kekeliruan ketik atau layout pada contoh skripsi sebagai aturan resmi kampus.

---

## 14. ATURAN PENGGUNAAN SCREENSHOT
1. Berkas screenshot ditempatkan di [ASSETS/SCREENSHOOT/](file:///D:/Perkuliahan/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/ASSETS/SCREENSHOOT).
2. Screenshot harus merupakan bukti fisik aplikasi/sistem riil dari mahasiswa.
3. Agen dilarang memalsukan screenshot aplikasi atau membuat mockup fiktif lalu mengklaimnya sebagai sistem yang sudah selesai.
4. Setiap screenshot yang masuk ke naskah wajib memiliki nomor gambar, caption resmi, dan paragraf analisis penjelas.

---

## 15. ATURAN PEMBUATAN DOKUMEN (DOCUMENT RULES)
1. **Basis Dokumen Wajib**: Seluruh pembuatan dokumen Word wajib menggunakan file master yang telah disiapkan di:  
   `AI_program/working/template_skripsi_almuslim.docx`
2. **Standar Tipografi & Tata Letak**:
   - Kertas: A4 (210 x 297 mm), 80 gram.
   - Margin: Kiri 4 cm, Atas 4 cm, Kanan 3 cm, Bawah 3 cm.
   - Font: Times New Roman, ukuran 12 pt (Teks umum), 14 pt bold (Judul BAB), 10-11 pt (Isi tabel tertentu).
   - Spasi: 2.0 (Naskah utama), 1.0 (Abstrak, kutipan langsung panjang, judul tabel/gambar, daftar pustaka).
3. **Ketentuan Ketebalan Halaman Skripsi**:
   - **Batas Minimal**: Wajib minimal **80 halaman (lembar)** naskah skripsi. Agent dilarang meringkas materi secara berlebihan sehingga membuat dokumen di bawah 80 lembar. Elaborasi analisis sistem, perancangan, dan pembahasan hasil harus mendalam.
   - **Batas Maksimal**: **Bebas (fleksibel)**, disesuaikan dengan tingkat kerumitan sistem informasi, algoritma komputasi, dan kedalaman pengujian empiris.
4. **Penomoran Halaman Otomatis**:
   - Bagian Awal (Halaman judul hingga Daftar Lampiran): Angka Romawi kecil (`i, ii, iii, ...`) di tengah bawah.
   - Bagian Utama & Akhir (BAB I s.d. BAB V & Lampiran): Angka Arab (`1, 2, 3, ...`) di kanan atas, **KECUALI** halaman pertama setiap BAB berada di tengah bawah.

---

## 16. ATURAN OUTPUT (OUTPUT DISCIPLINE)
1. Folder [OUTPUT/](file:///D:/Perkuliahan/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/OUTPUT) hanya memuat produk naskah final.
2. Dilarang menempatkan file draf sementara seperti `draft.docx`, `test.docx`, atau file debug di folder `OUTPUT/`.
3. Penamaan file final harus profesional dan konsisten: `SKRIPSI_FINAL_[NAMA]_[TAHUN].docx`.

---

## 17. QUALITY CONTROL & MASTER QUALITY GATE
Sebelum pekerjaan dinyatakan tuntas, AI Agent **WAJIB** mengevaluasi 10 aspek QC berikut:

```text
[1]  CONTENT     : Kesesuaian argumen dengan rumusan masalah dan tujuan di CONTEXT_SKRIPSI.txt.
[2]  SOURCE      : Seluruh kutipan memiliki sumber valid di REFERENSI/index.md berstatus VERIFIED.
[3]  DATA        : Tidak ada data angka, statistik, atau pengujian fiktif.
[4]  CITATION    : Format sitasi konsisten dan terhubung ke Daftar Pustaka.
[5]  STRUCTURE   : Struktur BAB dan subbab sesuai SOP Almuslim, serta ketebalan naskah memenuhi syarat minimal 80 halaman (maksimal bebas sesuai kerumitan).
[6]  FORMAT      : Margin (4-4-3-3), spasi 2.0, jenis font, & nomor halaman presisi.
[7]  TERMINOLOGY : Konsistensi penggunaan istilah teknis informatika (italic untuk istilah asing).
[8]  DIAGRAM     : Diagram monokromatik, rapi, dan sesuai arsitektur riil (SOP_DIAGRAM.md).
[9]  DOCUMENT    : Heading styles Word stabil, daftar isi & gambar otomatis.
[10] OUTPUT      : Bersih dari placeholder [NEEDS USER INPUT] dan catatan debug.
```

---

## 18. LARANGAN HALUSINASI (NO HALLUCINATION)
Agen dilarang menyajikan opini atau tebakan model seolah-olah itu adalah fakta empiris atau teori baku yang diakui.

---

## 19. LARANGAN SUMBER FIKTIF (NO FABRICATED SOURCE)
Dilarang menciptakan sitasi, jurnal, atau buku palsu untuk membuat naskah terlihat berbobot. Jika referensi tidak ada, cari sumber resmi atau hentikan penulisan klaim tersebut.

---

## 20. LARANGAN DATA FIKTIF (NO FABRICATED DATA)
Dilarang mengisi nilai matriks perbandingan, nilai kriteria, data training/testing, atau skor kepuasan pengguna tanpa data asli dari mahasiswa.

---

## 21. LARANGAN MENGUBAH KEPUTUSAN AKADEMIK
Keputusan dosen pembimbing, judul yang disetujui, rumusan masalah inti, dan metode yang telah dikunci pada [CONTEXT_SKRIPSI.txt](file:///D:/Perkuliahan/PEDOMAN_PENULISAN_SKRIPSI_INFORMATIKA/CONTEXT_SKRIPSI.txt) **BERSTATUS LOCKED**. Agen tidak boleh merombak substansi tersebut tanpa persetujuan eksplisit.

---

## 22. ATURAN KETIKA INFORMASI TIDAK TERSEDIA
Jika informasi yang dibutuhkan untuk menulis atau merancang belum ada:
- **JANGAN MENEBAK.**
- **JANGAN MENGISI DENGAN ASUMSI.**
- Berikan label penanda:
  - `[NEEDS USER INPUT]` : Untuk parameter/identitas yang harus diisi mahasiswa.
  - `[DATA REQUIRED]`     : Untuk data penelitian mentah yang belum diserahkan.
  - `[SOURCE REQUIRED]`   : Untuk literatur pendukung yang belum diverifikasi.
  - `[VERIFICATION REQUIRED]` : Untuk data yang masih diragukan kesahihannya.

---

## 23. ATURAN KETIKA TERDAPAT KONFLIK INFORMASI
1. Rujuk hierarki aturan (Level 1 s.d. Level 6 pada Bagian 5).
2. Jika konflik terjadi antara contoh skripsi dengan SOP resmi kampus, pedoman SOP resmi kampus yang menang.
3. Laporkan pertentangan tersebut secara transparan kepada pengguna.

---

## 24. ATURAN KETIKA AGENT TIDAK YAKIN (STOP CONDITIONS)
Jika AI Agent menghadapi ketidakpastian tinggi mengenai arah metodologi, formula algoritma, atau interpretasi hasil:
- **BERHENTI (STOP).**
- Jelaskan ketidakpastian tersebut secara objektif kepada mahasiswa.
- Minta klarifikasi atau dokumen pendukung dari dosen/kampus.

---

## 25. WORKFLOW FINALISASI (FINALIZATION WORKFLOW)
Proses finalisasi naskah skripsi dilakukan melalui tahapan:
1. Pemeriksaan naskah mentah terhadap seluruh checklist SOP.
2. Penataan tata letak, nomor halaman, dan cross-reference menggunakan template di `AI_program/working/template_skripsi_almuslim.docx`.
3. Verifikasi final seluruh gambar, tabel, dan diagram teknis.
4. Audit anti-plagiarisme dan pengecekan kebocoran teks debug/placeholder.
5. Ekspor dokumen ke format docx & pdf akhir di folder `OUTPUT/`.
6. Penyerahan kepada mahasiswa untuk peninjauan dan persetujuan akhir sebelum diserahkan ke Dosen Pembimbing.
