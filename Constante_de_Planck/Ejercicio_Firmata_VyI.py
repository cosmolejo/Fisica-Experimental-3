import numpy as np
import pyfirmata as pyF
from time import sleep
import os

file = open("datos_azul.dat", "w")

#####################################
## COMUNICACION
#####################################
port = 'com5'
board = pyF.Arduino(port)

it = pyF.util.Iterator(board)               #Estas lineas garantizan comunicacion con la tarjeta.
it.start()

######################################
##VECTORES
######################################
led=[1.6325,2.424,2.566,3.7095]
lamb=[1.10e6,1.60514e6,1.70648e6,2.14133e6]

volt_IR=[]
volt_red=[]
volt_blue=[]
volt_green=[]
volt_orange=[]


curr_IR=[]
curr_red=[]
curr_blue=[]
curr_green=[]
curr_orange=[]

#####################################
## LECTURA DE PINES
#####################################
a0 = board.get_pin('a:0:i')                 #a=analogo (d=digital), i=input (o=output,p=pwd)
a1 = board.get_pin('a:1:i') 
a2 = board.get_pin('a:2:i')
try:
    while True:
        p0 = a0.read()
        p1 = a1.read()
        p2 = a2.read()
        if (isinstance(p0,float) == True and  isinstance(p1,float) == True and  isinstance(p2,float) == True):     #Verifica si la variable es un float.    
            p0 = p0*5.0
            p1 = p1*5.0
            p2 = p2*5.0
            V=p0
            I=(p0-p1)/330.
            print('%f V , %f A' %(V,I))
            file.write('%f \t %f \n' %(V,I))
            sleep(1)                        #En este cod. las unidades son en segundos, no milisegundos.



except KeyboardInterrupt:                   #Nos permite salir del codigo mas facilmente.
    file.close() 
    board.exit()
    os._exit(0)
