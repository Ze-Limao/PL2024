import re #importar a biblioteca re para utilizar expressões regulares
import sys #importar a biblioteca sys para utilizar os argumentos da linha de comandos

def markdownToHtml(markdown, template):

    # expressões regulares para as diferentes formatações do markdown
    header_regex = re.compile(r'^(#{1,6})\s(.*)$')
    bold_regex = re.compile(r'\*\*(.*?)\*\*')
    italic_regex = re.compile(r'\*(.*?)\*')
    ul_regex = re.compile(r'^[\*\-\+]\s(.*)$')
    ol_regex = re.compile(r'^\d+\.\s(.*)$')
    img_regex = re.compile(r'!\[(.*?)\]\((.*?)\)')
    link_regex = re.compile(r'\[(.*?)\]\((.*?)\)')

    ul_flag = False
    ol_flag = False

    # Ler linha a linha do ficheiro markdown
    for line in markdown.split('\n'):

        # Cabeçalhos
        match = header_regex.match(line)
        if match:
            level = len(match.group(1))
            if level == 1:
                template += f"<h{level} class=\"bg-slate-200 py-4 text-3xl font-semibold text-white\" style=\"background-color: #6a0303;\">{match.group(2)}</h{level}>\n"
                continue
            else:
                template += f"<h{level} class=\"pt-16 pb-6 text-3xl font-semibold\" style=\"color: #6a0303; text-align: center;\">{match.group(2)}</h{level}>\n"
                continue

        # Negrito
        line = bold_regex.sub(r'<b>\1</b>', line)

        # Itálico
        line = italic_regex.sub(r'<i>\1</i>', line)
        
        # Lista não ordenada
        match = ul_regex.match(line)
        if match:
            if "<ul>" not in template or not ul_flag:
                template += "<ul>\n"
                ul_flag = True
            template += f"<li>{match.group(1)}</li>\n"
            continue

        # Lista ordenada
        match = ol_regex.match(line)
        if match:
            if "<ol>" not in template or not ol_flag:
                template += "<ol>\n"
                ol_flag = True
            template += f"<li>{match.group(1)}</li>\n"
            continue

        # Imagem
        line = img_regex.sub(r'<img src="\2" alt="\1">', line)

        # Link
        line = link_regex.sub(r'<a href="\2" alt="\1">\1</a>', line)

        template += line

        # Close any open lists using flags
        if ul_flag and not ul_regex.match(line):
            template += "</ul>\n"
            ul_flag = False
        if ol_flag and not ol_regex.match(line):
            template += "</ol>\n"
            ol_flag = False

    #Fechar o ficheiro HTML
    template += "\n</body>\n</html>"

    # Escrever no ficheiro HTML
    with open('Resultado.html', 'w') as file:
        file.write(template)


def main(args):
    # Template de página HTML
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Title Here</title>
    <!-- Additional head elements (stylesheets, scripts, etc.) can be added here -->
</head>
<body>
"""

    # Ler o ficheiro markdown e chamar a função markdownToHtml
    with open(args[1], 'r') as file:
        markdown = file.read()
        markdownToHtml(markdown, template)
    

    # Fechar o ficheiro HTML
    template += "</body>\n</html>"
    

if __name__ == "__main__":
    main(args=sys.argv)