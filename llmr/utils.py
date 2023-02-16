import PyPDF2

def extract_text_from_pdf(filepath):
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        number_of_pages = len(reader.pages)
        text = ''
        for page_number in range(number_of_pages):
            page = reader.pages[page_number]
            text += page.extract_text()
        return text


def spliter(text, maxlen): # maxlen = 4097
    chunks = []
    for i in range(0, len(text), maxlen):
        chunks.append(text[i:i+maxlen])
    return chunks
