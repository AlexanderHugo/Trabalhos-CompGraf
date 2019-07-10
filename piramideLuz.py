from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def calculaNormalFace(face):
    x = 0
    y = 1
    z = 2
    v0 = face[x]
    v1 = face[y]
    v2 = face[z]
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = math.sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])

    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)


def piramidePoligono(rBase, nBase ,altura):
    glBegin(GL_POLYGON)


    resolution = nBase
    height = [0,altura,0]
    radius = rBase

    for vertex in range(0, resolution):     
        glVertex3fv([math.cos(2* math.pi * vertex/resolution * radius), -1 , math.sin(2 * math.pi * vertex/resolution * radius)])

    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)

    glColor3fv(cores[vertex%len(cores)])
    glVertex3fv(height)    
	
    lista = []
    for vertex in range(0, resolution+1):
        f1 = math.cos(2* math.pi * vertex/resolution * radius)
        f2 = -1
        f3 = math.sin(2 * math.pi * vertex/resolution) * radius
        lista.append( (f1,f2,f3) )
        if len(lista) == 3:
            glNormal3fv(calculaNormalFace(lista))


        glColor3fv(cores[vertex%len(cores)])     
        glVertex3fv([math.cos(2* math.pi * vertex/resolution * radius), -1 , math.sin(2 * math.pi * vertex/resolution) * radius])

    glEnd()

                

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    piramidePoligono(1, 30, 1)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def init():
    mat_ambient = (0.5, 0.0, 0.5, 1)
    #mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (0.1, 0.5, 0.8, 1.0)
    mat_specular = (0, 0, 0, 0)
    mat_shininess = (50,)
    light_position = (1, 0.5, 0.3,0.05)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDENBASE")
init()
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(40,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
