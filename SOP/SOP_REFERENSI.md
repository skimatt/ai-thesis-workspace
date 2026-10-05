# SOP MANAJEMEN SUMBER DAN REFERENSI AKADEMIK

**Document ID:** SOP-REF-001  
**Version:** 1.0  
**Status:** MANDATORY  
**Scope:** Seluruh AI Agent dan proses sitasi/literatur di workspace ini.  

---

## 1. PRINSIP UTAMA: NO SOURCE, NO CLAIM

1. Setiap pernyataan ilmiah, teori, fakta eksternal, atau metodologi baku yang bukan gagasan asli mahasiswa **WAJIB** memiliki sumber referensi yang dapat diverifikasi.
2. AI Agent **DILARANG KERAS** mengarang:
   - Nama penulis atau nama jurnal/prosiding.
   - Tahun publikasi.
   - Judul artikel ilmiah atau buku.
   - Nomor DOI (Digital Object Identifier) atau link URL.
   - Volume, nomor issue, dan rentang halaman.
   - Isi kutipan, angka statistik, atau kesimpulan yang diatribusikan ke suatu sumber tanpa membaca sumber aslinya.
3. Jika informasi dari sumber belum diverifikasi secara nyata, statusnya adalah `UNVERIFIED` dan **TIDAK BOLEH** digunakan sebagai dasar klaim dalam naskah.

---

## 2. REPOSITORI DAN KATALOG REFERENSI

Seluruh referensi yang dikumpulkan dan digunakan harus tercatat di dalam:  
`REFERENSI/index.md`

### 2.1 Format ID Referensi
Setiap literatur wajib diberi pengenal unik:
- Format: `REF-001`, `REF-002`, `REF-003`, dst. (3 digit angka dengan padding nol).

### 2.2 Atribut Wajib Setiap Referensi
Setiap entri referensi wajib memiliki atribut:
1. **ID**: Pengenal unik (misal `REF-001`).
2. **Judul**: Judul lengkap publikasi sesuai dokumen asli.
3. **Penulis**: Seluruh penulis sesuai urutan di naskah asli.
4. **Tahun**: Tahun terbit resmi.
5. **Jenis Sumber**: Jurnal Nasional (Sinta), Jurnal Internasional (Scopus/DOAJ/WOS), Prosiding, Buku/Book Chapter, Laporan Pemerintah/Regulasi Resmi, atau Dokumentasi Resmi.
6. **DOI / URL**: DOI resmi yang dapat diakses atau URL valid ke penerbit/repositori.
7. **Nama File**: Nama file PDF yang tersimpan di folder `REFERENSI/` (contoh: `REF-001_sasmita_2021.pdf`).
8. **Status**: Status siklus hidup referensi (lihat Bagian 3).
9. **Digunakan Untuk**: BAB, subbab, atau konteks pembahasan (misal: "BAB II Landasan Teori - Weighted Product").
10. **Catatan Ringkas**: Temuan kunci / metodologi / kutipan penting yang relevan.

---

## 3. SIKLUS HIDUP DAN STATUS REFERENSI

Setiap sumber referensi wajib melalui tahapan status berikut:

```text
[DISCOVERED]  --> Ditemukan dari pencarian (metadata awal ada, belum ada naskah utuh)
      ↓
[DOWNLOADED]  --> Berkas PDF naskah utuh tersimpan di folder REFERENSI/
      ↓
    [READ]    --> Naskah utuh telah dibaca dan dianalisis
      ↓
  [VERIFIED]  --> Kebenaran data, metodologi, dan kutipan telah dipastikan valid
      ↓
    [USED]    --> Telah disitasi secara sah di dalam dokumen skripsi
```

### Definisi Status:
- **`DISCOVERED`**: Artikel ditemukan dari katalog/Google Scholar/repositori resmi, namun berkas naskah utuh belum diunduh/dibaca. *Belum boleh disitasi.*
- **`DOWNLOADED`**: File PDF lengkap telah ada di folder `REFERENSI/`.
- **`READ`**: Agen/mahasiswa telah membaca konten, metodologi, dan hasil studi.
- **`VERIFIED`**: Agen telah mencocokkan klaim yang akan dibuat dengan isi teks asli dari sumber tersebut.
- **`USED`**: Referensi telah dikutip pada naskah skripsi dan didaftarkan pada Daftar Pustaka.
- **`REJECTED`**: Sumber diperiksa namun tidak relevan, tidak kredibel, atau data tidak valid. Diberi keterangan alasan penolakan.

---

## 4. HIERARKI KREDIBILITAS SUMBER AKADEMIK

Prioritas pencarian dan penggunaan sumber:
1. **Prioritas 1**: Jurnal Ilmiah Bereputasi Internasional (Scopus/WoS) & Jurnal Nasional Terakreditasi (SINTA 1–4).
2. **Prioritas 2**: Buku Teks Akademik Resmi (dengan ISBN terverifikasi) dan Prosiding Konferensi Ilmiah Resmi.
3. **Prioritas 3**: Dokumen Regulasi Resmi Pemerintah / Standar Nasional (ISO, SNI, IEEE, Kemendikbudristek).
4. **Prioritas 4**: Dokumentasi Resmi Bahasa Pemrograman / Framework / Library (misalnya Python.org, Laravel.com).
5. **DILARANG**: Blog pribadi anonim, artikel WordPress/Blogspot, Wikipedia, forum publik tanpa moderasi (Brainly/Quora), naskah skripsi plagiat.

---

## 5. FORMAT SITASI DAN DAFTAR PUSTAKA

1. Format sitasi dalam naskah mengikuti gaya IEEE atau APA sesuai ketentuan resmi Universitas Almuslim (lihat [SOP_FORMAT.md](AI_AGENTS_SOP_PEDOMAN_SKRIPSI_ALMUSLIM.md)).
2. Setiap kali sitasi dimasukkan ke draf BAB I–V, agen **WAJIB** memastikan:
   - Sumber terdaftar di `REFERENSI/index.md` dengan status minimal `VERIFIED`.
   - File PDF sumber ada di folder `REFERENSI/` jika menggunakan file offline.
   - Informasi di naskah merefleksikan isi asli artikel, bukan hasil tebakan.
