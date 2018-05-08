import pygame

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
    def DrawObstacles(self):
        #Canvas creation and drawing
        #IDK how to create a canvas but I think the final result should look like this:
        #Canvas.FillRect(obstacleX, obstacleY, 10, 10, Color.orange)
        print("test")