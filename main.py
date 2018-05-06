#Main file of the digital simulation


import random, os.path

#import basic pygame modules
import pygame
from player import Player
from obstacle import Obstacle
from pygame.locals import *

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#Get he rect of the screen
SCREENRECT = Rect(0, 0, 1000, 500)
print(SCREENRECT.midbottom)

main_dir = os.path.split(os.path.abspath(__file__))[0]

#Load image
def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

#Load "images"
def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

#Irrelevent stuff
class dummysound:
    def play(self): pass

#♪♫ Load sounds like music ♪♫
def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()

#Main stuff
def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    #Load images, assign to sprite classes
    #(do this before the classes are used, after screen setup)
    img = load_image('player1.gif')
    Player.images = [img, pygame.transform.flip(img, 1, 0)]

    #decorate the game window
    icon = pygame.transform.scale(Player.images[0], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Gym 10.0')
    pygame.mouse.set_visible(0)

    #create the background, tile the bgd image
    bgdtile = load_image('background.gif')
    background = pygame.Surface(SCREENRECT.size)

    #Render the background
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        for y in range(0, SCREENRECT.height, bgdtile.get_height()):
            background.blit(bgdtile, (x, y))
    
    #Blit the background
    screen.blit(background, (0,0))
    pygame.display.flip()

    #assign default groups to each sprite class
    all = pygame.sprite.RenderUpdates()
    Player.containers = all
    player = Player()
    obs = Obstacle()
    player.setPos(SCREENRECT.width / 2, SCREENRECT.height / 2, 10, 10)

    #While EVERYTIME
    while True:
        pressed = pygame.key.get_pressed()
        #get input
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == pressed and event.key == K_ESCAPE):
                    return
        keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        #update all the sprites
        all.update()

        #handle player input

        #Set the direction
        direction = keystate[K_RIGHT] - keystate[K_LEFT]

        #Get agent input
        speed = 2
        if(pressed[pygame.K_UP]):
            player.moveUp(speed)
        if(pressed[pygame.K_DOWN]):
            player.moveDown(speed)
        if(pressed[pygame.K_LEFT]):
            player.moveLeft(speed)
        if(pressed[pygame.K_RIGHT]):
            player.moveRight(speed)
        if(pressed[pygame.K_SPACE]):
            obs.addObstacle(random.randint(0, 1000), random.randint(0, 500))
        player.move(direction)

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

    #Setup the mixer
    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()



#call the "main" function if running this script
if __name__ == '__main__': main()

