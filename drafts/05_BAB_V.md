# BAB V
# PENGUJIAN DAN PEMBAHASAN

## 5.1 Pengujian Model / Algoritma Komputasi
<!-- PANDUAN PENULISAN SUBBAB 5.1:
1. Verifikasi matematis: Bandingkan hasil perhitungan otomatis sistem terhadap kalkulasi manual formula teori di BAB II.
2. Gunakan data sampel alternatif faktual yang memiliki variasi skor pada seluruh kriteria.
3. Sajikan tabel normalisasi bobot, tabel kalkulasi nilai preferensi, dan tabel perangkingan akhir untuk membuktikan akurasi 100% presisi bebas deviasi galat komputasi.
-->

Pengujian model komputasi bertujuan memverifikasi ketepatan logika matematis sistem dengan cara membandingkan hasil perhitungan yang dieksekusi secara otomatis oleh perangkat lunak terhadap hasil kalkulasi manual yang dihitung berlandaskan formulasi teoritis formal pada BAB II. Data uji yang digunakan adalah data sampel alternatif faktual yang memiliki variasi nilai pada seluruh kriteria penilaian.

[Draf rincian langkah perhitungan matematis komparatif manual vs sistem akan disusun oleh AI Agent berlandaskan data sampel empiris terverifikasi]

## 5.2 Pengujian Fungsional Sistem (Black Box Testing)
<!-- PANDUAN PENULISAN SUBBAB 5.2:
Pengujian fungsionalitas sistem dilakukan menggunakan metode Black Box Testing untuk memastikan bahwa seluruh fungsi form, tombol, navigasi, validasi masukan, transaksi basis data, dan modul laporan beroperasi sesuai spesifikasi kebutuhan pada BAB III.
-->

Pengujian fungsionalitas sistem dilakukan menggunakan metode *Black Box Testing* guna memastikan seluruh komponen perangkat lunak bekerja secara optimal dan bebas dari kesalahan fungsional (*functional bugs*):

### Tabel 5.1 Hasil Pengujian Black Box Testing Sistem
| No | Komponen / Form yang Diuji | Butir Pengujian | Skenario Uji | Hasil yang Diharapkan | Hasil Pengamatan | Kesimpulan |
|:---:|:---|:---|:---|:---|:---|:---:|
| 1 | Form Autentikasi Login | Validasi Kredensial Benar | Memasukkan username dan password yang sah | Sistem menerima login dan mengarahkan pengguna ke Dashboard utama | Berhasil masuk ke halaman Dashboard utama | Valid |
| 2 | Form Autentikasi Login | Validasi Kredensial Salah | Memasukkan password yang keliru | Sistem menolak akses dan menampilkan pesan peringatan error | Muncul pesan peringatan error dan akses ditolak | Valid |
| 3 | Form Master Data Kriteria | Penambahan dan Edit Data | Mengisi form kriteria lengkap lalu menekan tombol simpan | Data kriteria dan bobot baru tersimpan ke dalam database MySQL | Data tersimpan dan tabel kriteria terbarui | Valid |
| 4 | Form Penilaian Alternatif | Validasi Rentang Nilai | Memasukkan nilai di luar batas skala parameter yang diizinkan | Sistem menolak masukan dan meminta pengguna mengoreksi nilai | Input diblokir dan muncul indikator batas nilai | Valid |
| 5 | Modul Komputasi Algoritma | Eksekusi Kalkulasi Otomatis | Menekan tombol proses kalkulasi pada data alternatif | Modul komputasi menghitung nilai preferensi dan menampilkan urutan ranking | Nilai preferensi dan urutan ranking tampil tepat | Valid |
| 6 | Modul Pelaporan Hasil | Ekspor Dokumen Laporan | Menekan tombol cetak laporan keputusan | Sistem menghasilkan berkas laporan digital siap cetak yang tertata rapi | Berkas laporan terunduh rapi sesuai format standar | Valid |

## 5.3 Pembahasan Hasil Penelitian
<!-- PANDUAN PENULISAN SUBBAB 5.3:
Lakukan analisis mendalam terhadap temuan pengujian yang mencakup 3 dimensi utama:
1. Peningkatan efisiensi waktu operasional (sebelum vs sesudah sistem diterapkan).
2. Peningkatan objektivitas dan akurasi keputusan (menghilangkan bias subjektif manual).
3. Implikasi praktis bagi manajemen dan efektivitas tata kelola data di objek penelitian.
-->

[Draf pembahasan analitis hasil penelitian, komparasi kinerja sebelum vs sesudah penerapan sistem terkomputerisasi, dan implikasi manajerial akan diuraikan secara kritis dan mendalam oleh AI Agent]
