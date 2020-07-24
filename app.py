import numpy
import pygame
import gameConfig as gc

from pygame import display, event, image
from animal import Animal
from time import sleep
pygame.init()

def find_index(x, y):
    row = y // gc.imageSize
    col = x // gc.imageSize
    index = row * gc.numTilesSide + col
    return index

display.set_caption("Card Matcher")
screen= display.set_mode((512,512))
matched = image.load('other_assets/matched.png')
#screen.blit(matched, (0,0))
#display.flip()
running= True
tiles =[Animal(i) for i in range(0, gc.numTilesTotal)]
currentImages = []
while running:
    current_events= event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running= False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running=False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            index = find_index(mouseX, mouseY)
            if index not in currentImages:
                currentImages.append(index)
            if len(currentImages) > 2:
                currentImages = currentImages[1:]

    
    screen.fill((255,255,255))
    totalSkipped =0
    
    for _,tile in enumerate(tiles):
        imageI = tile.image if tile.index in currentImages else tile.box
        if not tile.skip:
            screen.blit(imageI, (tile.col*gc.imageSize+gc.margin, tile.row*gc.imageSize+gc.margin))
        else:
            totalSkipped+=1   
    display.flip()

    if len(currentImages) == 2:
        index1, index2 =currentImages
        if tiles[index1].name == tiles[index2].name:
            tiles[index1].skip=True
            tiles[index2].skip=True
            sleep(0.4)
            screen.blit(matched,(0,0))
            display.flip()
            sleep(0.4)
            currentImages =[]
    if totalSkipped == len(tiles):
        running =False

print("Good Bye")