# Don't work offline

from gpt4all import GPT4All, Embed4All
from pathlib import Path


import fitz  

# Define the path to your PDF file
pdf_path = "docs/example.pdf"

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Initialize an empty string to store the concatenated text
all_text = ""

# Iterate through all pages in the PDF
for page_number in range(pdf_document.page_count):
    # Get the page
    page = pdf_document[page_number]

    # Get the text of the page
    page_text = page.get_text()

    # Concatenate the text
    all_text += page_text + "\n"

# Close the PDF document
pdf_document.close()

embedder = Embed4All()
output = embedder.embed(all_text)
print(output)

