import os
imageSize = 128
screenSize = 512
numTilesSide = 4
numTilesTotal = 16
margin = 4
assetDir='assets'
assetFile =[x for x in os.listdir(assetDir) if x[-3:].lower() == 'png']
assert len(assetFile) == 8
