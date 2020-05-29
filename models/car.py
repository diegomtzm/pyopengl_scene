from OpenGL.GL import *
from OpenGL.GLU import *
from models.texture import *

# car vertex
car_v = [(0,0,0),(0,0,0.7),(0.5,0,0.7),(0.75,0,1.2),(1.75,0,1.2),(1.75,0,0.7),(2.5,0,0.7),(2.5,0,0),
         (0,0.8,0),(0,0.8,0.7),(0.75,0.8,0.7),(0.75,0.8,1.2),(1.75,0.8,1.2),(1.75,0.8,0.7),(2.5,0.8,0.7),(2.5,0.8,0)]
         
wheels_v = [(0.37,-0.1,-0.2),(0.37,-0.1,0.2),(0.77,-0.1,0.2),(0.77,-0.1,-0.2),(0.37,0,-0.2),(0.37,0,0.2),(0.77,0,0.2),(0.77,0,-0.2),
            (0.37,0.9,-0.2),(0.37,0.9,0.2),(0.77,0.9,0.2),(0.77,0.9,-0.2),(0.37,0.8,-0.2),(0.37,0.8,0.2),(0.77,0.8,0.2),(0.77,0.8,-0.2),
            (1.73,-0.1,-0.2),(1.73,-0.1,0.2),(2.13,-0.1,0.2),(2.13,-0.1,-0.2),(1.73,0,-0.2),(1.73,0,0.2),(2.13,0,0.2),(2.13,0,-0.2),
            (1.73,0.9,-0.2),(1.73,0.9,0.2),(2.13,0.9,0.2),(2.13,0.9,-0.2),(1.73,0.8,-0.2),(1.73,0.8,0.2),(2.13,0.8,0.2),(2.13,0.8,-0.2)]

carVerts = car_v + wheels_v

# car faces
car_f_pol = [(0,1,2,3,4,5,6,7), (8,9,10,11,12,13,14,15)]
car_f_quad = [(0,1,9,8),(1,2,10,9),(3,4,12,11),(5,6,14,13),(6,7,15,14)]
car_glass = [(2,3,11,10),(4,5,13,12)]
wheels_f = [(16,17,18,19), (16,17,21,20),(17,18,22,21),(18,19,23,22),
            (32,33,34,35), (32,33,37,36),(33,34,38,37),(34,35,39,38)]
wheels_f_2 = [(24,25,26,27), (24,25,29,28),(25,26,30,29),(26,27,31,30),
              (40,41,42,43), (40,41,45,44),(41,42,46,45),(42,43,47,46)]

carFaces = car_f_pol + car_f_quad + wheels_f + wheels_f_2

colors = [(0,0,1), (0,1,0), (1,0,0), (1,0,1), (0,1,1), (1,1,0), (1,1,1), (0,0,0)]

# Function to draw the car
def car(translate=(0,0,0), scale=(1,1,1), color=(0,0,1), texture='red'):
    glPushMatrix()

    texture_id = read_texture('textures/car/tire.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-95, 1, 0, 0)
    glRotate(4,0,1,0)
    glScale(scale[0], scale[1], scale[2])
    glTranslate(translate[0], translate[1], translate[2])

    glBegin(GL_QUADS)
    glColor3fv((0,0,0))
    for wheelQuad in wheels_f_2:
        n = 0
        for wheelVertex in wheelQuad:
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
            glTexCoord2f(xv,yv); glVertex3fv(carVerts[wheelVertex])
            n += 1
    glEnd()

    glPopMatrix()

    glPushMatrix()
    imgPath = 'textures/car/' + texture + '.jpg'
    texture_id = read_texture(imgPath)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-95, 1, 0, 0)
    glRotate(4,0,1,0)
    glScale(scale[0], scale[1], scale[2])
    glTranslate(translate[0], translate[1], translate[2])

    glBegin(GL_POLYGON)
    glColor3fv(color)
    n = 0
    for carVertex in car_f_pol[1]:
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
        glTexCoord2f(xv,yv); glVertex3fv(carVerts[carVertex])
        n += 1
    glEnd()

    glPopMatrix()

    glPushMatrix()

    texture_id = read_texture('textures/car/glass.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-95, 1, 0, 0)
    glRotate(4,0,1,0)
    glScale(scale[0], scale[1], scale[2])
    glTranslate(translate[0], translate[1], translate[2])

    glBegin(GL_QUADS)
    glColor3fv((0.15,0.15,0.15))
    for glassQuad in car_glass:
        n = 0
        for glassVertex in glassQuad:
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
            glTexCoord2f(xv,yv); glVertex3fv(carVerts[glassVertex])
            n += 1
    glEnd()

    glPopMatrix()

    glPushMatrix()
    imgPath = 'textures/car/' + texture + '.jpg'
    texture_id = read_texture(imgPath)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-95, 1, 0, 0)
    glRotate(4,0,1,0)
    glScale(scale[0], scale[1], scale[2])
    glTranslate(translate[0], translate[1], translate[2])

    glBegin(GL_POLYGON)
    glColor3fv(color)
    n = 0
    for carVertex in car_f_pol[0]:
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
        glTexCoord2f(xv,yv); glVertex3fv(carVerts[carVertex])
        n += 1
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(color)
    for carQuad in car_f_quad:
        n = 0
        for carVertex in carQuad:
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
            glTexCoord2f(xv,yv); glVertex3fv(carVerts[carVertex])
            n += 1
    glEnd()

    glPopMatrix()

    glPushMatrix()

    texture_id = read_texture('textures/car/tire.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-95, 1, 0, 0)
    glRotate(4,0,1,0)
    glScale(scale[0], scale[1], scale[2])
    glTranslate(translate[0], translate[1], translate[2])

    glBegin(GL_QUADS)
    glColor3fv((0,0,0))
    for wheelQuad in wheels_f:
        n = 0
        for wheelVertex in wheelQuad:
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
            glTexCoord2f(xv,yv); glVertex3fv(carVerts[wheelVertex])
            n += 1
    glEnd()

    glPopMatrix()