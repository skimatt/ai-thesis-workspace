"""
QA AUDIT MODULE - PRE-FLIGHT QUALITY GATE INSPECTOR (ENHANCED v2.0)
SOP: AGENTS.md (10 Aspek Quality Control)
Memeriksa:
1. Placeholder sisa ([NEEDS USER INPUT], [DATA REQUIRED], dll.)
2. Integritas Sitasi Harvard vs REFERENSI/index.md, bibliography.bib, & registry
3. Keberadaan fisik berkas gambar/diagram
4. Estimasi jumlah kata dan ketebalan halaman (Syarat minimal 80 halaman)
5. Kepatuhan Aturan Anti-Bullet (100% Alfanumerik Bertingkat)
6. Integritas Pustaka Fisik PDF & Format BibTeX / Registry
7. Validasi Konfigurasi Proyek YAML (config/thesis.yaml, chapters.yaml, document.yaml)
"""

import os
import re
import glob
import json
import yaml

def check_placeholders(draft_files):
    """Mendeteksi tag placeholder yang belum diselesaikan mahasiswa/agent."""
    placeholder_patterns = [
        r'\[NEEDS USER INPUT\]',
        r'\[DATA REQUIRED\]',
        r'\[SOURCE REQUIRED\]',
        r'\[RESULT REQUIRED\]',
        r'\[PERLU VERIFIKASI\]'
    ]
    findings = []
    for fpath in draft_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for l_num, line in enumerate(lines, start=1):
            for pat in placeholder_patterns:
                if re.search(pat, line):
                    findings.append({
                        "file": os.path.basename(fpath),
                        "line": l_num,
                        "tag": pat.replace('\\', ''),
                        "snippet": line.strip()[:80]
                    })
    return findings

def extract_citations(draft_files):
    """Mengekstraksi sitasi Harvard (Nama, Tahun) dari seluruh draf."""
    # Pola: (Nama, 20xx) atau (Nama1 dan Nama2, 20xx) atau (Nama et al., 20xx)
    pattern = r'\(([A-Z][a-zA-Z\s\.\,\-]+?),\s*([12][09][0-9]{2})\)'
    citations = set()
    for fpath in draft_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        matches = re.findall(pattern, content)
        for author, year in matches:
            if not author.startswith("Tabel") and not author.startswith("Gambar"):
                citations.add((author.strip(), year.strip()))
    return citations

def check_references_catalog(citations, catalog_path="REFERENSI/index.md", bib_path="REFERENSI/bibliography.bib", reg_path="REFERENSI/reference_registry.yaml"):
    """Mengecek apakah sitasi terdaftar di REFERENSI/index.md, bibliography.bib, atau reference_registry.yaml."""
    combined_content = ""
    if os.path.exists(catalog_path):
        with open(catalog_path, 'r', encoding='utf-8') as f:
            combined_content += f.read() + "\n"
    if os.path.exists(bib_path):
        with open(bib_path, 'r', encoding='utf-8') as f:
            combined_content += f.read() + "\n"
    if os.path.exists(reg_path):
        with open(reg_path, 'r', encoding='utf-8') as f:
            combined_content += f.read() + "\n"

    if not combined_content:
        return {"catalog_exists": False, "missing_citations": list(citations)}

    missing = []
    for author, year in citations:
        # Cari author dan year di gabungan katalog
        if author not in combined_content or year not in combined_content:
            missing.append(f"{author} ({year})")

    return {"catalog_exists": True, "missing_citations": missing}

def check_pdf_taxonomy(pdf_root="REFERENSI/pdf"):
    """Memeriksa taksonomi repositori PDF referensi."""
    if not os.path.exists(pdf_root):
        return {"exists": False, "categories": {}, "total_pdfs": 0}

    categories = ["belum_diverifikasi", "jurnal", "buku", "prosiding", "laporan_resmi", "skripsi_tesis"]
    cat_counts = {}
    total_pdfs = 0
    for cat in categories:
        cat_dir = os.path.join(pdf_root, cat)
        if os.path.exists(cat_dir):
            pdfs = [f for f in os.listdir(cat_dir) if f.lower().endswith(".pdf")]
            cat_counts[cat] = len(pdfs)
            total_pdfs += len(pdfs)
        else:
            cat_counts[cat] = 0

    return {"exists": True, "categories": cat_counts, "total_pdfs": total_pdfs}

def check_config_integrity(config_dir="config"):
    """Memeriksa keberadaan dan validitas file konfigurasi YAML."""
    expected_files = ["thesis.yaml", "document.yaml", "chapters.yaml"]
    results = {}
    all_valid = True
    for ef in expected_files:
        cpath = os.path.join(config_dir, ef)
        if not os.path.exists(cpath):
            results[ef] = "TIDAK DITEMUKAN"
            all_valid = False
        else:
            try:
                with open(cpath, 'r', encoding='utf-8') as f:
                    yaml.safe_load(f)
                results[ef] = "VALID"
            except Exception as e:
                results[ef] = f"ERROR YAML: {e}"
                all_valid = False
    return {"all_valid": all_valid, "details": results}

def check_image_assets(draft_files):
    """Memverifikasi bahwa semua path gambar di markdown benar-benar ada di disk (mengabaikan komentar HTML)."""
    missing_images = []
    img_pattern = r'!\[(.*?)\]\((.*?)\)'
    for fpath in draft_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Bersihkan blok komentar HTML <!-- ... -->
        clean_content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        matches = re.findall(img_pattern, clean_content)
        for caption, img_rel_path in matches:
            img_abs = os.path.abspath(img_rel_path)
            if not os.path.exists(img_abs):
                missing_images.append({
                    "file": os.path.basename(fpath),
                    "caption": caption,
                    "path": img_rel_path
                })
    return missing_images

def check_bullet_points(draft_files):
    """Mendeteksi pelanggaran aturan anti-bullet (simbol -, *, • di awal baris rincian)."""
    bullet_findings = []
    for fpath in draft_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for l_num, line in enumerate(lines, start=1):
            if re.match(r'^\s*[\-\*•]\s+', line):
                bullet_findings.append({
                    "file": os.path.basename(fpath),
                    "line": l_num,
                    "snippet": line.strip()[:80]
                })
    return bullet_findings

def calculate_word_and_page_count(draft_files):
    """Menghitung total kata dan perkiraan halaman (asumsi ~300 kata / halaman spasi 1.5 baku Almuslim)."""
    total_words = 0
    per_file = {}
    for fpath in draft_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            words = len(f.read().split())
        total_words += words
        per_file[os.path.basename(fpath)] = words

    est_pages = round(total_words / 300, 1)
    return total_words, est_pages, per_file

def run_qa_audit(save_report=True):
    """Menjalankan inspeksi Quality Assurance menyeluruh dan mengekspor laporan."""
    logs = []
    def log(msg=""):
        print(msg)
        logs.append(msg)

    log("=" * 70)
    log("AI AGENT MASTER QUALITY AUDIT (PRE-FLIGHT CHECK v2.0)")
    log("Universitas Almuslim - Fakultas Ilmu Komputer")
    log("=" * 70)

    draft_files = sorted(glob.glob("drafts/*.md"))
    if not draft_files:
        log("[-] Tidak ada berkas draf di folder drafts/")
        return False

    # 1. Cek Placeholder
    placeholders = check_placeholders(draft_files)
    log(f"\n[1] PENGUJIAN PLACEHOLDER:")
    if placeholders:
        log(f"    [!] Ditemukan {len(placeholders)} placeholder yang masih membutuhkan input:")
        for p in placeholders[:5]:
            log(f"        - {p['file']}:{p['line']} [{p['tag']}] {p['snippet']}")
        if len(placeholders) > 5:
            log(f"        ... dan {len(placeholders) - 5} placeholder lainnya.")
    else:
        log("    [+] Bersih! 0 placeholder ditemukan.")

    # 2. Cek Sitasi & Referensi
    citations = extract_citations(draft_files)
    log(f"\n[2] PENGUJIAN SITASI & REFERENSI:")
    log(f"    - Total sitasi terdeteksi di draf: {len(citations)}")
    ref_check = check_references_catalog(citations)
    if ref_check["missing_citations"]:
        log(f"    [!] Ditemukan {len(ref_check['missing_citations'])} sitasi yang belum tercatat di katalog referensi:")
        for mc in ref_check["missing_citations"]:
            log(f"        - {mc}")
    else:
        log("    [+] Seluruh sitasi valid dan terdaftar di katalog referensi.")

    # 3. Cek Gambar & Diagram
    missing_imgs = check_image_assets(draft_files)
    log(f"\n[3] PENGUJIAN ASSET GAMBAR/DIAGRAM:")
    if missing_imgs:
        log(f"    [!] Ditemukan {len(missing_imgs)} file gambar yang tidak ditemukan di disk:")
        for mi in missing_imgs:
            log(f"        - {mi['caption']} -> {mi['path']} (dari {mi['file']})")
    else:
        log("    [+] Seluruh file gambar/diagram terverifikasi ada secara fisik.")

    # 4. Cek Tebal Halaman
    words, pages, file_breakdown = calculate_word_and_page_count(draft_files)
    log(f"\n[4] ESTIMASI KETEBALAN NASKAH (TARGET MINIMAL: 80 HALAMAN):")
    log(f"    - Total Kata: {words:,} kata")
    log(f"    - Estimasi Halaman Word (spasi 1.5): ~{pages} halaman")
    log(f"    - Rincian per bab:")
    for fn, wc in file_breakdown.items():
        log(f"        * {fn:20s}: {wc:,} kata")

    # 5. Cek Aturan Anti-Bullet (Strict Anti-Bullet Rule)
    bullets = check_bullet_points(draft_files)
    log(f"\n[5] PENGUJIAN ATURAN ANTI-BULLET (STRICT ANTI-BULLET RULE):")
    if bullets:
        log(f"    [!] Ditemukan {len(bullets)} pelanggaran simbol bullet points (*, -, •):")
        for b in bullets[:5]:
            log(f"        - {b['file']}:{b['line']} -> {b['snippet']}")
        if len(bullets) > 5:
            log(f"        ... dan {len(bullets) - 5} pelanggaran bullet lainnya.")
    else:
        log("    [+] Bersih! 0 simbol bullet ditemukan (100% alfanumerik bertingkat).")

    # 6. Cek Taksonomi PDF Referensi & BibTeX
    pdf_info = check_pdf_taxonomy()
    log(f"\n[6] PENGUJIAN TAKSONOMI FOLDER PDF & BIBTEX:")
    if pdf_info["exists"]:
        log(f"    [+] Direktori REFERENSI/pdf/ terverifikasi ({pdf_info['total_pdfs']} berkas PDF fisik):")
        for cat, cnt in pdf_info["categories"].items():
            log(f"        * {cat:20s}: {cnt} berkas")
    else:
        log("    [-] Direktori REFERENSI/pdf/ tidak ditemukan.")

    bib_exists = os.path.exists("REFERENSI/bibliography.bib")
    reg_exists = os.path.exists("REFERENSI/reference_registry.yaml")
    log(f"    - bibliography.bib     : {'TERSEDIA' if bib_exists else 'BELUM ADA'}")
    log(f"    - reference_registry.yaml: {'TERSEDIA' if reg_exists else 'BELUM ADA'}")

    # 7. Cek Konfigurasi Proyek YAML
    conf_check = check_config_integrity()
    log(f"\n[7] PENGUJIAN KONFIGURASI PROYEK YAML (config/):")
    for fname, stat in conf_check["details"].items():
        icon = "[+]" if stat == "VALID" else "[-]"
        log(f"    {icon} {fname:20s}: {stat}")

    status = (
        len(placeholders) == 0 and
        len(ref_check["missing_citations"]) == 0 and
        len(missing_imgs) == 0 and
        pages >= 80 and
        len(bullets) == 0 and
        conf_check["all_valid"]
    )

    log("\n" + "=" * 70)
    if status:
        log("[PASSED] STATUS KELAYAKAN QUALITY GATE: LOLOS (SIAP RELEASE)")
    else:
        log("[REVIEW] STATUS: DALAM PENGEMBANGAN (MENUNGGU PENYELESAIAN INPUT / TARGET HALAMAN)")
    log("=" * 70)

    # Simpan laporan ke direktori workspace/reports/
    if save_report:
        os.makedirs("workspace/reports", exist_ok=True)
        txt_path = "workspace/reports/qa_audit_report.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(logs) + "\n")

        json_path = "workspace/reports/qa_audit_report.json"
        report_data = {
            "status": "PASSED" if status else "REVIEW",
            "placeholders_count": len(placeholders),
            "missing_citations_count": len(ref_check["missing_citations"]),
            "missing_images_count": len(missing_imgs),
            "total_words": words,
            "estimated_pages": pages,
            "bullet_violations_count": len(bullets),
            "pdf_taxonomy": pdf_info,
            "config_valid": conf_check["all_valid"],
            "config_details": conf_check["details"]
        }
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        print(f"\n[+] Laporan audit QA disimpan ke:")
        print(f"    - {os.path.abspath(txt_path)}")
        print(f"    - {os.path.abspath(json_path)}")

    return status

if __name__ == "__main__":
    run_qa_audit()
