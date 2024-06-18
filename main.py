from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"c:\\Program Files\\Tesseract-OCR\\tesseract.exe"


print(pytesseract.image_to_pdf(Image.open('images\\mikah.jpg')))