import pygame
import random
# Tech Demo
pygame.init()
clock = pygame.time.Clock()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(GameObject, self).__init__()
        self.x = x
        self.y = y
        self.image = None
        self.vx = 0
        self.vy = 0
        self.rect = pygame.Rect(x - 10, y - 10, 20 ,20)
    
    def updateRect(self):
        w = 40
        self.rect = pygame.Rect(self.x - 10, self.y - 10, w, w)

    def loadPic(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()


class Zombie(GameObject):

    def __init__(self, x, y):
        super(Zombie, self).__init__(x, y)
        self.r = 20

    def display(self):
        pygame.draw.circle(screen, (0, 0, 255), (self.x + self.vx, self.y + self.vy), self.r)

class ZomBoids(Zombie):

    def __init__(self, x, y):
        super(ZomBoids, self).__init__(x, y)

class targetObject(GameObject):
    def __init__(self, x, y):
        super(targetObject, self).__init__(x, y)
        self.r = 20

    def display(self):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.r)
    
    def getPos(self):
        return (self.x, self.y)

targetGroup = pygame.sprite.Group()
boidsGroup = pygame.sprite.Group()

# init the player
zombieGroup = pygame.sprite.Group()
z = Zombie(400,400)
zombieGroup.add(z)
#z.loadPic('zombie.png')
for num in range(10):
    x = random.randint(-800, 1600)
    y = random.randint(-800, 1600)
    ob = targetObject(x, y)
    targetGroup.add(ob)


fps = 60
running = True
while running:
    time = clock.tick(fps)
    keysPressing = pygame.key.get_pressed()
    if keysPressing[pygame.K_UP]:
        for ob in targetGroup:
            ob.y += 10
            ob.updateRect()
        for nc in boidsGroup:
            nc.y += 10
            nc.updateRect()

    if keysPressing[pygame.K_DOWN]:
        for ob in targetGroup:
            ob.y -= 10
            ob.updateRect()
        for nc in boidsGroup:
            nc.y -= 10
            nc.updateRect()

    if keysPressing[pygame.K_LEFT]:
        for ob in targetGroup:
            ob.x += 10
            ob.updateRect()
        for nc in boidsGroup:
            nc.x += 10
            nc.updateRect()

    if keysPressing[pygame.K_RIGHT]:
        for ob in targetGroup:
            ob.x -= 10
            ob.updateRect()
        for nc in boidsGroup:
            nc.x -= 10
            nc.updateRect()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    detect = None
    detect = pygame.sprite.spritecollideany(z, targetGroup)
    if detect != None:                                          
        if pygame.sprite.collide_circle_ratio(20)(z, detect):
            bx, by = detect.getPos()
            newChild = ZomBoids(bx,by)
            boidsGroup.add(newChild)
            targetGroup.remove(detect) 

    screen.fill((255, 255, 255))
    z.display()
    for ob in targetGroup:
        ob.display()
    for child in boidsGroup:
        child.display()
    pygame.display.flip()
pygame.quit()