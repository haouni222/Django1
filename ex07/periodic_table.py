import sys

def parse_elements(filename):
    elements = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            name, rest = line.strip().split('=', 1)
            props = {}
            for item in rest.split(','):
                key, value = item.strip().split(':', 1)
                props[key.strip()] = value.strip()
            props['name'] = name.strip()
            props['position'] = int(props['position'])
            elements.append(props)
    return elements

def build_table(elements):
    table = []
    row = []
    for el in elements:
        pos = el['position']
        if pos == 0 and row:
            table.append(row)
            row = []
        while len(row) < pos:
            row.append(None)
        row.append(el)
    if row:
        table.append(row)
    return table

def element_to_html(el):
    if not el:
        return '<td></td>'
    html = '<td style="border:1px solid black; padding:10px; vertical-align:top; min-width:120px">'
    html += f'<h4>{el["name"]}</h4>\n<ul>'
    html += f'<li>No {el["number"]}</li>'
    html += f'<li>{el["small"]}</li>'
    html += f'<li>{el["molar"]}</li>'
    electrons = el["electron"].split()
    total_electrons = sum(int(x) for x in electrons)
    html += f'<li>{total_electrons} electron{"s" if total_electrons > 1 else ""}</li>'
    html += '</ul></td>'
    return html

def main():
    elements = parse_elements('periodic_table.txt')
    table = build_table(elements)
    with open('periodic_table.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
        f.write('<meta charset="UTF-8">\n<title>Periodic Table</title>\n</head>\n<body>\n')
        f.write('<h2>Periodic Table of Elements</h2>\n')
        f.write('<table style="border-collapse:collapse;">\n')
        for row in table:
            f.write('<tr>')
            for cell in row:
                f.write(element_to_html(cell))
            f.write('</tr>\n')
        f.write('</table>\n</body>\n</html>')

if __name__ == "__main__":
    main()