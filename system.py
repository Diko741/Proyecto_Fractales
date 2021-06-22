#Importamos pygame, sys y math
import pygame
import sys
import math
#Declaramos clase LSystem   
class LSystem():
    #Definimos lo que vamos a usar
    def __init__(self,axioma,reglas,dtheta,comenzar,longitud,proporcion):
        self.sentencia=axioma
        self.reglas=reglas
        self.theta=math.pi/2 #90 grados 
        self.dtheta=dtheta
        self.comenzar=comenzar
        self.x, self.y = comenzar
        self.longitud= longitud
        self.proporcion=proporcion
        self.posiciones =[]

    def __str__(self):
        return self.sentencia
        
    def generar(self):
        self.x, self.y = self.comenzar
        self.theta = math.pi/2 
        self.longitud *= self.proporcion
        nuevoStr =""
        for caracter in self.sentencia:
            mapeado = caracter
            try:
                mapeado=self.reglas[caracter]
            except:
                pass
            nuevoStr += mapeado
        self.sentencia = nuevoStr  
        #print('SENTENCIA',self.sentencia)
    def draw(self,screen):
        color=0
        decolorar=255/len(self.sentencia)
        for caracter in self.sentencia:
            if caracter=='F' or caracter=='G': #Significa avanzar
                x2= self.x - self.longitud * math.cos(self.theta)
                y2= self.y - self.longitud * math.sin(self.theta)
                #pygame.draw.line(superficie,color,inicio_posicion,final_posicion)
                pygame.draw.line(screen,(255-color,125 +decolorar/2,125+decolorar/2),(self.x,self.y),(x2,y2))
                self.x, self.y= x2, y2
                print('X:',self.x,'Y:',self.y,'THETA:', self.theta)
            elif caracter=='+': #Gira a la izquierda del angulo
                self.theta += self.dtheta
            elif caracter=='-': #Gira a la derecha del angulo
                self.theta -= self.dtheta
            elif caracter=='[': #Guardar los valores actuales de posicion y angulo
                self.posiciones.append({'x': self.x,'y': self.y,'theta': self.theta})
            elif caracter==']': #
                #Elimina y retorna un elemento de la lista posiciones en posision
                posicion= self.posiciones.pop() 
                #Se restauran las posiciones y angulo
                self.x, self.y, self.theta = posicion['x'], posicion['y'],posicion['theta']
            color+=decolorar
    
def main():
    #Lee tipo de archivo .txt a correr
    l_sys_text=sys.argv[1]
    #Iniciamos pygame
    pygame.init()
    #Ingresamos desde consola el tamanio de la pantalla
    size= int(sys.argv[2]),int(sys.argv[3])
    #Posicion en x,y ingresada desde consola donde comenzara a dibujar
    comenzar=int(sys.argv[4]), int(sys.argv[5])
    #Longitud con la cual va a crecer el fractal
    longitud = int(sys.argv[6])
    #Proporcion en que crecera conforme a la longitud 
    proporcion = float(sys.argv[7])
    system=None
    #Abre el archivo .txt como f
    with open(l_sys_text) as f:
        #Lee el axioma 
        axioma=f.readline()
        #El numero de reglas
        numReglas= int(f.readline())
        #Se agregan las reglas del .txt a reglas
        reglas={}
        #Recorre el numReglas 
        for i in range(numReglas):
            #Formamos una lista con las reglas separada por un espacio
            regla=f.readline().split(' ')
            #Posicionamos las reglas
            reglas[regla[0]]=regla[1]
        #Se lee en radianes el angulo del fractal
        dTheta=math.radians(int(f.readline()))
        #Le decimos a Windows que use nuestra clase LSystem junto con sus parametros
        system=LSystem(axioma,reglas, dTheta,comenzar,longitud,proporcion)
    #Ponemos la pantalla en visualizacion junto con su nombre
    screen= pygame.display.set_mode(size)
    pygame.display.set_caption("FRACTALES")

    corriendo=True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo=False
            if event.type ==pygame.MOUSEBUTTONDOWN:
                screen.fill((0,0,0))
                system.draw(screen)
                system.generar()
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

    