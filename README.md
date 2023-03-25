# clipboard_img_text
A tool which takes in an image in your clipboard and copies the text in the image back to your clipboard

Suppose you want to copy text (for example: some code) from a source. But the text is within an image.
Hence you won't be able to copy the text from that image.
This tool solves that problem.
You take a screenshot of the image on the screen with the text, then it will get copied on your clipboard (atleast that happens for most Windows devices. If that doesn't happen, then copy the image to the clipboard)
Run the tool. The text from the image will be extracted and will be copied onto your clipboard.

Some uses for this tool is to copy documentation if present in an image.


##Setup

Assuming you have python already set up

### Dependencies:
  We will be using the Tesseract OCR to extract text from images.
  '''
  [download](https://digi.bib.uni-mannheim.de/tesseract/) the latest version and set up Tesseract
 
 
## Libraries:
    `pip install pillow`
    '''
    `pip install pytesseract `
    '''
    `pip install pyperclip`
    
