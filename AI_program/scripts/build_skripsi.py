"""
BUILD SKRIPSI MODULE - MASTER DOCUMENT COMPILER (MARKDOWN -> DOCX & PDF)
Universitas Almuslim - Fakultas Ilmu Komputer - Program Studi Informatika
Acuan Baku: CONTOH_SKRIPSI/Contoh_skripsi.docx & SOP Resmi Almuslim

Fitur Unggulan Sempurna:
1. Cover: Formulasi Piramida Terbalik (Inverted Pyramid) dinamis proporsional pada judul.
2. Halaman Judul Dalam (Halaman i) & Sampul Luar terpisah secara presisi sesuai kaidah akademik.
3. Spasi: 1.5 Baku (Body & List), 1.0 (Abstrak, Judul Tabel/Gambar, Daftar Pustaka).
4. Tipografi: 100% Times New Roman, Heading 1 (14 pt Bold), Heading 2 & 3 (12 pt Bold), Body (12 pt).
5. Paragraf & List Rapih:
   - Paragraf Narasi: First Line Indent 1.25 cm, Justify, bebas distorsi spasi kosong.
   - List Alfanumerik Bertingkat (SOP 4-Tingkat):
     * Tingkat 1 (1., 2.): Left 1.25 cm, First -0.75 cm (hanging)
     * Tingkat 2 (a., b.): Left 1.75 cm, First -0.50 cm (hanging)
     * Tingkat 3 (1), a)): Left 2.25 cm, First -0.50 cm (hanging)
     * Tingkat 4 ((1), (a)): Left 2.50 cm, First -0.50 cm (hanging)
   - Strict Anti-Bullet: Dilarang keras bullet (*, -, •). Baris bullet diubah menjadi hanging indent tanpa simbol bullet.
   - Format inline markdown (**bold**, *italic*) diparsing sempurna menjadi Word runs.
   - Baris pendek pengantar: Left align (tidak dipaksa justify agar tidak melar).
6. Rumus Matematika (Native Office Math / OMML):
   - Sintaks LaTeX $$...$$ dikonversi otomatis menjadi objek persamaan native Word via Word COM.
   - Rumus diletakkan di tengah (center), mandiri pada paragraf tersendiri.
7. Format Tabel Akademik (Open Academic Table):
   - Model 3 garis horizontal terbuka (tanpa garis vertikal).
   - Lebar kolom proporsional otomatis (Matriks 8 kolom, Kebutuhan 4 kolom, Basis Data 5 kolom, dll).
   - Caption tabel di atas tabel rata kiri: **Tabel X.X** (Bold) dilanjutkan Judul (Reguler).
   - Pengulangan header tabel (tblHeader) dan anti-terbelah (cantSplit).
8. Smart Image Sizing & Diagram:
   - Dimensi gambar disesuaikan secara proporsional menggunakan Pillow (PIL).
   - Landscape: Lebar maks 13.5 cm, tinggi maks 11.0 cm.
   - Portrait: Tinggi maks 12.0 cm.
   - Setiap gambar memiliki keep_with_next = True (tidak terpisah dari caption).
   - Caption gambar di bawah tengah: **Gambar X.X** (Bold) dilanjutkan Judul (Reguler).
9. Anatomi 13 Preliminary Pages Baku:
   - Sampul Luar (unprinted)
   - Sampul Dalam (i unprinted)
   - Halaman Persetujuan (ii)
   - Halaman Pengesahan (iii)
   - Halaman Pernyataan Keaslian (iv)
   - Kata Pengantar (v - vi)
   - Abstrak Bahasa Indonesia (vii)
   - Abstract Bahasa Inggris (viii)
   - DAFTAR ISI (ix, line spacing 1.1 with dot leaders)
   - DAFTAR TABEL (x)
   - DAFTAR GAMBAR (xi)
   - BAB I PENDAHULUAN (Arab 1)
10. Section Breaks & Penomoran Halaman Word Dinamis:
   - Bagian Awal: Angka Romawi kecil di tengah bawah.
   - Bagian Bab: Angka Arab di kanan atas, KECUALI halaman pertama setiap bab di tengah bawah.
11. 2-Pass Compilation Pipeline:
   - Pass 1: Kompilasi naskah awal, konversi OMML, dan ekspor PDF awal.
   - Pemindaian nomor halaman riil dari PDF via PyMuPDF (fitz).
   - Pass 2: Kompilasi naskah final dengan DAFTAR ISI, TABEL, dan GAMBAR yang sinkron 100% presisi.
"""

import os
import re
import glob
import shutil
from pathlib import Path
import yaml
import docx
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.section import WD_SECTION
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn
from PIL import Image

import win32com.client
import fitz

from table_styler import style_academic_table, add_table_caption


def apply_tnr_rfonts(run):
    """Memastikan font Times New Roman terdaftar di rFonts OpenXML."""
    rPr = run._r.get_or_add_rPr()
    ex = rPr.find(qn('w:rFonts'))
    if ex is not None:
        rPr.remove(ex)
    rf = parse_xml(r'<w:rFonts %s w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>' % nsdecls('w'))
    rPr.append(rf)


def load_project_config():
    """Memuat konfigurasi deklaratif YAML dari config/ dengan fallback otomatis."""
    root_candidates = [
        Path(os.getcwd()),
        Path(__file__).resolve().parents[2],
        Path(__file__).resolve().parents[1]
    ]
    root = None
    for r in root_candidates:
        if (r / 'config' / 'document.yaml').exists():
            root = r
            break
    if root is None:
        root = Path(os.getcwd())

    doc_conf = {
        'margins_cm': {'top': 4.0, 'left': 4.0, 'right': 3.0, 'bottom': 3.0},
        'font': 'Times New Roman',
        'normal_pt': 12,
        'heading_1_pt': 14,
        'heading_2_pt': 12,
        'heading_3_pt': 12,
        'caption_pt': 11,
        'line_spacing': 1.5,
        'first_line_indent_cm': 1.25
    }
    thesis_meta = {
        'title': '[JUDUL PENELITIAN SKRIPSI INFORMATIKA]',
        'author': '[NAMA MAHASISWA]',
        'student_id': '[NIM / NPM]',
        'study_program': 'Informatika',
        'faculty': 'Fakultas Ilmu Komputer (FIKOM)',
        'institution': 'Universitas Almuslim',
        'year': '2026',
        'pembimbing1': '[DOSEN PEMBIMBING I]',
        'nidn1': '[NIDN PEMBIMBING I]',
        'pembimbing2': '[DOSEN PEMBIMBING II]',
        'nidn2': '[NIDN PEMBIMBING II]',
        'dekan': 'Taufiq, S.T., M.T',
        'nidn_dekan': '0120057501'
    }
    chapters_conf = [
        {'id': 1, 'roman': 'I', 'title': 'PENDAHULUAN', 'file': '01_BAB_I.md', 'enabled': True},
        {'id': 2, 'roman': 'II', 'title': 'LANDASAN TEORI', 'file': '02_BAB_II.md', 'enabled': True},
        {'id': 3, 'roman': 'III', 'title': 'ANALISA DAN PERANCANGAN SISTEM', 'file': '03_BAB_III.md', 'enabled': True},
        {'id': 4, 'roman': 'IV', 'title': 'IMPLEMENTASI SISTEM', 'file': '04_BAB_IV.md', 'enabled': True},
        {'id': 5, 'roman': 'V', 'title': 'PENGUJIAN DAN PEMBAHASAN', 'file': '05_BAB_V.md', 'enabled': True},
        {'id': 6, 'roman': 'VI', 'title': 'PENUTUP', 'file': '06_BAB_VI.md', 'enabled': True}
    ]

    try:
        doc_f = root / 'config' / 'document.yaml'
        if doc_f.exists():
            data = yaml.safe_load(doc_f.read_text(encoding='utf-8'))
            if data and 'document' in data:
                doc_conf.update(data['document'])
    except Exception:
        pass

    try:
        th_f = root / 'config' / 'thesis.yaml'
        if th_f.exists():
            data = yaml.safe_load(th_f.read_text(encoding='utf-8'))
            if data and 'thesis' in data:
                t = data['thesis']
                if 'title' in t and not t['title'].startswith('['): thesis_meta['title'] = t['title']
                if 'author' in t and not t['author'].startswith('['): thesis_meta['author'] = t['author']
                if 'student_id' in t and not t['student_id'].startswith('['): thesis_meta['npm'] = t['student_id']
                if 'supervisor_1' in t and not t['supervisor_1'].startswith('['): thesis_meta['pembimbing1'] = t['supervisor_1']
                if 'nidn_supervisor_1' in t and not t['nidn_supervisor_1'].startswith('['): thesis_meta['nidn1'] = t['nidn_supervisor_1']
                if 'supervisor_2' in t and not t['supervisor_2'].startswith('['): thesis_meta['pembimbing2'] = t['supervisor_2']
                if 'nidn_supervisor_2' in t and not t['nidn_supervisor_2'].startswith('['): thesis_meta['nidn2'] = t['nidn_supervisor_2']
                if 'dean' in t and not t['dean'].startswith('['): thesis_meta['dekan'] = t['dean']
                if 'year' in t and not str(t['year']).startswith('['): thesis_meta['year'] = str(t['year'])
    except Exception:
        pass

    try:
        ch_f = root / 'config' / 'chapters.yaml'
        if ch_f.exists():
            data = yaml.safe_load(ch_f.read_text(encoding='utf-8'))
            if data and 'chapters' in data:
                chapters_conf = data['chapters']
    except Exception:
        pass

    return root, doc_conf, thesis_meta, chapters_conf


def insert_native_word_field(paragraph, instruction, default_text="[Perbarui field di Word (Tekan F9)]"):
    """Menyisipkan dynamic field native Word (TOC, PAGE, SEQ)."""
    run = paragraph.add_run()
    r = run._r
    begin = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instr = parse_xml(r'<w:instrText %s xml:space="preserve"> %s </w:instrText>' % (nsdecls('w'), instruction))
    sep = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    t = parse_xml(r'<w:t %s>%s</w:t>' % (nsdecls('w'), default_text))
    end = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    r.extend([begin, instr, sep, t, end])


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

    clean_title = re.sub(r'\s+', ' ', title.strip()).upper()
    words = clean_title.split(' ')

    if len(clean_title) <= 42 or len(words) <= 5:
        return clean_title

    # Strategi 2 Baris (Optimal jika <= 80 karakter)
    if len(clean_title) <= 80:
        best_split = None
        min_diff = 999
        for i in range(2, len(words) - 1):
            line1 = " ".join(words[:i])
            line2 = " ".join(words[i:])
            diff = len(line1) - len(line2)
            # Inverted pyramid: baris 1 harus lebih panjang atau seimbang (diff >= 0)
            if 0 <= diff <= 20:
                if diff < min_diff:
                    min_diff = diff
                    best_split = f"{line1}\n{line2}"
        if best_split:
            return best_split

    # Strategi 3 Baris (Jika > 80 karakter atau pembagian 2 baris tidak simetris)
    best_3_split = None
    min_variance = 999
    for i in range(2, len(words) - 3):
        for j in range(i + 2, len(words) - 1):
            l1 = " ".join(words[:i])
            l2 = " ".join(words[i:j])
            l3 = " ".join(words[j:])
            # Syarat piramida terbalik: len(l1) >= len(l2) >= len(l3)
            if len(l1) >= len(l2) >= len(l3) and len(l3) >= 12:
                var = (len(l1) - len(l2)) + (len(l2) - len(l3))
                if var < min_variance:
                    min_variance = var
                    best_3_split = f"{l1}\n{l2}\n{l3}"

    if best_3_split:
        return best_3_3_split if 'best_3_3_split' in locals() else best_3_split

    # Fallback seimbang default
    mid = len(words) // 2
    return " ".join(words[:mid]) + "\n" + " ".join(words[mid:])


def create_clean_page_field(paragraph, alignment=WD_ALIGN_PARAGRAPH.CENTER):
    """
    Menyisipkan field dinamis PAGE ke dalam paragraf header/footer
    secara bersih tanpa duplikasi field dari kloning section sebelumnya.
    """
    p = paragraph
    p.text = ''
    p.alignment = alignment
    pPr = p._p.get_or_add_pPr()
    for child in list(p._p):
        if child.tag != pPr.tag:
            p._p.remove(child)

    r = p.add_run()
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    apply_tnr_rfonts(r)
    fld1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    inst = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fld2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fld3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    r._r.append(fld1)
    r._r.append(inst)
    r._r.append(fld2)
    r._r.append(fld3)


def add_toc_line(doc, title_text, page_str, is_bold=False, is_sub=False, tab_position_cm=14.0):
    """
    Menambahkan satu baris Daftar Isi/Tabel/Gambar sebagai satu paragraf utuh
    dengan tab stop dot-leader rata margin kanan (14.0 cm) seperti CONTOH_SKRIPSI.
    """
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.1
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Setup Tab Stop dengan Dot Leaders pada posisi 14.0 cm
    pPr = p._p.get_or_add_pPr()
    tabs = pPr.find(qn('w:tabs'))
    if tabs is not None:
        pPr.remove(tabs)
    tabs_xml = parse_xml(r'''
        <w:tabs %s>
            <w:tab w:val="right" w:leader="dot" w:pos="%d"/>
        </w:tabs>
    ''' % (nsdecls('w'), int(tab_position_cm * 567))) # 1 cm ~ 567 dxa
    pPr.append(tabs_xml)

    # Identasi untuk subbab
    if is_sub:
        p.paragraph_format.left_indent = Cm(0.75)

    r_title = p.add_run(title_text)
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(12)
    r_title.bold = is_bold
    apply_tnr_rfonts(r_title)

    r_tab = p.add_run("\t")
    r_tab.font.name = 'Times New Roman'
    r_tab.font.size = Pt(12)
    r_tab.bold = is_bold
    apply_tnr_rfonts(r_tab)

    r_page = p.add_run(str(page_str))
    r_page.font.name = 'Times New Roman'
    r_page.font.size = Pt(12)
    r_page.bold = is_bold
    apply_tnr_rfonts(r_page)

    return p


def apply_section_geometry(sec, doc_conf=None):
    """Menerapkan margin A4 4-4-3-3 cm baku Universitas Almuslim / dari document.yaml."""
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    m = doc_conf.get('margins_cm', {'top': 4.0, 'left': 4.0, 'right': 3.0, 'bottom': 3.0}) if doc_conf else {'top': 4.0, 'left': 4.0, 'right': 3.0, 'bottom': 3.0}
    sec.top_margin = Cm(float(m.get('top', 4.0)))
    sec.left_margin = Cm(float(m.get('left', 4.0)))
    sec.bottom_margin = Cm(float(m.get('bottom', 3.0)))
    sec.right_margin = Cm(float(m.get('right', 3.0)))
    sec.header_distance = Cm(1.5)
    sec.footer_distance = Cm(1.5)


def configure_doc_styles(doc, doc_conf=None):
    """Mengatur konfigurasi style dasar dokumen agar 100% konsisten Times New Roman."""
    styles = doc.styles
    font_name = doc_conf.get('font', 'Times New Roman') if doc_conf else 'Times New Roman'
    normal_sz = doc_conf.get('normal_pt', 12) if doc_conf else 12
    h1_sz = doc_conf.get('heading_1_pt', 14) if doc_conf else 14
    h2_sz = doc_conf.get('heading_2_pt', 12) if doc_conf else 12
    h3_sz = doc_conf.get('heading_3_pt', 12) if doc_conf else 12
    l_spacing = doc_conf.get('line_spacing', 1.5) if doc_conf else 1.5

    # Normal Style (Body Text)
    style_normal = styles['Normal']
    style_normal.font.name = font_name
    style_normal.font.size = Pt(normal_sz)
    style_normal.font.color.rgb = RGBColor(0, 0, 0)
    style_normal.paragraph_format.line_spacing = l_spacing
    style_normal.paragraph_format.space_before = Pt(0)
    style_normal.paragraph_format.space_after = Pt(2)
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Heading 1 (BAB & Judul Bagian Awal)
    if 'Heading 1' in styles:
        h1 = styles['Heading 1']
        h1.font.name = font_name
        h1.font.size = Pt(h1_sz)
        h1.font.bold = True
        h1.font.color.rgb = RGBColor(0, 0, 0)
        h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        h1.paragraph_format.line_spacing = l_spacing
        h1.paragraph_format.space_before = Pt(0)
        h1.paragraph_format.space_after = Pt(12)
        h1.paragraph_format.keep_with_next = True

    # Heading 2 (Subbab Tingkat 1)
    if 'Heading 2' in styles:
        h2 = styles['Heading 2']
        h2.font.name = font_name
        h2.font.size = Pt(h2_sz)
        h2.font.bold = True
        h2.font.color.rgb = RGBColor(0, 0, 0)
        h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        h2.paragraph_format.line_spacing = l_spacing
        h2.paragraph_format.space_before = Pt(12)
        h2.paragraph_format.space_after = Pt(4)
        h2.paragraph_format.keep_with_next = True

    # Heading 3 (Subbab Tingkat 2)
    if 'Heading 3' in styles:
        h3 = styles['Heading 3']
        h3.font.name = font_name
        h3.font.size = Pt(h3_sz)
        h3.font.bold = True
        h3.font.color.rgb = RGBColor(0, 0, 0)
        h3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        h3.paragraph_format.line_spacing = l_spacing
        h3.paragraph_format.space_before = Pt(8)
        h3.paragraph_format.space_after = Pt(2)
        h3.paragraph_format.keep_with_next = True


def add_formatted_runs(paragraph, text, base_font_size=Pt(12), base_bold=False, base_italic=False):
    """
    Memproses teks berformat markdown sederhana (**bold**, *italic*, ***bold italic***)
    menjadi Word runs yang tepat tanpa menyisakan karakter asterisk mentah.
    """
    pattern = r'(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*.*?\*)'
    tokens = re.split(pattern, text)

    for token in tokens:
        if not token:
            continue
        if token.startswith('***') and token.endswith('***') and len(token) > 6:
            r = paragraph.add_run(token[3:-3])
            r.bold = True
            r.italic = True
        elif token.startswith('**') and token.endswith('**') and len(token) > 4:
            r = paragraph.add_run(token[2:-2])
            r.bold = True
            r.italic = base_italic
        elif token.startswith('*') and token.endswith('*') and len(token) > 2:
            r = paragraph.add_run(token[1:-1])
            r.bold = base_bold
            r.italic = True
        else:
            r = paragraph.add_run(token)
            r.bold = base_bold
            r.italic = base_italic

        r.font.name = 'Times New Roman'
        r.font.size = base_font_size
        r.font.color.rgb = RGBColor(0, 0, 0)
        apply_tnr_rfonts(r)


def parse_markdown_table(lines):
    """Menguraikan baris-baris tabel Markdown menjadi daftar baris data sel."""
    table_data = []
    for line in lines:
        if re.match(r'^\s*\|?\s*[-:]+[-| :]*\|?\s*$', line):
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        table_data.append(cells)
    return table_data


def add_list_item(doc, prefix, body_text):
    """
    Menambahkan item daftar nomor/huruf akademik dengan indentasi bertingkat rapi:
    - Tingkat 1 (1., 2.): Left indent 1.25 cm, hanging -0.75 cm
    - Tingkat 2 (a., b.): Left indent 1.75 cm, hanging -0.50 cm
    - Tingkat 3 (1), a)): Left indent 2.25 cm, hanging -0.50 cm
    - Tingkat 4 ((1), (a)): Left indent 2.50 cm, hanging -0.50 cm
    """
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Penentuan tingkat indentasi hierarkis
    if re.match(r'^\d+\.', prefix): # 1., 2.
        p.paragraph_format.left_indent = Cm(1.25)
        p.paragraph_format.first_line_indent = Cm(-0.75)
    elif re.match(r'^[a-zA-Z]\.', prefix): # a., b.
        p.paragraph_format.left_indent = Cm(1.75)
        p.paragraph_format.first_line_indent = Cm(-0.50)
    elif re.match(r'^(\d+\)|[a-zA-Z]\))', prefix): # 1), a)
        p.paragraph_format.left_indent = Cm(2.25)
        p.paragraph_format.first_line_indent = Cm(-0.50)
    else: # (1), (a), dll
        p.paragraph_format.left_indent = Cm(2.50)
        p.paragraph_format.first_line_indent = Cm(-0.50)

    r_pref = p.add_run(prefix + "\t")
    r_pref.font.name = 'Times New Roman'
    r_pref.font.size = Pt(12)
    r_pref.bold = True
    apply_tnr_rfonts(r_pref)

    add_formatted_runs(p, body_text, base_font_size=Pt(12))


def add_latex_equation_placeholder(doc, latex_code):
    """
    Menyisipkan penanda rumus LaTeX khusus.
    Akan dikompilasi menjadi Office Math native Word melalui COM post-processor.
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True

    r = p.add_run(f"[EQ_LATEX] {latex_code.strip()}")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    apply_tnr_rfonts(r)


def add_smart_image(doc, img_path, caption_text=""):
    """
    Menyisipkan gambar dengan kalkulasi proporsi dimensi dinamis (Smart Image Sizing):
    - Landscape: Lebar maks 13.5 cm, tinggi maks 11.0 cm.
    - Portrait: Tinggi maks 12.0 cm agar tidak meluber melewati batas halaman.
    - keep_with_next = True untuk menjamin gambar dan caption selalu berada di satu halaman.
    """
    if not os.path.exists(img_path):
        return

    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.first_line_indent = Pt(0)
    p_img.paragraph_format.space_before = Pt(12)
    p_img.paragraph_format.space_after = Pt(2)
    p_img.paragraph_format.keep_with_next = True

    try:
        with Image.open(img_path) as im:
            w_px, h_px = im.size
            aspect = w_px / float(h_px) if h_px > 0 else 1.0

        if aspect >= 1.0: # Landscape
            p_img.add_run().add_picture(img_path, width=Cm(13.5))
        else: # Portrait
            calc_h = min(12.0, 13.5 / aspect)
            p_img.add_run().add_picture(img_path, height=Cm(calc_h))
    except Exception:
        p_img.add_run().add_picture(img_path, width=Cm(13.5))

    if caption_text:
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.first_line_indent = Pt(0)
        p_cap.paragraph_format.line_spacing = 1.0
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(12)

        # Parse: "Gambar X.X Judul Gambar"
        m = re.match(r'^(Gambar\s+\d+\.\d+)\s+(.*)', caption_text.strip())
        if m:
            r_num = p_cap.add_run(f"{m.group(1)}  ")
            r_num.font.name = 'Times New Roman'
            r_num.font.size = Pt(11)
            r_num.bold = True
            apply_tnr_rfonts(r_num)

            r_title = p_cap.add_run(m.group(2))
            r_title.font.name = 'Times New Roman'
            r_title.font.size = Pt(11)
            apply_tnr_rfonts(r_title)
        else:
            r = p_cap.add_run(caption_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            apply_tnr_rfonts(r)


def get_context_metadata():
    """Membaca parameter identitas penelitian dari CONTEXT_SKRIPSI.txt secara dinamis."""
    meta = {
        "title": "[JUDUL PENELITIAN SKRIPSI INFORMATIKA]",
        "author": "[NAMA MAHASISWA]",
        "npm": "[NIM / NPM]",
        "pembimbing1": "[DOSEN PEMBIMBING I]",
        "nidn1": "[NIDN PEMBIMBING I]",
        "pembimbing2": "[DOSEN PEMBIMBING II]",
        "nidn2": "[NIDN PEMBIMBING II]",
        "dekan": "[NAMA DEKAN / PIMPINAN FAKULTAS]",
        "nidn_dekan": "[NIDN DEKAN]",
        "year": "2026"
    }
    candidate_paths = [
        os.path.abspath("CONTEXT_SKRIPSI.txt"),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "CONTEXT_SKRIPSI.txt")),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "CONTEXT_SKRIPSI.txt")),
    ]
    c_path = None
    for cp in candidate_paths:
        if os.path.exists(cp):
            c_path = cp
            break

    if c_path and os.path.exists(c_path):
        try:
            with open(c_path, 'r', encoding='utf-8') as f:
                content = f.read()
            m_title = re.search(r'Judul Skripsi\s*:\s*(.+)', content)
            if m_title and not m_title.group(1).startswith('['):
                meta["title"] = m_title.group(1).strip()

            m_name = re.search(r'Nama Mahasiswa\s*:\s*(.+)', content)
            if m_name and not m_name.group(1).startswith('['):
                meta["author"] = m_name.group(1).strip()

            m_npm = re.search(r'NIM\s*/\s*NPM\s*:\s*(.+)', content)
            if m_npm and not m_npm.group(1).startswith('['):
                meta["npm"] = m_npm.group(1).strip()

            m_p1 = re.search(r'Dosen Pembimbing I\s*:\s*(.+)', content)
            if m_p1 and not m_p1.group(1).startswith('['):
                meta["pembimbing1"] = m_p1.group(1).strip()

            m_nidn1 = re.search(r'NIDN Pembimbing I\s*:\s*(.+)', content)
            if m_nidn1 and not m_nidn1.group(1).startswith('['):
                meta["nidn1"] = m_nidn1.group(1).strip()

            m_p2 = re.search(r'Dosen Pembimbing II\s*:\s*(.+)', content)
            if m_p2 and not m_p2.group(1).startswith('['):
                meta["pembimbing2"] = m_p2.group(1).strip()

            m_nidn2 = re.search(r'NIDN Pembimbing II\s*:\s*(.+)', content)
            if m_nidn2 and not m_nidn2.group(1).startswith('['):
                meta["nidn2"] = m_nidn2.group(1).strip()
        except Exception:
            pass
    return meta


def parse_and_add_content(doc, md_path):
    """
    Mengurai berkas Markdown bab per baris secara cerdas:
    - Heading 1, 2, 3
    - Paragraf narasi (first line indent 1.25 cm, justify)
    - List alfanumerik bertingkat (1., a., 1), (1))
    - Rumus matematika LaTeX $$...$$
    - Tabel Markdown
    - Gambar Markdown
    """
    if not os.path.exists(md_path):
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    idx = 0
    table_lines = []

    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()

        # Lewati blok kode penutup
        if stripped.startswith('```'):
            idx += 1
            continue

        # Proses Tabel Markdown
        if stripped.startswith('|'):
            table_lines.append(stripped)
            idx += 1
            continue
        elif table_lines:
            t_data = parse_markdown_table(table_lines)
            if t_data and len(t_data) > 1:
                t = doc.add_table(rows=len(t_data), cols=len(t_data[0]))
                for r_i, r_vals in enumerate(t_data):
                    for c_i, c_val in enumerate(r_vals):
                        if c_i < len(t.rows[r_i].cells):
                            cell = t.rows[r_i].cells[c_i]
                            cell.text = ''
                            p = cell.paragraphs[0]
                            add_formatted_runs(p, c_val, base_font_size=Pt(10))
                style_academic_table(t)
            table_lines = []
            continue

        if not stripped:
            idx += 1
            continue

        # Rumus Matematika LaTeX $$...$$
        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
            latex_code = stripped[2:-2].strip()
            add_latex_equation_placeholder(doc, latex_code)
            idx += 1
            continue

        # Judul Tabel (### Tabel X.X Judul)
        if stripped.startswith('### Tabel') or stripped.startswith('Tabel '):
            add_table_caption(doc, stripped)
            idx += 1
            continue

        # Heading 1 (BAB I, BAB II, dst.)
        if stripped.startswith('# '):
            h_text = stripped[2:].strip()
            p = doc.add_paragraph(style='Heading 1')
            r = p.add_run(h_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(14)
            r.bold = True
            apply_tnr_rfonts(r)
            idx += 1
            continue

        # Heading 2 (## 1.1, ## 1.2, dst.)
        if stripped.startswith('## '):
            h_text = stripped[3:].strip()
            p = doc.add_paragraph(style='Heading 2')
            r = p.add_run(h_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = True
            apply_tnr_rfonts(r)
            idx += 1
            continue

        # Heading 3 (### 1.1.1, ### 1.1.2, dst.)
        if stripped.startswith('### ') and not stripped.startswith('### Tabel'):
            h_text = stripped[4:].strip()
            p = doc.add_paragraph(style='Heading 3')
            r = p.add_run(h_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = True
            apply_tnr_rfonts(r)
            idx += 1
            continue

        # Gambar Markdown (![Caption](Path))
        m_img = re.match(r'^!\[(.*?)\]\((.*?)\)', stripped)
        if m_img:
            caption = m_img.group(1).strip()
            img_path = m_img.group(2).strip()
            add_smart_image(doc, img_path, caption)
            idx += 1
            continue

        # List Alfanumerik Bertingkat (misal: 1. , a. , 1) , (1) )
        m_num = re.match(r'^(\d+\.|[a-zA-Z]\.|\d+\)|[a-zA-Z]\)|\(\d+\)|\([a-zA-Z]\))\s+(.*)', stripped)
        if m_num:
            prefix, text_item = m_num.groups()
            add_list_item(doc, prefix, text_item)
            idx += 1
            continue

        # Penanganan Anti-Bullet (Jika tidak sengaja ada simbol -, *, •)
        m_bullet = re.match(r'^[\-\*•]\s+(.*)', stripped)
        if m_bullet:
            text_item = m_bullet.group(1)
            # Konversi menjadi format hanging tanpa simbol bullet
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1.25)
            p.paragraph_format.first_line_indent = Cm(-0.50)
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_formatted_runs(p, text_item, base_font_size=Pt(12))
            idx += 1
            continue

        # Baris Pendek Pengantar (misal: "Tujuan penelitian dirumuskan sebagai berikut:")
        if len(stripped) < 75 and (stripped.endswith(':') or not stripped.endswith('.')):
            p = doc.add_paragraph()
            p.paragraph_format.first_line_indent = Cm(1.25)
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_runs(p, stripped)
            idx += 1
            continue

        # Paragraf Narasi Normal (Multi-baris dikonsolidasikan agar justify mulus)
        prose_lines = [stripped]
        while idx + 1 < len(lines):
            next_line = lines[idx + 1].strip()
            if not next_line:
                break
            if next_line.startswith('#') or next_line.startswith('|') or next_line.startswith('![') or next_line.startswith('$$') or re.match(r'^(\d+\.|[a-zA-Z]\.|\d+\)|[a-zA-Z]\)|\(\d+\)|\([a-zA-Z]\)|[\-\*•])\s+', next_line):
                break
            prose_lines.append(next_line)
            idx += 1

        full_prose = " ".join(prose_lines)
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(1.25)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_formatted_runs(p, full_prose)
        idx += 1


def add_chapter_to_doc(doc, md_path, is_first_chapter=False, start_page_num=None):
    """Membaca file draf Markdown bab dan memasukkannya ke dokumen Word secara presisi."""
    if not os.path.exists(md_path):
        return

    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    apply_section_geometry(sec)
    sec.header.is_linked_to_previous = False
    sec.footer.is_linked_to_previous = False
    sec.different_first_page_header_footer = True

    # Section page numbering
    if start_page_num is not None:
        pg_arab = parse_xml(r'<w:pgNumType %s w:fmt="decimal" w:start="%d"/>' % (nsdecls('w'), start_page_num))
        sec._sectPr.append(pg_arab)
    elif is_first_chapter:
        pg_arab = parse_xml(r'<w:pgNumType %s w:fmt="decimal" w:start="1"/>' % nsdecls('w'))
        sec._sectPr.append(pg_arab)

    # First page: Center Footer, Header Kosong
    sec.first_page_header.paragraphs[0].text = ""
    create_clean_page_field(sec.first_page_footer.paragraphs[0], alignment=WD_ALIGN_PARAGRAPH.CENTER)

    # Subsequent pages: Right Header, Footer Kosong
    sec.footer.paragraphs[0].text = ""
    create_clean_page_field(sec.header.paragraphs[0], alignment=WD_ALIGN_PARAGRAPH.RIGHT)

    parse_and_add_content(doc, md_path)


def extract_structure_from_drafts():
    """
    Mengekstrak secara dinamis seluruh Bab, Subbab, Tabel, dan Gambar
    dari seluruh berkas draf Markdown secara otomatis.
    """
    candidates = sorted(glob.glob("drafts/0[1-9]_BAB_*.md") + glob.glob("../../drafts/0[1-9]_BAB_*.md"))
    if not candidates:
        candidates = sorted(glob.glob("drafts/*.md") + glob.glob("../../drafts/*.md"))

    toc_chapters = []
    tables = []
    figures = []

    for fpath in candidates:
        bn = os.path.basename(fpath)
        if "00_BAGIAN_AWAL" in bn or "07_DAFTAR_PUSTAKA" in bn or "08_DAFTAR_RIWAYAT_HIDUP" in bn:
            continue
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for line in lines:
                s = line.strip()
                if not s or s.startswith('<!--'):
                    continue
                # Heading 1
                if s.startswith('# ') and 'BAB' in s.upper():
                    clean_h1 = s[2:].strip()
                    toc_chapters.append((clean_h1, True, False))
                # Heading 2
                elif s.startswith('## ') and re.match(r'^##\s+\d+\.\d+', s):
                    clean_h2 = s[3:].strip()
                    toc_chapters.append((clean_h2, False, True))
                # Tabel
                elif s.startswith('### Tabel') or (s.startswith('Tabel ') and len(s) < 120 and '|' not in s):
                    clean_tbl = s.replace('###', '').strip()
                    if clean_tbl not in tables:
                        tables.append(clean_tbl)
                # Gambar
                elif s.startswith('!['):
                    m = re.match(r'^!\[(.*?)\]', s)
                    if m and ('Gambar' in m.group(1) or 'GAMBAR' in m.group(1)):
                        clean_fig = m.group(1).strip()
                        if clean_fig not in figures:
                            figures.append(clean_fig)
        except Exception:
            pass

    return toc_chapters, tables, figures


def build_full_thesis(output_docx_path, page_map=None):
    """
    Mengompilasi seluruh berkas draf menjadi dokumen skripsi Word resmi sempurna.
    page_map: Kamus hasil pemindaian nomor halaman riil dari Pass 1 PDF.
    """
    print(f"[*] Memulai kompilasi naskah skripsi resmi Almuslim...")
    root_dir, doc_conf, meta, chapters_conf = load_project_config()
    fb_meta = get_context_metadata()
    for k, v in fb_meta.items():
        if k not in meta or str(meta[k]).startswith('['):
            meta[k] = v

    doc = Document()
    configure_doc_styles(doc, doc_conf=doc_conf)

    logo_path = os.path.abspath("ASSETS/logo_umuslim.jpg")
    if not os.path.exists(logo_path):
        logo_path = os.path.abspath(os.path.join(str(root_dir), "ASSETS/logo_umuslim.jpg"))
    pyramid_title = format_inverted_pyramid(meta["title"])

    # ==========================================
    # SECTION 1: SAMPUL LUAR (Outer Cover)
    # Tanpa nomor halaman, tanpa kalimat pengajuan
    # ==========================================
    sec_cover = doc.sections[0]
    apply_section_geometry(sec_cover, doc_conf=doc_conf)
    sec_cover.header.is_linked_to_previous = False
    sec_cover.footer.is_linked_to_previous = False

    p_cov = doc.add_paragraph()
    p_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cov.paragraph_format.line_spacing = 1.15
    p_cov.paragraph_format.space_before = Pt(0)
    p_cov.paragraph_format.space_after = Pt(16)
    r_cov = p_cov.add_run(pyramid_title)
    r_cov.font.name = 'Times New Roman'
    r_cov.font.size = Pt(14)
    r_cov.bold = True
    apply_tnr_rfonts(r_cov)

    p_skrip = doc.add_paragraph()
    p_skrip.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_skrip.paragraph_format.space_after = Pt(24)
    r_skrip = p_skrip.add_run("SKRIPSI")
    r_skrip.font.name = 'Times New Roman'
    r_skrip.font.size = Pt(14)
    r_skrip.bold = True
    apply_tnr_rfonts(r_skrip)

    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_after = Pt(28)
    if os.path.exists(logo_path):
        p_logo.add_run().add_picture(logo_path, width=Cm(4.5))

    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.line_spacing = 1.15
    p_auth.paragraph_format.space_after = Pt(36)
    r_auth = p_auth.add_run(f"OLEH:\n\n{meta['author']}\nNPM. {meta['npm']}")
    r_auth.font.name = 'Times New Roman'
    r_auth.font.size = Pt(12)
    r_auth.bold = True
    apply_tnr_rfonts(r_auth)

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.line_spacing = 1.15
    r_inst = p_inst.add_run(f"PROGRAM STUDI INFORMATIKA\nFAKULTAS ILMU KOMPUTER\nUNIVERSITAS ALMUSLIM\nBIREUEN\n{meta['year']}")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(14)
    r_inst.bold = True
    apply_tnr_rfonts(r_inst)

    # ==========================================
    # SECTION 2: BAGIAN AWAL (Romawi Kecil: i s.d. xi)
    # Halaman Judul Dalam dihitung sebagai i (tidak dicetak)
    # ==========================================
    sec_prelim = doc.add_section(WD_SECTION.NEW_PAGE)
    apply_section_geometry(sec_prelim)
    sec_prelim.header.is_linked_to_previous = False
    sec_prelim.footer.is_linked_to_previous = False
    sec_prelim.different_first_page_header_footer = True
    pg_roman = parse_xml(r'<w:pgNumType %s w:fmt="lowerRoman" w:start="1"/>' % nsdecls('w'))
    sec_prelim._sectPr.append(pg_roman)

    # Halaman i (Halaman Judul): nomor tidak dicetak
    sec_prelim.first_page_footer.paragraphs[0].text = ""
    sec_prelim.first_page_header.paragraphs[0].text = ""

    # Halaman ii dst: nomor Romawi di tengah bawah
    p_foot_p = sec_prelim.footer.paragraphs[0]
    p_foot_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    create_clean_page_field(p_foot_p, alignment=WD_ALIGN_PARAGRAPH.CENTER)
    sec_prelim.header.paragraphs[0].text = ""

    # 1. HALAMAN JUDUL (Inner Title Page - Halaman i)
    p_in_cov = doc.add_paragraph()
    p_in_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_cov.paragraph_format.line_spacing = 1.15
    p_in_cov.paragraph_format.space_before = Pt(0)
    p_in_cov.paragraph_format.space_after = Pt(12)
    r_incov = p_in_cov.add_run(pyramid_title)
    r_incov.font.name = 'Times New Roman'
    r_incov.font.size = Pt(14)
    r_incov.bold = True
    apply_tnr_rfonts(r_incov)

    p_in_sub = doc.add_paragraph()
    p_in_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_sub.paragraph_format.line_spacing = 1.0
    p_in_sub.paragraph_format.space_after = Pt(16)
    r_insub = p_in_sub.add_run("SKRIPSI\n\nDiajukan Untuk Memenuhi Salah Satu Syarat\nMemperoleh Gelar Sarjana Komputer (S.Kom)\nPada Program Studi Informatika")
    r_insub.font.name = 'Times New Roman'
    r_insub.font.size = Pt(12)
    apply_tnr_rfonts(r_insub)

    p_in_logo = doc.add_paragraph()
    p_in_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_logo.paragraph_format.space_after = Pt(16)
    if os.path.exists(logo_path):
        p_in_logo.add_run().add_picture(logo_path, width=Cm(4.5))

    p_in_auth = doc.add_paragraph()
    p_in_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_auth.paragraph_format.line_spacing = 1.15
    p_in_auth.paragraph_format.space_after = Pt(20)
    r_inauth = p_in_auth.add_run(f"OLEH:\n\n{meta['author']}\nNPM. {meta['npm']}")
    r_inauth.font.name = 'Times New Roman'
    r_inauth.font.size = Pt(12)
    r_inauth.bold = True
    apply_tnr_rfonts(r_inauth)

    p_in_inst = doc.add_paragraph()
    p_in_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_in_inst.paragraph_format.line_spacing = 1.15
    r_ininst = p_in_inst.add_run(f"PROGRAM STUDI INFORMATIKA\nFAKULTAS ILMU KOMPUTER\nUNIVERSITAS ALMUSLIM\nBIREUEN\n{meta['year']}")
    r_ininst.font.name = 'Times New Roman'
    r_ininst.font.size = Pt(14)
    r_ininst.bold = True
    apply_tnr_rfonts(r_ininst)

    # 2. HALAMAN PERSETUJUAN (Halaman ii)
    doc.add_page_break()
    doc.add_paragraph("HALAMAN PERSETUJUAN", style='Heading 1')
    p_pers = doc.add_paragraph()
    p_pers.paragraph_format.line_spacing = 1.5
    p_pers.paragraph_format.space_before = Pt(12)
    p_pers.add_run("Skripsi dengan judul:\n\"").font.size = Pt(12)
    p_pers.add_run(meta["title"]).bold = True
    p_pers.add_run("\"\n\nTelah disetujui untuk disidangkan di hadapan Dewan Penguji Sidang Sarjana Program Studi Informatika, Fakultas Ilmu Komputer, Universitas Almuslim.\n\n\n")

    p_ttd_pers = doc.add_paragraph()
    p_ttd_pers.paragraph_format.line_spacing = 1.15
    p_ttd_pers.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ttd_pers.add_run(f"Menyetujui,\n\n\n\nPembimbing I\t\t\t\t\t\tPembimbing II\n\n\n\n\n{meta['pembimbing1']}\t\t\t\t{meta['pembimbing2']}\nNIDN. {meta['nidn1']}\t\t\t\t\tNIDN. {meta['nidn2']}")

    # 3. HALAMAN PENGESAHAN (Halaman iii)
    doc.add_page_break()
    doc.add_paragraph("HALAMAN PENGESAHAN", style='Heading 1')
    p_peng = doc.add_paragraph()
    p_peng.paragraph_format.line_spacing = 1.5
    p_peng.paragraph_format.space_before = Pt(12)
    p_peng.add_run("Skripsi dengan judul:\n\"").font.size = Pt(12)
    p_peng.add_run(meta["title"]).bold = True
    p_peng.add_run("\"\n\nTelah dipertahankan di hadapan Dewan Penguji Sidang Sarjana Program Studi Informatika, Fakultas Ilmu Komputer, Universitas Almuslim dan dinyatakan LULUS.\n\n\n")

    p_ttd = doc.add_paragraph()
    p_ttd.paragraph_format.line_spacing = 1.15
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ttd.add_run(f"Mengesahkan,\n\n\n\nDekan Fakultas Ilmu Komputer\t\t\t\tKetua Program Studi Informatika\n\n\n\n\n{meta['dekan']}\t\t\t\t{meta['pembimbing2']}\nNIDN. {meta['nidn_dekan']}\t\t\t\t\tNIDN. {meta['nidn2']}")

    # 4. HALAMAN PERNYATAAN KEASLIAN (Halaman iv)
    doc.add_page_break()
    doc.add_paragraph("HALAMAN PERNYATAAN KEASLIAN", style='Heading 1')
    p_perny = doc.add_paragraph()
    p_perny.paragraph_format.line_spacing = 1.5
    p_perny.paragraph_format.first_line_indent = Cm(1.25)
    p_perny.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_perny.add_run("Saya yang bertanda tangan di bawah ini menyatakan dengan sesungguhnya bahwa skripsi yang berjudul \"")
    p_perny.add_run(meta["title"]).bold = True
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
    r_abt = p_ab_title.add_run(meta["title"])
    r_abt.bold = True
    apply_tnr_rfonts(r_abt)

    p_ab_author = doc.add_paragraph()
    p_ab_author.paragraph_format.line_spacing = 1.0
    p_ab_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ab_author.paragraph_format.space_after = Pt(12)
    r_aba = p_ab_author.add_run(f"Oleh:\n{meta['author']} / {meta['npm']}")
    apply_tnr_rfonts(r_aba)

    p_abb = doc.add_paragraph()
    p_abb.paragraph_format.line_spacing = 1.0
    p_abb.paragraph_format.first_line_indent = Cm(1.25)
    p_abb.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_abb = p_abb.add_run("Abstrak disusun dalam satu paragraf tunggal yang memuat 150 hingga 250 kata dengan spasi 1.0 (tunggal). Memuat secara terpadu latar belakang fenomena masalah, rumusan masalah dan tujuan utama penelitian, metode komputasi serta arsitektur sistem informasi yang dibangun, hasil pengujian empiris dan kalkulasi validasi, serta kesimpulan praktis dan akademis yang dihasilkan.")
    apply_tnr_rfonts(r_abb)

    p_abk = doc.add_paragraph()
    p_abk.paragraph_format.line_spacing = 1.0
    p_abk.paragraph_format.space_before = Pt(8)
    r_kw_l = p_abk.add_run("Kata Kunci: ")
    r_kw_l.bold = True
    apply_tnr_rfonts(r_kw_l)
    r_kw_v = p_abk.add_run("Sistem Pendukung Keputusan, Metode Komputasi, Algoritma, Informatika, Universitas Almuslim.")
    apply_tnr_rfonts(r_kw_v)

    # 7. ABSTRACT (Halaman viii - Single Spacing, Italic)
    doc.add_page_break()
    doc.add_paragraph("ABSTRACT", style='Heading 1')
    p_aben_title = doc.add_paragraph()
    p_aben_title.paragraph_format.line_spacing = 1.15
    p_aben_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_aben_title.paragraph_format.space_after = Pt(4)
    r_en_t = p_aben_title.add_run(meta["title"])
    r_en_t.bold = True
    r_en_t.italic = True
    apply_tnr_rfonts(r_en_t)

    p_aben_author = doc.add_paragraph()
    p_aben_author.paragraph_format.line_spacing = 1.0
    p_aben_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_aben_author.paragraph_format.space_after = Pt(12)
    r_en_a = p_aben_author.add_run(f"By:\n{meta['author']} / {meta['npm']}")
    r_en_a.italic = True
    apply_tnr_rfonts(r_en_a)

    p_abben = doc.add_paragraph()
    p_abben.paragraph_format.line_spacing = 1.0
    p_abben.paragraph_format.first_line_indent = Cm(1.25)
    p_abben.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_en_b = p_abben.add_run("The abstract is written in a single paragraph comprising 150 to 250 words with 1.0 (single) line spacing. It comprehensively presents the research background, problem formulation and core objectives, computational methods, software system architecture, empirical testing and calculation results, as well as practical and academic conclusions.")
    r_en_b.italic = True
    apply_tnr_rfonts(r_en_b)

    p_abken = doc.add_paragraph()
    p_abken.paragraph_format.line_spacing = 1.0
    p_abken.paragraph_format.space_before = Pt(8)
    r_en_kl = p_abken.add_run("Keywords: ")
    r_en_kl.bold = True
    r_en_kl.italic = True
    apply_tnr_rfonts(r_en_kl)
    r_en_kv = p_abken.add_run("Decision Support System, Computational Method, Algorithm, Informatics, Universitas Almuslim.")
    r_en_kv.italic = True
    apply_tnr_rfonts(r_en_kv)

    # 8. DAFTAR ISI (Halaman ix)
    doc.add_page_break()
    doc.add_paragraph("DAFTAR ISI", style='Heading 1')

    # Sisipkan native Word Dynamic Field TOC
    p_fld_toc = doc.add_paragraph()
    insert_native_word_field(p_fld_toc, r'TOC \o "1-3" \h \z \u')

    # Mapping helper jika page_map tersedia
    def get_p(key, default):
        if page_map and key in page_map:
            return str(page_map[key])
        return str(default)

    # Ekstraksi dinamis struktur draf
    dyn_headings, dyn_tables, dyn_figures = extract_structure_from_drafts()

    # Preliminaries standar akademik
    toc_items = [
        ("HALAMAN JUDUL", get_p("HALAMAN_JUDUL", "i"), False, False),
        ("HALAMAN PERSETUJUAN", get_p("HALAMAN_PERSETUJUAN", "ii"), False, False),
        ("HALAMAN PENGESAHAN", get_p("HALAMAN_PENGESAHAN", "iii"), False, False),
        ("HALAMAN PERNYATAAN KEASLIAN", get_p("HALAMAN_PERNYATAAN", "iv"), False, False),
        ("KATA PENGANTAR", get_p("KATA_PENGANTAR", "v"), False, False),
        ("ABSTRAK", get_p("ABSTRAK", "vii"), False, False),
        ("ABSTRACT", get_p("ABSTRACT", "viii"), False, False),
        ("DAFTAR ISI", get_p("DAFTAR_ISI", "ix"), True, False),
        ("DAFTAR TABEL", get_p("DAFTAR_TABEL", "x"), False, False),
        ("DAFTAR GAMBAR", get_p("DAFTAR_GAMBAR", "xi"), False, False),
    ]

    if dyn_headings:
        for h_title, is_b, is_s in dyn_headings:
            # Ambil key nomor (misal 1.1 dari "1.1 Latar Belakang")
            m_k = re.match(r'^(\d+\.\d+|\bBAB\s+[IVXLCDM]+\b)', h_title)
            k = m_k.group(1).replace(' ', '_') if m_k else h_title[:10]
            p_val = get_p(k, "1" if "BAB_I" in k else "...")
            toc_items.append((h_title, p_val, is_b, is_s))
    else:
        # Fallback standar 6 BAB
        fallback_heads = [
            ("BAB I PENDAHULUAN", get_p("BAB_I", "1"), True, False),
            ("1.1 Latar Belakang Masalah", get_p("1.1", "1"), False, True),
            ("1.2 Rumusan Masalah", get_p("1.2", "3"), False, True),
            ("1.3 Batasan Masalah", get_p("1.3", "4"), False, True),
            ("1.4 Tujuan Penelitian", get_p("1.4", "4"), False, True),
            ("1.5 Manfaat Penelitian", get_p("1.5", "5"), False, True),
            ("1.6 Metodologi Penelitian", get_p("1.6", "5"), False, True),
            ("1.7 Sistematika Penulisan", get_p("1.7", "6"), False, True),
            ("BAB II LANDASAN TEORI", get_p("BAB_II", "8"), True, False),
            ("2.1 Konsep Sistem dan Objek Penelitian", get_p("2.1", "8"), False, True),
            ("2.2 Metode Komputasi / Algoritma", get_p("2.2", "11"), False, True),
            ("2.3 Konsep Pemodelan Sistem dan Basis Data", get_p("2.3", "16"), False, True),
            ("2.4 Perangkat Lunak dan Basis Data Pendukung", get_p("2.4", "19"), False, True),
            ("2.5 Penelitian Terkait", get_p("2.5", "21"), False, True),
            ("BAB III ANALISA DAN PERANCANGAN SISTEM", get_p("BAB_III", "24"), True, False),
            ("3.1 Analisa Sistem", get_p("3.1", "24"), False, True),
            ("3.2 Penentuan Kriteria dan Bobot Penilaian", get_p("3.2", "28"), False, True),
            ("3.3 Perancangan Sistem", get_p("3.3", "31"), False, True),
            ("3.4 Perancangan Basis Data", get_p("3.4", "35"), False, True),
            ("3.5 Perancangan Tampilan Antarmuka", get_p("3.5", "39"), False, True),
            ("BAB IV IMPLEMENTASI SISTEM", get_p("BAB_IV", "43"), True, False),
            ("4.1 Batasan dan Lingkungan Implementasi", get_p("4.1", "43"), False, True),
            ("4.2 Implementasi Modul Komputasi", get_p("4.2", "45"), False, True),
            ("4.3 Implementasi Antarmuka Pengguna", get_p("4.3", "49"), False, True),
            ("BAB V PENGUJIAN DAN PEMBAHASAN", get_p("BAB_V", "55"), True, False),
            ("5.1 Pengujian Model / Algoritma Komputasi", get_p("5.1", "55"), False, True),
            ("5.2 Pengujian Fungsional Sistem (Black Box Testing)", get_p("5.2", "61"), False, True),
            ("5.3 Pembahasan Hasil Penelitian", get_p("5.3", "66"), False, True),
            ("BAB VI PENUTUP", get_p("BAB_VI", "71"), True, False),
            ("6.1 Kesimpulan", get_p("6.1", "71"), False, True),
            ("6.2 Saran", get_p("6.2", "72"), False, True),
        ]
        toc_items.extend(fallback_heads)

    toc_items.append(("DAFTAR PUSTAKA", get_p("DAFTAR_PUSTAKA", "74"), True, False))
    toc_items.append(("DAFTAR RIWAYAT HIDUP", get_p("DAFTAR_RIWAYAT_HIDUP", "77"), True, False))

    for t_title, t_page, is_b, is_s in toc_items:
        add_toc_line(doc, t_title, t_page, is_bold=is_b, is_sub=is_s)

    # 9. DAFTAR TABEL (Halaman x)
    doc.add_page_break()
    doc.add_paragraph("DAFTAR TABEL", style='Heading 1')

    # Sisipkan native Word Dynamic Field Tabel
    p_fld_tbl = doc.add_paragraph()
    insert_native_word_field(p_fld_tbl, r'TOC \h \z \c "Tabel"')

    if dyn_tables:
        for tbl_title in dyn_tables:
            m_tnum = re.search(r'Tabel\s+(\d+\.\d+)', tbl_title)
            t_key = f"TABEL_{m_tnum.group(1).replace('.', '_')}" if m_tnum else "TABEL"
            tbl_page = get_p(t_key, "...")
            add_toc_line(doc, tbl_title, tbl_page, is_bold=False, is_sub=False)
    else:
        table_items = [
            ("Tabel 2.1 Matriks Perbandingan Penelitian Terdahulu", get_p("TABEL_2_1", "22")),
            ("Tabel 3.1 Kriteria Penilaian dan Bobot", get_p("TABEL_3_1", "28")),
            ("Tabel 3.2 Bobot Kriteria", get_p("TABEL_3_2", "29")),
            ("Tabel 3.3 Penentuan Nilai Bagi Setiap Alternatif", get_p("TABEL_3_3", "30")),
            ("Tabel 3.4 Kamus Data Tabel Pengguna", get_p("TABEL_3_4", "36")),
            ("Tabel 3.5 Kamus Data Tabel Kriteria", get_p("TABEL_3_5", "37")),
            ("Tabel 3.6 Kamus Data Tabel Alternatif", get_p("TABEL_3_6", "38")),
            ("Tabel 5.1 Nilai Data Alternatif Faktual", get_p("TABEL_5_1", "56")),
            ("Tabel 5.2 Hasil Normalisasi Matriks Keputusan", get_p("TABEL_5_2", "57")),
            ("Tabel 5.3 Hasil Akhir Nilai Preferensi Setiap Alternatif", get_p("TABEL_5_3", "59")),
            ("Tabel 5.4 Hasil Pengujian Black Box Testing Sistem", get_p("TABEL_5_4", "63")),
            ("Tabel 5.5 Perbandingan Hasil Manual vs Sistem", get_p("TABEL_5_5", "67"))
        ]
        for tbl_title, tbl_page in table_items:
            add_toc_line(doc, tbl_title, tbl_page, is_bold=False, is_sub=False)

    # 10. DAFTAR GAMBAR (Halaman xi)
    doc.add_page_break()
    doc.add_paragraph("DAFTAR GAMBAR", style='Heading 1')

    # Sisipkan native Word Dynamic Field Gambar
    p_fld_fig = doc.add_paragraph()
    insert_native_word_field(p_fld_fig, r'TOC \h \z \c "Gambar"')

    if dyn_figures:
        for fig_title in dyn_figures:
            m_fnum = re.search(r'Gambar\s+(\d+\.\d+)', fig_title)
            f_key = f"GAMBAR_{m_fnum.group(1).replace('.', '_')}" if m_fnum else "GAMBAR"
            fig_page = get_p(f_key, "...")
            add_toc_line(doc, fig_title, fig_page, is_bold=False, is_sub=False)
    else:
        figure_items = [
            ("Gambar 2.1 Simbol-simbol Data Flow Diagram (DFD)", get_p("GAMBAR_2_1", "17")),
            ("Gambar 2.2 Simbol-simbol Entity Relationship Diagram (ERD)", get_p("GAMBAR_2_2", "18")),
            ("Gambar 3.1 Diagram Konteks Sistem", get_p("GAMBAR_3_1", "32")),
            ("Gambar 3.2 Data Flow Diagram (DFD) Level 0", get_p("GAMBAR_3_2", "33")),
            ("Gambar 3.3 Data Flow Diagram (DFD) Level 1", get_p("GAMBAR_3_3", "34")),
            ("Gambar 3.4 Entity Relationship Diagram (ERD) Sistem", get_p("GAMBAR_3_4", "36")),
            ("Gambar 3.5 Rancangan Antarmuka Form Login", get_p("GAMBAR_3_5", "40")),
            ("Gambar 3.6 Rancangan Antarmuka Menu Utama (Dashboard)", get_p("GAMBAR_3_6", "40")),
            ("Gambar 3.7 Rancangan Antarmuka Input Kriteria", get_p("GAMBAR_3_7", "41")),
            ("Gambar 3.8 Rancangan Antarmuka Hasil Keputusan", get_p("GAMBAR_3_8", "42")),
            ("Gambar 4.1 Antarmuka Form Login Sistem", get_p("GAMBAR_4_1", "50")),
            ("Gambar 4.2 Antarmuka Menu Utama (Dashboard)", get_p("GAMBAR_4_2", "51")),
            ("Gambar 4.3 Antarmuka Input Data Kriteria", get_p("GAMBAR_4_3", "52")),
            ("Gambar 4.4 Antarmuka Hasil Perhitungan Keputusan", get_p("GAMBAR_4_4", "53")),
            ("Gambar 5.1 Pengujian Menu Login Berhasil", get_p("GAMBAR_5_1", "64")),
            ("Gambar 5.2 Pengujian Validasi Password Salah", get_p("GAMBAR_5_2", "65"))
        ]
        for fig_title, fig_page in figure_items:
            add_toc_line(doc, fig_title, fig_page, is_bold=False, is_sub=False)

    # ==========================================
    # SECTION 3: BAB-BAB AKTIF DARI CONFIG (YAML)
    # ==========================================
    active_chapters = []
    for item in chapters_conf:
        if item.get('enabled', True):
            fname = item.get('file', f"0{item['id']}_BAB_{item.get('roman', 'I')}.md")
            ch_cand = os.path.join("drafts", fname)
            if not os.path.exists(ch_cand):
                ch_cand = os.path.join(str(root_dir), "drafts", fname) if root_dir else ch_cand
            active_chapters.append((ch_cand, len(active_chapters) == 0))

    if not active_chapters:
        active_chapters = [
            ("drafts/01_BAB_I.md", True),
            ("drafts/02_BAB_II.md", False),
            ("drafts/03_BAB_III.md", False),
            ("drafts/04_BAB_IV.md", False),
            ("drafts/05_BAB_V.md", False),
            ("drafts/06_BAB_VI.md", False)
        ]

    for ch_path, is_first in active_chapters:
        if os.path.exists(ch_path):
            add_chapter_to_doc(doc, ch_path, is_first_chapter=is_first)

    # ==========================================
    # SECTION 4: DAFTAR PUSTAKA (Harvard Style)
    # ==========================================
    ref_file = "drafts/07_DAFTAR_PUSTAKA.md"
    if os.path.exists(ref_file):
        sec_dp = doc.add_section(WD_SECTION.NEW_PAGE)
        apply_section_geometry(sec_dp, doc_conf=doc_conf)
        sec_dp.header.is_linked_to_previous = False
        sec_dp.footer.is_linked_to_previous = False
        sec_dp.different_first_page_header_footer = True
        pg_dp = parse_xml(r'<w:pgNumType %s w:fmt="decimal"/>' % nsdecls('w'))
        sec_dp._sectPr.append(pg_dp)

        p_dp_f = sec_dp.first_page_footer.paragraphs[0]
        create_clean_page_field(p_dp_f, alignment=WD_ALIGN_PARAGRAPH.CENTER)
        sec_dp.first_page_header.paragraphs[0].text = ""

        p_dp_h = sec_dp.header.paragraphs[0]
        create_clean_page_field(p_dp_h, alignment=WD_ALIGN_PARAGRAPH.RIGHT)
        sec_dp.footer.paragraphs[0].text = ""

        doc.add_paragraph("DAFTAR PUSTAKA", style='Heading 1')

        with open(ref_file, 'r', encoding='utf-8') as f:
            ref_lines = f.readlines()
        for rline in ref_lines:
            rline = rline.strip()
            if not rline or rline.startswith('#') or rline.startswith('<!--'):
                continue
            p_ref = doc.add_paragraph()
            p_ref.paragraph_format.line_spacing = 1.0
            p_ref.paragraph_format.space_after = Pt(6)  # Spasi 1.5 antar-entri pustaka
            p_ref.paragraph_format.left_indent = Cm(1.25)
            p_ref.paragraph_format.first_line_indent = Cm(-1.25)
            p_ref.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_formatted_runs(p_ref, rline)

    # ==========================================
    # SECTION 5: DAFTAR RIWAYAT HIDUP
    # ==========================================
    rh_file = "drafts/08_DAFTAR_RIWAYAT_HIDUP.md"
    if os.path.exists(rh_file):
        sec_rh = doc.add_section(WD_SECTION.NEW_PAGE)
        apply_section_geometry(sec_rh, doc_conf=doc_conf)
        sec_rh.header.is_linked_to_previous = False
        sec_rh.footer.is_linked_to_previous = False
        sec_rh.different_first_page_header_footer = True
        pg_rh = parse_xml(r'<w:pgNumType %s w:fmt="decimal"/>' % nsdecls('w'))
        sec_rh._sectPr.append(pg_rh)

        p_rh_f = sec_rh.first_page_footer.paragraphs[0]
        create_clean_page_field(p_rh_f, alignment=WD_ALIGN_PARAGRAPH.CENTER)
        sec_rh.first_page_header.paragraphs[0].text = ""

        p_rh_h = sec_rh.header.paragraphs[0]
        create_clean_page_field(p_rh_h, alignment=WD_ALIGN_PARAGRAPH.RIGHT)
        sec_rh.footer.paragraphs[0].text = ""

        parse_and_add_content(doc, rh_file)

    # Aktifkan w:updateFields agar Word otomatis merefresh TOC saat dibuka
    try:
        settings = doc.settings.element
        update = parse_xml(r'<w:updateFields %s w:val="true"/>' % nsdecls('w'))
        settings.append(update)
    except Exception:
        pass

    os.makedirs(os.path.dirname(output_docx_path), exist_ok=True)
    doc.save(output_docx_path)
    print(f"[+] Kompilasi DOCX berhasil: {output_docx_path}")

    # Salin juga ke workspace/builds/skripsi_draft.docx
    workspace_build = os.path.abspath("workspace/builds/skripsi_draft.docx")
    try:
        os.makedirs(os.path.dirname(workspace_build), exist_ok=True)
        shutil.copy2(output_docx_path, workspace_build)
        print(f"[+] Salinan naskah tersimpan di workspace: {workspace_build}")
    except Exception:
        pass

    return os.path.exists(output_docx_path)


def convert_latex_equations_in_doc(docx_path):
    """
    Mengonversi seluruh placeholder [EQ_LATEX] di dalam dokumen Word menjadi
    persamaan matematika native Office Math (OMML) menggunakan Microsoft Word COM.
    Menghapus tepat 11 karakter '[EQ_LATEX] ' tanpa merusak tanda akhir paragraf.
    """
    docx_abs = os.path.abspath(docx_path)
    print(f"[*] Mengonversi placeholder rumus LaTeX ke Office Math native: {docx_abs}...")
    word = win32com.client.DispatchEx('Word.Application')
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        doc = word.Documents.Open(docx_abs)
        count = 0
        for p in doc.Paragraphs:
            t = p.Range.Text.strip()
            if t.startswith('[EQ_LATEX]'):
                doc.Range(p.Range.Start, p.Range.Start + 11).Delete()
                p.Range.OMaths.Add(p.Range)
                p.Range.OMaths.BuildUp()
                p.Alignment = 1 # Center
                count += 1
        doc.Save()
        doc.Close(False)
        print(f"[+] Berhasil mengonversi {count} persamaan matematika ke format Office Math native!")
        return count
    except Exception as e:
        print(f"[-] Terjadi kesalahan konversi persamaan: {e}")
        return 0
    finally:
        word.Quit()


def convert_docx_to_pdf(docx_path, pdf_path):
    """Mengonversi dokumen Word (.docx) ke PDF secara presisi menggunakan Microsoft Word (win32com)."""
    docx_abs = os.path.abspath(docx_path)
    pdf_abs = os.path.abspath(pdf_path)
    os.makedirs(os.path.dirname(pdf_abs), exist_ok=True)

    print(f"[*] Mengonversi {docx_abs} ke PDF via MS Word...")
    word = win32com.client.DispatchEx('Word.Application')
    word.Visible = False
    try:
        doc = word.Documents.Open(docx_abs)
        doc.SaveAs(pdf_abs, FileFormat=17) # 17 = wdFormatPDF
        doc.Close(False)
        print(f"[+] Konversi PDF berhasil! Berkas: {pdf_abs}")
        return True
    except Exception as e:
        print(f"[-] Terjadi kesalahan saat konversi PDF: {e}")
        return False
    finally:
        word.Quit()


def fitz_to_roman(num):
    """Mengonversi nomor integer menjadi Romawi kecil baku."""
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def scan_pdf_page_numbers(pdf_path):
    """
    Memindai naskah PDF secara otomatis untuk menentukan posisi halaman fisik dan halaman Arab
    dari setiap Bab, Subbab, Tabel, dan Gambar.
    """
    if not os.path.exists(pdf_path):
        return {}

    doc = fitz.open(pdf_path)
    print(f"[*] Memindai {pdf_path} (Total Halaman: {len(doc)})...")

    # Temukan halaman fisik tempat BAB I dimulai (halaman Arab 1)
    bab1_phys = None
    for p_no in range(len(doc)):
        txt = doc[p_no].get_text()
        if "DAFTAR ISI" in txt or "DAFTAR TABEL" in txt or "DAFTAR GAMBAR" in txt or "ABSTRAK" in txt:
            continue
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        if any(l == "BAB I" for l in lines) and any("PENDAHULUAN" in l for l in lines):
            bab1_phys = p_no
            break

    if bab1_phys is None:
        bab1_phys = 11 # Default fallback

    print(f"[+] BAB I ditemukan pada halaman fisik PDF: {bab1_phys + 1} (Arab 1)")

    def to_arab(phys_idx):
        return str(phys_idx - bab1_phys + 1)

    def find_page(term, start_idx=0, is_chapter=False):
        for idx in range(start_idx, len(doc)):
            txt = doc[idx].get_text()
            if "DAFTAR ISI" in txt or "DAFTAR TABEL" in txt or "DAFTAR GAMBAR" in txt:
                continue
            lines = [l.strip() for l in txt.split('\n') if l.strip()]
            for l in lines:
                if "...." in l or ". . ." in l:
                    continue
                if is_chapter:
                    if l == term:
                        return idx
                else:
                    if term.lower() in l.lower():
                        return idx
        return None

    pm = {}
    pm["HALAMAN_JUDUL"] = "i"
    pm["HALAMAN_PERSETUJUAN"] = "ii"
    pm["HALAMAN_PENGESAHAN"] = "iii"
    pm["HALAMAN_PERNYATAAN"] = "iv"
    pm["KATA_PENGANTAR"] = "v"

    # Cari posisi prelims
    for idx in range(4, bab1_phys):
        txt = doc[idx].get_text()
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        first_line = lines[0] if lines else ''
        sec_line = lines[1] if len(lines) > 1 else ''

        if first_line == "ABSTRAK" or sec_line == "ABSTRAK":
            pm["ABSTRAK"] = fitz_to_roman(idx)
        elif first_line == "ABSTRACT" or sec_line == "ABSTRACT":
            pm["ABSTRACT"] = fitz_to_roman(idx)
        elif "DAFTAR ISI" in first_line or "DAFTAR ISI" in sec_line:
            pm["DAFTAR_ISI"] = fitz_to_roman(idx)
        elif "DAFTAR TABEL" in first_line or "DAFTAR TABEL" in sec_line:
            pm["DAFTAR_TABEL"] = fitz_to_roman(idx)
        elif "DAFTAR GAMBAR" in first_line or "DAFTAR GAMBAR" in sec_line:
            pm["DAFTAR_GAMBAR"] = fitz_to_roman(idx)

    # Fallback romawi jika scanner perlu defaults
    if "ABSTRAK" not in pm: pm["ABSTRAK"] = "vii"
    if "ABSTRACT" not in pm: pm["ABSTRACT"] = "viii"
    if "DAFTAR_ISI" not in pm: pm["DAFTAR_ISI"] = "ix"
    if "DAFTAR_TABEL" not in pm: pm["DAFTAR_TABEL"] = "x"
    if "DAFTAR_GAMBAR" not in pm: pm["DAFTAR_GAMBAR"] = "xi"

    # Bab & Subbab target dinamis
    dyn_heads, _, _ = extract_structure_from_drafts()
    if dyn_heads:
        targets = []
        for h_title, is_b, is_s in dyn_heads:
            m_k = re.match(r'^(\d+\.\d+|\bBAB\s+[IVXLCDM]+\b)', h_title)
            k = m_k.group(1).replace(' ', '_') if m_k else h_title[:10]
            is_chap = is_b and ("BAB" in h_title.upper())
            targets.append((k, h_title, is_chap))
        targets.append(("DAFTAR_PUSTAKA", "DAFTAR PUSTAKA", True))
        targets.append(("DAFTAR_RIWAYAT_HIDUP", "DAFTAR RIWAYAT HIDUP", True))
    else:
        targets = [
            ("BAB_I", "BAB I", True),
            ("1.1", "1.1 Latar Belakang Masalah", False),
            ("1.2", "1.2 Rumusan Masalah", False),
            ("1.3", "1.3 Batasan Masalah", False),
            ("1.4", "1.4 Tujuan Penelitian", False),
            ("1.5", "1.5 Manfaat Penelitian", False),
            ("1.6", "1.6 Metodologi Penelitian", False),
            ("1.7", "1.7 Sistematika Penulisan", False),
            ("BAB_II", "BAB II", True),
            ("2.1", "2.1 Konsep Sistem dan Objek Penelitian", False),
            ("2.2", "2.2 Metode Komputasi", False),
            ("2.3", "2.3 Konsep Pemodelan Sistem", False),
            ("2.4", "2.4 Perangkat Lunak dan Basis Data", False),
            ("2.5", "2.5 Penelitian Terkait", False),
            ("BAB_III", "BAB III", True),
            ("3.1", "3.1 Analisa Sistem", False),
            ("3.2", "3.2 Penentuan Kriteria", False),
            ("3.3", "3.3 Perancangan Sistem", False),
            ("3.4", "3.4 Perancangan Basis Data", False),
            ("3.5", "3.5 Perancangan Tampilan", False),
            ("BAB_IV", "BAB IV", True),
            ("4.1", "4.1 Batasan dan Lingkungan", False),
            ("4.2", "4.2 Implementasi Modul Komputasi", False),
            ("4.3", "4.3 Implementasi Antarmuka", False),
            ("BAB_V", "BAB V", True),
            ("5.1", "5.1 Pengujian Model", False),
            ("5.2", "5.2 Pengujian Fungsional Sistem", False),
            ("5.3", "5.3 Pembahasan Hasil", False),
            ("BAB_VI", "BAB VI", True),
            ("6.1", "6.1 Kesimpulan", False),
            ("6.2", "6.2 Saran", False),
            ("DAFTAR_PUSTAKA", "DAFTAR PUSTAKA", True),
            ("DAFTAR_RIWAYAT_HIDUP", "DAFTAR RIWAYAT HIDUP", True)
        ]

    curr_p = bab1_phys
    for key, term, is_chap in targets:
        f_idx = find_page(term, start_idx=curr_p, is_chapter=is_chap)
        if f_idx is not None:
            pm[key] = to_arab(f_idx)
            curr_p = f_idx

    return pm


def build_perfect_thesis_pipeline(output_docx_path=None, output_pdf_path=None):
    """
    Pipeline Kompilasi 2-Pass Sempurna:
    Pass 1: Menghasilkan naskah draft, mengonversi rumus OMML, dan membuat PDF awal.
    Scan: Memindai halaman aktual dari PDF untuk seluruh Bab, Subbab, Tabel, dan Gambar.
    Pass 2: Mengompilasi ulang naskah dengan DAFTAR ISI, TABEL, dan GAMBAR berhalaman presisi 100%.
    """
    if output_docx_path is None:
        output_docx_path = os.path.abspath("AI_program/working/skripsi_compiled_preview.docx")
    if output_pdf_path is None:
        output_pdf_path = output_docx_path.replace(".docx", ".pdf")

    print("\n" + "="*70)
    print(">>> PIPELINE KOMPILASI SKRIPSI 2-PASS ALMUSLIM DIMULAI <<<")
    print("="*70)

    # --- PASS 1: Build Draft Awal ---
    print("\n--- [PASS 1] MEMBANGUN NASKAH AWAL ---")
    build_full_thesis(output_docx_path, page_map=None)
    convert_latex_equations_in_doc(output_docx_path)
    convert_docx_to_pdf(output_docx_path, output_pdf_path)

    # --- SCANNING: Pindai Nomor Halaman PDF ---
    print("\n--- [SCAN] MEMINDAI NOMOR HALAMAN PRESISI DARI PDF ---")
    page_map = scan_pdf_page_numbers(output_pdf_path)
    print(f"[+] Halaman BAB I: {page_map.get('BAB_I', '1')}")
    print(f"[+] Halaman BAB II: {page_map.get('BAB_II', '8')}")
    print(f"[+] Halaman BAB III: {page_map.get('BAB_III', '24')}")
    print(f"[+] Halaman DAFTAR PUSTAKA: {page_map.get('DAFTAR_PUSTAKA', '74')}")

    # --- PASS 2: Build Final Presisi 100% ---
    print("\n--- [PASS 2] MEMBANGUN NASKAH FINAL DENGAN TOC PRESISI ---")
    build_full_thesis(output_docx_path, page_map=page_map)
    convert_latex_equations_in_doc(output_docx_path)
    convert_docx_to_pdf(output_docx_path, output_pdf_path)

    # --- Salin Otomatis ke Workspace Builds Staging ---
    workspace_build_dir = os.path.abspath("workspace/builds")
    os.makedirs(workspace_build_dir, exist_ok=True)
    staging_docx = os.path.join(workspace_build_dir, "skripsi_draft.docx")
    staging_pdf = os.path.join(workspace_build_dir, "skripsi_draft.pdf")
    try:
        shutil.copy2(output_docx_path, staging_docx)
        if os.path.exists(output_pdf_path):
            shutil.copy2(output_pdf_path, staging_pdf)
        print(f"[+] Berkas build disinkronkan ke direktori workspace:")
        print(f"    - DOCX: {staging_docx}")
        print(f"    - PDF : {staging_pdf}")
    except Exception as e:
        print(f"[-] Catatan penyalinan ke workspace/builds: {e}")

    print("\n" + "="*70)
    print(f"[SUCCESS] NASKAH SKRIPSI FINAL BERHASIL DIKOMPILASI!")
    print(f"DOCX: {output_docx_path}")
    print(f"PDF : {output_pdf_path}")
    print("="*70 + "\n")
    return True


if __name__ == "__main__":
    out_file = os.path.abspath("AI_program/working/skripsi_compiled_preview.docx")
    build_perfect_thesis_pipeline(out_file)
