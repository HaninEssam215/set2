import weasyprint
# import base64
# from weasyprint.text.fonts import FontConfiguration


# path_to_file = 'reminder.html'

# # Read the HTML content from the file
# with open(path_to_file, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Create a WeasyPrint CSS object and customize the options
# font_config = FontConfiguration()
css = weasyprint.CSS(string="""
@page {
    margin: 0;
    padding: 0;
}
body {
    margin: 0;
    padding: 0;
    font-family: 'Forum', cursive;
}
""")



# # Generate the PDF using WeasyPrint and apply the custom options
# pdf = weasyprint.HTML(string=html_content).write_pdf(stylesheets=[css], encoding='utf-8')

# # Save the PDF to a file with the correct encoding
# with open('output.pdf', 'wb') as file:
#     file.write(pdf)


path_to_file = 'reminder.html'

# Read the HTML content from the file
with open(path_to_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Generate the PDF using WeasyPrint
pdf = weasyprint.HTML(string=html_content).write_pdf(stylesheets=[css], encoding='utf-8')

# Save the PDF to a file with the correct encoding
with open('output.pdf', 'wb') as file:
    file.write(pdf)
