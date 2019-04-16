import pygame
import os
import random
from classLibrary import *

pygame.init()
clock = pygame.time.Clock()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
fps = 50

targetGroup = pygame.sprite.Group()
boidsGroup = pygame.sprite.Group()
zombieGroup = pygame.sprite.Group()

z = Zombie(400,400)
z.loadPic(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'face.png'))
zombieGroup.add(z)

for num in range(10):
    x = random.randint(-800, 1600)
    y = random.randint(-800, 1600)
    people = passager(x, y)
    targetGroup.add(people)

running = True
while running:
    time = clock.tick(fps)
    screen.fill((255, 255, 255))
    keysPressing = pygame.key.get_pressed()
    if keysPressing[pygame.K_UP]:
        for ob in targetGroup:
            ob.y += z.v
        for nc in boidsGroup:
            nc.y += z.v


    if keysPressing[pygame.K_DOWN]:
        for ob in targetGroup:
            ob.y -= z.v
        for nc in boidsGroup:
            nc.y -= z.v


    if keysPressing[pygame.K_LEFT]:
        for ob in targetGroup:
            ob.x += z.v
            ob.updateRect()
        for nc in boidsGroup:
            nc.x += z.v


    if keysPressing[pygame.K_RIGHT]:
        for ob in targetGroup:
            ob.x -= z.v
            ob.updateRect()
        for nc in boidsGroup:
            nc.x -= z.v


    for ob in targetGroup:
        ob.display(screen)
        if pygame.sprite.collide_circle_ratio(0.8)(z, ob):
            bx, by = ob.getPos()
            newChild = ZomBoids(bx,by)
            boidsGroup.add(newChild)
            targetGroup.remove(ob) 

    for child in boidsGroup:
        child.display(screen)
        child.dodgeMove(z)
        child.follow(z)
                                       

    z.updateRect()
    for ob in targetGroup:
        ob.updateRect()
    for child in boidsGroup:
        child.updateRect()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    z.display(screen)
    pygame.display.flip()
pygame.quit()