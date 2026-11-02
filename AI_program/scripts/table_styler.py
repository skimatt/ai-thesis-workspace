"""
TABLE STYLER MODULE - FORMAT TABEL AKADEMIK RESMI ALMUSLIM
SOP: SOP_FORMAT (AI_AGENTS_SOP_PEDOMAN_SKRIPSI_ALMUSLIM.md)
Model: Open Table / Tabel Tiga Garis (Atas, Bawah Kepala, dan Penutup Bawah).
Tanpa garis vertikal. Font: Times New Roman 8.5 - 11 pt, Spasi 1.0.
"""

import re
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

def apply_tnr_rfonts(run):
    """Memastikan font Times New Roman terdaftar di rFonts OpenXML."""
    rPr = run._r.get_or_add_rPr()
    ex = rPr.find(qn('w:rFonts'))
    if ex is not None:
        rPr.remove(ex)
    rf = parse_xml(r'<w:rFonts %s w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>' % nsdecls('w'))
    rPr.append(rf)

def apply_open_table_borders(table):
    """
    Menerapkan format garis terbuka akademik (3 horizontal borders, no vertical borders).
    - Top horizontal: single, 4/8 pt (sz="6")
    - Bottom of table: single, 4/8 pt (sz="6")
    - Inside vertical: nil (tidak ada garis vertikal)
    - Outside vertical: nil
    """
    tblPr = table._tbl.tblPr
    existing_borders = tblPr.find(qn('w:tblBorders'))
    if existing_borders is not None:
        tblPr.remove(existing_borders)

    borders_xml = parse_xml(r'''
        <w:tblBorders %s>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>
            <w:left w:val="nil"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>
            <w:right w:val="nil"/>
            <w:insideH w:val="nil"/>
            <w:insideV w:val="nil"/>
        </w:tblBorders>
    ''' % nsdecls('w'))
    tblPr.append(borders_xml)

def apply_header_bottom_border(header_row):
    """Menambahkan garis horizontal di bawah baris kepala tabel."""
    for cell in header_row.cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(r'''
            <w:tcBorders %s>
                <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>
            </w:tcBorders>
        ''' % nsdecls('w'))
        tcPr.append(tcBorders)

def get_optimal_column_widths(table):
    """
    Menentukan lebar kolom optimal untuk tabel skripsi Almuslim
    berdasarkan struktur header atau jumlah kolomnya (lebar total kertas = 14.0 cm).
    """
    ncols = len(table.columns)
    if len(table.rows) == 0:
        return None

    header_cells = [c.text.strip().lower() for c in table.rows[0].cells]
    header_text = " ".join(header_cells)

    # 1. Tabel 2.1 Matriks Perbandingan Penelitian Terdahulu (8 kolom)
    if ncols == 8 or "peneliti" in header_text:
        return [Cm(0.8), Cm(2.2), Cm(2.0), Cm(1.8), Cm(1.8), Cm(1.6), Cm(1.9), Cm(2.0)] # Total 14.1 cm

    # 2. Tabel 3.1 Kebutuhan Fungsional (4 kolom)
    if ncols == 4 and "fungsional" in header_text:
        return [Cm(1.5), Cm(3.0), Cm(4.8), Cm(4.7)] # Total 14.0 cm

    # 3. Tabel 3.2 Kebutuhan Nonfungsional (3 kolom)
    if ncols == 3:
        return [Cm(1.5), Cm(3.5), Cm(9.0)] # Total 14.0 cm

    # 4. Tabel Kamus Data / Struktur Tabel Basis Data (5 kolom)
    if ncols == 5 and ("nama kolom" in header_text or "tipe data" in header_text):
        return [Cm(3.2), Cm(2.3), Cm(1.5), Cm(2.2), Cm(4.8)] # Total 14.0 cm

    # 5. Tabel 3.9 Skenario Black Box Testing (5 kolom)
    if ncols == 5 and ("skenario" in header_text or "kasus uji" in header_text or "fitur" in header_text):
        return [Cm(0.8), Cm(2.6), Cm(3.2), Cm(3.7), Cm(3.7)] # Total 14.0 cm

    # 6. Tabel 3.10 Kuesioner Baku SUS (7 kolom)
    if ncols == 7 or ("kuesioner" in header_text or "pernyataan" in header_text):
        return [Cm(0.8), Cm(8.2), Cm(1.0), Cm(1.0), Cm(1.0), Cm(1.0), Cm(1.0)] # Total 14.0 cm

    # Default pembagian rata jika tidak spesifik
    equal_w = Cm(round(14.0 / ncols, 2))
    return [equal_w] * ncols

def style_academic_table(table, col_widths=None, align_center=True):
    """
    Memformat tabel python-docx menjadi standar skripsi Almuslim:
    - Garis 3 horizontal monokrom tanpa garis vertikal.
    - Lebar kolom presisi sesuai peruntukan data.
    - Header: Bold, Center, 10-11 pt, spasi 1.0.
    - Data: Regular, 8.5-10 pt, spasi 1.0.
    - Padding sel presisi.
    - Pengulangan kepala tabel (tblHeader) dan anti-terbelah (cantSplit).
    """
    apply_open_table_borders(table)
    
    if len(table.rows) > 0:
        apply_header_bottom_border(table.rows[0])

    if align_center:
        table.alignment = WD_TABLE_ALIGNMENT.CENTER

    if col_widths is None:
        col_widths = get_optimal_column_widths(table)

    # Deteksi tabel 8 kolom untuk font ukuran 8.5 pt
    ncols = len(table.columns)
    base_font_pt = 8.5 if ncols == 8 else 10.0
    hdr_font_pt = 9.0 if ncols == 8 else 10.5

    for row_idx, row in enumerate(table.rows):
        is_header = (row_idx == 0)
        trPr = row._tr.get_or_add_trPr()
        if is_header:
            trPr.append(parse_xml(r'<w:tblHeader %s/>' % nsdecls('w')))
            trPr.append(parse_xml(r'<w:cantSplit %s/>' % nsdecls('w')))
        else:
            trPr.append(parse_xml(r'<w:cantSplit %s/>' % nsdecls('w')))

        for col_idx, cell in enumerate(row.cells):
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            # Terapkan lebar kolom presisi pada cell
            if col_widths and col_idx < len(col_widths):
                cell.width = col_widths[col_idx]

            # Atur padding sel (top/bottom 60 dxa ~ 3pt, left/right 100 dxa ~ 5pt)
            tcPr = cell._tc.get_or_add_tcPr()
            tcMar = parse_xml(r'''
                <w:tcMar %s>
                    <w:top w:w="60" w:type="dxa"/>
                    <w:bottom w:w="60" w:type="dxa"/>
                    <w:left w:w="100" w:type="dxa"/>
                    <w:right w:w="100" w:type="dxa"/>
                </w:tcMar>
            ''' % nsdecls('w'))
            tcPr.append(tcMar)

            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_before = Pt(1.5)
                p.paragraph_format.space_after = Pt(1.5)
                
                # Penataan perataan teks sel:
                if is_header:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    # Kolom nomor urut atau kode singkat rata tengah
                    if col_idx == 0:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    elif ncols == 7 and col_idx >= 2: # Kolom skala Likert STS, TS, N, S, SS
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    elif ncols == 5 and col_idx in [2, 3]: # Kolom panjang & kunci DB
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    else:
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT

                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(hdr_font_pt if is_header else base_font_pt)
                    r.font.color.rgb = RGBColor(0, 0, 0)
                    if is_header:
                        r.bold = True
                    apply_tnr_rfonts(r)

def add_table_caption(doc, full_caption_text):
    """
    Menambahkan judul/caption tabel di ATAS tabel rata kiri (SOP Almuslim).
    Format: 'Tabel X.X' dicetak Tebal (Bold), dilanjutkan dengan ' Judul Tabel' reguler.
    Contoh: 'Tabel 2.1  Matriks Perbandingan Penelitian Terdahulu'
    """
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Bersihkan jika ada awalan ###
    cleaned = full_caption_text.replace('###', '').strip()

    # Pisahkan nomor tabel dan judulnya: "Tabel 2.1" dan "Matriks..."
    m = re.match(r'^(Tabel\s+\d+\.\d+)\s+(.*)', cleaned)
    if m:
        num_str = m.group(1)
        title_str = m.group(2)
        r_num = p.add_run(f"{num_str}  ")
        r_num.font.name = 'Times New Roman'
        r_num.font.size = Pt(12)
        r_num.bold = True
        apply_tnr_rfonts(r_num)

        r_title = p.add_run(title_str)
        r_title.font.name = 'Times New Roman'
        r_title.font.size = Pt(12)
        apply_tnr_rfonts(r_title)
    else:
        r = p.add_run(cleaned)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.bold = True
        apply_tnr_rfonts(r)

    return p
