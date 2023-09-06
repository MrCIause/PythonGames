import pygame as pg
from sys import exit

pg.init()  # Important to start/initiate the pygame library, so it will work.
screen = pg.display.set_mode((800, 400))  # Creates a display.

pg.display.set_caption('Uncle Trump')  # Creates a caption name for the window.
icon = pg.image.load('Icon.png')  # Loads an image as "icon".
pg.display.set_icon(icon)  # Sets the "icon" var as window icon.

clock = pg.time.Clock()  # Sets the frameRate we want.

sky_surface = pg.image.load('graphics/Sky.png')
ground_surface = pg.image.load('graphics/ground.png')

test_font = pg.font.Font('font/Pixeltype.ttf', 50)  # First create a font with size.
text_surface = test_font.render('Score: ', False, 'black')  # Then set the surface.

while True:
    for event in pg.event.get():  # a for loop that checks for all possible events in pg library.
        if event.type == pg.QUIT:
            pg.quit()  # polar opposite of init() func, it kills the progress.
            exit()  # adding a system exit() func command improves it so the windows quits safely by making the while
            # loop false.
    # draw all our elements and update everything

    screen.blit(sky_surface, (0, 0))  # Block image transfer which places a surface on a surface.
    screen.blit(ground_surface, (0, 300))  # Sets the ground surface img.
    # Block images can overlap on each other by their order
    screen.blit(text_surface, (350, 50))
    pg.display.update()
    clock.tick(144)  # Sets the FPS for the game. need to account for pixel per second. 144 FPS = 144 pixelsPS.
