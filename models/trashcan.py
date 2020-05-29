from OpenGL.GL import *
from OpenGL.GLU import *
from models.texture import *

#trashcan vertex
trash = [(0,0,0), (0,0.5,0), (0.5,0.5,0), (0.5,0,0), (0,0,0.6), (0,0.5,0.6), (0.5,0.5,0.6), (0.5,0,0.6)]
trashVerts = trash

# trashcan faces
f_trash = [(0,1,2,3),(0,1,5,4),(0,3,7,4), (1,2,6,5), (3,2,6,7)]
f_top = [(4,5,6,7)]
trashFaces = f_trash
topFaces = f_top

# Function to draw the trashcan
def trashcan(translate=(0,0,0), rotate=(0,0,0), scale=(1,1,1)):
    # Push an pop matrix to apply transformations only to this object
    glPushMatrix()

    texture_id = read_texture('textures/blue.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-90,1,0,0)
    glRotate(10,0,0,1)
    glTranslate(translate[0],translate[1],translate[2])
    glScale(scale[0], scale[1], scale[2])
    
    glBegin(GL_QUADS)

    # set the color for the trash
    glColor3fv((0.4,0.4,0.4))
    for trashQuad in f_trash:
        n = 0
        for trashVertex in trashQuad:
            if n == 0:
                xv = 0.0
                yv = 0.0
            if n == 1:
                xv = 1.0
                yv = 0.0
            if n == 2:
                xv = 1.0
                yv = 1.0
            if n == 3:
                xv = 0.0
                yv = 1.0
            glTexCoord2f(xv,yv); glVertex3fv(trash[trashVertex])
            n += 1

    glColor3fv((0.2,0.2,0.2))
    for topQuad in topFaces:
        for trashVertex in topQuad:
            glVertex3fv(trashVerts[trashVertex])
    
    glEnd()

    glPopMatrix()