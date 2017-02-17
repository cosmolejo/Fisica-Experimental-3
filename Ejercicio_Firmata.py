import numpy as np
import pyfirmata as pyF
from time import sleep
import os

#####################################
## COMUNICACION
#####################################
port = 'com4'
board = pyF.Arduino(port)

it = pyF.util.Iterator(board)               #Estas lineas garantizan comunicacion con la tarjeta.
it.start()


#####################################
## LECTURA DE PINES
#####################################
a0 = board.get_pin('a:0:i')                 #a=analogo (d=digital), i=input (o=output,p=pwd)

try:
    while True:
        p = a0.read()
        if isinstance(p,float) == True:     #Verifica si la variable es un float.    
            p = p*5.0
            print ('%.3f V' %p)
            sleep(1)                        #En este cod. las unidades son en segundos, no milisegundos.



except KeyboardInterrupt:                   #Nos permite salir del codigo mas facilmente.
    board.exit()
    os._exit()
