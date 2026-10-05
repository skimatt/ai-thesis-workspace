# SOP PEMBUATAN DIAGRAM TEKNIS SKRIPSI INFORMATIKA
## STANDARISASI DIAGRAM-AS-CODE (MERMAID, PLANTUML, DRAW.IO) & VISUAL ZERO-DEFECT

**Document ID:** SOP-DIAGRAM-002  
**Version:** 2.0 (Enhanced Technical Specification)  
**Status:** MANDATORY & STRICT ENFORCEMENT  
**Scope:** Seluruh AI Agent dan pembuatan diagram sistem, ERD, UML, flowchart, dan arsitektur pada naskah skripsi.  

---

## 1. TUJUAN DAN PRINSIP UTAMA
File ini menetapkan standar teknis pembuatan diagram skripsi informatika agar **bebas cacat sintaks (*zero-defect*)**, **terbaca sempurna saat dicetak monokrom**, dan **merefleksikan sistem nyata tanpa komponen fiktif**.

```text
+--------------------------------------------------------------------------+
| 1. ACCURATE   : Wajib sesuai arsitektur code dan database faktual.       |
| 2. MONOCHROME : Garis hitam solid, teks hitam, latar dan isi putih murni.|
| 3. CODE-BASED : Dibuat menggunakan sintaks teknis resmi (Mermaid/PlantUML|
|                 /Draw.io XML) yang dapat di-compile tanpa error.         |
| 4. NO SHADOW  : Bebas warna gradasi, bayangan (shadow), glow, dan 3D.    |
| 5. ACADEMIC   : Tipografi Times New Roman, ukuran proporsional (10-12 pt)|
|                 dan lebar maksimal 14 cm (pas di margin Word 4-4-3-3).   |
+--------------------------------------------------------------------------+
```

---

## 2. STANDAR BAHASA TEKNIS PEMROGRAMAN DIAGRAM (*DIAGRAM-AS-CODE*)

AI Agent **WAJIB** menggunakan salah satu dari 3 bahasa teknis berikut saat memprogram diagram:

1. **Mermaid.js (`mermaid`)**: Bahasa standar utama untuk preview langsung di Markdown, chat, dan diekspor ke SVG/PNG.
2. **PlantUML (`puml`)**: Standar formal rekayasa perangkat lunak internasional untuk pemodelan UML kompleks.
3. **Draw.io XML / Draw.io CSV**: Format visual interaktif jika pengguna memerlukan pengeditan manual via aplikasi desktop Draw.io.

---

## 3. KONFIGURASI TEMA MONOKROM BAKU (*ZERO-DEFECT PALETTE*)

### 3.1 Direktif Wajib Mermaid.js
Setiap kode Mermaid **WAJIB** diawali dengan direktif tema monokrom berikut:

```text
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#ffffff',
    'primaryTextColor': '#000000',
    'primaryBorderColor': '#000000',
    'lineColor': '#000000',
    'secondaryColor': '#ffffff',
    'tertiaryColor': '#ffffff',
    'fontFamily': 'Times New Roman, serif',
    'fontSize': '12px'
  }
}}%%
```

### 3.2 Direktif Wajib PlantUML
Setiap diagram PlantUML **WAJIB** menyertakan parameter `skinparam` monokrom tanpa bayangan:

```plantuml
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName "Times New Roman"
skinparam defaultFontSize 12
skinparam backgroundColor #FFFFFF
skinparam ArrowColor #000000
skinparam BorderColor #000000
skinparam BoxPadding 10
skinparam ParticipantPadding 15
skinparam RoundCorner 0
@enduml
```

---

## 4. TEMPLATE SINTAKS BAKU PER JENIS DIAGRAM SKRIPSI

### 4.1 Flowchart / Diagram Alir Algoritma (Standar ANSI/ISO)
Flowchart digunakan untuk menjelaskan alur sistem atau tahapan kalkulasi metode/algoritma di BAB III dan BAB IV.

* **Simbol Standar:**
  - Oval / Rounded: Terminator (Mulai / Selesai)
  - Persegi Panjang: Proses Komputasi
  - Belah Ketupat: Keputusan / Percabangan (*Decision*)
  - Jajar Genjang: Input / Output Data

* **Kode Mermaid Baku:**
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000'}}}%%
flowchart TD
    A(["Mulai"]) --> B[/"Input Data Kriteria & Bobot"/]
    B --> C["Normalisasi Matriks Keputusan"]
    C --> D{"Apakah Data Lengkap?"}
    D -- "Tidak" --> E["Tampilkan Notifikasi Error"]
    E --> B
    D -- "Ya" --> F["Hitung Vektor Preferensi (Metode WP)"]
    F --> G["Perangkingan Nilai Alternatif"]
    G --> H[/"Output Laporan Perangkingan"/]
    H --> I(["Selesai"])

    style A stroke:#000,fill:#fff,stroke-width:1.5px;
    style B stroke:#000,fill:#fff,stroke-width:1.5px;
    style C stroke:#000,fill:#fff,stroke-width:1.5px;
    style D stroke:#000,fill:#fff,stroke-width:1.5px;
    style E stroke:#000,fill:#fff,stroke-width:1.5px;
    style F stroke:#000,fill:#fff,stroke-width:1.5px;
    style G stroke:#000,fill:#fff,stroke-width:1.5px;
    style H stroke:#000,fill:#fff,stroke-width:1.5px;
    style I stroke:#000,fill:#fff,stroke-width:1.5px;
```

---

### 4.2 Use Case Diagram (UML)
Menggambarkan interaksi fungsional antara aktor dengan sistem di BAB III.

* **Aturan Kritis:**
  - Aktor **selalu berada di luar** *System Boundary*.
  - Nama use case diawali kata kerja tindakan (contoh: *Mengelola Data*, *Melakukan Penilaian*).
  - Relasi `<<include>>` untuk fungsi wajib, `<<extend>>` untuk fungsi opsional/kondisional.

* **Kode PlantUML Baku:**
```plantuml
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName "Times New Roman"
left to right direction

actor "Administrator" as Admin
actor "Pimpinan / Kepala" as Pimpinan

rectangle "Sistem Pendukung Keputusan Rekrutmen" {
    usecase "Login Sistem" as UC_Login
    usecase "Kelola Kriteria & Bobot" as UC_Kriteria
    usecase "Input Data Pelamar" as UC_Pelamar
    usecase "Proses Penilaian (Algoritma)" as UC_Hitung
    usecase "Verifikasi Hasil Seleksi" as UC_Verifikasi
    usecase "Cetak Laporan Perangkingan" as UC_Laporan
}

Admin --> UC_Login
Admin --> UC_Kriteria
Admin --> UC_Pelamar
Admin --> UC_Hitung
Admin --> UC_Laporan

Pimpinan --> UC_Login
Pimpinan --> UC_Verifikasi
Pimpinan --> UC_Laporan

UC_Hitung ..> UC_Login : <<include>>
UC_Laporan ..> UC_Hitung : <<include>>
@enduml
```

* **Kode Mermaid Baku:**
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000'}}}%%
flowchart LR
    subgraph AktorPengguna ["Aktor"]
        Admin(("Administrator"))
        Pimpinan(("Pimpinan"))
    end

    subgraph BatasSistem ["Sistem Pendukung Keputusan"]
        UC1(["Login Sistem"])
        UC2(["Kelola Data Kriteria"])
        UC3(["Input Data Alternatif"])
        UC4(["Proses Perhitungan"])
        UC5(["Lihat & Cetak Laporan"])
    end

    Admin --- UC1
    Admin --- UC2
    Admin --- UC3
    Admin --- UC4
    Admin --- UC5
    Pimpinan --- UC1
    Pimpinan --- UC5

    UC4 -.->|"<<include>>"| UC1
    UC5 -.->|"<<include>>"| UC4
```

---

### 4.3 Activity Diagram (UML)
Menjelaskan alur aktivitas proses bisnis secara runtut antara aktor dan sistem (dengan swimlane).

* **Kode PlantUML Baku (Dengan Swimlane):**
```plantuml
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName "Times New Roman"

|Pengguna|
start
:Mengisi formulir penilaian;
:Menekan tombol simpan & hitung;

|Sistem|
:Menerima data nilai alternatif;
if (Apakah data lengkap?) then (Ya)
  :Mengambil bobot kriteria dari database;
  :Melakukan kalkulasi vektor normalisasi;
  :Menghitung nilai preferensi akhir;
  :Menyimpan hasil perangkingan ke database;
  |Pengguna|
  :Melihat hasil perangkingan di layar;
  stop
else (Tidak)
  |Sistem|
  :Menampilkan pesan validasi gagal;
  |Pengguna|
  :Memperbaiki data input;
  stop
endif
@enduml
```

---

### 4.4 Sequence Diagram (UML)
Menjelaskan pertukaran pesan antar-objek/komponen berdasarkan urutan waktu.

* **Kode Mermaid Baku:**
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000'}}}%%
sequenceDiagram
    autonumber
    actor Pengguna as Admin
    participant UI as Interface Penilaian
    participant Ctr as Controller SPK
    participant Alg as Engine Algoritma
    participant DB as Basis Data (MySQL)

    Pengguna->>UI: Input nilai kriteria alternatif
    UI->>Ctr: Kirim request prosesData(input)
    activate Ctr
    Ctr->>DB: Query bobot kriteria & data alternatif
    DB-->>Ctr: Return recordset data
    Ctr->>Alg: Eksekusi hitungPreferensi(data, bobot)
    activate Alg
    Alg-->>Ctr: Return matriks ranking terurut
    deactivate Alg
    Ctr->>DB: Simpan hasil ranking
    Ctr-->>UI: Tampilkan tabel perankingan
    deactivate Ctr
    UI-->>Pengguna: Tampilan hasil seleksi siap cetak
```

---

### 4.5 Entity-Relationship Diagram (ERD / Relasi Tabel Basis Data)
ERD wajib menggambarkan skema database aktual sesuai migration atau SQL script.

* **Aturan Kritis:**
  - Cantumkan nama tabel, primary key (`PK`), foreign key (`FK`), serta tipe data.
  - Kardinalitas relasi menggunakan notasi *Crow's Foot*:
    - `||--||` : One-to-One
    - `||--o{` : One-to-Many
    - `}|--o{` : Many-to-Many (wajib dipecah lewat tabel asosiasi)

* **Kode Mermaid Baku:**
```mermaid
erDiagram
    PENGGUNA ||--o{ LOG_AKTIVITAS : "melakukan"
    PENGGUNA {
        int id_pengguna PK
        string nama_lengkap
        string username
        string password
        string peran
    }

    KRITERIA ||--o{ DETAIL_PENILAIAN : "menjadi acuan"
    KRITERIA {
        int id_kriteria PK
        string kode_kriteria
        string nama_kriteria
        float bobot
        string jenis_kriteria
    }

    ALTERNATIF ||--o{ DETAIL_PENILAIAN : "memiliki nilai"
    ALTERNATIF ||--o{ HASIL_AKHIR : "mendapatkan ranking"
    ALTERNATIF {
        int id_alternatif PK
        string kode_alternatif
        string nama_calon
        string asal_institusi
        date tanggal_daftar
    }

    DETAIL_PENILAIAN {
        int id_detail PK
        int id_alternatif FK
        int id_kriteria FK
        float nilai_input
    }

    HASIL_AKHIR {
        int id_hasil PK
        int id_alternatif FK
        float nilai_preferensi
        int peringkat
        date tanggal_hitung
    }
```

---

### 4.6 Class Diagram (UML)
Menampilkan struktur kelas perangkat lunak, atribut, method, dan keterhubungannya di BAB III.

* **Kode PlantUML Baku:**
```plantuml
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName "Times New Roman"

class Alternatif {
  - id: int
  - kode: string
  - nama: string
  + simpan(): boolean
  + update(): boolean
  + hapus(): boolean
}

class Kriteria {
  - id: int
  - kode: string
  - nama: string
  - bobot: double
  - jenis: string
  + getBobotNormalisasi(): double
}

class SpkCalculator {
  - alternatifList: List<Alternatif>
  - kriteriaList: List<Kriteria>
  + hitungVektorS(): double[]
  + hitungVektorV(): double[]
  + urutkanRanking(): List<HasilRanking>
}

class HasilRanking {
  - alternatifId: int
  - skorAkhir: double
  - peringkat: int
  + cetakLaporan(): void
}

SpkCalculator "1" o-- "*" Alternatif
SpkCalculator "1" o-- "*" Kriteria
SpkCalculator ..> HasilRanking : generates
@enduml
```

---

### 4.7 Arsitektur Sistem (Layered Architecture)
Menunjukkan arsitektur perangkat lunak dari sisi antarmuka, routing, server logika, hingga database.

* **Kode Mermaid Baku:**
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000'}}}%%
flowchart TD
    subgraph ClientLayer ["1. Presentation Layer (Client)"]
        UI["Web Browser / Antarmuka Pengguna (HTML5 / Bootstrap / JS)"]
    end

    subgraph AppLayer ["2. Application & Controller Layer"]
        Route["Routing Engine (Web Router)"]
        Ctrl["Controller Logika Bisnis & Validasi"]
        Engine["Algoritma SPK (Calculation Module)"]
    end

    subgraph DataLayer ["3. Data Access & Persistence Layer"]
        ORM["Data Access Object / ORM (Query Builder)"]
        DB[(Basis Data Relasional MySQL)]
    end

    UI <-->|"HTTP Request / JSON Response"| Route
    Route --> Ctrl
    Ctrl <--> Engine
    Ctrl <--> ORM
    ORM <-->|"SQL Query / Resultset"| DB

    style ClientLayer stroke:#000,fill:#fff,stroke-dasharray: 5 5;
    style AppLayer stroke:#000,fill:#fff,stroke-dasharray: 5 5;
    style DataLayer stroke:#000,fill:#fff,stroke-dasharray: 5 5;
    style UI stroke:#000,fill:#fff;
    style Route stroke:#000,fill:#fff;
    style Ctrl stroke:#000,fill:#fff;
    style Engine stroke:#000,fill:#fff;
    style ORM stroke:#000,fill:#fff;
    style DB stroke:#000,fill:#fff;
```

---

## 5. ATURAN ANTI-CACAT SINTAKS (*ZERO-DEFECT SYNTAX RULES*)

Agar diagram tidak mengalami error saat di-*compile* atau rusak saat diekspor, patuhi 7 aturan ketat berikut:

1. **Wajib Menggunakan Tanda Petik pada Label Khusus**:
   - *Salah:* `A(Proses (Normalisasi)) --> B` (Error karena kurung di dalam kurung).
   - *Benar:* `A["Proses (Normalisasi)"] --> B` (Aman dari benturan sintaks).
2. **Hindari Garis Menyilang (*Line Crossing Prevention*)**:
   - Gunakan arah `TD` (Top-to-Bottom) untuk diagram alir sekuensial dan `LR` (Left-to-Right) untuk Use Case.
   - Jangan membuat tautan balik yang membelah diagram jika bisa menggunakan simpul konektor (*Connector node*).
3. **Pemisahan Teks Panjang Menggunakan Baris Baru**:
   - Batasi panjang teks dalam satu kotak simpul maksimal 4-5 kata per baris. Gunakan `\n` atau `<br/>` untuk memecah baris.
4. **Semantik Aktor & Boundary yang Valid**:
   - Aktor manusia tidak boleh diletakkan di dalam kotak sistem (*System Boundary*).
5. **Kardinalitas Basis Data yang Logis**:
   - Dilarang membuat relasi `Many-to-Many` (`M:N`) langsung tanpa tabel perantara (*junction table*) pada rancangan fisik ERD.
6. **Proporsi Skala Cetak (Print Dimensions)**:
   - Lebar maksimum diagram saat ditempelkan ke Microsoft Word adalah **14 cm** (agar tidak melanggar margin kiri 4 cm dan kanan 3 cm kertas A4).
   - Tinggi diagram tidak boleh melebihi **20 cm** agar tidak memicu pemotongan halaman secara liar.
7. **Resolusi Ekspor**:
   - Format wajib: **Vektor SVG** (pilihan utama) atau **PNG monokrom minimum 300 DPI**.

---

## 6. PENAMAAN BERKAS & LOKASI PENYIMPANAN
Seluruh diagram yang dihasilkan wajib disimpan pada folder:  
`ASSETS/DIAGRAM/`

Format penamaan berkas:
- Flowchart Algoritma : `diagram_3_1_flowchart_algoritma.[puml/mmd/svg/png]`
- Use Case Diagram    : `diagram_3_2_use_case.[puml/mmd/svg/png]`
- Activity Diagram    : `diagram_3_3_activity_penilaian.[puml/mmd/svg/png]`
- Sequence Diagram    : `diagram_3_4_sequence_kalkulasi.[puml/mmd/svg/png]`
- Class Diagram       : `diagram_3_5_class_diagram.[puml/mmd/svg/png]`
- Entity Relationship : `diagram_3_6_erd.[puml/mmd/svg/png]`
- Arsitektur Sistem   : `diagram_3_7_arsitektur_sistem.[puml/mmd/svg/png]`

---

## 7. QUALITY CONTROL CHECKLIST SEBELUM DIAGRAM MASUK NASKAH

Sebelum diagram dimasukkan ke dalam draf naskah skripsi, agent wajib memverifikasi:
- [ ] **Sintaks Valid**: Tidak ada pesan error parser pada editor Mermaid/PlantUML.
- [ ] **Warna Monokrom Murni**: Latar putih (#FFFFFF), garis hitam solid (#000000), tanpa bayangan (*no shadows*).
- [ ] **Kesesuaian Teks**: Setiap entitas, tabel, field, dan aktor memiliki kesamaan nama 100% dengan teks di [CONTEXT_SKRIPSI.txt](CONTEXT_SKRIPSI.txt).
- [ ] **Nomor & Caption**: Memiliki caption resmi di bawah gambar (Contoh: *Gambar 3.1 Flowchart Metode Weighted Product*).
- [ ] **Paragraf Penjelas**: Terdapat minimal satu paragraf narasi analitis di dalam teks skripsi yang membahas diagram tersebut.
