from OpenGL.GL import *
from OpenGL.GLU import *

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
    glRotate(-5,0,0,1)

    glBegin(GL_QUADS)
    glColor3fv((0.45,0.49,0.52))
    for vertex in street_vertices:
        glVertex3fv(vertex) 
    glEnd()

    glPopMatrix()

    glBegin(GL_TRIANGLES)
    glColor3fv((0.14,0.16,0.2))
    for vertex in ground_vertices:
        glVertex3fv(vertex)
    glEnd()

def sky():
    glPushMatrix()
    glRotate(90,0,1,0)

    glBegin(GL_QUADS)
    glColor3fv((0.32, 0.52, 0.58))
    for verts in sky1_vertices:
        glVertex3fv(verts)
    glEnd()

    glPopMatrix()

    glBegin(GL_QUADS)
    glColor3fv((0.32, 0.52, 0.6))
    for verts in sky2_vertices:
        glVertex3fv(verts)
    glEnd()

def sideWalks():
    # Push an pop matrix to apply transformations only to this object
    glPushMatrix()
    glRotate(-5,0,0,1)

    glBegin(GL_QUADS)
    glColor3fv((0.53, 0.5, 0.43))
    for vertex in sidewalk_vertices:
        glVertex3fv(vertex)
    for vertex in sidewalk2_vertices:
        glVertex3fv(vertex)
    glEnd()

    glPopMatrix()

def environment():
    sky()
    street()
    sideWalks()