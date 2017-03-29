# python3 ~/PycharmProjects/TesserAct/applyTesseract.py "*tif" "-l fin9 --psm 7"
import glob
from os.path import basename
import sys
import os

fnames =glob.glob(sys.argv[1])


for fname in fnames:
    command='tesseract '+fname+' stdout '
    if len(sys.argv) > 2:
        command = command + sys.argv[2]
    print(fname)
    os.system(command)


