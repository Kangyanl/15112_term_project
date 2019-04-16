import pygame

# This GameObject class is referenced from TA's Website
#https://qwewy.gitbooks.io/pygame-module-manual/tutorials/using-sprites/making-a-game-with-sprites.html
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(GameObject, self).__init__()
        # x, y define the center of the object
        self.x, self.y = x, y
        #self.baseImage = image.copy()  # non-rotated version of image
        self.image = None
        self.picW = 50
        self.picH = 50
        self.updateRect()

    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        self.rect = pygame.Rect(self.x - self.picW / 2, self.y - self.picH / 2, \
            self.picW, self.picH)

    def loadPic(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.picW, self.picH))

    def display(self, screen):
        screen.blit(self.image, (self.x - self.picW, self.y - self.picH))


# Class of player
class Zombie(GameObject):

    def __init__(self, x, y):
        super(Zombie, self).__init__(x, y)
        self.v = 10

# Class of boids
class ZomBoids(Zombie):

    def __init__(self, x, y):
        super(ZomBoids, self).__init__(x, y)
        self.r = 20
        self.v = 10

    def display(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.r)
    
    def dodgeMove(self, other):
        #if(pygame.sprite.collide_circle_ratio(1.2)(self, other)):
        tempX = self.x - other.x
        tempY = self.y - other.y
        normalize = (tempX ** 2 + tempY ** 2) ** 0.5
        if normalize <= 80:
            offsetX = (tempX / normalize) * self.v
            offsetY = (tempY / normalize) * self.v
            print(offsetX,offsetY)
            self.x += int(offsetX)
            self.y += int(offsetY)

    def follow(self, other):
        tempX = other.x - self.x
        tempY = other.y - self.y
        normalize = (tempX ** 2 + tempY ** 2) ** 0.5
        if normalize >= 200:
            offsetX = (tempX / normalize) * self.v
            offsetY = (tempY / normalize) * self.v
            self.x += int(offsetX)
            self.y += int(offsetY)



# Class of passager
class passager(GameObject):
    def __init__(self, x, y):
        super(passager, self).__init__(x, y)
        self.r = 20

    def getPos(self):
        return (self.x, self.y)

    def display(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.r)



