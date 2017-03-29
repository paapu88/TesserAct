# for corrections use
# copy png to ./tmp and cd there
# python3 ../../../noQTpicture2rectangle.py 63 85

tesseract fin9.Plate.exp0.png fin9.Plate.exp0 box.train
 
unicharset_extractor fin9.Plate.exp0.box
 
# font name <italic> <bold> <fixed> <serif> <fraktur>
echo "Plate 0 0 0 0 0" > font_properties
 
shapeclustering -F font_properties -U unicharset fin9.Plate.exp0.tr
 
mftraining -F font_properties -U unicharset -O fin9.unicharset 
    fin9.Plate.exp0.tr
 
cntraining fin9.Plate.exp0.tr
 
 
# prefix "relevant" files with our language code
mv inttemp fin9.inttemp
mv normproto fin9.normproto
mv pffmtable fin9.pffmtable
mv shapetable fin9.shapetable
combine_tessdata fin9.
 
# copy the created eng2.traineddata to the tessdata folder
# so tesseract is able to find it
sudo cp fin9.traineddata /usr/local/share/tessdata/
