import numpy as np
import matplotlib.pyplot as plt
import random


def f_dev(x):
    return (10*x)-20

def generarBinario(numero):
    return format(numero, '05b')
def generarPoblacion(n,maximo,minimo):
    return [random.sample(list(range(minimo,maximo)),n),[]]

def ordenarFitnnes(poblacionInicial,maximo):
    i=0
    while(i<maximo):
        j=0
        while(j<maximo):
            if((abs(poblacionInicial[1][i]))<(abs(poblacionInicial[1][j]))):
                aux=poblacionInicial[1][j]
                poblacionInicial[1][j]=poblacionInicial[1][i]
                poblacionInicial[1][i]=aux

                aux=poblacionInicial[0][j]
                poblacionInicial[0][j]=poblacionInicial[0][i]
                poblacionInicial[0][i]=aux
            j+=1
        i+=1
    return poblacionInicial


def reproducir(poblacionInicial,maximo,mutacion):
    supervivientes=poblacionInicial[0][:4]
    nuevaGeneracion=[]
    i=0
    print("Supervivientes de la generacion")
    print(supervivientes)
    while(i<maximo):
        r1=random.randint(0,3)
        r2=random.randint(0,3)
        hijo=""
        while(r1==r2):
            r1=random.randint(0,3)
            
        padre1=generarBinario(supervivientes[r1])
        padre2=generarBinario(supervivientes[r2])
        j=0;
        while(j<len(padre1)):
            if(mutacion<random.randint(0,50)):
                if(j==0):
                    aux=random.randint(0,1)
                    if(aux==0):
                        hijo+=str(aux)
                    else:
                        hijo+="-"
                else:
                    hijo+=str(random.randint(0,1))
                     
            else:
                if(random.randint(0,50)<=25):
                    hijo+=padre1[random.randint(1,len(padre1)-1)]
                else:
                    hijo+=padre2[random.randint(1,len(padre1)-1)]
            j+=1
        nuevaGeneracion.append(int(hijo,2))
        i+=1
    return nuevaGeneracion
    




mutacion=25
rangoSupervivencia=4;
poblacionInicial= generarPoblacion(8,20,-10)
i=1
index=-1
while(i<50):
    j=0
    r=0
    print("----Poblacion generacion "+str(i)+"-----")
    print(poblacionInicial[0])
    
    for x in poblacionInicial[0]:
        res=f_dev(x)
        poblacionInicial[1].append(res)

    if(0 in poblacionInicial[1]):
        print ("Cero encontrado")
        index= poblacionInicial[1].index(0)
        break

    ordenarFitnnes(poblacionInicial,8)
    poblacionInicial[0]=reproducir(poblacionInicial,8,mutacion)
    del poblacionInicial[1][:]
    i+=1
    
    
if(index!=-1):
    print("La funcion no es decreciente ni creciente cuando x vale "+ str(poblacionInicial[0][index]))
else:
    for x in poblacionInicial[0]:
        res=f_dev(x)
        poblacionInicial[1].append(res)
    ordenarFitnnes(poblacionInicial,8)
    print("El valor aproximado para que la funcion no sea creciente ni decreciente cuando x vale "+ str(poblacionInicial[0][0])+" que arroja el valor de "+ str(poblacionInicial[1][0]))

print("Ultima poblacion",poblacionInicial)



    
