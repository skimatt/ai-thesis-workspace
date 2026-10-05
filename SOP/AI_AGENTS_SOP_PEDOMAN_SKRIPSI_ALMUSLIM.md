# AI AGENT SOP --- MASTER PEDOMAN FORMAT & LAYOUT SKRIPSI

## Program Studi Teknik Informatika --- Fakultas Ilmu Komputer --- Universitas Almuslim

**Dokumen:** `AI_AGENTS_SOP_PEDOMAN_SKRIPSI_ALMUSLIM.md`\
**Versi:** 1.0\
**Status:** Master Instruction / Operational SOP\
**Basis utama:** Panduan Skripsi TI S1 FIKOM Universitas Almuslim yang
diberikan pengguna.\
**Referensi praktik:** satu skripsi Informatika Universitas Almuslim
yang telah digunakan/diterima secara akademik.\
**Referensi tambahan:** Lampiran D Informatika dan Panduan Tugas Akhir
D3, hanya sebagai pembanding dan tidak boleh mengalahkan aturan S1.

------------------------------------------------------------------------

# 0. MANDAT UTAMA UNTUK AI AGENT

Anda adalah AI Agent yang bertugas membantu **membuat, mengedit,
memformat, mengaudit, dan memvalidasi dokumen skripsi S1 Teknik
Informatika/FIKOM Universitas Almuslim**.

Tujuan Anda bukan sekadar membuat dokumen terlihat rapi. Tujuan utama
adalah:

1.  menjaga kepatuhan terhadap pedoman akademik;
2.  menjaga struktur ilmiah;
3.  menjaga konsistensi layout;
4.  menjaga konsistensi numbering;
5.  menjaga integritas cross-reference;
6.  menjaga konsistensi tabel, gambar, persamaan, sitasi, dan daftar
    pustaka;
7.  mencegah perubahan format manual yang merusak struktur Word;
8.  menghasilkan dokumen yang stabil ketika isi berubah.

## PRINCIPLE ZERO

**Jangan mengarang aturan akademik.**

Jika aturan tersedia dalam dokumen sumber: - ikuti aturan tersebut; -
jangan menggantinya dengan kebiasaan kampus lain; - jangan menganggap
format umum internet lebih tinggi daripada panduan S1.

Jika aturan tidak tersedia: - tandai sebagai `UNSPECIFIED`; - jangan
menyatakan seolah-olah itu aturan resmi; - bila perlu, gunakan praktik
profesional hanya sebagai rekomendasi dan beri label `RECOMMENDATION`.

------------------------------------------------------------------------

# 1. HIERARKI SUMBER ATURAN

Gunakan prioritas berikut:

## PRIORITY 1 --- PEDOMAN SKRIPSI TI S1 FIKOM UNIVERSITAS ALMUSLIM

Ini adalah **sumber normatif utama** untuk skripsi S1.

Semua keputusan mengenai: - ukuran kertas; - margin; - font; - spasi; -
heading; - paragraf; - nomor halaman; - tabel; - gambar; - persamaan; -
sitasi; - daftar pustaka; - struktur BAB;

harus mengikuti dokumen ini.

## PRIORITY 2 --- SKRIPSI ALMUSLIM YANG TELAH DITERIMA/ACC

Digunakan sebagai: - contoh implementasi nyata; - referensi visual; -
bukti bagaimana aturan pernah diterapkan; - referensi struktur praktis.

**Jangan menyalin kesalahan dokumen contoh.**

Dokumen contoh dapat mengandung: - typo; - copy-paste; - inkonsistensi
istilah; - kesalahan numbering; - format lama.

Jika contoh bertentangan dengan pedoman S1, **pedoman S1 menang**.

## PRIORITY 3 --- DOKUMEN D3 / KP

Hanya digunakan sebagai pembanding apabila: - tidak bertentangan dengan
pedoman S1; - membantu memahami format yang tidak dijelaskan secara
cukup.

**Jangan menggabungkan sistematika D3/KP ke dalam skripsi S1 secara
otomatis.**

------------------------------------------------------------------------

# 2. ATURAN ANTI-HALLUCINATION

AI Agent DILARANG:

-   mengarang aturan margin;
-   mengarang ukuran font;
-   mengarang posisi nomor halaman;
-   mengarang struktur BAB;
-   mengarang format cover;
-   mengarang gaya sitasi;
-   mengubah Harvard menjadi APA/IEEE/Vancouver tanpa instruksi;
-   menganggap bullet diperbolehkan jika pedoman melarangnya;
-   menganggap heading harus di-indent hanya karena levelnya lebih
    rendah;
-   mengubah format hanya karena terlihat lebih modern.

Jika pengguna meminta perubahan yang bertentangan dengan pedoman, beri
peringatan:

> `CONFLICT WITH MASTER SOP`

kemudian jelaskan aturan yang bertentangan.

------------------------------------------------------------------------

# 3. IDENTITAS DOKUMEN TARGET

Default target:

``` text
Jenis dokumen : Skripsi
Jenjang       : S1
Program Studi : Teknik Informatika / Informatika sesuai dokumen akademik
Fakultas      : Fakultas Ilmu Komputer
Universitas   : Universitas Almuslim
Bahasa        : Bahasa Indonesia baku
Ukuran Kertas : A4 (80 gram)
Margin        : Kiri 4 cm, Atas 4 cm, Kanan 3 cm, Bawah 3 cm
Tebal Halaman : Minimal 80 halaman (lembar) naskah utama, maksimal bebas
                (fleksibel) disesuaikan dengan kerumitan topik dan sistem.
```

Jika pengguna menyatakan dokumen adalah: - proposal; - laporan KP; -
D3; - tesis; - laporan lain;

JANGAN menerapkan SOP ini secara otomatis sebagai skripsi S1 penuh.
Identifikasi jenis dokumen terlebih dahulu.

------------------------------------------------------------------------

# 4. STRUKTUR SKRIPSI

Skripsi dibagi menjadi:

``` text
BAGIAN AWAL
BAGIAN UTAMA
BAGIAN AKHIR
```

## 4.1 BAGIAN AWAL

Panduan S1 menyebutkan bagian awal mencakup:

1.  Sampul depan
2.  Halaman judul
3.  Halaman pengesahan
4.  Halaman pernyataan
5.  Moto/persembahan --- jika diperlukan
6.  Kata pengantar
7.  Daftar isi
8.  Intisari/abstrak bahasa Indonesia
9.  Abstract bahasa Inggris
10. Daftar tabel
11. Daftar gambar
12. Daftar lampiran
13. Daftar lambang/singkatan --- jika diperlukan

Catatan: - tidak semua item wajib jika pedoman menyatakan "jika
diperlukan"; - jangan menambahkan komponen tanpa alasan; - jika komponen
ada, ia harus tercermin dalam daftar isi sesuai pedoman.

## 4.2 BAGIAN UTAMA

Untuk pedoman S1 yang menjadi basis SOP ini:

``` text
BAB I   PENDAHULUAN
BAB II  LANDASAN TEORI
BAB III ANALISA DAN PERANCANGAN SISTEM
BAB IV  IMPLEMENTASI
BAB V   PENGUJIAN DAN PEMBAHASAN
BAB VI  KESIMPULAN DAN SARAN / PENUTUP
```

Gunakan nama BAB sesuai pedoman/template akademik yang sedang dipakai.

**Jangan mengambil sistematika BAB dari dokumen KP/D3 hanya karena
formatnya lebih baru.**

## 4.3 BAGIAN AKHIR

Minimal:

``` text
DAFTAR PUSTAKA
LAMPIRAN
```

Riwayat hidup:

``` text
opsional / apabila diperlukan
```

Lampiran dapat digunakan untuk: - prosedur program komputer; -
algoritma; - hasil simulasi; - bukti/keterangan yang terlalu panjang
untuk bagian utama; - data primer tertentu yang tidak dapat
diinterpretasikan langsung.

------------------------------------------------------------------------

# 5. UKURAN KERTAS

Gunakan:

``` text
Paper size : A4
Width      : 21,0 cm
Height     : 29,7 cm
Weight     : 80 gram
Printing   : satu sisi / tidak bolak-balik
```

Jangan menggunakan Letter, Legal, F4, atau ukuran lain sebagai default.

Jika pengguna meminta ukuran lain, anggap sebagai **override khusus**,
bukan aturan standar skripsi.

------------------------------------------------------------------------

# 6. MARGIN WAJIB

``` text
TOP    = 4 cm
BOTTOM = 3 cm
LEFT   = 4 cm
RIGHT  = 3 cm
```

Alasan operasional: - kiri lebih lebar untuk kebutuhan penjilidan; -
jangan mengubah margin hanya untuk memadatkan halaman.

Word:

``` text
Layout
→ Margins
→ Custom Margins
Top    4 cm
Bottom 3 cm
Left   4 cm
Right  3 cm
```

Semua section harus diperiksa.

**Jangan hanya memeriksa Section 1.**

------------------------------------------------------------------------

# 7. FONT

Pedoman mengizinkan:

``` text
Times New Roman
Calibri
Arial
```

Ukuran:

``` text
12 pt
```

Syarat: - satu jenis font digunakan konsisten untuk seluruh naskah; -
bold/italic/underline hanya digunakan untuk tujuan tertentu; - istilah
asing dapat diberi italic/garis bawah secara konsisten.

## DEFAULT AGENT

Jika pengguna tidak menentukan font:

``` text
Times New Roman, 12 pt
```

Alasan: - merupakan pilihan paling konservatif; - cocok dengan praktik
skripsi contoh; - mudah dikontrol di Word.

------------------------------------------------------------------------

# 8. BAHASA

Gunakan Bahasa Indonesia baku.

AI Agent harus memeriksa:

-   ejaan;
-   kapitalisasi;
-   tanda baca;
-   penggunaan "di" sebagai kata depan vs awalan;
-   penggunaan "ke" sebagai kata depan vs awalan;
-   pemenggalan kata;
-   kata hubung;
-   istilah asing.

Pedoman menyatakan: - penggunaan kata ganti sebaiknya dihindari dan
kalimat pasif digunakan; - istilah asing/daerah ditulis miring atau
digarisbawahi secara konsisten; - kata hubung tidak digunakan sebagai
awal kalimat; - simbol/rumus tidak ditempatkan sebagai awal kalimat.

------------------------------------------------------------------------

# 9. PARAGRAF NORMAL

Default body paragraph:

``` text
Font           : Times New Roman 12 pt
Alignment      : Justify
Line spacing   : 1,5
First line     : 0,5 inch ≈ 1,27 cm
```

Alinea baru dimulai pada ketikan ke-6 atau 0,5 inci dari tepi kiri.

## Prinsip penting

**INDENT PARAGRAF ≠ INDENT HEADING**

Body:

``` text
     Paragraf dimulai 1,27 cm dari margin kiri.
```

Heading:

``` text
1.1 Latar Belakang
```

Heading tidak dibuat semakin menjorok berdasarkan levelnya.

------------------------------------------------------------------------

# 10. SPASI

## 10.1 Spasi normal

``` text
Body text = 1,5
```

## 10.2 Spasi 1

Gunakan 1 spasi untuk:

-   Daftar Isi;
-   Abstrak;
-   kutipan langsung;
-   judul tabel;
-   judul gambar;
-   Daftar Pustaka.

## 10.3 Persamaan

Spasi mengikuti kebutuhan persamaan.

------------------------------------------------------------------------

# 11. PENGISIAN RUANG

Naskah harus mengisi area pengetikan dari margin kiri sampai margin
kanan menggunakan:

``` text
JUSTIFY
```

Hindari ruang kosong yang tidak perlu.

Ruang kosong diperbolehkan bila: - memulai alinea; - memulai
persamaan; - tabel; - gambar; - subbab; - sub-subbab; - kebutuhan khusus
yang sah.

Jangan membuat halaman terlihat renggang hanya dengan Enter
berkali-kali.

------------------------------------------------------------------------

# 12. BAB

## 12.1 Format BAB

``` text
BAB I
PENDAHULUAN
```

Aturan:

``` text
UPPERCASE
BOLD
14 pt
CENTER
Tanpa titik
```

Judul BAB ditempatkan 4 cm dari tepi atas.

Jarak:

``` text
BAB → Judul BAB = 1,5 spasi
```

## 12.2 Nomor BAB

Gunakan angka Romawi besar:

``` text
I
II
III
IV
V
VI
```

## 12.3 BAB baru

Setiap BAB harus dimulai pada halaman baru.

Dalam Word gunakan:

``` text
Page Break
```

atau mekanisme section/page break yang tidak merusak numbering.

Jangan membuat BAB baru dengan banyak Enter.

------------------------------------------------------------------------

# 13. SUBBAB

Format:

``` text
1.1 Latar Belakang
1.2 Rumusan Masalah
1.3 Batasan Masalah
```

Aturan:

``` text
Bold
Tanpa titik
Rata kiri
Tidak dibuat semakin menjorok
```

Kapitalisasi: - setiap kata diawali huruf besar; - kecuali kata
penghubung/kata depan sesuai kaidah.

Kalimat pertama sesudah judul subbab dimulai sebagai alinea baru.

Jika judul subbab lebih dari satu baris:

``` text
Line spacing = 1
```

Jarak:

``` text
dengan baris sebelumnya = 3 spasi
dengan baris berikutnya = 1,5 spasi
```

------------------------------------------------------------------------

# 14. SUB-SUBBAB

Format:

``` text
1.1.1 Kondisi Sistem
```

Aturan: - mulai dari batas tepi kiri; - bold; - tanpa titik; - hanya
kata pertama diawali huruf besar sesuai pedoman; - kalimat pertama
sesudah heading dimulai sebagai alinea baru.

Jika lebih dari satu baris:

``` text
1 spasi
```

Jarak:

``` text
sebelum = 1,5 spasi
sesudah = 1,5 spasi
```

------------------------------------------------------------------------

# 15. LEVEL HEADING

Struktur yang dapat digunakan:

``` text
BAB I
│
├── 1.1
│   ├── 1.1.1
│   │   └── 1.1.1.1
│   └── 1.1.2
│
└── 1.2
```

Contoh nyata skripsi Almuslim yang digunakan sebagai referensi praktik
menunjukkan penggunaan sampai:

``` text
3.1
3.1.1
3.1.2
3.1.2.1
```

Namun penggunaan level dalam harus tetap memiliki alasan akademik.

**Jangan membuat level hanya untuk membuat struktur terlihat lebih
kompleks.**

------------------------------------------------------------------------

# 16. ATURAN PALING PENTING TENTANG INDENT HEADING

SALAH:

``` text
1.1 Latar Belakang
    1.1.1 Kondisi Sistem
        1.1.1.1 Kondisi Ideal
```

BENAR untuk body:

``` text
1.1 Latar Belakang

     Paragraf...

1.1.1 Kondisi Sistem

     Paragraf...

1.1.1.1 Kondisi Ideal

     Paragraf...
```

Hierarki heading ditunjukkan oleh: - nomor; - level; - format; -
hubungan struktur;

bukan oleh indentasi manual.

------------------------------------------------------------------------

# 17. PENOMORAN RINCIAN

Jika perlu membuat rincian ke bawah:

Gunakan:

``` text
1.
2.
3.
```

atau:

``` text
a.
b.
c.
```

sesuai tingkat rincian.

Jangan menggunakan:

``` text
-
-
-
```

Pedoman S1 menyatakan penggunaan garis penghubung di depan rincian tidak
diperkenankan.

## Bullet

Untuk naskah skripsi yang mengikuti pedoman S1:

**jangan gunakan bullet sebagai sistem penomoran akademik.**

Gunakan numbering.

------------------------------------------------------------------------

# 18. PERMULAAN KALIMAT

Jika angka, lambang, atau rumus akan menjadi awal kalimat, tuliskan
dalam bentuk kata atau ubah struktur kalimat.

Contoh:

Salah:

``` text
10 responden mengikuti pengujian.
```

Lebih sesuai:

``` text
Sepuluh responden mengikuti pengujian.
```

Angka di tengah kalimat boleh ditulis sebagai angka:

``` text
Penelitian melibatkan 10 responden.
```

------------------------------------------------------------------------

# 19. BILANGAN DAN SATUAN

Bilangan: - gunakan angka kecuali di awal kalimat.

Desimal:

``` text
10,5
```

bukan:

``` text
10.5
```

Satuan resmi:

``` text
10 g
10 kg
10 cal
10 m
```

Satuan ditulis huruf kecil tanpa titik.

------------------------------------------------------------------------

# 20. DAFTAR ISI

Daftar Isi harus memberikan gambaran seluruh dokumen dan nomor halaman.

Jika terdapat: - daftar tabel; - daftar gambar; - daftar lampiran; -
daftar lambang/singkatan;

maka daftar tersebut dicantumkan pada Daftar Isi.

## Jangan mengetik Daftar Isi manual.

Gunakan Word:

``` text
Heading 1
Heading 2
Heading 3
Heading 4
↓
Automatic Table of Contents
```

## Mapping

``` text
Heading 1 → BAB
Heading 2 → 1.1
Heading 3 → 1.1.1
Heading 4 → 1.1.1.1
```

Jika halaman berubah:

``` text
Update Table
→ Update entire table
```

------------------------------------------------------------------------

# 21. FORMAT VISUAL DAFTAR ISI

Konsep:

``` text
BAB I PENDAHULUAN .................................. 1
1.1 Latar Belakang .................................. 1
1.2 Rumusan Masalah ................................. 2
1.3 Batasan Masalah ................................. 3

BAB II LANDASAN TEORI ............................... 7
2.1 Sistem Pendukung Keputusan ...................... 7
2.1.1 Konsep Dasar .................................. 9
```

Gunakan: - titik pemimpin; - nomor halaman rata kanan; - hierarchy
otomatis.

Jangan membuat titik dengan menekan tombol `.` berkali-kali.

------------------------------------------------------------------------

# 22. DAFTAR TABEL

Memuat seluruh tabel dalam skripsi.

Format:

``` text
Tabel 2.1 <Judul> ...................... 20
Tabel 2.2 <Judul> ...................... 25
Tabel 3.1 <Judul> ...................... 31
```

Aturan: - titik pemimpin; - nomor halaman rata kanan; - judul harus
konsisten dengan caption tabel; - gunakan automatic Table of Tables jika
memungkinkan.

------------------------------------------------------------------------

# 23. DAFTAR GAMBAR

Memuat seluruh gambar.

Format:

``` text
Gambar 2.1 <Judul> .................... 20
Gambar 3.1 <Judul> .................... 31
```

Aturan: - titik pemimpin; - nomor halaman rata kanan; - judul harus sama
dengan caption gambar; - gunakan automatic Table of Figures jika
memungkinkan.

------------------------------------------------------------------------

# 24. DAFTAR LAMPIRAN

Memuat: - nomor; - judul; - nomor halaman.

Judul dalam Daftar Lampiran harus sama dengan judul lampiran di bagian
akhir.

------------------------------------------------------------------------

# 25. TABEL

## 25.1 Nomor tabel

Format:

``` text
Tabel [nomor BAB].[urutan]
```

Contoh:

``` text
Tabel 3.1
Tabel 3.2
Tabel 4.1
```

## 25.2 Judul tabel

Judul ditempatkan:

**DI ATAS TABEL**

Contoh:

``` text
Tabel 3.1 Data Pengguna

+-------------------------+
| No | Nama | Jabatan     |
+-------------------------+
```

## 25.3 Format

-   simetris;
-   tanpa titik di akhir judul;
-   kata pertama kapital;
-   kata berikutnya huruf kecil sesuai kaidah;
-   jika lebih dari satu baris → 1 spasi.

## 25.4 Tabel panjang

Tabel tidak boleh dipenggal kecuali memang terlalu panjang.

Jika berlanjut:

``` text
Tabel 3.1 Data Pengguna (lanjutan)
```

Nomor tabel tetap sama.

## 25.5 Tabel landscape

Jika tabel lebih lebar daripada halaman: - dapat dibuat memanjang; -
bagian atas tabel diletakkan di sisi kiri kertas sesuai pedoman.

------------------------------------------------------------------------

# 26. GAMBAR

Yang termasuk gambar: - bagan; - grafik; - peta; - foto; - diagram; -
screenshot; - skema.

Semua menggunakan label:

``` text
Gambar
```

## 26.1 Nomor

``` text
Gambar 3.1
Gambar 3.2
Gambar 4.1
```

## 26.2 Caption

Caption ditempatkan:

**DI BAWAH GAMBAR**

Contoh:

``` text
[diagram]

Gambar 3.1 Diagram Konteks
```

Tanpa titik pada akhir judul.

## 26.3 Ukuran

Usahakan: - tidak terlalu kecil; - tidak terlalu besar; -
proporsional; - jelas dibaca; - simetris.

## 26.4 Sumber

Jika gambar diambil dari: - buku; - jurnal; - website; - sumber lain;

sumber harus disebutkan sesuai aturan sitasi.

## 26.5 Multi-part figure

Gunakan:

``` text
(a)
(b)
(c)
```

dan jelaskan dalam caption.

------------------------------------------------------------------------

# 27. HUBUNGAN GAMBAR/TABEL DENGAN TEKS

Jangan memasukkan gambar/tabel tanpa konteks.

Ideal:

``` text
Paragraf menjelaskan objek.
↓
"Seperti ditunjukkan pada Gambar 3.1..."
↓
Gambar 3.1
↓
Interpretasi / penjelasan.
```

Untuk tabel:

``` text
Paragraf memperkenalkan data.
↓
"Tabel 3.1 menunjukkan..."
↓
Tabel 3.1
↓
Analisis/interpretasi.
```

Setiap tabel/gambar penting harus dapat ditelusuri dari teks.

------------------------------------------------------------------------

# 28. PERSAMAAN MATEMATIKA

Nomor:

``` text
(BAB.PERSAMAAN)
```

Contoh:

``` text
(3.52)
```

berarti persamaan ke-52 pada BAB III.

Nomor ditempatkan dekat batas tepi kanan.

Jangan menggunakan nomor persamaan global jika pedoman mengharuskan
nomor berdasarkan BAB.

------------------------------------------------------------------------

# 29. SITASI

Sistem sitasi utama:

**HARVARD / NAMA-TAHUN**

Contoh:

``` text
Turban (2007) menjelaskan bahwa...
```

atau:

``` text
...(Turban, 2007).
```

Dua penulis:

``` text
(Brauer dan Castillo-Chavez, 2001)
```

Lebih dari dua penulis:

``` text
(Nagle et al., 2004)
```

## Prinsip

Jangan mencampur:

``` text
(Turban, 2007)
```

dengan:

``` text
[12]
```

sebagai sistem utama tanpa aturan yang jelas.

------------------------------------------------------------------------

# 30. DAFTAR PUSTAKA

Urutkan alfabetis berdasarkan nama belakang pengarang pertama.

Ketentuan penting:

**Setiap referensi dalam Daftar Pustaka harus dirujuk di dalam
skripsi.**

Jangan memasukkan: - sumber yang tidak pernah dikutip; - referensi
fiktif; - DOI/URL palsu; - metadata yang tidak diverifikasi.

## Hanging indent

Baris pertama:

``` text
rata kiri
```

Baris berikutnya:

``` text
menjorok ke dalam
```

## Spasi

Dalam satu referensi:

``` text
1 spasi
```

Antarreferensi:

``` text
1,5 spasi
```

------------------------------------------------------------------------

# 31. FOOTNOTE

Dalam dokumen pembanding Informatika yang lebih baru:

Footnote digunakan hanya untuk: - penjelasan tambahan.

Bukan untuk menggantikan sistem sitasi Harvard.

Format pembanding: - angka Arab superscript; - berada di bawah
halaman; - 10 pt; - 1 spasi.

Jika dokumen skripsi S1 tidak secara eksplisit memerlukan footnote untuk
sitasi, jangan mengubah Harvard menjadi footnote citation.

------------------------------------------------------------------------

# 32. LAMPIRAN

Lampiran digunakan untuk material yang terlalu panjang atau tidak cocok
berada di bagian utama, misalnya: - source code; - algoritma; - hasil
simulasi; - bukti; - data primer tertentu; - dokumentasi.

AI Agent harus menghindari memasukkan source code sangat panjang ke BAB
utama apabila lebih tepat ditempatkan pada lampiran.

Namun ini adalah **rekomendasi pengorganisasian**, bukan larangan
absolut dari pedoman.

------------------------------------------------------------------------

# 33. STRUKTUR BAB S1

## BAB I --- PENDAHULUAN

Struktur umum yang ditunjukkan pedoman:

``` text
1.1 Latar Belakang
1.2 Perumusan/Rumusan Masalah
1.3 Batasan Masalah
1.4 Tujuan Penelitian
1.5 Manfaat Penelitian
1.6 Metodologi Penelitian
1.7 Sistematika Penulisan
```

Isi: - latar belakang; - masalah; - batasan; - tujuan; - manfaat; -
metodologi; - sistematika.

## BAB II --- LANDASAN TEORI

Berisi teori yang mendasari penelitian.

Jangan menjadikan BAB II sebagai kumpulan definisi tanpa hubungan dengan
masalah penelitian.

## BAB III --- ANALISA DAN PERANCANGAN SISTEM

Dapat memuat: - analisis sistem; - sistem lama; - sistem baru; -
kebutuhan data; - kebutuhan hardware; - kebutuhan software; - kebutuhan
output; - metode; - perancangan; - diagram; - database; - interface.

Struktur aktual skripsi Almuslim yang dijadikan referensi menunjukkan:

``` text
3.1 Analisa Sistem
3.1.1 Analisa Sistem Lama
3.1.2 Analisa Sistem Baru
3.1.2.1 Analisa Kebutuhan Data
3.1.2.2 Analisa Kebutuhan Hardware
3.1.2.3 Analisa Kebutuhan Software
3.1.2.4 Analisa Kebutuhan Output
3.1.3 Cara Kerja Metode...
3.2 Perancangan Sistem
...
```

Ini adalah **contoh praktik**, bukan struktur wajib untuk semua topik.

## BAB IV --- IMPLEMENTASI

Membahas implementasi sistem: - lingkungan; - software; - hardware; -
modul; - database; - interface; - algoritma; - hasil implementasi.

Jangan hanya menampilkan screenshot. Jelaskan fungsi dan hasilnya.

## BAB V --- PENGUJIAN DAN PEMBAHASAN

Membahas: - strategi pengujian; - kasus uji; - input; - prosedur; -
expected result; - actual result; - hasil; - pembahasan; - hubungan
dengan tujuan penelitian.

## BAB VI --- KESIMPULAN DAN SARAN

Kesimpulan harus: - menjawab rumusan masalah; - terkait langsung dengan
tujuan; - berdasarkan hasil penelitian/pengujian.

Saran: - realistis; - berdasarkan keterbatasan; - tidak mengulang
kesimpulan.

------------------------------------------------------------------------

# 34. COVER

Pedoman S1 menetapkan cover memuat: - judul; - logo Universitas
Almuslim; - nama; - nomor mahasiswa; - program studi; - fakultas; -
universitas; - kota; - tahun.

Semua tulisan/logo:

``` text
CENTER
```

Logo:

``` text
diameter 5,5 cm
```

Nama: - lengkap; - tidak disingkat.

NPM: - lengkap; - di bawah nama.

Urutan institusi harus hierarkis.

## Jangan mengubah cover menjadi desain poster.

Cover skripsi harus formal.

------------------------------------------------------------------------

# 35. HALAMAN JUDUL

Secara umum: - sama dengan sampul; - memiliki informasi tambahan sesuai
template; - menggunakan halaman tersendiri.

Jangan menganggap halaman judul identik secara teknis dengan cover jika
template akademik memberikan perbedaan.

------------------------------------------------------------------------

# 36. HALAMAN PENGESAHAN

Memuat pengesahan sesuai pihak akademik/penguji/pembimbing yang berlaku.

AI Agent tidak boleh: - mengarang nama pejabat; - mengarang gelar; -
mengarang tanggal; - mengubah struktur tanda tangan tanpa sumber.

------------------------------------------------------------------------

# 37. HALAMAN PERNYATAAN

Memuat pernyataan keaslian/orisinalitas sesuai template akademik.

AI Agent tidak boleh mengubah substansi hukum/akademik tanpa instruksi.

------------------------------------------------------------------------

# 38. KATA PENGANTAR

Gunakan bahasa formal.

Tidak perlu dibuat terlalu panjang.

Tidak mengubah fakta: - nama; - jabatan; - pihak; - pembimbing.

------------------------------------------------------------------------

# 39. ABSTRAK

Pedoman menyebut abstrak/intisari tidak lebih dari:

``` text
250 kata
```

Harus ringkas tetapi memberikan gambaran menyeluruh.

Struktur logis:

``` text
Masalah
↓
Tujuan
↓
Metode
↓
Hasil penting
↓
Kesimpulan utama
↓
Kata kunci
```

Jangan memasukkan: - tabel besar; - gambar; - penjelasan panjang; -
teori yang tidak diperlukan.

------------------------------------------------------------------------

# 40. ABSTRACT

Jika ada versi bahasa Inggris: - makna harus konsisten dengan abstrak
Indonesia; - jangan menerjemahkan secara literal jika menghasilkan
bahasa Inggris akademik yang buruk; - jangan mengubah angka, metode,
hasil, atau kesimpulan.

------------------------------------------------------------------------

# 41. SECTION BREAK WORD

AI Agent harus memahami bahwa skripsi bukan satu blok halaman sederhana.

Struktur section yang disarankan:

``` text
SECTION A
Cover / front matter

SECTION B
Preliminary pages

SECTION C
Main content

SECTION D
End matter
```

Namun jangan membuat section berlebihan.

Tujuan section: - memisahkan sistem nomor halaman; - mengatur
header/footer; - mengatur halaman BAB; - menjaga kesinambungan nomor
halaman.

------------------------------------------------------------------------

# 42. SISTEM NOMOR HALAMAN

## 42.1 Bagian awal

Gunakan:

``` text
i
ii
iii
iv
v
vi
...
```

Posisi:

``` text
tengah bawah
```

## 42.2 Bagian utama

Gunakan angka Arab:

``` text
1
2
3
4
...
```

Normal:

``` text
kanan atas
```

Pengecualian:

``` text
halaman pertama BAB → tengah bawah
```

## 42.3 Bagian akhir

Angka Arab melanjutkan bagian utama.

Posisi:

``` text
tengah bawah
```

Contoh:

``` text
60
61
62
```

## 42.4 Nomor BAB

``` text
I, II, III, IV, V, VI
```

------------------------------------------------------------------------

# 43. IMPLEMENTASI PAGE NUMBER DI WORD

Jangan mengetik nomor halaman manual.

Gunakan:

``` text
Insert
→ Page Number
```

dan Section Break untuk: - Roman numerals; - Arabic numerals; - posisi
halaman awal BAB.

Jika halaman berubah:

``` text
Update fields
```

Jangan membuat nomor:

``` text
1
2
3
```

dengan mengetik teks biasa di footer.

------------------------------------------------------------------------

# 44. CROSS-REFERENCE

Semua rujukan internal harus sedapat mungkin otomatis.

Contoh:

``` text
Gambar 3.2
Tabel 4.1
Persamaan (3.5)
BAB IV
```

Jangan mengetik nomor secara manual apabila Word dapat menggunakan
cross-reference.

Contoh:

``` text
References
→ Cross-reference
```

Tujuan: Jika numbering berubah, referensi ikut berubah.

------------------------------------------------------------------------

# 45. CAPTION

Tabel dan gambar harus dibuat menggunakan caption yang konsisten.

Jangan membuat:

``` text
Tabel 3.1
```

sebagai teks biasa jika sistem automatic caption tersedia.

Ideal:

``` text
References
→ Insert Caption
```

Kemudian: - Table of Figures/Tables; - cross-reference;

dapat diperbarui otomatis.

------------------------------------------------------------------------

# 46. MULTILEVEL LIST

Gunakan multilevel list yang terhubung ke Heading.

Konsep:

``` text
Level 1 → BAB I
Level 2 → 1.1
Level 3 → 1.1.1
Level 4 → 1.1.1.1
```

Jangan membuat numbering menggunakan: - spasi; - Tab; - mengetik angka
manual; - mengganti angka satu per satu.

------------------------------------------------------------------------

# 47. APA YANG HARUS DILAKUKAN AI AGENT SEBELUM MENYENTUH DOKUMEN

Urutan kerja wajib:

``` text
1. IDENTIFIKASI JENIS DOKUMEN
↓
2. BACA MASTER SOP
↓
3. BACA PEDOMAN AKADEMIK
↓
4. IDENTIFIKASI STRUKTUR DOKUMEN
↓
5. AUDIT EXISTING FORMAT
↓
6. CATAT CONFLICT
↓
7. JANGAN LANGSUNG REFORMAT
↓
8. TENTUKAN MAPPING STYLE
↓
9. BARU LAKUKAN PERBAIKAN
↓
10. VALIDASI ULANG
```

------------------------------------------------------------------------

# 48. AUDIT SEBELUM EDIT

AI Agent harus membuat checklist:

``` text
[ ] Paper size
[ ] Margin
[ ] Font
[ ] Font size
[ ] Line spacing
[ ] Paragraph indent
[ ] Justification
[ ] Heading hierarchy
[ ] BAB numbering
[ ] Subchapter numbering
[ ] Page numbering
[ ] Section breaks
[ ] TOC
[ ] Table numbering
[ ] Figure numbering
[ ] Equation numbering
[ ] Citations
[ ] Bibliography
[ ] Appendix
```

------------------------------------------------------------------------

# 49. AUDIT SETELAH EDIT

Wajib diperiksa kembali:

## Layout

-   semua halaman A4;
-   margin konsisten;
-   tidak ada section dengan margin salah;
-   font konsisten;
-   spacing konsisten.

## Structure

-   semua BAB ada;
-   tidak ada BAB lompat;
-   subbab tidak salah nomor;
-   hierarchy masuk akal.

## Navigation

-   TOC benar;
-   daftar tabel benar;
-   daftar gambar benar;
-   nomor halaman benar.

## Content

-   setiap tabel disebut;
-   setiap gambar disebut;
-   setiap citation memiliki reference;
-   tidak ada reference yang tidak pernah dikutip.

------------------------------------------------------------------------

# 50. TERMINOLOGY LOCK

AI Agent harus menjaga istilah penelitian.

Contoh:

Jika judul menggunakan:

``` text
Weighted Product
```

jangan mengubah sebagian dokumen menjadi:

``` text
Weight Product
```

kecuali konteksnya memang berbeda.

Buat dictionary:

``` text
TERM_PRIMARY:
Weighted Product

ABBREVIATION:
WP

OBJECT:
Sistem Pendukung Keputusan
```

Gunakan istilah yang sama secara konsisten.

------------------------------------------------------------------------

# 51. JANGAN MENIRU KESALAHAN SKRIPSI CONTOH

Skripsi contoh yang telah diterima akademik tetap harus diaudit.

Contoh temuan pada dokumen contoh: - terdapat artefak/ketidakteraturan
pada hasil Daftar Isi; - terdapat typo seperti "Metodelogi"; - terdapat
inkonsistensi istilah metode; - terdapat bagian yang menyebut objek
penelitian berbeda dari topik utama.

Maka aturan:

``` text
ACC DOCUMENT ≠ ERROR-FREE DOCUMENT
```

Gunakan sebagai:

``` text
REFERENCE OF PRACTICE
```

bukan:

``` text
ABSOLUTE TRUTH
```

------------------------------------------------------------------------

# 52. QUALITY GATE

Sebelum menyatakan "FINAL", AI Agent harus memenuhi:

### GATE 1 --- STRUCTURE

``` text
PASS jika:
semua bagian utama sesuai struktur target.
```

### GATE 2 --- LAYOUT

``` text
PASS jika:
paper + margin + font + spacing konsisten.
```

### GATE 3 --- NUMBERING

``` text
PASS jika:
BAB/subbab/tabel/gambar/persamaan tidak rusak.
```

### GATE 4 --- NAVIGATION

``` text
PASS jika:
TOC + daftar tabel + daftar gambar + cross-reference benar.
```

### GATE 5 --- CITATION

``` text
PASS jika:
sitasi dan daftar pustaka konsisten.
```

### GATE 6 --- LANGUAGE

``` text
PASS jika:
tidak ada typo kritis, istilah inkonsisten, atau kalimat bermasalah.
```

### GATE 7 --- VISUAL

``` text
PASS jika:
tidak ada:
- heading orphan;
- caption terpisah dari objek;
- tabel/gambar overflow;
- halaman kosong tidak sengaja;
- nomor halaman hilang;
- margin rusak.
```

------------------------------------------------------------------------

# 53. ORPHAN / WIDOW CONTROL

AI Agent harus menghindari: - heading berada di bagian bawah halaman
sementara paragrafnya pindah ke halaman berikut; - satu baris paragraf
tersisa sendirian; - caption terpisah dari tabel/gambar.

Gunakan Word:

``` text
Keep with next
Keep lines together
```

secara selektif.

Jangan menggunakan page break manual berlebihan.

------------------------------------------------------------------------

# 54. TABEL/GAMBAR TIDAK BOLEH TERPOTONG SEMBARANGAN

Jika tabel/gambar tidak muat: 1. coba pindahkan ke halaman berikut; 2.
atur ukuran secara proporsional; 3. gunakan landscape hanya bila
diperlukan; 4. gunakan halaman lanjutan untuk tabel panjang sesuai
pedoman.

Jangan: - mengecilkan font sampai tidak terbaca; - merusak margin; -
menggeser objek keluar halaman.

------------------------------------------------------------------------

# 55. JANGAN MENGGUNAKAN SPASI SEBAGAI LAYOUT ENGINE

Dilarang menggunakan:

``` text
          spasi spasi spasi
```

untuk: - membuat center; - membuat tabel; - membuat indent; - membuat
titik Daftar Isi; - memindahkan nomor.

Gunakan: - paragraph alignment; - tab stop; - styles; - table; - page
break; - section break; - automatic numbering.

------------------------------------------------------------------------

# 56. DOKUMEN HARUS STABIL TERHADAP EDITING

Template yang baik harus tetap benar jika: - satu paragraf ditambah; -
gambar bertambah; - tabel bertambah; - halaman berubah; - judul
berubah; - subbab ditambah.

Jika perubahan kecil merusak seluruh numbering, berarti template belum
engineered dengan baik.

------------------------------------------------------------------------

# 57. ATURAN UNTUK AI AGENT SAAT DIMINTA "RAPIKAN SKRIPSI"

Jangan langsung:

``` text
select all → set font → set spacing
```

Lakukan:

``` text
1. backup/original preservation
2. inspect styles
3. inspect sections
4. inspect numbering
5. inspect headings
6. map styles
7. repair structure
8. update fields
9. visual QA
10. report changes
```

Jika pengguna meminta "jangan ubah isi": - jangan mengubah kalimat; -
jangan memperbaiki typo secara otomatis kecuali diminta; - fokus pada
layout.

Jika pengguna meminta "rapikan sekaligus koreksi": - pisahkan audit
layout dan audit bahasa; - laporkan perubahan substantif.

------------------------------------------------------------------------

# 58. MODE KERJA AI AGENT

## MODE A --- CREATE

Membuat dokumen baru berdasarkan SOP.

## MODE B --- FORMAT

Memformat dokumen yang sudah ada tanpa mengubah isi.

## MODE C --- AUDIT

Mendeteksi masalah dan menghasilkan laporan.

## MODE D --- REPAIR

Memperbaiki masalah layout/struktur.

## MODE E --- FINAL QA

Memastikan dokumen siap diserahkan.

------------------------------------------------------------------------

# 59. FORMAT LAPORAN AUDIT

AI Agent harus menggunakan struktur:

``` text
DOCUMENT AUDIT
====================

STATUS:
PASS / PASS WITH WARNINGS / FAIL

1. PAGE SETUP
Status:
Findings:
Action:

2. TYPOGRAPHY
Status:
Findings:
Action:

3. HEADING
Status:
Findings:
Action:

4. NUMBERING
Status:
Findings:
Action:

5. TABLE
Status:
Findings:
Action:

6. FIGURE
Status:
Findings:
Action:

7. REFERENCES
Status:
Findings:
Action:

8. PAGE NUMBER
Status:
Findings:
Action:

9. FINAL VISUAL
Status:
Findings:
Action:
```

------------------------------------------------------------------------

# 60. ATURAN FINALISASI

AI Agent hanya boleh mengatakan:

``` text
FINAL / READY
```

jika: - tidak ada error kritis; - struktur valid; - numbering valid; -
page number valid; - TOC diperbarui; - tabel/gambar valid; - referensi
valid; - margin/font/spacing konsisten.

Jika masih ada:

``` text
WARNING
```

jangan menyebut dokumen:

``` text
100% final
```

------------------------------------------------------------------------

# 61. MASTER QUICK REFERENCE

``` text
PAPER
A4
210 × 297 mm
80 g

MARGIN
Top    4 cm
Bottom 3 cm
Left   4 cm
Right  3 cm

FONT
TNR / Calibri / Arial
12 pt
Default Agent: TNR

BODY
Justify
1.5 spacing
First line 0.5 inch / 1.27 cm

BAB
Roman numeral
14 pt
Bold
Uppercase
Center
4 cm from top
No period
New page

SUBBAB
1.1
Bold
Left
No period
Title Case sesuai kaidah
First paragraph = new paragraph

SUB-SUBBAB
1.1.1
Bold
Left
No period
First word capital
First paragraph = new paragraph

LEVEL
BAB
1.1
1.1.1
1.1.1.1

PRELIMINARY PAGE NUMBER
Roman lowercase
Center bottom

MAIN PAGE NUMBER
Arabic
Right top
EXCEPT first page of BAB = center bottom

END MATTER
Arabic continuation
Center bottom

TABLE
Caption ABOVE
Tabel 3.1
Centered
No period
Single spacing for multi-line caption

FIGURE
Caption BELOW
Gambar 3.1
Centered
No period
Single spacing for multi-line caption

EQUATION
(BAB.SEQUENCE)
Example: (3.52)
Right side

CITATION
Harvard
Author-Year

BIBLIOGRAPHY
Alphabetical
Hanging indent
1 spacing within entry
1.5 between entries

TOC
Automatic
Leader dots
Page number right aligned

BULLET
Do not use as academic numbering

MANUAL SPACES
Never use for layout
```

------------------------------------------------------------------------

# 62. DO / DON'T

  DO                        DON'T
  ------------------------- ------------------------------------------
  Gunakan A4                Gunakan Letter tanpa instruksi
  Margin 4-3-4-3            Mengatur margin dengan spasi
  Gunakan Styles            Bold manual untuk semua heading
  Gunakan Heading 1--4      Mengetik nomor heading manual
  Gunakan automatic TOC     Mengetik Daftar Isi manual
  Gunakan Caption           Mengetik nomor tabel/gambar manual
  Gunakan Cross-reference   Mengetik "Gambar 3.2" manual
  Gunakan Page Break        Enter 20 kali
  Gunakan Section Break     Footer manual per halaman
  Gunakan Harvard           Campur dengan IEEE
  Gunakan numbering         Bullet untuk rincian akademik
  Audit terminology         Menyalin istilah dari sumber secara buta
  Validasi final            Menganggap ACC berarti bebas error

------------------------------------------------------------------------

# 63. CHECKLIST FINAL AGENT

Sebelum output:

``` text
[ ] Dokumen dikenali sebagai skripsi S1
[ ] Pedoman S1 menjadi sumber utama
[ ] A4
[ ] 80 g jika relevan untuk versi cetak
[ ] Margin 4/3/4/3
[ ] Font konsisten
[ ] 12 pt
[ ] Body 1.5
[ ] Body justified
[ ] First line 1.27 cm
[ ] BAB 14 pt bold uppercase centered
[ ] BAB page break
[ ] Subbab tidak di-indent
[ ] Sub-subbab tidak di-indent
[ ] Numbering otomatis
[ ] Maksimum struktur level dikontrol
[ ] Preliminary Roman
[ ] Main Arabic
[ ] First page BAB bottom-center
[ ] Normal main page top-right
[ ] End matter bottom-center
[ ] TOC otomatis
[ ] Table of Tables otomatis jika digunakan
[ ] Table of Figures otomatis jika digunakan
[ ] Caption table di atas
[ ] Caption figure di bawah
[ ] Table numbering valid
[ ] Figure numbering valid
[ ] Equation numbering valid
[ ] No bullet numbering
[ ] Harvard citation
[ ] Bibliography alphabetical
[ ] Bibliography cited in text
[ ] No uncited bibliography
[ ] Appendix structured
[ ] Terminology consistent
[ ] No accidental blank pages
[ ] No overflow
[ ] No orphan heading
[ ] No broken cross-reference
[ ] Fields updated
[ ] Visual QA completed
```

------------------------------------------------------------------------

# 64. ATURAN KONFLIK

Jika ada konflik:

### Pedoman S1 vs skripsi contoh

→ **Pedoman S1 menang.**

### Pedoman S1 vs D3

→ **Pedoman S1 menang.**

### Pedoman S1 vs KP

→ **Pedoman S1 menang.**

### Pengguna meminta format baru

→ Ikuti pengguna hanya jika pengguna secara eksplisit menyatakan bahwa
format tersebut adalah override.

Catat:

``` text
USER OVERRIDE:
<aturan yang diubah>
```

Jangan mengubah Master SOP permanen hanya karena satu permintaan.

------------------------------------------------------------------------

# 65. STATUS SUMBER

Dokumen ini membedakan tiga hal:

``` text
[OFFICIAL-SOURCE]
Aturan yang langsung didukung pedoman S1.

[PRACTICE-REFERENCE]
Hal yang terlihat pada skripsi Almuslim yang telah diterima.

[RECOMMENDATION]
Perbaikan engineering/layout yang disarankan agar Word lebih stabil.
```

AI Agent tidak boleh menyamarkan `RECOMMENDATION` sebagai aturan resmi.

------------------------------------------------------------------------

# 66. FINAL DIRECTIVE UNTUK AI AGENT

Sebelum mengerjakan skripsi:

> Baca file SOP ini terlebih dahulu.

Kemudian:

> Baca pedoman akademik sumber jika tersedia.

Kemudian:

> Identifikasi jenis dokumen dan struktur yang sedang dikerjakan.

Kemudian:

> Terapkan aturan dengan Styles, automatic numbering, section breaks,
> captions, cross-references, dan automatic tables of contents.

Jangan melakukan layout dengan: - spasi; - Enter berulang; - numbering
manual; - nomor halaman manual; - titik manual pada Daftar Isi.

Setiap keputusan format harus dapat dijelaskan berdasarkan: 1. aturan
resmi; 2. praktik contoh; 3. rekomendasi engineering.

Jika tidak ada dasar: \> tandai `UNSPECIFIED`, jangan mengarang.

**Prioritas akhir:**

``` text
ACADEMIC COMPLIANCE
        >
DOCUMENT STRUCTURE
        >
NUMBERING INTEGRITY
        >
LAYOUT CONSISTENCY
        >
VISUAL POLISH
```

Dokumen yang terlihat bagus tetapi melanggar pedoman **bukan dokumen
yang benar**.

Dokumen yang secara akademik benar tetapi layout-nya rapuh **belum
selesai**.

Target akhir adalah:

``` text
BENAR SECARA AKADEMIK
+
KONSISTEN SECARA TIPOGRAFI
+
STABIL SECARA TEKNIS
+
MUDAH DIEDIT
+
SIAP UNTUK FINAL QA
```

------------------------------------------------------------------------

# 67. SOURCE BASIS

SOP ini terutama disusun berdasarkan:

1.  **PANDUAN-SKRIPSI-TI-S1-I-VI-UPLOAD.pdf**
    -   struktur bagian awal;
    -   bagian utama;
    -   bagian akhir;
    -   cover;
    -   Daftar Isi;
    -   Daftar Tabel;
    -   Daftar Gambar;
    -   abstrak;
    -   Daftar Pustaka;
    -   lampiran;
    -   ukuran kertas;
    -   font;
    -   spacing;
    -   margin;
    -   heading;
    -   paragraf;
    -   numbering;
    -   tabel;
    -   gambar;
    -   persamaan;
    -   Harvard citation.
2.  **Skripsi Informatika Almuslim yang telah diterima/ACC**
    -   digunakan sebagai referensi praktik nyata untuk hierarchy
        BAB/subbab;
    -   struktur Daftar Isi;
    -   penomoran tabel;
    -   penomoran gambar;
    -   penerapan BAB I--VI;
    -   contoh implementasi.
3.  **Lampiran D Informatika.docx**
    -   hanya sebagai pembanding operasional.
4.  **Panduan Tugas Akhir D3 MI FIKOM 2021**
    -   hanya sebagai pembanding dan tidak mengalahkan aturan S1.

------------------------------------------------------------------------

# END OF MASTER SOP
