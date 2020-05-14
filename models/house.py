from OpenGL.GL import *
from OpenGL.GLU import *

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
f_ceil    = [(42, 43, 45, 44), (42, 43, 47, 46), (47, 46, 44, 45), (42, 44, 46), (43, 45, 47)]

print(f_base2)

houseFaces = f_base + f_facade + f_base2 + f_ceil

# Function to draw the house
def house():
    glBegin(GL_QUADS)
    for houseQuad in houseFaces:
        for houseVertex in houseQuad:
            glVertex3fv(houseVerts[houseVertex])
    glEnd()
    