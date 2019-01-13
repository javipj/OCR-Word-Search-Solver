from PIL import Image
import pytesseract

#resizes the wordsearch and turns into text
def translate(image):
    im = Image.open(image)
    basewidth = 6000
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    text = pytesseract.image_to_string(im, lang = "eng")

    return text

wordsearch = translate("code.png")
array = list(wordsearch)

def toArray(text):
    

