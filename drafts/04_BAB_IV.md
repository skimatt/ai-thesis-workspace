# BAB IV
# IMPLEMENTASI SISTEM

## 4.1 Batasan dan Lingkungan Implementasi
<!-- PANDUAN PENULISAN SUBBAB 4.1:
Implementasi sistem merupakan tahap penerjemahan rancangan logis dan arsitektur yang telah disusun pada BAB III ke dalam bentuk program fisik yang siap dijalankan pada lingkungan operasional yang sebenarnya.
-->

### 4.1.1 Kebutuhan Perangkat Keras (Hardware)
Pengembangan dan pengujian operasional sistem dilaksanakan menggunakan seperangkat komputer dengan konfigurasi perangkat keras sebagai berikut:
1. **Unit Pemroses Sentral (CPU)**: Prosesor Intel Core i5 / AMD Ryzen 5 berkecepatan minimal 2.4 GHz multi-core.
2. **Memori Utama (RAM)**: Kapasitas memori 8 GB DDR4 untuk menjamin kelancaran pemrosesan data konkuren.
3. **Media Penyimpanan**: Solid State Drive (SSD) dengan sisa ruang kosong minimal 50 GB.
4. **Perangkat Masukan dan Keluaran**: Papan ketik (*keyboard*), tetikus (*mouse*), monitor beresolusi Full HD (1920x1080), serta printer untuk verifikasi cetak fisik dokumen laporan.

### 4.1.2 Kebutuhan Perangkat Lunak (Software)
Lingkungan perangkat lunak yang dikonfigurasi selama tahapan implementasi meliputi susunan teknologi berikut:
1. **Sistem Operasi**: Microsoft Windows 11 Pro 64-bit sebagai lingkungan utama pengkodean dan pengujian lokal.
2. **Lingkungan Pengembangan (IDE)**: Visual Studio Code dilengkapi ekstensi bahasa dan penataan format kode.
3. **Penerjemah Bahasa Pemrograman**: Runtime lingkungan pemrograman modern tingkat tinggi sesuai spesifikasi pada CONTEXT_SKRIPSI.txt.
4. **Server Basis Data**: MySQL Server versi 8.0 dengan antarmuka manajemen basis data relasional.
5. **Peramban Web (Browser)**: Google Chrome dan Mozilla Firefox versi terbaru sebagai lingkungan pengujian antarmuka pengguna.

## 4.2 Implementasi Modul Komputasi / Algoritma
<!-- PANDUAN PENULISAN SUBBAB 4.2:
1. Uraikan logika pemrograman modul komputasi algoritma yang telah dibangun.
2. Jelaskan struktur fungsi/method utama (misal: normalisasi bobot, kalkulasi vektor preferensi, pengurutan/sorting nilai perankingan).
3. Sajikan potongan kode program inti (clean code snippet) yang mengimplementasikan formula matematis tersebut.
-->

[Draf implementasi modul logika pemrograman, fungsi komputasi algoritma, dan dokumentasi algoritma ke dalam bahasa pemrograman akan disusun secara rinci oleh AI Agent]

## 4.3 Implementasi Antarmuka Pengguna (User Interface)
<!-- PANDUAN PENULISAN SUBBAB 4.3:
Dokumentasikan tampilan layar sistem nyata yang telah dibangun (screenshot faktual dari folder ASSETS/SCREENSHOOT/):
1. Gambar 4.1: Antarmuka Form Login Sistem
2. Gambar 4.2: Antarmuka Menu Utama (Dashboard)
3. Gambar 4.3: Antarmuka Form Penginputan Data Master Kriteria dan Alternatif
4. Gambar 4.4: Antarmuka Hasil Perhitungan Keputusan dan Cetak Laporan
-->

Hasil konstruksi antarmuka pengguna sistem perangkat lunak yang telah dibangun diwujudkan dalam beberapa layar fungsional utama:
1. **Antarmuka Form Autentikasi Login**: Halaman pembuka yang mengamankan hak akses sistem berdasarkan kredensial akun pengguna terdaftar.
2. **Antarmuka Menu Utama (Dashboard)**: Halaman beranda yang menyajikan informasi statistik ringkas, status data operasional, dan navigasi menu terstruktur.
3. **Antarmuka Master Kriteria dan Bobot**: Halaman manajemen untuk meninjau, memperbarui, dan menyimpan konfigurasi kriteria penilaian beserta nilai bobot preferensinya.
4. **Antarmuka Penginputan Data Alternatif dan Nilai**: Form interaktif yang memfasilitasi pengguna dalam menginput data identitas alternatif serta mengisikan nilai skor untuk setiap parameter kriteria.
5. **Antarmuka Modul Eksekusi Perhitungan**: Halaman pemrosesan yang menyajikan tombol eksekusi kalkulasi algoritma secara otomatis dan menampilkan rincian hasil matriks perhitungan langkah demi langkah.
6. **Antarmuka Tampilan dan Cetak Laporan**: Halaman penyajian tabel rekomendasi urutan rangking terbaik yang dilengkapi fitur cetak dokumen formal berformat portabel untuk diserahkan kepada pimpinan instansi.
