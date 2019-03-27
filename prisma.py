#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:06:21 2019

@author: aluno
"""


from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random

h = 1

vertices_t = (
        
    
    ( 1, -1, 1), # 2
    ( 1, -1,-1), # 3
    (-1, -1,-1), # 4
    (-1, -1, 1), # 5        
    )

vertices_t2 = (
            
    ( 1, 3, 1), # 2
    ( 1, 3,-1), # 3
    (-1, 3,-1), # 4
    (-1, 3, 1), # 5        
    )

vertices_t3 = (            
    ( 1, -1, 1), # 2
    ( 1, -1,-1), # 3
    (-1, -1,-1), # 4
    (-1, -1, 1), # 5            
    
    ( 1, 3, 1), # 2
    ( 1, 3,-1), # 3
    (-1, 3,-1), # 4
    (-1, 3, 1), # 5        
    )


faces = (
   (0,1,2,3)    
    )
faces_t = ( # 3 pontos
    # (1,2,5,6), (1,4,5,8), (3,4,7,8),(2,3,6,7)
    (0,1,4,5), (0,3,4,7), (2,3,6,7),(1,2,5,6)
    
        
        )


cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Cubo():
    # Desenha o cubo ou outro poligono
    #glBegin(GL_QUAD_STRIP)
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        #for vertex in face:
            #glColor3fv(cores[vertex]) # vai interpolar para colorir faz degrade
        glVertex3fv(vertices_t[face])
        i = i+1
    glEnd()

    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        #for vertex in face:
            #glColor3fv(cores[vertex]) # vai interpolar para colorir faz degrade
        glVertex3fv(vertices_t2[face])
        i = i+1
    glEnd()
    
    glBegin(GL_QUAD_STRIP)
    i = 0
    for face in faces_t:
        glColor3fv(cores[i])        
        for vertice in face:        
            glVertex3fv(vertices_t3[vertice])
        i = i+1
    glEnd()
    
    # Desenha a Linha
    #glColor3fv((0,0,0)) # cor das linhas


def draw_sin(): # abacaxi
    # Apaga a tela e apaga o buffer de profundidade
    # buffer de profundidade serve para controlar a ordem dos objetos, saber o que vai imprimir ou nao
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # matriz de rotação primeiro parametro é a variação em x e depois em y
    #num = random.randrange(-100,100,180)
    glRotatef(2,1,0,0) # rotacao no eixo X
    #glRotatef(2,0,1,0) # rotacao no eixo Y
    #glRotatef(2,0,0,1) # rotacao no eixo Z
    #glRotated(12,35,15,15)
    Cubo()
    # Troca as areas de memoria - area que esta sendo apresentada e uam que desenha
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5,timer,0)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
# nome da janela
glutCreateWindow("#AGORAFOI")
glutDisplayFunc(draw_sin) # abacaxi
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
# Cor de fundo
glClearColor(0.,0.,0.,0.1)

# Perspectiva 
gluPerspective(100,800.0/600.0,0.1,50.0)
# posicao
glTranslatef(0.0,0.0,-8)
# Rotacionar
#glRotatef(1,45,1,50)

# Daqui a 50ms chame a funcao time o 1 é parametro mas n serve pra nada
glutTimerFunc(50,timer,1)
glutMainLoop()

