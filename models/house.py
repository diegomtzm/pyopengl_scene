from OpenGL.GL import *
from OpenGL.GLU import *
from models.texture import *

# house vertex
v_base = [(4, 4, 0),   (7, 4, 0),   (4, 7, 0),   (7, 7, 0),   (4, 5.5, 0),   (3.7, 5, 0),   (3.7, 4.5, 0),
            (4, 4, 2.5), (7, 4, 2.5), (4, 7, 2.5), (7, 7, 2.5), (4, 5.5, 2.5), (3.7, 5, 2.5), (3.7, 4.5, 2.5)]
            
v_facade = [(3.9, 3.9, 2.5), (7.1, 3.9, 2.5), (3.9, 7.1, 2.5), (7.1, 7.1, 2.5), (3.9, 5.5, 2.5), (3.6, 5, 2.5), (3.6, 4.5, 2.5),
            (3.9, 3.9, 2.6), (7.1, 3.9, 2.6), (3.9, 7.1, 2.6), (7.1, 7.1, 2.6), (3.9, 5.5, 2.6), (3.6, 5, 2.6), (3.6, 4.5, 2.6)]
            
v_base2 = [(4, 4, 2.6), (7, 4, 2.6), (4, 7, 2.6), (7, 7, 2.6), (4, 5.5, 2.6), (3.7, 5, 2.6), (3.7, 4.5, 2.6),
            (4, 4, 5.1), (7, 4, 5.1), (4, 7, 5.1), (7, 7, 5.1), (4, 5.5, 5.1), (3.7, 5, 5.1), (3.7, 4.5, 5.1)]
            
v_ceil = [(3.8, 3.8, 5.1), (7.2, 3.8, 5.1), (3.8, 7.2, 5.1), (7.2, 7.2, 5.1), (3.8, 5.5, 6.5), (7.2, 5.5, 6.5)]

houseVerts = v_base + v_facade + v_base2 + v_ceil

# house faces
f_base    = [(0, 1, 3, 2, 4, 5, 6), (0, 1, 8, 7), (0, 6, 13, 7), (5, 6, 13, 12), (4, 5, 12, 11), (2, 3, 10, 9), (7, 8, 10, 9, 11, 12, 13), (1, 8, 10, 3), (0, 7, 9, 2)]
f_facade  = [tuple(map(lambda x: x + 14, y)) for y in f_base]
f_base2   = [tuple(map(lambda x: x + 14, y)) for y in f_facade]
f_ceil    = [(42, 43, 45, 44), (42, 43, 47, 46), (47, 46, 44, 45)]
f_ceil2   = [(42, 44, 46)]#, (43, 45, 47)]

# Function to draw the house
def house(translate=(0,0,0), scale=(1,1,1), base=(0,0,1), roof=(0,0,0), house='house4'):
    # House Base
    glPushMatrix()

    imgPath = 'textures/' + house + '/house1.jpg'
    texture_id = read_texture(imgPath)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-90,1,0,0)
    glRotate(90,0,0,1)
    glTranslate(translate[0],translate[1],translate[2])
    glScale(scale[0], scale[1], scale[2])

    glBegin(GL_POLYGON)
    for base_face in f_base:
        n = 0
        for v in base_face:
            if n == 0:
                xv = 0.0
                yv = 1.0
            if n == 1:
                xv = 1.0
                yv = 1.0
            if n == 2:
                xv = 1.0
                yv = 0.0
            if n == 3:
                xv = 0.0
                yv = 0.0
            glTexCoord2f(xv,yv); glVertex3fv(houseVerts[v])
            n += 1
    glEnd()

    glPopMatrix()

    # House Facade
    glPushMatrix()

    imgPath = 'textures/' + house + '/house2.jpg'
    texture_id = read_texture(imgPath)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-90,1,0,0)
    glRotate(90,0,0,1)
    glTranslate(translate[0],translate[1],translate[2])
    glScale(scale[0], scale[1], scale[2])

    glBegin(GL_POLYGON)
    for facade_face in f_facade:
        n = 0
        for v in facade_face:
            if n == 0:
                xv = 0.0
                yv = 1.0
            if n == 1:
                xv = 1.0
                yv = 1.0
            if n == 2:
                xv = 1.0
                yv = 0.0
            if n == 3:
                xv = 0.0
                yv = 0.0
            glTexCoord2f(xv,yv); glVertex3fv(houseVerts[v])
            n += 1
    glEnd()

    glPopMatrix()

    # House Top
    glPushMatrix()

    imgPath = 'textures/' + house + '/house3.jpg'
    texture_id = read_texture(imgPath)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-90,1,0,0)
    glRotate(90,0,0,1)
    glTranslate(translate[0],translate[1],translate[2])
    glScale(scale[0], scale[1], scale[2])

    glBegin(GL_POLYGON)
    for base2_face in f_base2:
        n = 0
        for v in base2_face:
            if n == 0:
                xv = 1.0
                yv = 1.0
            if n == 1:
                xv = 1.0
                yv = 0.0
            if n == 2:
                xv = 0.0
                yv = 0.0
            if n == 3:
                xv = 0.0
                yv = 1.0
            glTexCoord2f(xv,yv); glVertex3fv(houseVerts[v])
            n += 1
    glEnd()

    glPopMatrix()

    # House Roof
    glPushMatrix()

    glRotate(-90,1,0,0)
    glRotate(90,0,0,1)
    glTranslate(translate[0],translate[1],translate[2])
    glScale(scale[0], scale[1], scale[2])

    glBegin(GL_POLYGON)
    glColor3fv(roof)
    for ceil_face in f_ceil:
        n = 0
        for v in ceil_face:
            # if n == 1:
            #     xv = 1.0
            #     yv = 1.0
            # if n == 2:
            #     xv = 1.0
            #     yv = 0.0
            # if n == 3:
            #     xv = 0.0
            #     yv = 0.0
            # if n == 0:
            #     xv = 0.0
            #     yv = 1.0
            # glTexCoord2f(xv,yv); glVertex3fv(houseVerts[v])
            # n += 1
            glVertex3fv(houseVerts[v])
    glEnd()
    glPopMatrix()

    # House Roof 2
    glPushMatrix()

    imgPath = 'textures/' + house + '/house4.png'
    texture_id = read_texture(imgPath)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-90,1,0,0)
    glRotate(90,0,0,1)
    glTranslate(translate[0],translate[1],translate[2])
    glScale(scale[0], scale[1], scale[2])

    glBegin(GL_POLYGON)
    for ceil_face in f_ceil2:
        n = 0
        for v in ceil_face:
            if n == 0:
                xv = 0.0
                yv = 0.0
            if n == 1:
                xv = 1.0
                yv = 0.0
            if n == 2:
                xv = 0.5
                yv = 1.0
            glTexCoord2f(xv,yv); glVertex3fv(houseVerts[v])
            n += 1
            glVertex3fv(houseVerts[v])
    glEnd()
    glPopMatrix()