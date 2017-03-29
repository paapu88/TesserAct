""" python3 convert2gray.py "ofromPlateiMovedrekkariKirjaimistoMusta300dpi.tif" "GetTesseractTrainingFiles/Train/fin9.Plate.exp0.tif"
"""

import cv2, sys

gray = cv2.imread(sys.argv[1], 0)
cv2.imwrite(sys.argv[2], gray)