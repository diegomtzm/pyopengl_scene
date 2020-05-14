import pygame as pg
from pygame.locals import *

from models.tree import *
from models.house import *
from models.car import *
from models.environment import *
from models.stairs import *

def main():
    # initialization of the pygame modules
    pg.init()
    # define the window size
    display = (800, 600)
    # specify that we use OpenGL with double buffering
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    # This is what will represent the camera's sight
    # Params: Field of view, Aspect ratio, min draw distance and max draw distance
    gluPerspective(60, (display[0]/display[1]), 0.1, 50.0)

    # Zoom the camara out in z axis to see the object
    glTranslatef(0.4, -1, -13)
    glRotate(10, 1, 0, 0)

    def handleEvents():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    glRotate(-10, 0, 0, 1)
                if event.key == pg.K_RIGHT:
                    glRotate(10, 0, 0, 1)
                if event.key == pg.K_UP:
                    glRotate(-10, 1, 0, 0)
                if event.key == pg.K_DOWN:
                    glRotate(10, 1, 0, 0)
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1)
                if event.button == 5:
                    glTranslatef(0,0,-1)

    while True:
        handleEvents()
        # Clears the buffers to repaint the canvas
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # draw models into the scene
        environment()
        tree(translate=(3.2,1.6,0))
        tree(translate=(0.6,2.4,0.15))
        tree(translate=(-2.4,3.3,0.3))
        car(translate=(-5.8,-3.5,0), scale=(0.75,0.75,0.75), color=(0.64, 0, 0.14))
        car(translate=(-1.8,-3.65,0), scale=(0.75,0.75,0.75), color=(0.17,0.32,0.49))
        car(translate=(2.3,-3.65,0), scale=(0.75,0.75,0.75), color=(0.87, 0.58, 0.24))
        
        # Updates the window with the active buffer contents
        pg.display.flip()
        pg.time.wait(1)

main()
