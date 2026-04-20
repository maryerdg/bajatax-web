import fitz  # PyMuPDF

pdf_path = "assets/boletines/boletin-jornada-laboral-2026.pdf"
img_path = "assets/boletines/boletin-preview.png"

try:
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)  # first page
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # zoom for better quality
    pix.save(img_path)
    print(f"Successfully generated real preview to {img_path}")
except Exception as e:
    print(f"Failed to generate preview: {e}")
