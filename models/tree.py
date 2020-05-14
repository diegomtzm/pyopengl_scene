from OpenGL.GL import *
from OpenGL.GLU import *

# tree vertex
tronco = [(0,0,0), (0,0.1,0), (0.1,0.1,0), (0.1,0,0), (0,0,0.75), (0,0.1,0.75), (0.1,0.1,0.75), (0.1,0,0.75)]
copa1 = [(-0.2,-0.2,0.6), (-0.2,0.2,0.6), (0.2,0.2,0.6), (0.2,-0.2,0.6), (-0.2,-0.2,0.9), (-0.2,0.2,0.9), (0.2,0.2,0.9), (0.2,-0.2,0.9)]
copa2 = [(-0.04,0.03,0.8), (-0.04,0.38,0.8), (0.31,0.38,0.8), (0.31,0.03,0.8), (-0.04,0.03,1.05), (-0.04,0.38,1.05), (0.31,0.38,1.05), (0.31,0.03,1.05)]
copa3 = [(-0.3,-0.05,0.75), (-0.3,0.45,0.75), (0.15,0.45,0.75), (0.15,-0.05,0.75), (-0.3,-0.05,1.1), (-0.3,0.45,1.1), (0.15,0.45,1.1), (0.15,-0.05,1.1)]
treeVerts = tronco + copa1 + copa2 + copa3

# tree faces
f_tronco = [(0,1,2,3), (4,5,6,7), (0,1,5,4), (0,3,7,4), (1,2,6,5), (3,2,6,7)]
f_copa1 = [(8,9,10,11), (12,13,14,15), (8,9,13,12), (8,11,15,12), (9,10,14,13), (11,10,14,15)]
f_copa2 = [(16,17,18,19), (20,21,22,23), (16,17,21,20), (16,19,23,20), (17,18,22,21), (19,18,22,23)]
f_copa3 = [(24,25,26,27), (28,29,30,31), (24,25,29,28), (24,27,31,28), (25,26,30,29), (27,26,30,31)]
treeFaces = f_tronco + f_copa1 + f_copa2 + f_copa3
copasFaces = f_copa1 + f_copa2 + f_copa3

# Function to draw the tree
def tree(translate=(0,0,0), rotate=(0,0,0), scale=(1,1,1)):
    # Push an pop matrix to apply transformations only to this object
    glPushMatrix()
    glRotate(-90,1,0,0)
    glRotate(10,0,0,1)
    glTranslate(translate[0],translate[1],translate[2])
    glScale(scale[0], scale[1], scale[2])
    
    glBegin(GL_QUADS)
    # set the color for the trunk
    glColor3fv((0.31,0.21,0.09))
    for troncoQuad in f_tronco:
        for troncoVertex in troncoQuad:
            glVertex3fv(tronco[troncoVertex])
    glColor3fv((0.28,0.41,0.11))
    for copasQuad in copasFaces:
        for copasVertex in copasQuad:
            glVertex3fv(treeVerts[copasVertex])
    glEnd()

    glPopMatrix()