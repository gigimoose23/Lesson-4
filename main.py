import pgzrun
import random
state = False
WIDTH = 900
HEIGHT = 500
Score = 0
Bee = Actor("bumblebee")
Flower = Actor("sunflower")


Bee.pos = (90,90)
Flower.pos = (50,50)

def draw():
    global state
    screen.blit("background", (0,0))
    Bee.draw()
    Flower.draw()
    if state == False:
        screen.draw.text("Your score: " + str(Score), color=(0,0,0), topleft=(0,0))
    else:
        screen.fill((255,255,255))
        screen.draw.text("Your final score: " + str(Score), color=(0,0,0),topleft=(0,0))
    

def moveFlower():
    Flower.x = random.randint(0,850)
    Flower.y = random.randint(0,850)

def timeUp():
    global state 
    state = True
    print(state)

def update():
    global Score
    global state
    if keyboard.left:
        Bee.x -= 4
    elif keyboard.right:
        Bee.x += 4
    elif keyboard.up:
        Bee.y -= 4
    elif keyboard.down:
        Bee.y += 4

    if Bee.colliderect(Flower):
        Score += 1
        moveFlower()

    

clock.schedule(timeUp, 3)

moveFlower()
pgzrun.go()