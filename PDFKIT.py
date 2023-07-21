import pdfkit

path_to_file = 'reminder.html'


options = {
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
}

pdfkit.from_file(path_to_file, 'output.pdf', options=options)