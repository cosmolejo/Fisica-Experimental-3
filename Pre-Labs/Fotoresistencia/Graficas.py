# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

datos1 = np.loadtxt('datos.txt')
datos1 = datos1[np.argsort(datos1[:, 0])]
fotor = datos1[:, 0]
led = datos1[:, 1]

fotor_lux = (fotor * fotor / 330) * 683
led_lux = (led * led / 330) * 683

t = []

for i in range(len(led)): t += [i * 0.5]

plt.plot(t, led_lux, 'ro-', label='led')
plt.plot(t, fotor_lux, 'bo-', label='fotoresistencia')
plt.ylim(0, 20)
plt.grid(True)
plt.legend(loc='upper left')
plt.xlabel('Tiempo [$s$]')
plt.ylabel('luminosidad [$lumens$]')
plt.title('lumen vs t')
plt.savefig('lumen_vs_t.png')

#plt.show()
'''
fotoresistor en el medio, led variando
datos2 = [[45, 0.0088],
          [70, 0.0206],
          [90, 0.039],
          [110, 0.029],
          [120, 0.029],
          [140, 0.01],
          [150, 0.01]]

'''
#led en el centro, fotoresistor variando
datos2 = np.array([
          [np.pi/9,0.0295],
          [np.pi/4., 0.0298],
          [(7*np.pi)/18., 0.0291],
          [np.pi/2., 0.0308],
          [(11*np.pi)/18., 0.0293],
          [(2*np.pi)/3., 0.0302],
          [(7*np.pi)/9., 0.0294],
          [(5*np.pi)/6., 0.0290],
          [(11*np.pi)/12,0.0295]])

for i in range(len(datos2)):
    datos2[i,1]= ((datos2[i,1]*datos2[i,1]) /330)*683.
    #print  datos2[i,1]

plt.cla()
ax = plt.subplot(111, projection='polar')
ax.plot(datos2[:,0], datos2[:,1],'o-')#ax.plot(theta, r)
ax.grid(True)
ax.set_rmax(0.003)
ax.set_rlabel_position(-22.5)
ax.set_title("lumen vs theta", va='bottom')
plt.savefig('lumen_vs_theta.png')
plt.show()



datos3=np.array([[1,0.088],[5,0.060],[8,0.048],[11,0.037],[14,0.030]])
datos3[:,1]= ((datos3[:,1]*datos3[:,1]) /330)*683.

plt.cla()
plt.plot(datos3[:,0],datos3[:,1],'o-',label='luminosidad')
#plt.ylim(0, 20)
plt.grid(True)
plt.legend(loc='upper right')
plt.xlabel('distancia [$cm$]')
plt.ylabel('luminosidad [$lumens$]')
plt.title('lumen vs distancia')
plt.savefig('lumen_vs_dist.png')
#plt.show()
