"""
RENDER ACADEMIC DIAGRAMS MODULE
Universitas Almuslim - Fakultas Ilmu Komputer - Program Studi Informatika
Acuan Baku: SOP_DIAGRAM.md v3.0 & ASSETS/DIAGRAM/STANDARD_EXAMPLES/

Menghasilkan diagram monokromatik beresolusi tinggi (300 DPI) siap cetak skripsi:
1. Use Case Diagram (Subsystem boundary, stick-figure actors, use case ovals)
2. ERD Notasi Peter Chen (Entitas kotak, Relasi diamond, Atribut elips bergaris bawah, Kardinalitas 1:N)
3. DFD Diagram Konteks / Level 0 (Lingkaran proses pusat, Entitas luar kapital, Panah berlabel)
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Konfigurasi tipografi baku monokrom skripsi
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'cm'


def draw_stick_figure(ax, x, y, scale=0.08, label="Aktor"):
    """Menggambar aktor stick figure monokrom akademik."""
    # Kepala (lingkaran)
    head_r = scale * 0.4
    circle = patches.Circle((x, y + scale * 1.4), head_r, fill=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(circle)
    # Badan (garis vertikal)
    ax.plot([x, x], [y + scale * 1.0, y + scale * 0.2], color='black', linewidth=1.5)
    # Lengan (garis horizontal miring)
    ax.plot([x - scale * 0.7, x + scale * 0.7], [y + scale * 0.7, y + scale * 0.7], color='black', linewidth=1.5)
    # Kaki kiri & kanan
    ax.plot([x, x - scale * 0.6], [y + scale * 0.2, y - scale * 0.7], color='black', linewidth=1.5)
    ax.plot([x, x + scale * 0.6], [y + scale * 0.2, y - scale * 0.7], color='black', linewidth=1.5)
    # Label nama aktor di bawah
    ax.text(x, y - scale * 1.1, label, ha='center', va='top', fontsize=10, fontweight='bold')


def render_use_case_diagram(output_path, system_title, actors_left, actors_right, use_cases, connections):
    """
    Merender Use Case Diagram persis standar Gambar 1 (01_contoh_use_case_diagram.png):
    - Subsystem Boundary Box persegi panjang dengan judul «subsystem» [system_title]
    - Aktor stick-figure di sisi kiri dan kanan
    - Use case berupa elips horizontal dengan teks terpusat
    - Garis asosiasi solid lurus
    """
    fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Kotak pembatas sistem (System boundary)
    box_left = 3.0
    box_width = 4.2
    box_bottom = 0.5
    box_height = 7.0
    rect = patches.Rectangle((box_left, box_bottom), box_width, box_height, fill=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)

    # Label Subsystem di pojok kiri atas boundary
    ax.text(box_left + 0.15, box_bottom + box_height - 0.25, f"«subsystem»\n{system_title}", 
            ha='left', va='top', fontsize=11, fontweight='bold')

    # Posisi elips Use Case di dalam boundary
    n_uc = len(use_cases)
    uc_positions = {}
    y_step = (box_height - 1.5) / max(1, n_uc)
    start_y = box_bottom + box_height - 1.5

    for i, uc_text in enumerate(use_cases):
        cy = start_y - i * y_step
        cx = box_left + box_width / 2.0
        uc_positions[uc_text] = (cx, cy)
        # Gambar Elips horizontal
        el = patches.Ellipse((cx, cy), width=2.8, height=0.75, fill=True, facecolor='white', edgecolor='black', linewidth=1.5, zorder=3)
        ax.add_patch(el)
        ax.text(cx, cy, uc_text, ha='center', va='center', fontsize=9.5, zorder=4)

    # Aktor Kiri
    actor_positions = {}
    n_al = len(actors_left)
    y_step_al = 6.0 / max(1, n_al)
    for i, act_name in enumerate(actors_left):
        ay = 6.0 - i * y_step_al
        ax_pos = 1.2
        draw_stick_figure(ax, ax_pos, ay, scale=0.45, label=act_name)
        actor_positions[act_name] = (ax_pos + 0.35, ay + 0.3)

    # Aktor Kanan
    n_ar = len(actors_right)
    if n_ar > 0:
        y_step_ar = 6.0 / max(1, n_ar)
        for i, act_name in enumerate(actors_right):
            ay = 6.0 - i * y_step_ar
            ax_pos = 8.8
            draw_stick_figure(ax, ax_pos, ay, scale=0.45, label=act_name)
            actor_positions[act_name] = (ax_pos - 0.35, ay + 0.3)

    # Garis Asosiasi Lurus
    for act_name, uc_text in connections:
        if act_name in actor_positions and uc_text in uc_positions:
            x1, y1 = actor_positions[act_name]
            cx, cy = uc_positions[uc_text]
            # Hubungkan ke tepi kiri atau kanan elips
            edge_x = cx - 1.4 if x1 < cx else cx + 1.4
            ax.plot([x1, edge_x], [y1, cy], color='black', linewidth=1.2, zorder=2)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.close()
    print(f"[+] Use Case Diagram tersimpan: {output_path}")
    return os.path.exists(output_path)


def render_chen_erd(output_path, entities, relationships, attributes):
    """
    Merender ERD Notasi Peter Chen persis standar Gambar 2 & 3:
    - Entitas: Persegi panjang garis hitam
    - Relasi: Belah ketupat (Diamond)
    - Atribut: Elips dengan Primary Key bertanda bintang / garis bawah
    - Kardinalitas: Angka 1 dan N / M pada garis
    """
    fig, ax = plt.subplots(figsize=(10, 7.5), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Gambar Entitas (Kotak Persegi Panjang)
    ent_coords = {}
    for ent_name, (cx, cy) in entities.items():
        w, h = 2.0, 0.75
        rect = patches.Rectangle((cx - w/2, cy - h/2), w, h, fill=True, facecolor='white', edgecolor='black', linewidth=1.5, zorder=3)
        ax.add_patch(rect)
        ax.text(cx, cy, ent_name, ha='center', va='center', fontsize=10.5, fontweight='bold', zorder=4)
        ent_coords[ent_name] = (cx, cy)

    # Gambar Relasi (Belah Ketupat / Diamond)
    rel_coords = {}
    for rel_name, (cx, cy), ent1, ent2, card1, card2 in relationships:
        dw, dh = 1.4, 0.9
        diamond = patches.Polygon([[cx, cy + dh/2], [cx + dw/2, cy], [cx, cy - dh/2], [cx - dw/2, cy]],
                                  fill=True, facecolor='white', edgecolor='black', linewidth=1.5, zorder=3)
        ax.add_patch(diamond)
        ax.text(cx, cy, rel_name, ha='center', va='center', fontsize=9, zorder=4)
        rel_coords[rel_name] = (cx, cy)

        # Garis hubung ke ent1 dan kardinalitas
        x1, y1 = ent_coords[ent1]
        ax.plot([cx, x1], [cy, y1], color='black', linewidth=1.2, zorder=2)
        mid_x1 = (cx + x1) / 2.0
        mid_y1 = (cy + y1) / 2.0
        ax.text(mid_x1, mid_y1 + 0.15, str(card1), fontsize=9.5, fontweight='bold')

        # Garis hubung ke ent2 dan kardinalitas
        x2, y2 = ent_coords[ent2]
        ax.plot([cx, x2], [cy, y2], color='black', linewidth=1.2, zorder=2)
        mid_x2 = (cx + x2) / 2.0
        mid_y2 = (cy + y2) / 2.0
        ax.text(mid_x2, mid_y2 + 0.15, str(card2), fontsize=9.5, fontweight='bold')

    # Gambar Atribut (Elips)
    for ent_name, attr_list in attributes.items():
        ex, ey = ent_coords[ent_name]
        for attr_name, (ax_x, ax_y), is_pk in attr_list:
            # Hubungkan garis ke entitas
            ax.plot([ex, ax_x], [ey, ax_y], color='black', linewidth=1.0, zorder=1)
            # Elips atribut
            el = patches.Ellipse((ax_x, ax_y), width=1.6, height=0.6, fill=True, facecolor='white', edgecolor='black', linewidth=1.2, zorder=3)
            ax.add_patch(el)
            txt_weight = 'bold' if is_pk else 'normal'
            txt_disp = f"*{attr_name}" if is_pk else attr_name
            ax.text(ax_x, ax_y, txt_disp, ha='center', va='center', fontsize=8.5, fontweight=txt_weight, zorder=4)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.close()
    print(f"[+] Chen ERD Diagram tersimpan: {output_path}")
    return os.path.exists(output_path)


def render_dfd_context(output_path, system_title, entities_data):
    """
    Merender DFD Diagram Konteks (Level 0) persis standar Gambar 4 (04_contoh_dfd_level_0_konteks.png):
    - Lingkaran proses tunggal di tengah
    - Entitas eksternal (kotak persegi panjang)
    - Garis panah berarah dengan label dokumen/informasi terperinci
    """
    fig, ax = plt.subplots(figsize=(9.5, 7.5), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Lingkaran proses pusat
    pc_x, pc_y, pc_r = 6.0, 4.5, 1.4
    circle = patches.Circle((pc_x, pc_y), pc_r, fill=True, facecolor='white', edgecolor='black', linewidth=2.0, zorder=3)
    ax.add_patch(circle)
    ax.text(pc_x, pc_y, system_title, ha='center', va='center', fontsize=10.5, fontweight='bold', zorder=4)

    # Render Entitas dan Panah Aliran Data
    for ent_name, (ex, ey, ew, eh), flows in entities_data:
        # Kotak entitas eksternal
        rect = patches.Rectangle((ex - ew/2, ey - eh/2), ew, eh, fill=True, facecolor='white', edgecolor='black', linewidth=1.5, zorder=3)
        ax.add_patch(rect)
        ax.text(ex, ey, ent_name, ha='center', va='center', fontsize=10, fontweight='bold', zorder=4)

        # Garis panah aliran data (inbound & outbound)
        n_flows = len(flows)
        for i, (direction, label_text) in enumerate(flows):
            # Hitung offset vertikal agar panah-panah sejajar tidak bertumpuk
            offset = (i - (n_flows - 1) / 2.0) * 0.35
            if ex < pc_x:  # Entitas di sebelah kiri proses
                start_pt = (ex + ew/2, ey + offset)
                end_pt = (pc_x - pc_r * 0.9, pc_y + offset)
            elif ex > pc_x: # Entitas di sebelah kanan proses
                start_pt = (ex - ew/2, ey + offset)
                end_pt = (pc_x + pc_r * 0.9, pc_y + offset)
            else: # Entitas di atas proses
                start_pt = (ex + offset, ey - eh/2)
                end_pt = (pc_x + offset, pc_y + pc_r * 0.9)

            if direction == 'in':  # Dari entitas masuk ke proses
                p1, p2 = start_pt, end_pt
            else:                  # Dari proses keluar ke entitas
                p1, p2 = end_pt, start_pt

            # Gambar panah
            ax.annotate("", xy=p2, xytext=p1,
                        arrowprops=dict(arrowstyle="->", color="black", lw=1.2), zorder=2)
            # Label aliran teks
            mid_x = (p1[0] + p2[0]) / 2.0
            mid_y = (p1[1] + p2[1]) / 2.0 + 0.12
            ax.text(mid_x, mid_y, label_text, ha='center', va='bottom', fontsize=7.5, zorder=5)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.close()
    print(f"[+] DFD Diagram Konteks tersimpan: {output_path}")
    return os.path.exists(output_path)


if __name__ == "__main__":
    test_dir = os.path.abspath("ASSETS/DIAGRAM/GENERATED_TESTS")
    os.makedirs(test_dir, exist_ok=True)

    # 1. Test Generate Use Case
    render_use_case_diagram(
        os.path.join(test_dir, "test_use_case.png"),
        "Sistem ATM Bank",
        ["Nasabah", "Teknisi ATM"],
        ["Pihak Bank"],
        ["Cek Saldo", "Setor Tunai", "Tarik Tunai", "Transfer Dana", "Perawatan Sistem", "Perbaikan Teknis"],
        [("Nasabah", "Cek Saldo"), ("Nasabah", "Setor Tunai"), ("Nasabah", "Tarik Tunai"), ("Nasabah", "Transfer Dana"),
         ("Teknisi ATM", "Perawatan Sistem"), ("Teknisi ATM", "Perbaikan Teknis"),
         ("Pihak Bank", "Cek Saldo"), ("Pihak Bank", "Transfer Dana")]
    )

    # 2. Test Generate Chen ERD
    render_chen_erd(
        os.path.join(test_dir, "test_chen_erd.png"),
        entities={"mahasiswa": (3.0, 6.5), "dosen": (3.0, 2.5), "mata_kuliah": (9.0, 6.5), "ruang": (9.0, 2.5)},
        relationships=[
            ("membimbing", (3.0, 4.5), "dosen", "mahasiswa", "1", "N"),
            ("mengambil", (6.0, 6.5), "mahasiswa", "mata_kuliah", "M", "N"),
            ("mengajar", (6.0, 3.5), "dosen", "mata_kuliah", "1", "N"),
            ("digunakan", (9.0, 4.5), "ruang", "mata_kuliah", "1", "1")
        ],
        attributes={
            "mahasiswa": [("nim", (1.5, 7.5), True), ("nama_mhs", (3.0, 8.0), False), ("alamat", (1.5, 6.0), False)],
            "dosen": [("nip", (1.5, 1.5), True), ("nama_dosen", (3.0, 1.0), False)],
            "mata_kuliah": [("kode_mk", (9.0, 8.0), True), ("nama_mk", (10.5, 7.5), False)],
            "ruang": [("kode_ruang", (9.0, 1.0), True), ("kapasitas", (10.5, 1.5), False)]
        }
    )

    # 3. Test Generate DFD Konteks
    render_dfd_context(
        os.path.join(test_dir, "test_dfd_konteks.png"),
        "SI Penjualan\nMapleway Healthy\n& Snack",
        [
            ("MANAJER", (6.0, 8.5, 2.2, 0.9), [('in', 'Data Produk'), ('in', 'Data Admin')]),
            ("MARKETING", (1.8, 4.5, 2.2, 0.9), [('out', 'Info Konfirmasi'), ('in', 'Data Komentar')]),
            ("PEMBELI", (10.2, 4.5, 2.2, 0.9), [('in', 'Data Pembelian'), ('out', 'Validasi Pendaftaran')])
        ]
    )
