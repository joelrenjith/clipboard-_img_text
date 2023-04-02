#! C:\\Users\\joelr\\AppData\\Local\\Programs\\Python\\Python310\\pythonw.exe
from PIL import Image,ImageGrab
from pytesseract import pytesseract
import pyperclip
from win10toast import ToastNotifier
import time
try:
    path_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    toast = ToastNotifier()
    img = ImageGrab.grabclipboard()
    if(isinstance(img, Image.Image)):    
        pytesseract.tesseract_cmd = path_tesseract
        l = (pytesseract.image_to_string(img))
        print(l)
        try:
            pyperclip.copy(l)
            print("copied to clipboard")
            toast.show_toast("Clipboard_img_text","Copied to clipboard")

        except:
            print("couldnt copy to clipboard")
            toast.show_toast("Clipboard_img_text","Couldnt copy to clipboard")

    else:
        print("no image found in clipboard :(")
        toast.show_toast("Clipboard_img_text","no image found in clipboard :(")
except Exception as e:
    print(e)
    toast.show_toast("Clipboard_img_text","exception occured")
    
time.sleep(3)
quit()
