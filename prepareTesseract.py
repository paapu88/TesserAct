
import glob
from os.path import basename
import sys
import os

fnames =glob.glob(sys.argv[1])


for fname in fnames:
    command='tesseract '+fname+' '+basename(fname)+'  batch.nochop makebox'
    os.system(command)


