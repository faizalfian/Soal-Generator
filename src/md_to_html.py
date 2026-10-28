import re
import html
import sys
import os
import textwrap

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script>
        // Prevent Flash of Unstyled Content (FOUC) by applying saved theme immediately
        (function() {{
            const savedTheme = localStorage.getItem('soal_theme') || 'light';
            document.documentElement.setAttribute('data-theme', savedTheme);
        }})();
    </script>
    <style>
        :root {{
            --bg-body: #f8fafc;
            --bg-card: #ffffff;
            --bg-subtle: #f1f5f9;
            --bg-table-head: #f8fafc;
            --bg-table-even: #fcfcfd;
            --text-main: #1e293b;
            --text-heading: #0f172a;
            --text-muted: #64748b;
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --primary-light: #eff6ff;
            --accent: #7c3aed;
            --accent-light: #f5f3ff;
            --border: #e2e8f0;
            --border-highlight: #cbd5e1;
            --code-bg: #0f172a;
            --code-text: #f1f5f9;
            --inline-code-bg: #f1f5f9;
            --inline-code-text: #0f172a;
            --warning-bg: #fffbeb;
            --warning-border: #f59e0b;
            --warning-text: #92400e;
            --decom-bg: #faf5ff;
            --decom-border: #c084fc;
            --decom-title: #6b21a8;
            --callout-bg: #f8fafc;
        }}

        [data-theme="dark"] {{
            --bg-body: #0b1120;
            --bg-card: #1e293b;
            --bg-subtle: #0f172a;
            --bg-table-head: #0f172a;
            --bg-table-even: #162032;
            --text-main: #e2e8f0;
            --text-heading: #f8fafc;
            --text-muted: #94a3b8;
            --primary: #3b82f6;
            --primary-hover: #2563eb;
            --primary-light: rgba(59, 130, 246, 0.15);
            --accent: #a78bfa;
            --accent-light: rgba(167, 139, 250, 0.15);
            --border: #334155;
            --border-highlight: #475569;
            --code-bg: #090d16;
            --code-text: #f1f5f9;
            --inline-code-bg: #0f172a;
            --inline-code-text: #38bdf8;
            --warning-bg: rgba(245, 158, 11, 0.12);
            --warning-border: #f59e0b;
            --warning-text: #fde68a;
            --decom-bg: rgba(139, 92, 246, 0.1);
            --decom-border: #8b5cf6;
            --decom-title: #c4b5fd;
            --callout-bg: #162032;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.65;
            padding: 2rem 1rem;
            transition: background-color 0.2s ease, color 0.2s ease;
        }}

        .container {{
            max-width: 960px;
            margin: 0 auto;
        }}

        /* Header & Metadata */
        .header-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            transition: background-color 0.2s ease, border-color 0.2s ease;
        }}

        .header-title {{
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--text-heading);
            margin-bottom: 1rem;
        }}

        .badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.25rem;
        }}

        .badge {{
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.025em;
            text-transform: uppercase;
        }}

        .badge-primary {{ background: var(--primary-light); color: var(--primary); }}
        .badge-purple {{ background: var(--accent-light); color: var(--accent); }}
        .badge-gray {{ background: var(--bg-subtle); color: var(--text-muted); border: 1px solid var(--border); }}

        /* Action Toolbar */
        .toolbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.75rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border);
        }}

        .toolbar-group {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.6rem 1.1rem;
            border-radius: 8px;
            font-size: 0.875rem;
            font-weight: 600;
            cursor: pointer;
            border: 1px solid transparent;
            transition: all 0.2s;
            text-decoration: none;
            font-family: inherit;
        }}

        .btn-primary {{
            background: var(--primary);
            color: #ffffff;
        }}
        .btn-primary:hover {{ background: var(--primary-hover); }}

        .btn-outline {{
            background: var(--bg-card);
            border-color: var(--border);
            color: var(--text-main);
        }}
        .btn-outline:hover {{ background: var(--bg-subtle); border-color: var(--border-highlight); }}

        /* Callout Banners */
        .callout {{
            background: var(--callout-bg);
            border-left: 4px solid var(--primary);
            padding: 1.25rem 1.5rem;
            border-radius: 0 8px 8px 0;
            margin: 1.5rem 0;
        }}

        .callout-warning {{
            background: var(--warning-bg);
            border-left-color: var(--warning-border);
            color: var(--warning-text);
        }}

        .callout-title {{
            font-weight: 700;
            margin-bottom: 0.5rem;
            font-size: 1rem;
        }}

        /* Case Studies (Cards) */
        .card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);
            clear: both;
            transition: background-color 0.2s ease, border-color 0.2s ease;
        }}

        .card-header {{
            border-bottom: 2px solid var(--primary-light);
            padding-bottom: 0.75rem;
            margin-bottom: 1.25rem;
        }}

        .card-header-accent {{
            border-bottom: 2px solid var(--accent-light);
            padding-bottom: 0.75rem;
            margin-bottom: 1.25rem;
        }}

        h2 {{
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--text-heading);
        }}

        h3 {{
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--text-heading);
            margin-top: 1.25rem;
            margin-bottom: 0.5rem;
        }}

        h4 {{
            font-size: 1rem;
            font-weight: 600;
            color: var(--text-main);
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }}

        p {{
            margin-bottom: 1rem;
        }}

        ul, ol {{
            margin-left: 1.5rem;
            margin-bottom: 1rem;
        }}

        li {{
            margin-bottom: 0.4rem;
        }}

        /* Math & Constraint Badges */
        .math-badge {{
            display: inline-block;
            font-family: 'Fira Code', Consolas, monospace;
            background: var(--inline-code-bg);
            color: var(--inline-code-text);
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            font-size: 0.9em;
            font-weight: 600;
            border: 1px solid var(--border-highlight);
            letter-spacing: 0.03em;
        }}

        .var-math {{
            font-family: 'Inter', -apple-system, sans-serif;
            font-style: italic;
            font-weight: 600;
            color: var(--text-heading);
            padding: 0 0.15rem;
        }}

        /* Lembar Analisis (Worksheet Box) */
        .decom-box {{
            background: var(--decom-bg);
            border: 1.5px dashed var(--decom-border);
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            clear: both;
        }}

        .decom-box h4 {{
            color: var(--decom-title);
            margin-top: 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        /* Code Blocks */
        pre {{
            background: var(--code-bg);
            color: var(--code-text);
            padding: 1.25rem;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Fira Code', Consolas, monospace;
            font-size: 0.875rem;
            line-height: 1.5;
            margin: 1rem 0;
            border: 1px solid var(--border);
            position: relative;
        }}

        code {{
            font-family: 'Fira Code', Consolas, monospace;
            font-size: 0.9em;
        }}

        p code, li code, td code {{
            background: var(--inline-code-bg);
            color: var(--inline-code-text);
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            border: 1px solid var(--border);
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            font-size: 0.925rem;
        }}

        th, td {{
            padding: 0.75rem 1rem;
            text-align: left;
            border: 1px solid var(--border);
        }}

        th {{
            background: var(--bg-table-head);
            font-weight: 600;
            color: var(--text-heading);
        }}

        tr:nth-child(even) {{
            background: var(--bg-table-even);
        }}

        /* Teacher's Solutions Section */
        .teacher-section {{
            margin-top: 3rem;
            border-top: 3px double var(--border-highlight);
            padding-top: 2rem;
        }}

        .teacher-group {{
            margin-top: 2rem;
            margin-bottom: 2.5rem;
        }}

        .teacher-group-title {{
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--accent);
            background: var(--accent-light);
            padding: 0.85rem 1.25rem;
            border-radius: 8px;
            margin-bottom: 1.25rem;
            border-left: 5px solid var(--accent);
        }}

        /* Print Media Queries (Always Print Clean Light Mode) */
        @media print {{
            body {{
                background: #ffffff !important;
                color: #000000 !important;
                padding: 0;
            }}

            .toolbar, .btn {{
                display: none !important;
            }}

            .card, .header-card {{
                background: #ffffff !important;
                color: #000000 !important;
                box-shadow: none !important;
                border: 1px solid #ccc !important;
                page-break-inside: avoid;
                margin-bottom: 1.5rem;
            }}

            h1, h2, h3, h4, p, li, td, th {{
                color: #000000 !important;
            }}

            .decom-box {{
                border-color: #666 !important;
                background: #fafafa !important;
            }}

            pre {{
                background: #f8f8f8 !important;
                color: #000000 !important;
                border: 1px solid #ddd !important;
            }}

            .math-badge, p code, li code {{
                border: 1px solid #999 !important;
                background: #f0f0f0 !important;
                color: #000000 !important;
            }}

            .hide-on-print {{
                display: none !important;
            }}
        }}

        .hidden {{
            display: none !important;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Main Content -->
        {content}
    </div>

    <script>
        function updateThemeBtnText() {{
            const current = document.documentElement.getAttribute('data-theme') || 'light';
            const btn = document.getElementById('btnThemeToggle');
            if (btn) {{
                btn.innerHTML = current === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
            }}
        }}

        function toggleTheme() {{
            const current = document.documentElement.getAttribute('data-theme') || 'light';
            const next = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('soal_theme', next);
            updateThemeBtnText();
        }}

        function toggleTeacherSection() {{
            const sec = document.getElementById('kunci-jawaban');
            const btn = document.getElementById('btnToggleSolutions');
            if (!sec) return;
            if (sec.classList.contains('hidden')) {{
                sec.classList.remove('hidden');
                btn.innerHTML = '👁️ Sembunyikan Kunci & Pembahasan (Mode Siswa)';
                btn.classList.remove('btn-outline');
                btn.classList.add('btn-primary');
            }} else {{
                sec.classList.add('hidden');
                btn.innerHTML = '🔓 Tampilkan Kunci & Pembahasan (Mode Guru)';
                btn.classList.remove('btn-primary');
                btn.classList.add('btn-outline');
            }}
        }}

        function printDoc() {{
            window.print();
        }}

        document.addEventListener('DOMContentLoaded', updateThemeBtnText);
    </script>
</body>
</html>
"""

def clean_math_expression(expr):
    """Mengubah format math/LaTeX menjadi HTML Entity yang 100% aman di browser apa pun."""
    expr = re.sub(r'\\text\{([^}]+)\}', r'\1', expr)
    expr = expr.strip()
    
    if re.match(r'^[a-zA-Z]$', expr):
        return f'<span class="var-math">{expr}</span>'

    escaped = html.escape(expr)
    escaped = escaped.replace('&lt;=', '&le;').replace('&gt;=', '&ge;')
    escaped = escaped.replace('<=', '&le;').replace('>=', '&ge;')
    escaped = escaped.replace('\\le', '&le;').replace('\\ge', '&ge;')
    escaped = escaped.replace('≤', '&le;').replace('≥', '&ge;')
    escaped = escaped.replace('\\ne', '&ne;').replace('!=', '&ne;').replace('≠', '&ne;')
    escaped = escaped.replace('\\times', '&times;').replace('×', '&times;')
    escaped = escaped.replace('\\rightarrow', '&rarr;').replace('→', '&rarr;')

    if any(sym in escaped for sym in ['&le;', '&ge;', '=', '&lt;', '&gt;', '+', '-', '&times;', '&rarr;']):
        return f'<span class="math-badge">{escaped}</span>'
        
    return f'<span class="var-math">{escaped}</span>'

def inline_format(text):
    def math_sub(match):
        inner = match.group(1)
        return clean_math_expression(inner)
        
    text = re.sub(r'\$([^$]+)\$', math_sub, text)
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)
    text = text.replace('\\le', '&le;').replace('\\ge', '&ge;').replace('≤', '&le;').replace('≥', '&ge;')
    text = text.replace('\\times', '&times;').replace('×', '&times;')
    text = text.replace('\\rightarrow', '&rarr;').replace('→', '&rarr;')
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    return text

def parse_markdown_to_html(md_text):
    meta = {}
    content = md_text
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            fm_lines = parts[1].strip().split("\n")
            for line in fm_lines:
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            content = parts[2].strip()

    title = meta.get("materi", "Modul Latihan C++").replace("-", " ").title()

    code_blocks = []
    def repl_code(match):
        lang = match.group(1) or ""
        code = textwrap.dedent(match.group(2)).strip()
        idx = len(code_blocks)
        escaped_code = html.escape(code)
        code_blocks.append(f'<pre><code class="language-{lang}">{escaped_code}</code></pre>')
        return f"\n__CODE_BLOCK_{idx}__\n"

    content = re.sub(r'```([a-zA-Z0-9_\-]*)\n(.*?)```', repl_code, content, flags=re.DOTALL)

    lines = content.split("\n")
    html_out = []

    in_card = False
    in_decom_box = False
    in_teacher_section = False
    in_teacher_group = False
    in_table = False
    table_header_done = False
    in_list = False
    list_type = None

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html_out.append(f"</{list_type}>")
            in_list = False
            list_type = None

    def close_table():
        nonlocal in_table, table_header_done
        if in_table:
            html_out.append("</tbody></table>")
            in_table = False
            table_header_done = False

    def close_decom_box():
        nonlocal in_decom_box
        if in_decom_box:
            close_list()
            close_table()
            html_out.append("</div> <!-- /.decom-box -->")
            in_decom_box = False

    def close_card():
        nonlocal in_card
        if in_card:
            close_decom_box()
            close_list()
            close_table()
            html_out.append("</div> <!-- /.card -->")
            in_card = False

    def close_teacher_group():
        nonlocal in_teacher_group
        if in_teacher_group:
            close_card()
            html_out.append("</div> <!-- /.teacher-group -->")
            in_teacher_group = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("# ") and ("Panduan Pengajar" in stripped or "Kunci Jawaban" in stripped):
            close_teacher_group()
            close_card()
            if not in_teacher_section:
                in_teacher_section = True
                html_out.append('<div id="kunci-jawaban" class="teacher-section hidden">')
                title_clean = stripped.replace("#", "").strip()
                html_out.append(f'''
                <div class="header-card" style="border-left: 6px solid var(--accent);">
                    <h2 style="color:var(--accent);">📘 {title_clean}</h2>
                    <p style="color:var(--text-muted); margin-top:0.5rem;">
                        Bagian ini dirancang khusus untuk pegangan pengajar/asisten, dilengkapi penjelasan langkah demi langkah dan kode solusi acuan C++.
                    </p>
                </div>
                ''')
            i += 1
            continue

        if stripped in ["---", "--- ---"]:
            close_decom_box()
            i += 1
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            close_list()
            cells = [c.strip() for c in stripped[1:-1].split("|")]
            if not in_table:
                in_table = True
                table_header_done = False
                html_out.append('<table><thead><tr>')
                for c in cells:
                    html_out.append(f'<th>{inline_format(c)}</th>')
                html_out.append('</tr></thead><tbody>')
                i += 1
                continue
            elif in_table and not table_header_done and re.match(r'^[\s\-:|]+$', stripped):
                table_header_done = True
                i += 1
                continue
            else:
                html_out.append('<tr>')
                for c in cells:
                    html_out.append(f'<td>{inline_format(c)}</td>')
                html_out.append('</tr>')
                i += 1
                continue
        else:
            close_table()

        bullet_match = re.match(r'^(\*|-)\s+(.*)', stripped)
        num_match = re.match(r'^(\d+)\.\s+(.*)', stripped)

        if bullet_match or num_match:
            cur_type = 'ul' if bullet_match else 'ol'
            item_text = bullet_match.group(2) if bullet_match else num_match.group(2)
            if not in_list:
                in_list = True
                list_type = cur_type
                html_out.append(f'<{list_type}>')
            elif list_type != cur_type:
                html_out.append(f'</{list_type}>')
                list_type = cur_type
                html_out.append(f'<{list_type}>')
            html_out.append(f'<li>{inline_format(item_text)}</li>')
            i += 1
            continue
        else:
            close_list()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("__CODE_BLOCK_"):
            html_out.append(stripped)
            i += 1
            continue

        # H1: Document Header
        if stripped.startswith("# "):
            title_text = inline_format(stripped[2:])
            html_out.append(f'''
            <div class="header-card">
                <div class="badges">
                    <span class="badge badge-primary">{meta.get("id", "SOAL")}</span>
                    <span class="badge badge-purple">{meta.get("subjek", "C++").upper()}</span>
                    <span class="badge badge-gray">{meta.get("tingkat", "Beginner").upper()}</span>
                    <span class="badge badge-gray">{meta.get("jumlah_soal", "")} SOAL</span>
                </div>
                <h1 class="header-title">{title_text}</h1>
                <div class="toolbar">
                    <div class="toolbar-group">
                        <a href="../../../../index.html" class="btn btn-outline">
                            🏠 Kembali ke Portal
                        </a>
                        <button id="btnThemeToggle" class="btn btn-outline" onclick="toggleTheme()">
                            🌙 Dark Mode
                        </button>
                    </div>
                    <div class="toolbar-group">
                        <button id="btnToggleSolutions" class="btn btn-outline" onclick="toggleTeacherSection()">
                            🔓 Tampilkan Kunci & Pembahasan (Mode Guru)
                        </button>
                        <button class="btn btn-outline" onclick="printDoc()">
                            🖨️ Cetak / PDF
                        </button>
                    </div>
                </div>
            </div>
            ''')
            i += 1
            continue

        # H2: Major Sections or Pembahasan Kasus
        if stripped.startswith("## "):
            h2_text = inline_format(stripped[3:])
            close_card()
            if "Pembahasan Kasus" in h2_text:
                close_teacher_group()
                in_teacher_group = True
                html_out.append(f'<div class="teacher-group"><div class="teacher-group-title">🎯 {h2_text}</div>')
            else:
                html_out.append(f'<div class="callout callout-warning"><div class="callout-title">📌 {h2_text}</div></div>')
            i += 1
            continue

        # H3: Case Studies or Questions or Approaches
        if stripped.startswith("### "):
            h3_text = inline_format(stripped[4:])
            close_card()
            header_class = "card-header-accent" if in_teacher_section else "card-header"
            html_out.append(f'<div class="card"><div class="{header_class}"><h2>{h3_text}</h2></div>')
            in_card = True
            i += 1
            continue

        # H4: Sub-headers or Lembar Analisis
        if stripped.startswith("#### "):
            h4_text = inline_format(stripped[5:])
            if "Lembar Analisis & Dekomposisi" in h4_text:
                close_decom_box()
                html_out.append(f'<div class="decom-box"><h4>📝 {h4_text}</h4>')
                in_decom_box = True
            else:
                close_decom_box()
                html_out.append(f'<h4>{h4_text}</h4>')
            i += 1
            continue

        if stripped.startswith("> "):
            quote_text = inline_format(stripped[2:])
            html_out.append(f'<div class="callout"><p>{quote_text}</p></div>')
            i += 1
            continue

        html_out.append(f'<p>{inline_format(stripped)}</p>')
        i += 1

    close_card()
    close_teacher_group()
    if in_teacher_section:
        html_out.append('</div> <!-- /#kunci-jawaban -->')

    raw_html = "\n".join(html_out)

    for idx, block in enumerate(code_blocks):
        raw_html = raw_html.replace(f"__CODE_BLOCK_{idx}__", block)

    return HTML_TEMPLATE.format(title=title, content=raw_html)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--all":
        import glob
        md_files = sorted(glob.glob("outputs/**/*.md", recursive=True))
        for md_path in md_files:
            html_path = os.path.splitext(md_path)[0] + ".html"
            with open(md_path, 'r', encoding='utf-8') as f:
                md = f.read()
            res = parse_markdown_to_html(md)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(res)
            print(f"Converted: {md_path} -> {html_path}")
    elif len(sys.argv) >= 3:
        in_path = sys.argv[1]
        out_path = sys.argv[2]
        with open(in_path, 'r', encoding='utf-8') as f:
            md = f.read()
        res = parse_markdown_to_html(md)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(res)
        print(f"Successfully converted {in_path} -> {out_path}")
    else:
        print("Usage: python md_to_html.py <input.md> <output.html> OR python md_to_html.py --all")
        sys.exit(1)
