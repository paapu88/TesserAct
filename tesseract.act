
#synaptic:
# python3-pyocr
# tesseract-ocr language files for Finnish
#
# sudo -H pip3 install pytesseract
#
# download jTessBoxEditor

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import sys
print(pytesseract.image_to_string(Image.open(sys.argv[1])))
print(pytesseract.image_to_string(Image.open(sys.argv[1]), lang='fin'))
