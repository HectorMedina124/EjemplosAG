import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x*x*x*x
def f1_dev1(x):
    return 4*x*x*x
def f1_dev2(x):
    return 12*x*x
def f1_dev2_0(x):
    return 0;

x= np.linspace(-4,4,11)
i=0 #para moverme entre las posiciones
desc=0;
asc=0;
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
            
            
          

y=f1(x)
plt.plot(x,y)
plt.show()
