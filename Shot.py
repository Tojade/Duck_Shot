"""
    Program......: Shot.py
    Author.......: Jaiden
    Date.........: 8/06/22
    Description..: Own Version of duck shot
"""

# Import modules
import pygame ,sys, random



# CLASS ====================================
# Name.........: Crosshair
# Description..: Creates/Sets mouse to the crosshair
# Syntax.......: Crosshair()
# ==========================================
class Crosshair(pygame.sprite.Sprite):
    def __init__(self,pic_path):
        super().__init__() # Calls class to use the attributes (multiple inheritance)
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect() # Draws an image around the rect
        self.gunshot = pygame.mixer.Sound('images/gunshot.wav')
    def update(self): # Class method that is pre defined in sprite class
        self.rect.center = pygame.mouse.get_pos()
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True) # Checks two sprites overlap by removing it




# CLASS ====================================
# Name.........: Target
# Description..: Sets target in different locations
# Syntax.......: Target()
# ==========================================
class Target(pygame.sprite.Sprite):
    def __init__(self,pic_path,x,y):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]


       


pygame.init()
clock = pygame.time.Clock()



# Create game canvas
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height), pygame.FULLSCREEN)
background = pygame.image.load('images/bg.png')
pygame.mouse.set_visible(False)
# Create a resize variable to scale the background image with the window
resized_background = pygame.transform.scale(background,(screen_width,screen_height))



# Creates an object inputing the values of the object (width,height,x,y,color)
crosshair = Crosshair('images/crosshair.png')
crosshair_group = pygame.sprite.Group() # Creating a sprite groups
crosshair_group.add(crosshair)


# Creates a target object
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('images/target.png',random.randrange(0,screen_width),random.randrange(0,screen_height)) # Uses randrange function to create random targets with the width and height of the screen
    target_group.add(new_target)   
    



# Loop the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # If the mouse is clicked the sound plays
            crosshair.shoot()


    pygame.display.flip()
    screen.blit(resized_background,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update() # Each object is called everytime the sprite is called
    clock.tick(80)
