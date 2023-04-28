# Import the libraries
# Will convert the image to text string:
import pytesseract

# Adds image processing capabilities:
from PIL import Image	

# Opening an image from the source path:
img = Image.open('text2.jpg')	

# Describes image format in the output:
print(img)			

# Path where the tesseract module is installed:
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'

# Converts the image to result and saves it into a result variable:
result = pytesseract.image_to_string(img)

# Write text in a text file and save it to source path:
with open('abc.txt',mode ='w') as file:	
	
				file.write(result)
				print(result)
				

