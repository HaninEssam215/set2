import pdfkit

path_to_file = 'reminder.html'


options = {
    'page-size': 'A4',
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
    'enable-local-file-access': True,
}

pdfkit.from_file(path_to_file, 'output.pdf', options=options)