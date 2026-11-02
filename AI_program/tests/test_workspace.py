"""
UNIT TEST SUITE - WORKSPACE SKRIPSI INFORMATIKA ENGINE
Memvalidasi fungsionalitas seluruh modul Python inti sebelum digunakan dalam penulisan naskah.
Menggunakan library bawaan Python (unittest) tanpa dependensi eksternal.
"""

import os
import sys
import unittest
import docx

# Daftarkan scripts ke sys.path
sys.path.insert(0, os.path.abspath("AI_program/scripts"))

class TestWorkspaceEngine(unittest.TestCase):

    def test_template_exists_and_valid(self):
        """Memastikan master template Word ada dan memiliki konfigurasi baku."""
        template_path = os.path.abspath("AI_program/working/template_skripsi_almuslim.docx")
        self.assertTrue(os.path.exists(template_path), "Template Word master tidak ditemukan!")
        doc = docx.Document(template_path)
        self.assertGreaterEqual(len(doc.sections), 5, "Jumlah section Word kurang dari 5!")
        
        # Periksa margin A4 (4-4-3-3 cm) pada section pertama
        sec0 = doc.sections[0]
        self.assertEqual(round(sec0.top_margin.cm, 1), 4.0)
        self.assertEqual(round(sec0.left_margin.cm, 1), 4.0)
        self.assertEqual(round(sec0.right_margin.cm, 1), 3.0)
        self.assertEqual(round(sec0.bottom_margin.cm, 1), 3.0)

    def test_draft_files_exist(self):
        """Memastikan seluruh berkas draf BAB I s.d. BAB VI tersedia di drafts/."""
        expected_files = [
            "drafts/00_BAGIAN_AWAL.md",
            "drafts/01_BAB_I.md",
            "drafts/02_BAB_II.md",
            "drafts/03_BAB_III.md",
            "drafts/04_BAB_IV.md",
            "drafts/05_BAB_V.md",
            "drafts/06_BAB_VI.md",
            "drafts/07_DAFTAR_PUSTAKA.md",
            "drafts/08_DAFTAR_RIWAYAT_HIDUP.md"
        ]
        for ef in expected_files:
            self.assertTrue(os.path.exists(ef), f"Berkas draf {ef} tidak ditemukan!")

    def test_table_styler_module(self):
        """Menguji pembuatan tabel tiga garis akademik Almuslim."""
        from table_styler import style_academic_table
        doc = docx.Document()
        tbl = doc.add_table(rows=3, cols=4)
        style_academic_table(tbl)
        self.assertEqual(len(tbl.rows), 3)
        self.assertEqual(len(tbl.columns), 4)

    def test_compiler_output_preview(self):
        """Menguji kompilasi draf menjadi file Word preview."""
        from build_skripsi import build_full_thesis
        preview_path = os.path.abspath("AI_program/temp/test_preview.docx")
        success = build_full_thesis(preview_path)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(preview_path))
        doc = docx.Document(preview_path)
        self.assertGreater(len(doc.paragraphs), 50)

    def test_qa_audit_runs_cleanly(self):
        """Menguji script QA audit berjalan tanpa exception."""
        from qa_audit import calculate_word_and_page_count, check_placeholders
        import glob
        drafts = sorted(glob.glob("drafts/*.md"))
        words, pages, breakdown = calculate_word_and_page_count(drafts)
        self.assertGreater(words, 0)
        self.assertGreater(pages, 0)
        placeholders = check_placeholders(drafts)
        self.assertIsInstance(placeholders, list)

if __name__ == "__main__":
    unittest.main()

