import pgzrun
import random

WIDTH = 300
HEIGHT = 500

Bee = Actor("bumblebee")
Flower = Actor("sunflower")


Bee.pos = (90,90)
Flower.pos = (50,50)

def draw():
    screen.blit("background", (0,0))
    Bee.draw()
    Flower.draw()

pgzrun.go()