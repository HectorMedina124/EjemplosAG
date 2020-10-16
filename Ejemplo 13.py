import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return (x*x*x*x/4)-(9*x*x/2)
def f1_dev1(x):
    return (x*x*x)-(9*x)
def f1_dev2(x):
    return (3*x*x)-9
def f1_dev1Factor(x):
    return x*(x+3)*(x-3)

x= np.linspace(-3,3,num=13)
i=0 #para moverme entre las posiciones
hubo=0;
y=f1(x)
plt.plot(x,y)
desc=0;
asc=0;

print(x)
for x_ in x:
       if(f1_dev1(x_)==0):
           print("Punto critico encontrado ",x_)
           print("Coordenadas completas en (",x_,",",f1(x_),")")
           plt.scatter(x_, f1(x_), s=30)
           
           
for x_ in x:
        if(f1_dev1(x_)<0 and asc==0):
            desc=1
        if(f1_dev1(x_)<0 and asc==1):
            print("es concava hacia abajo")
            break;
        if(f1_dev1(x_)>0 and desc==0):
            asc=1;
        if(f1_dev1(x_)>0 and desc==1):
              print("es concava hacia arriba")
              break;
            
plt.show()

