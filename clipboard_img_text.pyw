#! C:\\Users\\joelr\\AppData\\Local\\Programs\\Python\\Python310\\pythonw.exe
from PIL import Image,ImageGrab
from pytesseract import pytesseract
import pyperclip
from win11toast import toast
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
            toast("Clipboard_img_text","Copied to clipboard")

        except:
            print("couldnt copy to clipboard")
            toast("Clipboard_img_text","Couldnt copy to clipboard")

    else:
        print("no image found in clipboard :(")
        toast("Clipboard_img_text","no image found in clipboard :(")
except Exception as e:
    print(e)
    toast("Clipboard_img_text","exception occured")
    
quit()
