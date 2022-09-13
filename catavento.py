from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

listaCores = [
    [1.0,1.0,1.0],
    [0.0,0.0,1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0]
    ]

def flordeabril():
    glClear(GL_COLOR_BUFFER_BIT)

    corBaixo = listaCores[0]
    corEsquerdo = listaCores[1]
    corCima = listaCores[2]
    corDireito = listaCores[3]


# caule
    glColor3f (1.0, 1.0, .0);
    glBegin(GL_POLYGON)
    glVertex3f(249.0, 250.0, -1.0)
    glVertex3f(251.0, 250.0, -1.0)
    glVertex3f(249.0, 100.0, -1.0)
    glVertex3f(251.0, 100.0, -1.0)
    glEnd()
    

    # baixo
    x,y,z = corBaixo
    glColor3f(x,y,z)
    glBegin(GL_TRIANGLES)
    glVertex2f(250.0, 250.0)
    glVertex2f(230.0, 200.0)
    glVertex2f(270.0, 200.0)
    glEnd()

    # direita
    x,y,z = corDireito
    glColor3f(x,y,z)
    glBegin(GL_TRIANGLES)
    glVertex2f(250.0, 250.0)
    glVertex2f(300.0, 230.0)
    glVertex2f(300.0, 270.0)
    glEnd()

    # cima
    x,y,z = corCima
    glColor3f (x,y,z)
    glBegin(GL_TRIANGLES)
    glVertex2f(250.0, 250.0)
    glVertex2f(230.0, 300.0)
    glVertex2f(270.0, 300.0)
    glEnd()

    # esquerda
    x,y,z = corEsquerdo
    glColor3f(x,y,z)
    glBegin(GL_TRIANGLES)
    glVertex2f(250.0, 250.0)
    glVertex2f(200.0, 270.0)
    glVertex2f(200.0, 230.0)
    glEnd()

    glFlush()

def trocaCores():
    
    while True:

        temp0 = listaCores[0]
        listaCores[0] = listaCores[1]
        listaCores[1] = listaCores[2]
        listaCores[2] = listaCores[3]
        listaCores[3] = temp0
        flordeabril()
        time.sleep(.3)

def init():
  
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glMatrixMode(GL_PROJECTION)
    glOrtho(0.0, 500.0, 0.0, 400.0, -1.0, 1.0)

def main():
    glutInit();
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 400)
    glutInitWindowPosition (200, 200)
    glutCreateWindow("Flor de Abril")

    init()
    trocaCores()

main()