
import turtle
import random


#controlar parametros 
window = turtle.Screen()
#color de lienzo
window.bgcolor("black")
tortuga = turtle.Turtle()
#Se controla la velocidad, posición 
tortuga.speed(0)
tortuga.left(90)
#Función recursiva 
def dibujarArbol(tRama, tortuga):
    #Tamaño del trazo
    tortuga.pensize(tRama/15)
    #Condición para establecer la salida de la función recursiva
    if (tRama < 32):
        #Hojas 
        tortuga.dot(10,"Chartreuse")
        return
    #dibujar la rama
    tortuga.forward(tRama)
    #Indica la posición de la Izquierda 
    tortuga.left(20)
    #Porcentajes para establecer la asimetria a la derecha
    dibujarArbol(tRama*random.uniform(0.7,1), tortuga)
    tortuga.right(40)
    #Dibujar acorde a el numero al porcentaje aleatorio a la Izquierda
    dibujarArbol(tRama*random.uniform(0.8, 0.9), tortuga)
    tortuga.left(20)

    tortuga.backward(tRama)
#mover de posición sin que dibuje 
tortuga.penup()
#Posición de donde inicia la tortuga en eje Y
tortuga.setpos(0, -320)
#Volver a dibijar
tortuga.pendown()
#No mostrar la flecha que traza 
tortuga.hideturtle()
#Color de trazado del arbol
tortuga.color("MAGENTA")
#Longitud inicial
dibujarArbol(100, tortuga)
#cerrar al dar clic 
window.exitonclick()
