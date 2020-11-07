import numpy as np
import matplotlib.pyplot as plt
import math

def f1(x):
    return (x*x)-(math.sin(x))
def f1_dev1(x):
    return (2*x)-(math.cos(x))
def f1_dev2(x):
    return (math.sin(x))+(2)
def f1_dev2_0(x):
    return 0;

#busqueda exhaustiva
x=-1.6;
h=0.1;
bandera=0;
while(x<=1.6):
    #print(x)
    
    if(x!=-1.6 and x!=1.6):
        if(f1_dev2(x)==0):
            ant=f1_dev2(x-h)
            sig=f1_dev2(x+h)
            if((ant<0 and sig>0) or (ant>0 and sig<0)):
                print("Punto de inflexion en ", x);
                print("Punto anterio siguiente ", sig);
                print("Punto anterior  ", ant);
                plt.scatter(x, f1(x), s=30)
                bandera=1
            
    x+=h
    

if(bandera==0):
    print("No hubo puntos de inflexion")


#----Seccion dorada-------

tau=2-1.618033988
epsilon=1e-6
a=0
b=1
a1=0
a2=0
i=0
while 1:
    a1=a*(1-tau)+b*(tau)
    a2=a*(tau)+b*(1-tau)
    if(f1(a1)>f1(a2)):
        a=a1
    else:
        b=a2
    if(np.abs(f1(a1)-f1(a2))>epsilon):
        i+=1
    else:
        break

plt.scatter(a1, f1(a1), s=30)
print("--Seccion dorada--")
print("Numero de iteraciones ocupadas con el metodo de la seccion dorada",i)
print("El minimo de la funcion esta en ",a1,f1(a1))

"---Metodo de newton----"
i=0
x0=0
while 1:
    x1=x0 - f1_dev1(x0)/f1_dev2(x0)
    x0=x1
    if(np.abs(f1_dev1(x1))>epsilon):
        i+=i+1;
    else:
        break;
print("--Metodo de newton--")
print("Numero de iteraciones ocupadas con el metodo de newton",i)

print("El minimo de la funcion esta en",x1,f1(x1))



x= np.linspace(0,1,num=10)
y= np.vectorize(f1) 
plt.plot(x,y(x))
plt.show()
