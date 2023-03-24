from PIL import Image,ImageGrab
from pytesseract import pytesseract
import pyperclip

try:
    path_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = ImageGrab.grabclipboard()
    if(isinstance(img, Image.Image)):    
        pytesseract.tesseract_cmd = path_tesseract
        l = (pytesseract.image_to_string(img))
        print(l)
        try:
            pyperclip.copy(l)
            print("copied to clipboard")
        except:
            print("couldnt copy to clipboard")

    else:
        print("no image found in clipboard :(")
except Exception as e:
    print(e)
if(input()=='exit'):
    quit
