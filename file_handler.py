from docx import Document
from PyPDF2 import PdfReader
from odf.opendocument import OpenDocumentText
from odf.text import P

def extract_text_from_file(filepath):
    """Extrait le texte d'un fichier supporté."""
    try:
        if filepath.endswith('.txt'):
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        elif filepath.endswith('.pdf'):
            reader = PdfReader(filepath)
            return '\n'.join(page.extract_text() for page in reader.pages)
        elif filepath.endswith('.docx'):
            doc = Document(filepath)
            return '\n'.join(paragraph.text for paragraph in doc.paragraphs)
        else:
            raise ValueError("Format de fichier non supporté.")
    except Exception as e:
        raise Exception(f"Erreur lors de la lecture du fichier : {e}")

def save_text_to_file(text, output_path, file_format):
    """Enregistre le texte dans le format choisi."""
    try:
        if file_format == "txt":
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(text)
        elif file_format == "odt":
            odt_doc = OpenDocumentText()
            p = P(text=text)
            odt_doc.text.addElement(p)
            odt_doc.save(output_path)
        else:
            raise ValueError("Format non supporté pour l'enregistrement.")
    except Exception as e:
        raise Exception(f"Erreur lors de l'enregistrement du fichier : {e}")
