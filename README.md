# Duck_Shot
This is a python based game using the module pygame, random, and sys. This basic shooting game was inspired by the carnival duck shooting games with a rifle, instead of the rifle, a crosshair is replaced. This game was made by stratch using object oriented programming, using Multilevel inheritance to inherit sprite attributes, as well as well as loading images of the sprites. However, the background and images were used by Kenney Vleugels.

## Problems that occured
The problems that occured during this project were sound mixer files. The pygame mixer.Sound() function cannot use every sound wav, to fix this requirement, use another sound wav or use a long ogg file play length depending on the sound. To do this, make a loop usually at the end of your program (while loop). Another issue was the background image sizing. The background image was too small for the window/canvas it was being displayed, this came problematic due to the sprite not being placed on the image. To fix this, using the pygame.transform.scale() method allowed the image to resized based on the canvas width and height.

## Required
Importing the pygame module is required for python IDLE that was used. To import the module go to the command line and type "pip install pygame". Otherwise using a different idle will automatically have pygame installed such as Visual Studio Code and Pycharm. 

## Installing the game 
To install the game on your idle simply download all the content (images, main file) and open them up using the preferred development environment.

## Installing the game 
To install the game on your idle simply download all the content (images, main file) and open them up using the preferred development environment.

![alt text](https://github.com/Tojade/Duck_Shot/blob/main/Duck_Shoot.png)

