import pygame
import random
import time
from pygame.locals import *

#THE PLAYER
class Player(pygame.sprite.Sprite):
    pygame.init()

    images = []
    speed = 20
    bounce = 24
    gun_offset = -11

    size = [1000, 500]
    screen = pygame.display.set_mode(size)

    white = (255, 128, 0)

    font1 = pygame.font.SysFont("calibri",40)

    clock = pygame.time.Clock()

    playerW = 50
    playerH = 50

    #Init player
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 50
        self.h = 50
        self.clock.tick(60)
        self.drawSensor()

    def drawPlayer(self, px, py, pw, ph, pcolor, pwidth):
        pygame.draw.rect(self.screen, pcolor, [px, py, pw, ph], pwidth)
        pygame.display.update()

    def drawSensor(self):
        pygame.draw.line(self.screen, self.white, [self.x + self.playerW / 2, self.y], [self.x + self.playerW / 2, self.y - 100], 5)
        pygame.display.update()

    #Repaint on movement
    def move(self, direction):
        self.drawPlayer(self.x, self.y, self.playerW, self.playerH, self.white, 5)
        pygame.display.update()
        self.drawSensor()
        pygame.display.update()

        text = self.font1.render("TextA", True,(255,255,255))
        self.screen.blit(text, [0, 0])

        print(self.x, self.y, self.w, self.h)

    #Default aliens example shooter pos
    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top

    #Set pos of the player
    def setPos(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        pygame.display.update()
    
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