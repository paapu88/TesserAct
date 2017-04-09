from __future__ import print_function
from tesserocr import PyTessBaseAPI, PSM, Justification
import glob
import sys
from matplotlib import pyplot as plt
import cv2

images = glob.glob(sys.argv[1])
try:
    showImages = int(sys.argv[2])
except:
    showImages = 1

with PyTessBaseAPI(psm=PSM.SINGLE_CHAR, lang='eng') as api:
    api.SetVariable("tessedit_char_whitelist","ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ-0123456789")
    #api.SetVariable(
    
    for img in images:
        api.SetImageFile(img)
        print(api.GetUTF8Text())
        #print(api.GetUnichar())
        print(api.AllWordConfidences())
        if showImages:
            show = cv2.imread(img)
            plt.imshow(show)
            plt.xticks([]), plt.yticks([])  # to hide tick values
            plt.show()

