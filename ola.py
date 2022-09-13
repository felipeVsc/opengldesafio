from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

listaEntrada = [[270,300],[270,300],[270,300],[270,300],[270,300]]

def quadrado1():
    glClear(GL_COLOR_BUFFER_BIT);
#1
    
    primeiroQ = listaEntrada[0]
    segundoQ = listaEntrada[1]
    terceiroQ = listaEntrada[2]
    quartoQ = listaEntrada[3]
    quintoQ = listaEntrada[4]


    glColor3f(1,0,0)
    glBegin( GL_QUADS ) 
    glVertex2f( 10.0, primeiroQ[0] ) 
    glVertex2f( 40.0, primeiroQ[0] ) 
    glVertex2f( 40.0, primeiroQ[1] ) 
    glVertex2f( 10.0, primeiroQ[1] ) 
    glEnd()
#2
    glColor3f(1,1,0)
    glBegin( GL_QUADS ) 
    glVertex2f( 50.0, segundoQ[0] ) 
    glVertex2f( 80.0, segundoQ[0] ) 
    glVertex2f( 80.0, segundoQ[1] ) 
    glVertex2f( 50.0, segundoQ[1] )  
    glEnd()
#3
    glColor3f(1,1,1)
    glBegin( GL_QUADS ) 
    glVertex2f( 90.0, terceiroQ[0] ) 
    glVertex2f( 120.0, terceiroQ[0] ) 
    glVertex2f( 120.0, terceiroQ[1] ) 
    glVertex2f( 90.0, terceiroQ[1] )  
    glEnd()
#4
    glColor3f(0,1,0)
    glBegin( GL_QUADS ) 
    glVertex2f( 130, quartoQ[0] ) 
    glVertex2f( 160.0, quartoQ[0] ) 
    glVertex2f( 160.0, quartoQ[1] ) 
    glVertex2f( 130.0, quartoQ[1] )  
    glEnd()
#5
    glColor3f(0,1,1)
    glBegin( GL_QUADS ) 
    glVertex2f( 170.0, quintoQ[0] ) 
    glVertex2f( 200.0, quintoQ[0] ) 
    glVertex2f( 200.0, quintoQ[1] ) 
    glVertex2f( 170.0, quintoQ[1] )  
    glEnd()
    

def mostrar():
    quadrado1()
    glFlush()


def ola():
    contador = 0
    while True:

        if listaEntrada[contador-1][0]>270:
            # é porque ta alto, logo desce        
            listaEntrada[contador-1][0] = 270
            listaEntrada[contador-1][1] = 300

        listaEntrada[contador][0]+=30
        listaEntrada[contador][1]+=30

        mostrar()

        if contador==4:
            contador = 0
        else:
            contador+=1
      
        time.sleep(.3)
def inicializajanela():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(400, 250)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Ola")
    gluOrtho2D(0, 500, 0, 500)

def main():
    inicializajanela()
    ola()
    

main()