from PIL import Image
import pytesseract

# Load the image from the file path
image_path = './image.png'
img = Image.open(image_path)

# Use Tesseract to extract text from the image
extracted_text = pytesseract.image_to_string(img)
extracted_text
