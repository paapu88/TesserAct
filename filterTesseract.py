# python3 ~/PycharmProjects/TesserAct/filterTesseract.py "*jpg"
import glob
from os.path import basename
import sys
import os

fnames =glob.glob(sys.argv[1])


for fname in fnames:
    command='convert -density 300 -depth 8 '+fname+' -background white -flatten +matte -compress none -monochrome '+basename(fname)+'.png' 
    print(fname)
    os.system(command)


