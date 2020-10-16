import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return (x*x*x*x/12)-(x*x*x/2)+(x*x)+(10)
def f1_dev1(x):
    return (x*x*x/3)-(3*x*x/2)+(2*x)
def f1_dev2(x):
    return (x*x)-(3*x)+(2)

x= np.linspace(-2,3,num=51)
#[-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5],
i=0 #para moverme entre las posiciones
hubo=0;
print(x)
for x_ in x:
   if(i!=0 and i!=len(x)-1):
       if(f1_dev2(x_)==0):
           ant=x[i-1];
           sig=x[i+1];
           if((f1_dev2(ant)<0 and f1_dev2(sig)>0) or (f1_dev2(ant)>0 and f1_dev2(sig)<0)):
             print("Punto de inflexion en: ", x_)
             print(" f'' de ",round(ant,1)," que es el Punto anterior: ",round(f1_dev2(ant),2))
             print(" f'' de ",sig," que es el Punto anterior: ",round (f1_dev2(sig),2))
             plt.scatter(x_, f1(x_), s=30)
             
             hubo=1;
   i=1+i          

if(hubo==0):
    print("No hubo puntos de inflexion")
y=f1(x)
plt.plot(x,y)
plt.show()
