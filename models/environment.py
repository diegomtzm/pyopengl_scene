from OpenGL.GL import *
from OpenGL.GLU import *
from models.texture import *

# street vertex
street_vertices = [(-5,0.1,5),(5,0.1,5),(5,0.1,-5),(-5,0.1,-5)]
ground_vertices = [(-5,0,5),(5.2,-0.33,5),(-5,0.6,5)]

# sky vertex
sky2_vertices = [(-5,0,5),(-5,5,5),(-5,5,-5),(-5,0,-5)]
sky1_vertices = [(-5,1,2),(-5,4,2),(-5,4,-5),(-5,1,-5)]

# sidewalks vertex
sidewalk_vertices = [(-5,0.15,5),(5,0.15,5),(5,0.15,3),(-5,0.15,3)]
sidewalk2_vertices = [(-5,0.15,-5),(5,0.15,-5),(5,0.15,-2),(-5,0.15,-2)]

def street():
    # Push an pop matrix to apply transformations only to this object
    glPushMatrix()

    texture_id = read_texture('textures/environment/street.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-5,0,0,1)

    glBegin(GL_QUADS)
    glColor3fv((0.45,0.49,0.52))
    n = 0
    for vertex in street_vertices:
        if n == 0:
            xv = 0.0
            yv = 1.0
        if n == 1:
            xv = 0.0
            yv = 0.0
        if n == 2:
            xv = 1.0
            yv = 0.0
        if n == 3:
            xv = 1.0
            yv = 1.0
        glTexCoord2f(xv,yv); glVertex3fv(vertex) 
        n += 1
    glEnd()

    glPopMatrix()

    glPushMatrix()

    texture_id = read_texture('textures/environment/street.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_TRIANGLES)
    glColor3fv((0.14,0.16,0.2))
    n = 0
    for vertex in ground_vertices:
        if n == 0:
            xv = 0.0
            yv = 1.0
        if n == 1:
            xv = 0.0
            yv = 0.0
        if n == 2:
            xv = 1.0
            yv = 0.0
        if n == 3:
            xv = 1.0
            yv = 1.0
        glTexCoord2f(xv,yv); glVertex3fv(vertex) 
        n += 1
    glEnd()

    glPopMatrix()

def sky():
    glPushMatrix()

    texture_id = read_texture('textures/environment/sky.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(90,0,1,0)

    glBegin(GL_QUADS)
    glColor3fv((0.32, 0.52, 0.58))
    n = 0
    for verts in sky1_vertices:
        if n == 0:
            xv = 0.0
            yv = 1.0
        if n == 1:
            xv = 0.0
            yv = 0.0
        if n == 2:
            xv = 1.0
            yv = 0.0
        if n == 3:
            xv = 1.0
            yv = 1.0
        glTexCoord2f(xv,yv); glVertex3fv(verts)
        n += 1
    glEnd()

    glPopMatrix()

    glPushMatrix()

    texture_id = read_texture('textures/environment/sky.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glColor3fv((0.32, 0.52, 0.6))
    n = 0
    for verts in sky2_vertices:
        if n == 0:
            xv = 0.0
            yv = 1.0
        if n == 1:
            xv = 0.0
            yv = 0.0
        if n == 2:
            xv = 1.0
            yv = 0.0
        if n == 3:
            xv = 1.0
            yv = 1.0
        glTexCoord2f(xv,yv); glVertex3fv(verts)
        n += 1
    glEnd()

    glPopMatrix()

def sideWalks():
    # Push an pop matrix to apply transformations only to this object
    glPushMatrix()

    texture_id = read_texture('textures/environment/sidewalk.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glRotate(-5,0,0,1)

    glBegin(GL_QUADS)
    glColor3fv((0.53, 0.5, 0.43))
    n = 0
    for vertex in sidewalk_vertices:
        if n == 0:
            xv = 0.0
            yv = 1.0
        if n == 1:
            xv = 0.0
            yv = 0.0
        if n == 2:
            xv = 1.0
            yv = 0.0
        if n == 3:
            xv = 1.0
            yv = 1.0
        glTexCoord2f(xv,yv); glVertex3fv(vertex)
        n += 1
    n = 0
    for vertex in sidewalk2_vertices:
        if n == 0:
            xv = 0.0
            yv = 1.0
        if n == 1:
            xv = 0.0
            yv = 0.0
        if n == 2:
            xv = 1.0
            yv = 0.0
        if n == 3:
            xv = 1.0
            yv = 1.0
        glTexCoord2f(xv,yv); glVertex3fv(vertex)
        n += 1
    glEnd()

    glPopMatrix()

def environment():
    sky()
    street()
    sideWalks()