# BAB III
# ANALISA DAN PERANCANGAN SISTEM

## 3.1 Analisa Sistem
<!-- PANDUAN PENULISAN SUBBAB 3.1:
1. 3.1.1 Analisa Sistem Berjalan: Uraikan alur kerja manual saat ini, dokumen yang terlibat, pihak yang bertanggung jawab, serta identifikasi titik lemah (bottleneck) dan potensi distorsi data.
2. 3.1.2 Analisa Sistem Baru: Uraikan perbaikan yang ditawarkan oleh sistem terkomputerisasi, otomasi pemrosesan, dan peningkatan akurasi keputusan.
3. 3.1.3 Analisa Kebutuhan: Rincikan Kebutuhan Fungsional (SRS) dan Kebutuhan Nonfungsional dalam bentuk tabel standar.
-->

### 3.1.1 Analisa Sistem yang Sedang Berjalan
[Draf analisa sistem berjalan pada objek penelitian akan diuraikan oleh AI Agent berdasarkan hasil observasi dan wawancara faktual]

### 3.1.2 Analisa Sistem Baru yang Diusulkan
[Draf perbaikan alur operasional dan mekanisme otomasi komputasi yang diusulkan oleh sistem baru]

### 3.1.3 Analisa Kebutuhan Fungsional dan Nonfungsional
Kebutuhan fungsional dan nonfungsional perangkat lunak didefinisikan secara terstruktur guna memastikan sistem yang dibangun memenuhi ekspektasi operasional pengguna:

### Tabel 3.1 Kebutuhan Fungsional Sistem
| No | Kode Kebutuhan | Nama Fitur Fungsional | Deskripsi Kebutuhan |
|:---:|:---|:---|:---|
| 1 | SKF-01 | Modul Otentikasi Pengguna | Sistem memverifikasi kredensial login pengguna secara aman |
| 2 | SKF-02 | Manajemen Data Master | Sistem memfasilitasi penambahan, pengubahan, dan penghapusan data parameter |
| 3 | SKF-03 | Pengolahan Evaluasi Data | Sistem mencatat nilai penilaian alternatif berdasarkan kriteria yang ditentukan |
| 4 | SKF-04 | Komputasi Algoritma | Sistem mengeksekusi perhitungan matematis algoritma secara otomatis |
| 5 | SKF-05 | Pembuatan Laporan Keputusan | Sistem menyajikan tabel perangkingan hasil dan fasilitas ekspor/cetak laporan |

### Tabel 3.2 Kebutuhan Nonfungsional Sistem
| No | Parameter Nonfungsional | Spesifikasi dan Tolok Ukur Kinerja |
|:---:|:---|:---|
| 1 | Keamanan (*Security*) | Enkripsi kata sandi menggunakan hashing standar industri dan validasi hak akses per sesi |
| 2 | Keandalan (*Reliability*) | Sistem mampu beroperasi dengan ketersediaan tinggi tanpa anomali kegagalan transaksi basis data |
| 3 | Kinerja (*Performance*) | Waktu respons eksekusi perhitungan algoritma berlangsung dalam durasi di bawah 3 detik |
| 4 | Kegunaan (*Usability*) | Antarmuka pengguna ergonomis, mudah dipahami (*user-friendly*), dan kompatibel pada berbagai peramban web modern |

## 3.2 Penentuan Kriteria dan Bobot Penilaian
<!-- PANDUAN PENULISAN SUBBAB 3.2:
1. Jelaskan setiap parameter kriteria penilaian yang disepakati bersama pihak objek riset.
2. Tentukan jenis kriteria (Benefit / Cost) dan rentang nilai skala yang digunakan.
3. Sajikan pembobotan preferensi pada Tabel 3.3.
-->

### Tabel 3.3 Kriteria Penilaian dan Bobot Preferensi
| No | Kode Kriteria | Nama Parameter Kriteria | Jenis Kriteria | Bobot Awal | Bobot Ternormalisasi |
|:---:|:---|:---|:---:|:---:|:---:|
| 1 | C1 | [Nama Parameter Kriteria 1] | Benefit | [Nilai 1] | [Bobot 1] |
| 2 | C2 | [Nama Parameter Kriteria 2] | Benefit | [Nilai 2] | [Bobot 2] |
| 3 | C3 | [Nama Parameter Kriteria 3] | Cost | [Nilai 3] | [Bobot 3] |
| 4 | C4 | [Nama Parameter Kriteria 4] | Benefit | [Nilai 4] | [Bobot 4] |
| 5 | C5 | [Nama Parameter Kriteria 5] | Benefit | [Nilai 5] | [Bobot 5] |

## 3.3 Perancangan Pemodelan Sistem
<!-- PANDUAN PENULISAN SUBBAB 3.3:
Sajikan diagram pemodelan monokromatik (Diagram-as-Code) yang telah dirender ke folder ASSETS/DIAGRAM/:
1. Gambar 3.1: Diagram Konteks Sistem
2. Gambar 3.2: Data Flow Diagram (DFD) Level 0
3. Gambar 3.3: Data Flow Diagram (DFD) Level 1
-->

### 3.3.1 Diagram Konteks
Diagram Konteks memberikan gambaran menyeluruh mengenai batas lingkup sistem dan seluruh entitas eksternal yang berinteraksi langsung dengan sistem:

<!-- PANDUAN DIAGRAM: Render diagram monokromatik via script render_diagram.py ke ASSETS/DIAGRAM/diagram_konteks.png lalu buka baris gambar berikut -->
<!-- ![Gambar 3.1 Diagram Konteks Sistem](ASSETS/DIAGRAM/diagram_konteks.png) -->
[Gambar 3.1 Diagram Konteks Sistem akan disisipkan di sini setelah dirender melalui Mode DIAGRAM]

### 3.3.2 Data Flow Diagram (DFD) Level 0
DFD Level 0 menguraikan proses utama pada sistem yang meliputi proses autentikasi, manajemen data master, penginputan evaluasi, eksekusi komputasi algoritma, serta penyajian laporan:

<!-- PANDUAN DIAGRAM: Render diagram ke ASSETS/DIAGRAM/dfd_level_0.png lalu buka baris gambar berikut -->
<!-- ![Gambar 3.2 Data Flow Diagram (DFD) Level 0](ASSETS/DIAGRAM/dfd_level_0.png) -->
[Gambar 3.2 Data Flow Diagram (DFD) Level 0 akan disisipkan di sini setelah dirender melalui Mode DIAGRAM]

### 3.3.3 Data Flow Diagram (DFD) Level 1
DFD Level 1 merinci sub-proses komputasi algoritma dan tahapan normalisasi matematis data secara presisi:

<!-- PANDUAN DIAGRAM: Render diagram ke ASSETS/DIAGRAM/dfd_level_1.png lalu buka baris gambar berikut -->
<!-- ![Gambar 3.3 Data Flow Diagram (DFD) Level 1](ASSETS/DIAGRAM/dfd_level_1.png) -->
[Gambar 3.3 Data Flow Diagram (DFD) Level 1 akan disisipkan di sini setelah dirender melalui Mode DIAGRAM]

## 3.4 Perancangan Basis Data
<!-- PANDUAN PENULISAN SUBBAB 3.4:
1. Sajikan Entity Relationship Diagram (ERD) sistem pada Gambar 3.4.
2. Sajikan Kamus Data Teknis untuk setiap tabel basis data dalam bentuk tabel standar 5 kolom (Nama Kolom, Tipe Data, Panjang, Kunci, Keterangan).
-->

### 3.4.1 Entity Relationship Diagram (ERD)
Hubungan antar-entitas data logis dimodelkan dalam ERD monokromatik yang memuat tabel pengguna, tabel master kriteria, tabel alternatif, dan tabel hasil perhitungan keputusan:

<!-- PANDUAN DIAGRAM: Render diagram ke ASSETS/DIAGRAM/erd_sistem.png lalu buka baris gambar berikut -->
<!-- ![Gambar 3.4 Entity Relationship Diagram (ERD) Sistem](ASSETS/DIAGRAM/erd_sistem.png) -->
[Gambar 3.4 Entity Relationship Diagram (ERD) Sistem akan disisipkan di sini setelah dirender melalui Mode DIAGRAM]

### 3.4.2 Desain Struktur File Database (Kamus Data)
Struktur fisik setiap tabel diuraikan secara rinci dalam kamus data teknis berikut:

### Tabel 3.4 Kamus Data Tabel Pengguna (users)
| No | Nama Kolom | Tipe Data | Panjang | Kunci | Keterangan |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | id_user | INT | 11 | Primary Key | Identifikator unik pengguna sistem |
| 2 | username | VARCHAR | 50 | - | Nama akun pengguna untuk login |
| 3 | password | VARCHAR | 255 | - | Kata sandi pengguna terenkripsi |
| 4 | nama_lengkap | VARCHAR | 100 | - | Nama lengkap resmi pengguna |
| 5 | level_akses | ENUM | - | - | Tingkatan hak akses pengguna (Admin/Pimpinan) |

### Tabel 3.5 Kamus Data Tabel Kriteria (criteria)
| No | Nama Kolom | Tipe Data | Panjang | Kunci | Keterangan |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | id_kriteria | INT | 11 | Primary Key | Identifikator unik parameter kriteria |
| 2 | kode_kriteria | VARCHAR | 10 | - | Kode penanda kriteria (C1, C2, dst.) |
| 3 | nama_kriteria | VARCHAR | 100 | - | Nama lengkap parameter penilaian |
| 4 | bobot | DECIMAL | 5,2 | - | Nilai bobot kepentingan preferensi |
| 5 | jenis | ENUM | - | - | Klasifikasi kriteria (Benefit / Cost) |

## 3.5 Perancangan Tampilan Antarmuka (Wireframe / Mockup)
<!-- PANDUAN PENULISAN SUBBAB 3.5:
Rancangan antarmuka pengguna disusun dengan mengedepankan prinsip kemudahan penggunaan (User Experience) dan tata letak yang ergonomis:
1. Perancangan Halaman Login
2. Perancangan Menu Utama (Dashboard)
3. Perancangan Form Input Data Kriteria dan Alternatif
4. Perancangan Halaman Hasil Keputusan dan Cetak Laporan
-->

Rancangan antarmuka pengguna dirancang dengan mengedepankan prinsip kemudahan penggunaan (*User Experience*) dan tata letak yang ergonomis:
1. **Perancangan Halaman Login**: Menyediakan form masukan nama pengguna dan kata sandi dengan validasi keamanan.
2. **Perancangan Menu Utama (Dashboard)**: Menyajikan ringkasan statistik jumlah data kriteria, alternatif, dan tombol navigasi modul utama.
3. **Perancangan Form Master Kriteria**: Menyediakan sarana penambahan, pengubahan, dan pengaturan bobot kriteria.
4. **Perancangan Form Penilaian Alternatif**: Antarmuka terstruktur untuk memasukkan nilai evaluasi alternatif berdasarkan parameter kriteria.
5. **Perancangan Halaman Proses Komputasi dan Laporan**: Menampilkan visualisasi langkah perhitungan matematis, tabel perangkingan hasil keputusan akhir, dan fasilitas ekspor laporan.
