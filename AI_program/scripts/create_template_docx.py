"""
CREATE TEMPLATE DOCX - MASTER TEMPLATE GENERATOR RESMI ALMUSLIM
Program Studi Informatika - Fakultas Ilmu Komputer - Universitas Almuslim
Acuan Baku: CONTOH_SKRIPSI/Contoh_skripsi.docx & AI_AGENTS_SOP_PEDOMAN_SKRIPSI_ALMUSLIM.md

Spesifikasi Baku:
1. Cover: Judul Piramida Terbalik (Inverted Pyramid), Center, 14 pt Bold, Spasi 1.15.
2. Halaman Judul Dalam (Halaman i) & Sampul Luar terpisah secara presisi sesuai kaidah akademik.
3. Layout Kertas: A4 (210 x 297 mm), Margin 4-4-3-3 cm (Kiri 4, Atas 4, Kanan 3, Bawah 3).
4. Spasi: 1.5 (Naskah Utama & Subbab), 1.0 (Abstrak, Judul Tabel/Gambar, Daftar Pustaka).
5. Tipografi: Times New Roman 12 pt (Body), 14 pt Bold (Heading 1), 12 pt Bold (Heading 2 & 3).
6. Front Matter Lengkap: Halaman Judul, Halaman Pengesahan, Pernyataan Keaslian, Kata Pengantar, Abstrak ID & EN,
   Daftar Isi, Daftar Tabel, Daftar Gambar (dengan Tab Stop 14.0 cm dan Leader Dots, alignment LEFT).
7. 6 BAB Baku: BAB I s.d. BAB VI + DAFTAR PUSTAKA + DAFTAR RIWAYAT HIDUP.
8. Penomoran Halaman:
   - Bagian Awal: Romawi kecil (i s.d. ix) di tengah bawah (halaman i tidak dicetak nomornya).
   - Bagian Bab: Angka Arab (1, 2, ...) di kanan atas, KECUALI halaman pertama setiap BAB di tengah bawah.
"""

import os
import re
import docx
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.section import WD_SECTION
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from table_styler import style_academic_table, add_table_caption


def format_inverted_pyramid(title):
    """
    Memformat judul skripsi menjadi susunan Piramida Terbalik (Inverted Pyramid) yang proporsional.
    Bila sudah memiliki line break eksplisit, pertahankan.
    Bila panjang <= 42 karakter, cukup 1 baris.
    Bila panjang > 42 karakter, pilih kombinasi 2 atau 3 baris yang mengerucut ke bawah
    (baris atas lebih panjang daripada baris bawah) tanpa menyisakan kata tunggal terisolasi.
    """
    if '\n' in title:
        return title.strip().upper()

    words = title.strip().upper().split()
    if not words:
        return title

    total_len = sum(len(w) for w in words) + len(words) - 1
    if total_len <= 42:
        return ' '.join(words)

    n = len(words)
    best_candidate = None
    best_penalty = float('inf')

    # Opsi 2 baris (len1 >= len2)
    for i in range(1, n):
        l1 = ' '.join(words[:i])
        l2 = ' '.join(words[i:])
        len1, len2 = len(l1), len(l2)
        if len1 <= 62 and len2 >= 10 and len1 >= len2:
            diff = len1 - len2
            penalty = diff * 0.8
            if total_len > 90:
                penalty += 35
            if penalty < best_penalty:
                best_penalty = penalty
                best_candidate = (l1, l2)

    # Opsi 3 baris (len1 >= len2 >= len3)
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            l1 = ' '.join(words[:i])
            l2 = ' '.join(words[i:j])
            l3 = ' '.join(words[j:])
            len1, len2, len3 = len(l1), len(l2), len(l3)
            if len1 <= 62 and len2 <= 55 and len3 >= 12 and len1 >= len2 and len2 >= len3:
                diff1 = len1 - len2
                diff2 = len2 - len3
                penalty = abs(diff1 - diff2) * 1.0 + (62 - len1) * 0.15
                if penalty < best_penalty:
                    best_penalty = penalty
                    best_candidate = (l1, l2, l3)

    if best_candidate:
        return '\n'.join(best_candidate)

    mid = n // 2
    return f"{' '.join(words[:mid])}\n{' '.join(words[mid:])}"


def set_page_number_field(run):
    """Menyisipkan field dinamis PAGE ke dalam run Word."""
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)


def add_leader_tab_item(doc, title, page_str, level=1, is_bold=False):
    """
    Menambahkan entri daftar dengan tab stop dot leader 14.0 cm rata kanan.
    Alignment diset LEFT agar teks judul tidak terdistorsi spasi justify.
    """
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(3 if level == 1 else 1)
    p.paragraph_format.space_after = Pt(2 if level == 1 else 1)

    if level == 2:
        p.paragraph_format.left_indent = Cm(0.63)
    elif level == 3:
        p.paragraph_format.left_indent = Cm(1.25)

    p.paragraph_format.tab_stops.add_tab_stop(Cm(14.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)

    r1 = p.add_run(title)
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    if is_bold or level == 1:
        r1.bold = True

    p.add_run('\t')

    r2 = p.add_run(str(page_str))
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    if is_bold or level == 1:
        r2.bold = True
    return p


def apply_section_geometry(sec):
    """Margin resmi Almuslim A4: Kiri 4cm, Atas 4cm, Kanan 3cm, Bawah 3cm."""
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(4.0)
    sec.bottom_margin = Cm(3.0)
    sec.left_margin = Cm(4.0)
    sec.right_margin = Cm(3.0)


def create_almuslim_skripsi_template(output_path, title=None, author_name=None, author_npm=None, year="2026"):
    """
    Membangun master template Word skripsi resmi Universitas Almuslim yang sempurna.
    """
    doc = Document()

    # Konfigurasi Font & Paragraf Dasar (Normal)
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    p_format = normal_style.paragraph_format
    p_format.line_spacing = 1.5  # Baku Almuslim 1.5 spasi
    p_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_format.space_before = Pt(0)
    p_format.space_after = Pt(0)

    # Heading 1 (BAB I, BAB II, dst.)
    h1_style = doc.styles['Heading 1']
    h1_style.font.name = 'Times New Roman'
    h1_style.font.size = Pt(14)
    h1_style.font.bold = True
    h1_style.font.color.rgb = RGBColor(0, 0, 0)
    h1_format = h1_style.paragraph_format
    h1_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1_format.line_spacing = 1.15
    h1_format.space_before = Pt(12)
    h1_format.space_after = Pt(12)

    # Heading 2 (1.1, 1.2, dst.)
    h2_style = doc.styles['Heading 2']
    h2_style.font.name = 'Times New Roman'
    h2_style.font.size = Pt(12)
    h2_style.font.bold = True
    h2_style.font.color.rgb = RGBColor(0, 0, 0)
    h2_format = h2_style.paragraph_format
    h2_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h2_format.line_spacing = 1.5
    h2_format.space_before = Pt(12)
    h2_format.space_after = Pt(6)

    # Heading 3 (3.1.1, dst.)
    h3_style = doc.styles['Heading 3']
    h3_style.font.name = 'Times New Roman'
    h3_style.font.size = Pt(12)
    h3_style.font.bold = True
    h3_style.font.color.rgb = RGBColor(0, 0, 0)
    h3_format = h3_style.paragraph_format
    h3_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h3_format.line_spacing = 1.5
    h3_format.space_before = Pt(6)
    h3_format.space_after = Pt(4)

    raw_title = title if title else "PENERAPAN METODE WEIGHTED PRODUCT PADA SISTEM PENDUKUNG KEPUTUSAN PENERIMAAN REKRUTMEN GURU PESANTREN UMMULQURA INDONESIA"
    pyramid_title = format_inverted_pyramid(raw_title)
    mhs_name = author_name if author_name else "ARZA ULFA SASMITA"
    mhs_npm = author_npm if author_npm else "1505020027"
    logo_path = os.path.abspath("ASSETS/logo_umuslim.jpg")

    # ==========================================
    # SECTION 1: SAMPUL LUAR (Outer Cover)
    # Tanpa nomor halaman, tanpa kalimat pengajuan
    # ==========================================
    sec_cover = doc.sections[0]
    apply_section_geometry(sec_cover)
    sec_cover.header.is_linked_to_previous = False
    sec_cover.footer.is_linked_to_previous = False

    p_cover_title = doc.add_paragraph()
    p_cover_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cover_title.paragraph_format.line_spacing = 1.15
    p_cover_title.paragraph_format.space_before = Pt(0)
    p_cover_title.paragraph_format.space_after = Pt(16)
    r_t = p_cover_title.add_run(pyramid_title)
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(14)
    r_t.bold = True

    p_cover_skrip = doc.add_paragraph()
    p_cover_skrip.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cover_skrip.paragraph_format.space_after = Pt(24)
    r_sk = p_cover_skrip.add_run("SKRIPSI")
    r_sk.font.name = 'Times New Roman'
    r_sk.font.size = Pt(14)
    r_sk.bold = True

    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_after = Pt(28)
    if os.path.exists(logo_path):
        p_logo.add_run().add_picture(logo_path, width=Cm(4.5))

    p_author = doc.add_paragraph()
    p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_author.paragraph_format.line_spacing = 1.15
    p_author.paragraph_format.space_after = Pt(36)
    r_auth = p_author.add_run(f"OLEH:\n\n{mhs_name}\nNPM. {mhs_npm}")
    r_auth.font.name = 'Times New Roman'
    r_auth.font.size = Pt(12)
    r_auth.bold = True

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.line_spacing = 1.15
    r_inst = p_inst.add_run(f"PROGRAM STUDI INFORMATIKA\nFAKULTAS ILMU KOMPUTER\nUNIVERSITAS ALMUSLIM\nBIREUEN\n{year}")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(14)
    r_inst.bold = True

    # ==========================================
    # SECTION 2: BAGIAN AWAL (Romawi Kecil: i s.d. ix)
    # Halaman Judul Dalam dihitung sebagai i (tidak dicetak)
    # ==========================================
    sec_prelim = doc.add_section(WD_SECTION.NEW_PAGE)
    apply_section_geometry(sec_prelim)
    sec_prelim.header.is_linked_to_previous = False
    sec_prelim.footer.is_linked_to_previous = False
    sec_prelim.different_first_page_header_footer = True

    pg_roman = parse_xml(r'<w:pgNumType %s w:fmt="lowerRoman" w:start="1"/>' % nsdecls('w'))
    sec_prelim._sectPr.append(pg_roman)

    # Halaman i: nomor tidak dicetak
    sec_prelim.first_page_footer.paragraphs[0].text = ""
    sec_prelim.first_page_header.paragraphs[0].text = ""

    # Halaman ii dst: nomor Romawi di tengah bawah
    p_foot_p = sec_prelim.footer.paragraphs[0]
    p_foot_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_foot = p_foot_p.add_run()
    r_foot.font.name = 'Times New Roman'
    r_foot.font.size = Pt(12)
    set_page_number_field(r_foot)
    sec_prelim.header.paragraphs[0].text = ""

    # 1. HALAMAN JUDUL (Inner Title Page - Halaman i)
    p_in_t = doc.add_paragraph()
    p_in_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_t.paragraph_format.line_spacing = 1.15
    p_in_t.paragraph_format.space_before = Pt(0)
    p_in_t.paragraph_format.space_after = Pt(12)
    r_int = p_in_t.add_run(pyramid_title)
    r_int.font.name = 'Times New Roman'
    r_int.font.size = Pt(14)
    r_int.bold = True

    p_in_sub = doc.add_paragraph()
    p_in_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_sub.paragraph_format.line_spacing = 1.0
    p_in_sub.paragraph_format.space_after = Pt(16)
    r_insub = p_in_sub.add_run("SKRIPSI\n\nDiajukan Untuk Memenuhi Salah Satu Syarat\nMemperoleh Gelar Sarjana Komputer (S.Kom)\nPada Program Studi Informatika")
    r_insub.font.name = 'Times New Roman'
    r_insub.font.size = Pt(12)

    p_in_logo = doc.add_paragraph()
    p_in_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_logo.paragraph_format.space_after = Pt(16)
    if os.path.exists(logo_path):
        p_in_logo.add_run().add_picture(logo_path, width=Cm(4.5))

    p_in_auth = doc.add_paragraph()
    p_in_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_auth.paragraph_format.line_spacing = 1.15
    p_in_auth.paragraph_format.space_after = Pt(20)
    r_inauth = p_in_auth.add_run(f"OLEH:\n\n{mhs_name}\nNPM. {mhs_npm}")
    r_inauth.font.name = 'Times New Roman'
    r_inauth.font.size = Pt(12)
    r_inauth.bold = True

    p_in_inst = doc.add_paragraph()
    p_in_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_inst.paragraph_format.line_spacing = 1.15
    r_ininst = p_in_inst.add_run(f"PROGRAM STUDI INFORMATIKA\nFAKULTAS ILMU KOMPUTER\nUNIVERSITAS ALMUSLIM\nBIREUEN\n{year}")
    r_ininst.font.name = 'Times New Roman'
    r_ininst.font.size = Pt(14)
    r_ininst.bold = True

    # 2. HALAMAN PERSETUJUAN (Halaman ii)
    doc.add_page_break()
    doc.add_paragraph("HALAMAN PERSETUJUAN", style='Heading 1')
    p_pers = doc.add_paragraph()
    p_pers.paragraph_format.line_spacing = 1.5
    p_pers.paragraph_format.space_before = Pt(12)
    p_pers.add_run("Skripsi dengan judul:\n\"").font.size = Pt(12)
    p_pers.add_run(raw_title).bold = True
    p_pers.add_run("\"\n\nTelah disetujui untuk disidangkan di hadapan Dewan Penguji Sidang Sarjana Program Studi Informatika, Fakultas Ilmu Komputer, Universitas Almuslim.\n\n\n")

    p_ttd_pers = doc.add_paragraph()
    p_ttd_pers.paragraph_format.line_spacing = 1.15
    p_ttd_pers.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ttd_pers.add_run("Menyetujui,\n\n\n\nPembimbing I\t\t\t\t\t\tPembimbing II\n\n\n\n\nDr. Saifullah, M.Pd\t\t\t\tRiyadhul Fajri, S.ST., M.Kom\nNIDN. 0111018001\t\t\t\t\tNIDN. 0115048502")

    # 3. HALAMAN PENGESAHAN (Halaman iii)
    doc.add_page_break()
    doc.add_paragraph("HALAMAN PENGESAHAN", style='Heading 1')
    p_peng = doc.add_paragraph()
    p_peng.paragraph_format.line_spacing = 1.5
    p_peng.paragraph_format.space_before = Pt(12)
    p_peng.add_run("Skripsi dengan judul:\n\"").font.size = Pt(12)
    p_peng.add_run(raw_title).bold = True
    p_peng.add_run("\"\n\nTelah dipertahankan di hadapan Dewan Penguji Sidang Sarjana Program Studi Informatika, Fakultas Ilmu Komputer, Universitas Almuslim dan dinyatakan LULUS.\n\n\n")

    p_ttd = doc.add_paragraph()
    p_ttd.paragraph_format.line_spacing = 1.15
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ttd.add_run("Mengesahkan,\n\n\n\nDekan Fakultas Ilmu Komputer\t\t\t\tKetua Program Studi Informatika\n\n\n\n\nTaufiq, S.T., M.T\t\t\t\tRiyadhul Fajri, S.ST., M.Kom\nNIDN. 0120057501\t\t\t\t\tNIDN. 0115048502")

    # 4. HALAMAN PERNYATAAN KEASLIAN (Halaman iv)
    doc.add_page_break()
    doc.add_paragraph("HALAMAN PERNYATAAN KEASLIAN", style='Heading 1')
    p_perny = doc.add_paragraph()
    p_perny.paragraph_format.line_spacing = 1.5
    p_perny.paragraph_format.first_line_indent = Cm(1.25)
    p_perny.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_perny.add_run("Saya yang bertanda tangan di bawah ini menyatakan dengan sesungguhnya bahwa skripsi yang berjudul \"")
    p_perny.add_run(raw_title).bold = True
    p_perny.add_run("\" ini adalah murni hasil karya sendiri dan bukan merupakan plagiasi maupun manipulasi dari karya ilmiah orang lain, baik sebagian maupun seluruhnya.")

    p_perny2 = doc.add_paragraph()
    p_perny2.paragraph_format.line_spacing = 1.5
    p_perny2.paragraph_format.first_line_indent = Cm(1.25)
    p_perny2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_perny2.add_run("Apabila di kemudian hari terbukti bahwa skripsi ini mengandung unsur plagiarisme, manipulasi data empiris, atau pelanggaran integritas akademik, maka saya bersedia menerima sanksi akademik pencabutan gelar kesarjanaan sesuai dengan peraturan perundang-undangan yang berlaku di Universitas Almuslim.")

    # 5. KATA PENGANTAR (Halaman v)
    doc.add_page_break()
    doc.add_paragraph("KATA PENGANTAR", style='Heading 1')
    p_kp1 = doc.add_paragraph()
    p_kp1.paragraph_format.line_spacing = 1.5
    p_kp1.paragraph_format.first_line_indent = Cm(1.25)
    p_kp1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_kp1.add_run("Puji dan syukur penulis panjatkan ke hadirat Allah SWT atas segala limpahan rahmat, karunia, dan hidayah-Nya sehingga penulis dapat menyelesaikan penulisan naskah skripsi ini dengan baik. Shalawat beserta salam senantiasa tercurahkan kepada Baginda Rasulullah SAW yang telah menuntun umat manusia menuju jalan ilmu pengetahuan dan peradaban yang mulia.")

    p_kp2 = doc.add_paragraph()
    p_kp2.paragraph_format.line_spacing = 1.5
    p_kp2.paragraph_format.first_line_indent = Cm(1.25)
    p_kp2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_kp2.add_run("Penyusunan skripsi ini diajukan sebagai salah satu syarat akademik guna menyelesaikan studi strata satu (S1) dan memperoleh gelar Sarjana Komputer (S.Kom) pada Program Studi Informatika, Fakultas Ilmu Komputer, Universitas Almuslim. Ucapan terima kasih yang tulus dan penghargaan setinggi-tingginya penulis haturkan kepada Rektor Universitas Almuslim, Dekan Fakultas Ilmu Komputer, Ketua Program Studi Informatika, para Dosen Pembimbing, serta kedua orang tua tercinta yang tiada henti memanjatkan doa demi kelancaran studi penulis.")

    # 6. ABSTRAK (Halaman vii - 1 Paragraf Tunggal, Spasi 1.0)
    doc.add_page_break()
    doc.add_paragraph("ABSTRAK", style='Heading 1')
    p_ab_title = doc.add_paragraph()
    p_ab_title.paragraph_format.line_spacing = 1.15
    p_ab_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ab_title.paragraph_format.space_after = Pt(4)
    p_ab_title.add_run(raw_title).bold = True

    p_ab_author = doc.add_paragraph()
    p_ab_author.paragraph_format.line_spacing = 1.0
    p_ab_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ab_author.paragraph_format.space_after = Pt(12)
    p_ab_author.add_run(f"Oleh:\n{mhs_name} / {mhs_npm}")

    p_ab_body = doc.add_paragraph()
    p_ab_body.paragraph_format.line_spacing = 1.0
    p_ab_body.paragraph_format.first_line_indent = Cm(1.25)
    p_ab_body.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_ab_body.add_run("Abstrak disusun dalam satu paragraf tunggal yang memuat 150 hingga 250 kata dengan spasi 1.0 (tunggal). Memuat secara terpadu latar belakang fenomena masalah, rumusan masalah dan tujuan utama penelitian, metode komputasi serta arsitektur sistem informasi yang dibangun, hasil pengujian empiris dan kalkulasi validasi, serta kesimpulan praktis dan akademis yang dihasilkan.")

    p_ab_kw = doc.add_paragraph()
    p_ab_kw.paragraph_format.line_spacing = 1.0
    p_ab_kw.paragraph_format.space_before = Pt(8)
    p_ab_kw.add_run("Kata Kunci: ").bold = True
    p_ab_kw.add_run("Sistem Pendukung Keputusan, Metode Komputasi, Algoritma, Informatika, Universitas Almuslim.")

    # 7. ABSTRACT (Halaman viii - Single Spacing, Italic)
    doc.add_page_break()
    doc.add_paragraph("ABSTRACT", style='Heading 1')
    p_aben_title = doc.add_paragraph()
    p_aben_title.paragraph_format.line_spacing = 1.15
    p_aben_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_aben_title.paragraph_format.space_after = Pt(12)
    r_en_t = p_aben_title.add_run(raw_title)
    r_en_t.font.italic = True

    p_aben_body = doc.add_paragraph()
    p_aben_body.paragraph_format.line_spacing = 1.0
    p_aben_body.paragraph_format.first_line_indent = Cm(1.25)
    p_aben_body.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_enb = p_aben_body.add_run("The abstract must be written in English within a single paragraph containing 150 to 250 words using single spacing and italic font. It concisely outlines the background of the study, the core research problems and objectives, the computational methodology applied, the empirical system development and validation results, as well as the concluding remarks.")
    r_enb.font.italic = True

    p_aben_kw = doc.add_paragraph()
    p_aben_kw.paragraph_format.line_spacing = 1.0
    p_aben_kw.paragraph_format.space_before = Pt(8)
    r_kwt = p_aben_kw.add_run("Keywords: ")
    r_kwt.bold = True
    r_kwt.font.italic = True
    r_kwe = p_aben_kw.add_run("Decision Support System, Computational Method, Algorithm, Informatics, Universitas Almuslim.")
    r_kwe.font.italic = True

    # 8. DAFTAR ISI (Halaman ix - Tab Stops 14.0 cm & Dot Leaders)
    doc.add_page_break()
    doc.add_paragraph("DAFTAR ISI", style='Heading 1')

    toc_items = [
        ("HALAMAN JUDUL", "i", 1),
        ("HALAMAN PERSETUJUAN", "ii", 1),
        ("HALAMAN PENGESAHAN", "iii", 1),
        ("HALAMAN PERNYATAAN KEASLIAN", "iv", 1),
        ("KATA PENGANTAR", "v", 1),
        ("ABSTRAK", "vii", 1),
        ("ABSTRACT", "viii", 1),
        ("DAFTAR ISI", "ix", 1),
        ("DAFTAR TABEL", "x", 1),
        ("DAFTAR GAMBAR", "xi", 1),
        ("BAB I PENDAHULUAN", "1", 1),
        ("1.1 Latar Belakang Masalah", "1", 2),
        ("1.2 Rumusan Masalah", "3", 2),
        ("1.3 Batasan Masalah", "4", 2),
        ("1.4 Tujuan Penelitian", "4", 2),
        ("1.5 Manfaat Penelitian", "5", 2),
        ("1.6 Metodologi Penelitian", "5", 2),
        ("1.7 Sistematika Penulisan", "6", 2),
        ("BAB II LANDASAN TEORI", "8", 1),
        ("2.1 Konsep Sistem dan Objek Penelitian", "8", 2),
        ("2.2 Metode Komputasi / Algoritma", "11", 2),
        ("2.3 Konsep Pemodelan Sistem dan Basis Data", "16", 2),
        ("2.4 Perangkat Lunak dan Basis Data Pendukung", "19", 2),
        ("2.5 Penelitian Terkait", "21", 2),
        ("BAB III ANALISA DAN PERANCANGAN SISTEM", "24", 1),
        ("3.1 Analisa Sistem", "24", 2),
        ("3.2 Penentuan Kriteria dan Bobot Penilaian", "28", 2),
        ("3.3 Perancangan Sistem", "31", 2),
        ("3.4 Perancangan Basis Data", "35", 2),
        ("3.5 Perancangan Tampilan Antarmuka", "39", 2),
        ("BAB IV IMPLEMENTASI SISTEM", "43", 1),
        ("4.1 Batasan dan Lingkungan Implementasi", "43", 2),
        ("4.2 Implementasi Modul Komputasi", "45", 2),
        ("4.3 Implementasi Antarmuka Pengguna", "49", 2),
        ("BAB V PENGUJIAN DAN PEMBAHASAN", "55", 1),
        ("5.1 Pengujian Model / Algoritma Komputasi", "55", 2),
        ("5.2 Pengujian Fungsional Sistem (Black Box Testing)", "61", 2),
        ("5.3 Pembahasan Hasil Penelitian", "66", 2),
        ("BAB VI PENUTUP", "71", 1),
        ("6.1 Kesimpulan", "71", 2),
        ("6.2 Saran", "72", 2),
        ("DAFTAR PUSTAKA", "74", 1),
        ("DAFTAR RIWAYAT HIDUP", "77", 1),
        ("LAMPIRAN", "78", 1)
    ]

    for t_title, t_page, t_lvl in toc_items:
        add_leader_tab_item(doc, t_title, t_page, level=t_lvl)

    # 9. DAFTAR TABEL (Halaman x)
    doc.add_page_break()
    doc.add_paragraph("DAFTAR TABEL", style='Heading 1')

    table_items = [
        ("Tabel 2.1 Matriks Perbandingan Penelitian Terdahulu", "22"),
        ("Tabel 3.1 Kriteria Penilaian dan Bobot", "28"),
        ("Tabel 3.2 Bobot Kriteria", "29"),
        ("Tabel 3.3 Penentuan Nilai Bagi Setiap Alternatif", "30"),
        ("Tabel 3.4 Kamus Data Tabel Pengguna", "36"),
        ("Tabel 3.5 Kamus Data Tabel Kriteria", "37"),
        ("Tabel 3.6 Kamus Data Tabel Alternatif", "38"),
        ("Tabel 5.1 Nilai Data Alternatif Faktual", "56"),
        ("Tabel 5.2 Hasil Normalisasi Matriks Keputusan", "57"),
        ("Tabel 5.3 Hasil Akhir Nilai Preferensi Setiap Alternatif", "59"),
        ("Tabel 5.4 Hasil Pengujian Black Box Testing Sistem", "63"),
        ("Tabel 5.5 Perbandingan Hasil Manual vs Sistem", "67")
    ]

    for tbl_title, tbl_page in table_items:
        add_leader_tab_item(doc, tbl_title, tbl_page, level=1, is_bold=False)

    # 10. DAFTAR GAMBAR (Halaman xi)
    doc.add_page_break()
    doc.add_paragraph("DAFTAR GAMBAR", style='Heading 1')

    figure_items = [
        ("Gambar 2.1 Simbol-simbol Data Flow Diagram (DFD)", "17"),
        ("Gambar 2.2 Simbol-simbol Entity Relationship Diagram (ERD)", "18"),
        ("Gambar 3.1 Diagram Konteks Sistem", "32"),
        ("Gambar 3.2 Data Flow Diagram (DFD) Level 0", "33"),
        ("Gambar 3.3 Data Flow Diagram (DFD) Level 1", "34"),
        ("Gambar 3.4 Entity Relationship Diagram (ERD) Sistem", "36"),
        ("Gambar 3.5 Rancangan Antarmuka Form Login", "40"),
        ("Gambar 3.6 Rancangan Antarmuka Menu Utama (Dashboard)", "40"),
        ("Gambar 3.7 Rancangan Antarmuka Input Kriteria", "41"),
        ("Gambar 3.8 Rancangan Antarmuka Hasil Keputusan", "42"),
        ("Gambar 4.1 Antarmuka Form Login Sistem", "50"),
        ("Gambar 4.2 Antarmuka Menu Utama (Dashboard)", "51"),
        ("Gambar 4.3 Antarmuka Input Data Kriteria", "52"),
        ("Gambar 4.4 Antarmuka Hasil Perhitungan Keputusan", "53"),
        ("Gambar 5.1 Pengujian Menu Login Berhasil", "64"),
        ("Gambar 5.2 Pengujian Validasi Password Salah", "65")
    ]

    for fig_title, fig_page in figure_items:
        add_leader_tab_item(doc, fig_title, fig_page, level=1, is_bold=False)

    # ==========================================
    # SECTION 3: BAB I s.d. BAB VI
    # ==========================================
    # BAB I PENDAHULUAN
    sec_bab1 = doc.add_section(WD_SECTION.NEW_PAGE)
    apply_section_geometry(sec_bab1)
    sec_bab1.header.is_linked_to_previous = False
    sec_bab1.footer.is_linked_to_previous = False
    sec_bab1.different_first_page_header_footer = True
    pg_arab = parse_xml(r'<w:pgNumType %s w:fmt="decimal" w:start="1"/>' % nsdecls('w'))
    sec_bab1._sectPr.append(pg_arab)

    p_f1 = sec_bab1.first_page_footer.paragraphs[0]
    p_f1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_f1 = p_f1.add_run()
    r_f1.font.name = 'Times New Roman'
    r_f1.font.size = Pt(12)
    set_page_number_field(r_f1)
    sec_bab1.first_page_header.paragraphs[0].text = ""

    p_h1 = sec_bab1.header.paragraphs[0]
    p_h1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_h1 = p_h1.add_run()
    r_h1.font.name = 'Times New Roman'
    r_h1.font.size = Pt(12)
    set_page_number_field(r_h1)
    sec_bab1.footer.paragraphs[0].text = ""

    doc.add_paragraph("BAB I\nPENDAHULUAN", style='Heading 1')
    doc.add_paragraph("1.1 Latar Belakang Masalah", style='Heading 2')
    p_body = doc.add_paragraph("Perkembangan teknologi informasi dan sistem komputer pada era modern telah berkembang dengan sangat pesat dan menjadi salah satu pilar penunjang utama dalam meningkatkan kinerja operasional, efisiensi kerja, serta keakuratan pengolahan data pada berbagai instansi, lembaga pendidikan, maupun perusahaan. Pemanfaatan sistem terkomputerisasi mampu meminimalkan tingkat kesalahan manusia (*human error*), mempercepat proses pengolahan informasi, serta menyajikan dasar pertimbangan analitis yang sangat krusial bagi pimpinan organisasi dalam merumuskan kebijakan strategis secara objektif dan akuntabel...")
    p_body.paragraph_format.first_line_indent = Cm(1.25)
    p_body.paragraph_format.line_spacing = 1.5
    p_body.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_paragraph("1.2 Rumusan Masalah", style='Heading 2')
    doc.add_paragraph("1.3 Batasan Masalah", style='Heading 2')
    doc.add_paragraph("1.4 Tujuan Penelitian", style='Heading 2')
    doc.add_paragraph("1.5 Manfaat Penelitian", style='Heading 2')
    doc.add_paragraph("1.6 Metodologi Penelitian", style='Heading 2')
    doc.add_paragraph("1.7 Sistematika Penulisan", style='Heading 2')

    # Helper function untuk menambahkan bab berikutnya
    def add_chapter_section(bab_title, subchapters):
        sec = doc.add_section(WD_SECTION.NEW_PAGE)
        apply_section_geometry(sec)
        sec.header.is_linked_to_previous = False
        sec.footer.is_linked_to_previous = False
        sec.different_first_page_header_footer = True
        pg = parse_xml(r'<w:pgNumType %s w:fmt="decimal"/>' % nsdecls('w'))
        sec._sectPr.append(pg)

        p_f = sec.first_page_footer.paragraphs[0]
        p_f.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_f = p_f.add_run()
        r_f.font.name = 'Times New Roman'
        r_f.font.size = Pt(12)
        set_page_number_field(r_f)
        sec.first_page_header.paragraphs[0].text = ""

        p_h = sec.header.paragraphs[0]
        p_h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_h = p_h.add_run()
        r_h.font.name = 'Times New Roman'
        r_h.font.size = Pt(12)
        set_page_number_field(r_h)
        sec.footer.paragraphs[0].text = ""

        doc.add_paragraph(bab_title, style='Heading 1')
        for sub_title, text_sample in subchapters:
            doc.add_paragraph(sub_title, style='Heading 2')
            p = doc.add_paragraph(text_sample)
            p.paragraph_format.first_line_indent = Cm(1.25)
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # BAB II s.d. BAB VI
    add_chapter_section("BAB II\nLANDASAN TEORI", [
        ("2.1 Konsep Sistem dan Objek Penelitian", "Secara konseptual, sistem didefinisikan sebagai kumpulan elemen atau subsistem yang saling berinteraksi, terorganisasi secara terpadu, dan beroperasi bersama untuk mencapai sasaran tertentu. Sistem pendukung keputusan dirancang adaptif untuk membantu pengambil kebijakan memecahkan permasalahan terstruktur maupun semi-terstruktur secara objektif..."),
        ("2.2 Metode Komputasi / Algoritma", "Formulasi komputasi yang diterapkan dirancang untuk memproses pembobotan multi-kriteria secara sistematis melalui normalisasi bobot preferensi dan kalkulasi vektor nilai alternatif guna menghasilkan urutan peringkat rekomendasi yang presisi..."),
        ("2.3 Konsep Pemodelan Sistem dan Basis Data", "Kaidah pemodelan fungsional digambarkan melalui Data Flow Diagram (DFD) dan Entity Relationship Diagram (ERD) guna merepresentasikan aliran informasi dan integritas relasional basis data secara konsisten..."),
        ("2.4 Perangkat Lunak dan Basis Data Pendukung", "Konstruksi sistem memanfaatkan susunan teknologi modern yang stabil, aman, dan berkinerja tinggi berbasis arsitektur terintegrasi dan sistem manajemen basis data relasional MySQL..."),
        ("2.5 Penelitian Terkait", "Analisis kritis terhadap studi literatur terdahulu dilakukan guna memetakan posisi keilmuan dan menetapkan titik kebaruan (*novelty*) penelitian ini terhadap kajian-kajian sebelumnya disajikan dalam bentuk matriks komparasi...")
    ])

    add_chapter_section("BAB III\nANALISA DAN PERANCANGAN SISTEM", [
        ("3.1 Analisa Sistem", "Analisa mendalam terhadap investigasi proses kerja konvensional saat ini guna mengidentifikasi celah inefisiensi, kebutuhan data, perangkat keras, perangkat lunak, serta spesifikasi fungsional sistem baru yang diusulkan..."),
        ("3.2 Penentuan Kriteria dan Bobot Penilaian", "Penetapan parameter kriteria keputusan berlandaskan prioritas kebijakan organisasi, normalisasi bobot preferensi, serta penentuan skala nilai konversi parameter evaluasi..."),
        ("3.3 Perancangan Sistem", "Visualisasi pemodelan diagram sistem monokromatik presisi mencakup Diagram Konteks, Data Flow Diagram (DFD) Level 0 dan Level 1..."),
        ("3.4 Perancangan Basis Data", "Perancangan Entity Relationship Diagram (ERD) relasional dan spesifikasi kamus data setiap tabel basis data..."),
        ("3.5 Perancangan Tampilan Antarmuka", "Wireframe rancangan antarmuka pengguna form login, dashboard utama, form master kriteria, form penilaian alternatif, proses komputasi, dan pencetakan laporan...")
    ])

    add_chapter_section("BAB IV\nIMPLEMENTASI SISTEM", [
        ("4.1 Batasan dan Lingkungan Implementasi", "Konfigurasi spesifikasi perangkat keras dan lingkungan perangkat lunak yang digunakan selama pengkodean dan penerapan sistem perangkat lunak..."),
        ("4.2 Implementasi Modul Komputasi", "Penerapan algoritma komputasi ke dalam baris kode program inti pengolahan data, normalisasi bobot, dan perangkingan keputusan..."),
        ("4.3 Implementasi Antarmuka Pengguna", "Dokumentasi visual tangkapan layar sistem riil yang telah dibangun mencakup antarmuka form login, menu utama, input kriteria, penilaian alternatif, eksekusi komputasi, dan cetak laporan...")
    ])

    add_chapter_section("BAB V\nPENGUJIAN DAN PEMBAHASAN", [
        ("5.1 Pengujian Model / Algoritma Komputasi", "Verifikasi pembuktian ketepatan logika komputasi matematis dengan membandingkan hasil perhitungan otomatis sistem terhadap kalkulasi manual teoritis guna membuktikan akurasi 100%..."),
        ("5.2 Pengujian Fungsional Sistem (Black Box Testing)", "Pengujian fungsionalitas tombol, navigasi, validasi masukan, dan laporan sistem menggunakan metode pengujian sistem Black Box Testing..."),
        ("5.3 Pembahasan Hasil Penelitian", "Analisis mendalam mengenai efisiensi waktu operasional, reduksi subjektivitas keputusan, serta keandalan penyimpanan data pada objek penelitian...")
    ])

    add_chapter_section("BAB VI\nPENUTUP", [
        ("6.1 Kesimpulan", "Rangkuman kesimpulan menyeluruh yang menjawab rumusan masalah dan membuktikan pencapaian tujuan penelitian skripsi..."),
        ("6.2 Saran", "Rekomendasi teknis bagi pengembangan sistem lanjutan dan saran operasional bagi pemanfaatan berkelanjutan oleh instansi...")
    ])

    # ==========================================
    # SECTION 4: DAFTAR PUSTAKA
    # ==========================================
    sec_dp = doc.add_section(WD_SECTION.NEW_PAGE)
    apply_section_geometry(sec_dp)
    sec_dp.header.is_linked_to_previous = False
    sec_dp.footer.is_linked_to_previous = False
    sec_dp.different_first_page_header_footer = True
    pg_dp = parse_xml(r'<w:pgNumType %s w:fmt="decimal"/>' % nsdecls('w'))
    sec_dp._sectPr.append(pg_dp)

    p_dp_f = sec_dp.first_page_footer.paragraphs[0]
    p_dp_f.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_dp_f = p_dp_f.add_run()
    r_dp_f.font.name = 'Times New Roman'
    r_dp_f.font.size = Pt(12)
    set_page_number_field(r_dp_f)
    sec_dp.first_page_header.paragraphs[0].text = ""

    p_dp_h = sec_dp.header.paragraphs[0]
    p_dp_h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_dp_h = p_dp_h.add_run()
    r_dp_h.font.name = 'Times New Roman'
    r_dp_h.font.size = Pt(12)
    set_page_number_field(r_dp_h)
    sec_dp.footer.paragraphs[0].text = ""

    doc.add_paragraph("DAFTAR PUSTAKA", style='Heading 1')

    ref_samples = [
        "Connolly, T. dan Begg, C. 2015. Database Systems: A Practical Approach to Design, Implementation, and Management. Edisi Ke-6. Boston: Pearson Education.",
        "Dennis, A., Wixom, B. H. dan Roth, R. M. 2018. Systems Analysis and Design. Edisi Ke-7. Hoboken: John Wiley & Sons.",
        "Pressman, R. S. dan Maxim, B. R. 2020. Software Engineering: A Practitioner's Approach. Edisi Ke-9. New York: McGraw-Hill Education.",
        "Sasmita, A. U. 2021. Penerapan Metode Weighted Product pada Sistem Pendukung Keputusan Penerimaan Rekrutmen Guru. Jurnal Informatika Almuslim, 5(2), hlm. 45-52.",
        "Turban, E., Aronson, J. E. dan Liang, T. P. 2007. Decision Support Systems and Intelligent Systems. Edisi Ke-8. Upper Saddle River: Pearson Prentice Hall."
    ]

    for ref_text in ref_samples:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.line_spacing = 1.0
        p_ref.paragraph_format.space_after = Pt(6)  # Spasi 1.5 antar-entri pustaka
        p_ref.paragraph_format.left_indent = Cm(1.25)
        p_ref.paragraph_format.first_line_indent = Cm(-1.25)
        p_ref.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r_rf = p_ref.add_run(ref_text)
        r_rf.font.name = 'Times New Roman'
        r_rf.font.size = Pt(12)

    # ==========================================
    # SECTION 5: DAFTAR RIWAYAT HIDUP
    # ==========================================
    sec_rh = doc.add_section(WD_SECTION.NEW_PAGE)
    apply_section_geometry(sec_rh)
    sec_rh.header.is_linked_to_previous = False
    sec_rh.footer.is_linked_to_previous = False
    sec_rh.different_first_page_header_footer = True
    pg_rh = parse_xml(r'<w:pgNumType %s w:fmt="decimal"/>' % nsdecls('w'))
    sec_rh._sectPr.append(pg_rh)

    p_rh_f = sec_rh.first_page_footer.paragraphs[0]
    p_rh_f.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_rh_f = p_rh_f.add_run()
    r_rh_f.font.name = 'Times New Roman'
    r_rh_f.font.size = Pt(12)
    set_page_number_field(r_rh_f)
    sec_rh.first_page_header.paragraphs[0].text = ""

    p_rh_h = sec_rh.header.paragraphs[0]
    p_rh_h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_rh_h = p_rh_h.add_run()
    r_rh_h.font.name = 'Times New Roman'
    r_rh_h.font.size = Pt(12)
    set_page_number_field(r_rh_h)
    sec_rh.footer.paragraphs[0].text = ""

    doc.add_paragraph("DAFTAR RIWAYAT HIDUP", style='Heading 1')

    doc.add_paragraph("DATA PRIBADI", style='Heading 2')
    p_rh = doc.add_paragraph()
    p_rh.paragraph_format.line_spacing = 1.15
    r_bio = p_rh.add_run(f"Nama Lengkap\t\t: {mhs_name}\nNomor Pokok Mahasiswa\t: {mhs_npm}\nTempat / Tanggal Lahir\t: Bireuen, 01 Januari 2003\nJenis Kelamin\t\t: Laki-laki / Perempuan\nAgama\t\t\t: Islam\nProgram Studi\t\t: Informatika\nFakultas\t\t\t: Fakultas Ilmu Komputer\nPerguruan Tinggi\t: Universitas Almuslim\nAlamat Rumah\t\t: Jl. Almuslim No. 01, Bireuen, Aceh")
    r_bio.font.name = 'Times New Roman'
    r_bio.font.size = Pt(12)

    doc.add_paragraph("RIWAYAT PENDIDIKAN", style='Heading 2')
    p_edu = doc.add_paragraph()
    p_edu.paragraph_format.line_spacing = 1.15
    r_edu = p_edu.add_run("1. Tahun 2009 - 2015 : SD Negeri 1 Bireuen\n2. Tahun 2015 - 2018 : SMP Negeri 1 Bireuen\n3. Tahun 2018 - 2021 : SMA Negeri 1 Bireuen\n4. Tahun 2021 - 2026 : Program Studi Informatika, Fakultas Ilmu Komputer, Universitas Almuslim")
    r_edu.font.name = 'Times New Roman'
    r_edu.font.size = Pt(12)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    print(f"[+] Master template Word resmi Almuslim berhasil dibuat: {output_path}")
    return os.path.exists(output_path)


if __name__ == "__main__":
    out_template = os.path.abspath("AI_program/working/template_skripsi_almuslim.docx")
    create_almuslim_skripsi_template(out_template)
