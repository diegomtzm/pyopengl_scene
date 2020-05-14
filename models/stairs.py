from OpenGL.GL import *
from OpenGL.GLU import *

# stairs vertex
walls_v = [(0,0,0),(0,0,0.6),(0.2,0,0.6),(1.2,0,1.5),(1.2,0,0),
         (0,-0.1,0),(0,-0.1,0.6),(0.2,-0.1,0.6),(1.2,-0.1,1.5),(1.2,-0.1,0),
         (0,1,0),(0,1,0.6),(0.2,1,0.6),(1.2,1,1.5),(1.2,1,0),
         (0,0.9,0),(0,0.9,0.6),(0.2,0.9,0.6),(1.2,0.9,1.5),(1.2,0.9,0)]
stairs_v = [(0.2,0,0),(0.2,0,0.15),(0.4,0,0.15),(0.4,0,0.3),(0.6,0,0.3),(0.6,0,0.45),(0.8,0,0.45),(0.8,0,0.6),(1,0,0.6),(1,0,0.75),(1.2,0,0.75),
          (0.2,0.9,0),(0.2,0.9,0.15),(0.4,0.9,0.15),(0.4,0.9,0.3),(0.6,0.9,0.3),(0.6,0.9,0.45),(0.8,0.9,0.45),(0.8,0.9,0.6),(1,0.9,0.6),(1,0.9,0.75),(1.2,0.9,0.75)]

stairsVerts = walls_v + stairs_v

# stairs faces
wall1_f = [(0,1,2,3,4),(5,6,7,8,9),(0,5,6,1),(6,7,2,1),(7,8,3,2)]
wall2_f = [(10,11,12,13,14),(15,16,17,18,19),(10,15,16,11),(16,17,12,11),(17,18,13,12)]
stairs_f = [(20,21,32,31),(21,22,33,32),(22,23,34,33),(23,24,35,34),(24,25,36,35),(25,26,37,36),(26,27,38,37),(27,28,39,38),(28,29,40,39), (29,30,41,40), (30,41,19,4)]

stairsFaces = wall1_f + wall2_f + stairs_f

# Function to draw the stairs
def stairs():
    glBegin(GL_POLYGON)
    glColor3fv((1,0,0))
    for wallsQuad in wall2_f:
        for wallsVertex in wallsQuad:
            glVertex3fv(walls_v[wallsVertex])
    glEnd()

    glBegin(GL_POLYGON)
    glColor3fv((0,0,1))
    for wallsQuad in wall1_f:
        for wallsVertex in wallsQuad:
            glVertex3fv(walls_v[wallsVertex])
    glEnd()

    glBegin(GL_QUADS)   
    glColor3fv((0,1,0))
    for stairsQuad in stairs_f:
        for stairsVertex in stairsQuad:
            glVertex3fv(stairsVerts[stairsVertex])
    glEnd()