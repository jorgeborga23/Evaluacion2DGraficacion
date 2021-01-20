import numpy as np
import matplotlib.pyplot as plt


#Inicio 
plt.axis([0,160,0,160])
plt.axis("on")
plt.grid(True)



#Definimos un circulo con los valores de nuestro numero de control
ultimodigito = 3
xc= 40  #centro en el punto x
yc= 80	#centro en el punto y
r=ultimodigito * 5  #radio

p1=0*np.pi/180
p2=365*np.pi/180
dp=(p2-p1)/100
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1,p2+dp,dp):
    xp =xc+r*np.cos(p)
    yp= yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=(0/10,6/10,3/10), linewidth="2")
    xlast=xp
    ylast=yp



#Rectangulo 1
#Dibujamos un rectangulo con el largo = 2 * Diametro
px=np.array([40,100,100,40,40])
py=np.array([80,80,40,40,80])

plt.plot(px,py,linewidth=3,color=(0/10,6/10,3/10))




#Rectangulo 2
#Dibujamos un rectangulo con el largo = 2 * Diametro con la traslacion
trasx=30 #incremento en x
trasy=20 #incremento en y

px=np.array([40-trasx,100-trasx,100-trasx,40-trasx,40-trasx]) #Trasladamos el rectangulo restando el incremento en x
py=np.array([80+trasy,80+trasy,40+trasy,40+trasy,80+trasy]) #Trasladamos el rectangulo sumando el incremento en la y para que suba

plt.plot(px,py,linewidth=3,color=(0/10,6/10,3/10))



plt.title("Test 2D")
plt.show()