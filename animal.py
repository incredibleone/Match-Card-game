import os
import random
import gameConfig as gc
from pygame import image, transform
animalsCount= dict((a,0) for a in gc.assetFile)

def availableAnimals():
    return [a for a, c in animalsCount.items() if c<2]

class Animal:
    def __init__(self, index):
        self.index = index
        self.row = index // gc.numTilesSide
        self.col = index % gc.numTilesSide
        self.name = random.choice(availableAnimals())
        animalsCount[self.name]+=1
        self.imagePath = os.path.join(gc.assetDir, self.name)
        self.image = image.load(self.imagePath)
        self.image= transform.scale(self.image, (gc.imageSize - 2*gc.margin, gc.imageSize-2*gc.margin))
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))
        self.skip = False
