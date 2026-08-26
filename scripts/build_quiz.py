# -*- coding: utf-8 -*-
import re, glob, json, os, html

TOPIC_FILES = [
    ("csharp",      "C# & OOP Fundamentals",              "#b5502f"),
    ("dotnet",      ".NET Core, ASP.NET & Web API",        "#2f6f6b"),
    ("ef",          "Entity Framework & Data Access",      "#3a7a8c"),
    ("sql",         "SQL Server & Databases",              "#3d4e8c"),
    ("angular",     "Angular & Frontend",                  "#6b7a3a"),
    ("azure",       "Cloud & Azure",                       "#7a4a6b"),
    ("arch",        "Microservices & Architecture",        "#46586b"),
    ("patterns",    "Design Patterns & SOLID",             "#a67c2e"),
    ("concurrency", "Multithreading & Async",              "#9c4a5c"),
    ("testing",     "Testing & Code Quality",              "#7a5a3a"),
    ("devops",      "DevOps, Git & Agile",                 "#5a6b3a"),
    ("coding",      "Coding & Algorithm Challenges",       "#5a3a7a"),
    ("scenario",    "Scenario & Behavioral",                "#8c5a3a"),
]

FILE_ORDER = [
    "01-csharp-oop.md",
    "02-dotnet-aspnet-webapi.md",
    "03-entity-framework-data-access.md",
    "04-sql-server.md",
    "05-angular-frontend.md",
    "06-azure-cloud.md",
    "07-microservices-architecture.md",
    "08-design-patterns-solid.md",
    "09-concurrency-async.md",
    "10-testing-quality.md",
    "11-devops-git-agile.md",
    "12-coding-challenges.md",
    "13-scenario-behavioral.md",
]

def inline_md(text):
    text = html.escape(text, quote=False)
    # bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # italic (single asterisk, after bold is already consumed)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # inline code
    text = re.sub(r'`([^`]+?)`', r'<code>\1</code>', text)
    # links [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    return text

def md_to_html(body):
    lines = body.split('\n')
    out = []
    i = 0
    para_buf = []
    list_buf = []
    list_type = None
    in_table = False
    table_rows = []

    def flush_para():
        if para_buf:
            out.append('<p>' + inline_md(' '.join(para_buf).strip()) + '</p>')
            para_buf.clear()

    def flush_list():
        nonlocal list_type
        if list_buf:
            tag = 'ol' if list_type == 'ol' else 'ul'
            out.append('<' + tag + '>' + ''.join('<li>' + inline_md(x) + '</li>' for x in list_buf) + '</' + tag + '>')
            list_buf.clear()
        list_type = None

    def flush_table():
        nonlocal in_table
        if table_rows:
            header = table_rows[0]
            body_rows = table_rows[2:] if len(table_rows) > 1 else []
            th = ''.join('<th>' + inline_md(c.strip()) + '</th>' for c in header)
            trs = ''
            for r in body_rows:
                trs += '<tr>' + ''.join('<td>' + inline_md(c.strip()) + '</td>' for c in r) + '</tr>'
            out.append('<div class="tbl-wrap"><table><thead><tr>' + th + '</tr></thead><tbody>' + trs + '</tbody></table></div>')
            table_rows.clear()
        in_table = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith('```'):
            flush_para(); flush_list(); flush_table()
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            code_text = html.escape('\n'.join(code_lines))
            out.append(f'<pre><code class="lang-{lang or "text"}">{code_text}</code></pre>')
            i += 1
            continue

        if stripped.startswith('|'):
            flush_para(); flush_list()
            in_table = True
            cells = [c for c in stripped.strip('|').split('|')]
            table_rows.append(cells)
            i += 1
            continue
        else:
            if in_table:
                flush_table()

        if re.match(r'^[-*]\s+', stripped):
            flush_para()
            if list_type != 'ul':
                flush_list()
            list_type = 'ul'
            list_buf.append(re.sub(r'^[-*]\s+', '', stripped))
            i += 1
            continue

        if re.match(r'^\d+\.\s+', stripped):
            flush_para()
            if list_type != 'ol':
                flush_list()
            list_type = 'ol'
            list_buf.append(re.sub(r'^\d+\.\s+', '', stripped))
            i += 1
            continue

        if stripped == '':
            flush_para(); flush_list()
            i += 1
            continue

        if stripped.startswith('>'):
            flush_para(); flush_list()
            out.append('<blockquote>' + inline_md(re.sub(r'^>\s?', '', stripped)) + '</blockquote>')
            i += 1
            continue

        # plain paragraph line
        flush_list()
        para_buf.append(stripped)
        i += 1

    flush_para(); flush_list(); flush_table()
    return '\n'.join(out)

def parse_file(path, cat_key, cat_label, cat_color):
    with open(path, encoding='utf-8') as f:
        content = f.read()

    # split on level-2 headings, skip TOC
    parts = re.split(r'\n(?=## )', content)
    cards = []
    for part in parts:
        m = re.match(r'^##\s+(?:\d+\.\s*)?(.*?)\n', part)
        if not m:
            continue
        heading = m.group(1).strip()
        if heading.lower() == 'table of contents':
            continue
        body = part[m.end():]
        # strip back-to-top link line
        body = re.sub(r'\*\*\[⬆ Back to Top\]\([^)]*\)\*\*\s*$', '', body.strip(), flags=re.MULTILINE).strip()
        answer_html = md_to_html(body)
        question_html = inline_md(heading)
        cards.append({
            "cat": cat_key,
            "q": question_html,
            "a": answer_html,
        })
    return cards

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    topics_dir = os.path.join(repo_root, 'topics')

    all_cards = []
    categories = []
    for (key, label, color), fname in zip(TOPIC_FILES, FILE_ORDER):
        path = os.path.join(topics_dir, fname)
        cards = parse_file(path, key, label, color)
        for idx, c in enumerate(cards):
            c['id'] = f'{key}-{idx}'
        all_cards.extend(cards)
        categories.append({"key": key, "label": label, "color": color, "count": len(cards)})
        print(f'{fname}: {len(cards)} cards')

    print(f'TOTAL: {len(all_cards)} cards')

    data_json = json.dumps({"categories": categories, "cards": all_cards}, ensure_ascii=False)

    template_path = os.path.join(script_dir, 'quiz_template.html')
    with open(template_path, encoding='utf-8') as f:
        template = f.read()

    output_html = template.replace('__CARD_DATA_JSON__', data_json)

    docs_dir = os.path.join(repo_root, 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    out_path = os.path.join(docs_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(output_html)
    print('Wrote', out_path, f'({len(output_html)} bytes)')

if __name__ == '__main__':
    main()
