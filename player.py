import pygame
import random
from pygame.locals import *

#THE PLAYER
class Player(pygame.sprite.Sprite):
    images = []
    speed = 20
    bounce = 24
    gun_offset = -11

    #Init player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.screenrect = Rect(self.x, self.y, self.w, self.h)
        self.rect = self.image.get_rect(midbottom=self.screenrect.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    #Repaint on movement
    def move(self, direction):
        if direction: self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screenrect)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2)

    #Default aliens example shooter pos
    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top

    #Set pos of the player
    def setPos(self, x, y, w, h):
        self.screenrect = Rect(x, y, w, h)
        self.rect = self.image.get_rect(midbottom=self.screenrect.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    #Move stuff
    def moveUp(self, increment):
        if self.y > 0:
            self.setPos(self.x, self.y - increment, self.w, self.h)

    def moveDown(self, increment):
        if self.y < 500:
            self.setPos(self.x, self.y + increment, self.w, self.h)

    def moveLeft(self, increment):
        if self.x > 0:
            self.setPos(self.x - increment, self.y, self.w, self.h)

    def moveRight(self, increment):
        if self.x < 1000:
            self.setPos(self.x + increment, self.y, self.w, self.h)

#THE OBSTACLE STUFF
class Obstacle(pygame.sprite.Sprite):
    #Obstacle class
    obstaclesX = []
    obstaclesY = []
    obstacleNum = 0

    #Init the obstacles
    def __init__(self):
        obstacleNum = 0
        obstaclesX = []
        obstaclesY = []

    #Add a new obstacle in the defined position
    def addObstacle(self, x, y):
        self.obstacleNum = self.obstacleNum + 1

        self.x = x
        self.y = y

        self.obstaclesX.append(self.x)
        self.obstaclesY.append(self.y)

        print(self.obstaclesX, self.obstaclesY)

    #Draw stuff
    def DrawObstacles():
        #Canvas creation and drawing
        #IDK how to create a canvas but I think the final result should look like this:
        #Canvas.FillRect(obstacleX, obstacleY, 10, 10, Color.white)
        print("test")