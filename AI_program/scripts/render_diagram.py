"""
RENDER DIAGRAM MODULE - DIAGRAM-AS-CODE RESILIENT RENDERER
SOP: SOP_DIAGRAM.md (Monokrom Standar Almuslim)
Dukungan: Mermaid.js (.mmd) -> PNG 300 DPI / SVG
Engine: Headless Edge (Playwright) dengan fallback ke Mermaid.ink API
"""

import os
import sys
import base64
import json
import requests
from pathlib import Path

# Tema Monokrom Baku Almuslim (SOP_DIAGRAM.md)
MONOCHROME_CONFIG = {
    "theme": "base",
    "themeVariables": {
        "primaryColor": "#ffffff",
        "primaryTextColor": "#000000",
        "primaryBorderColor": "#000000",
        "lineColor": "#000000",
        "secondaryColor": "#ffffff",
        "tertiaryColor": "#ffffff",
        "fontFamily": "Times New Roman, serif",
        "fontSize": "13px"
    }
}

def render_with_playwright(mmd_content, output_png_path, scale=3):
    """Me-render diagram Mermaid menggunakan headless Edge lokal via Playwright."""
    from playwright.sync_api import sync_playwright

    escaped_mmd = mmd_content.replace("\\", "\\\\").replace("`", "\\`")
    config_json = json.dumps(MONOCHROME_CONFIG)

    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        body {{
            margin: 10px;
            padding: 10px;
            background: #ffffff;
            font-family: 'Times New Roman', serif;
        }}
        #diagram {{
            display: inline-block;
            background: #ffffff;
        }}
    </style>
</head>
<body>
    <div id="diagram" class="mermaid">
{mmd_content}
    </div>
    <script>
        mermaid.initialize({config_json});
    </script>
</body>
</html>"""

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        # scale=3 menghasilkan ~300 DPI untuk cetak Word A4
        page = browser.new_page(device_scale_factor=scale)
        page.set_content(html_template, wait_until="networkidle")
        element = page.wait_for_selector("#diagram svg", timeout=10000)
        os.makedirs(os.path.dirname(output_png_path), exist_ok=True)
        element.screenshot(path=output_png_path)
        browser.close()

    return os.path.exists(output_png_path)

def render_with_mermaid_ink(mmd_content, output_png_path):
    """Fallback: Me-render menggunakan mermaid.ink REST API jika browser offline."""
    graph_bytes = mmd_content.encode('utf-8')
    base64_str = base64.urlsafe_b64encode(graph_bytes).decode('ascii')
    url = f"https://mermaid.ink/img/{base64_str}?bgColor=ffffff"
    
    resp = requests.get(url, timeout=15)
    if resp.status_code == 200:
        os.makedirs(os.path.dirname(output_png_path), exist_ok=True)
        with open(output_png_path, "wb") as f:
            f.write(resp.content)
        return True
    return False

def render_mermaid(mmd_source, output_png_path):
    """
    Fungsi utama merender Mermaid:
    - mmd_source: bisa berupa path file .mmd atau string kode Mermaid
    - output_png_path: path berkas target PNG
    """
    if os.path.isfile(mmd_source):
        with open(mmd_source, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = mmd_source

    print(f"[*] Merender diagram ke: {output_png_path}...")
    try:
        success = render_with_playwright(content, output_png_path)
        if success:
            print(f"[+] Berhasil merender via Playwright Edge (300 DPI).")
            return True
    except Exception as e:
        print(f"[-] Playwright gagal ({e}), beralih ke mermaid.ink fallback...")

    try:
        success = render_with_mermaid_ink(content, output_png_path)
        if success:
            print(f"[+] Berhasil merender via mermaid.ink.")
            return True
    except Exception as e:
        print(f"[-] mermaid.ink fallback gagal: {e}")

    return False

if __name__ == "__main__":
    test_code = """flowchart TD
    A(["Mulai"]) --> B[/"Input Data Kriteria & Bobot"/]
    B --> C["Normalisasi Matriks Keputusan"]
    C --> D{"Apakah Data Lengkap?"}
    D -- "Tidak" --> E["Tampilkan Notifikasi Error"]
    E --> B
    D -- "Ya" --> F["Hitung Vektor Preferensi (Metode WP)"]
    F --> G["Perangkingan Nilai Alternatif"]
    G --> H(["Selesai"])"""

    target = os.path.abspath("ASSETS/DIAGRAM/contoh_flowchart_wp.png")
    ok = render_mermaid(test_code, target)
    if ok:
        print(f"Ukuran file: {os.path.getsize(target)} bytes")
