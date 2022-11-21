from pandas import DataFrame as df
from tkinter import messagebox
import namegenerator
import random
import time
import csv
import os
import re
class Demostracion():
    #____________TIMSORT___________________
    def timsort(self,arr):
        self.__MINIMO = 32
        def encontrarMinimo(n):
            r=0
            while n>=self.__MINIMO:
                r|=n&1
                n>>=1
            return n+r

        def insertionSort(arr,left,right):
            for i in range(left+1,right+1):
                element=arr[i]
                j=i-1
                while element<arr[j] and j>=left:
                    arr[j+1]=arr[j]
                    j-=1
                arr[j+1]=element
            return arr

        def merge(arr,l,m,r):
            arr_lenght1=m-l+1
            arr_lenght2=r-m
            left=[]
            right=[]

            for i in range(0,arr_lenght1):
                left.append(arr[l+i])
            for i in range(0,arr_lenght2):
                right.append(arr[m+1+i])

            i=0
            j=0
            k=l

            while j<arr_lenght2 and i<arr_lenght1:
                if left[i]<=right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                k+=1
            while i<arr_lenght1:
                arr[k]=left[i]
                k+=1
                i+=1
            while j<arr_lenght2:
                arr[k]=right[j]
                k+=1
                j+=1

        def inicio(arr):
            n=len(arr)
            minRun=encontrarMinimo(n)

            for start in range(0,n,minRun):
                end=min(start+minRun-1,n-1)
                insertionSort(arr,start,end)
            size=minRun
            while size<n:
                for left in range (0,n,2*size):

                    mid=min(n-1,left+size-1)
                    right=min((left+2*size-1),(n-1))
                    merge(arr,left,mid,right)

                size=2*size
        inicio(arr)
    #____________TIMSORT___________________
    #____________QUICKSORT_________________
    def quicksort(self,arr):
        def partition(array, low, high):

            pivot = array[high]
            i = low - 1

            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])

            (array[i + 1], array[high]) = (array[high], array[i + 1])

            return i + 1

        def ordenar(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                ordenar(array, low, pi - 1)
                ordenar(array, pi + 1, high)

        def inicio(arr):
            size=len(arr)
            ordenar(arr,0,size-1)
        inicio(arr)
    #____________QUICKSORT_________________
    #____________BUBBLESORT________________
    def bubblesort(self,arr):
        for i in range(0,len(arr)-1):
            for j in range(len(arr)-1):
                if(arr[j]>arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr
    #____________BUBBLESORT________________

    def numeros_Aleatorios(self,cantDatos):
        datos=list()
        for i in range(0,cantDatos):
            datos.append(random.randint(-1000000,1000000))
        return datos

    def palabras_Aleatorias(self,cantDatos):
        datos=list()
        for i in range(0,cantDatos):
            datos.append(namegenerator.gen().split('-')[random.randint(0,2)])
        return datos

    def crearArchivos(self,cantArchivos)->bool:
        try:
            x=0
            while x<cantArchivos:
                s=random.randint(0,9)
                if s<5:
                    cantDatos=random.randint(1000,10000)
                    numeros=self.numeros_Aleatorios(cantDatos)
                    with open(f'Archivos entrada/Numeros_#{random.randint(1,1000)}_Dat{cantDatos}.csv','w') as csvfile:
                        writer=csv.writer(csvfile,lineterminator='\n')
                        for i in numeros:
                            writer.writerow([i])
                    csvfile.close()
                else:
                    cantDatos=random.randint(1000,10000)
                    palabras=self.palabras_Aleatorias(cantDatos)
                    with open(f'Archivos entrada/Palabras_#{random.randint(1,1000)}_Dat{cantDatos}.csv','w') as csvfile:
                        writer=csv.writer(csvfile,lineterminator='\n')
                        for i in palabras:
                            writer.writerow([i])
                    csvfile.close()
                x+=1
            return True
        except Exception as e:
            messagebox.showerror(message=f"No se encontro el directorio 'Archivos entrada'\n se creera inmediatamente en la carpeta de este programa{e}",title='Error')
            os.mkdir('Archivos entrada')
            self.crearArchivos(cantArchivos)

    def ordenarArchivos(self,ruta,flagBubble)->df:
        info=list()
        try:
            for filename in os.listdir(ruta):
                f=os.path.join(ruta,filename)
                if os.path.isfile(f) and filename.endswith(".csv"):
                    arrT=list()
                    with open(f,newline='') as csvfile:

                        for i in csv.reader(csvfile):
                            if re.match(re.compile(r'^\-?[1-9][0-9]*$'),i[0]):
                                arrT.append(int(i[0]))
                            else:
                                arrT.append(i[0])

                        c=len(arrT)
                        inicioB=0
                        finB=0
                        arrQ=arrT
                        arrB=arrT

                        inicioQ=time.time()
                        self.quicksort(arrQ)
                        finQ=time.time()

                        inicioT=time.time()
                        self.timsort(arrT)
                        finT=time.time()
                        if flagBubble:
                            inicioB=time.time()
                            self.bubblesort(arrB)
                            finB=time.time()

                        name=f.split('.')[0].split(str('\\'))
                        info.append((name.pop(),c,finT-inicioT,finQ-inicioQ,finB-inicioB))
                self.datosOrdenados(arrT)
            return df(sorted(info,key=lambda x:x[1]))
        except Exception as e:
            messagebox.showerror(message=f'error{e}',title='Error')
            return df()

    def datosOrdenados(self,arr)->None:
        try:
            with open(f'Archivos salida/Archivo_Ordenado#{len(arr)}.csv','w') as csvfile:
                writer=csv.writer(csvfile,lineterminator='\n')
                for i in arr:
                    writer.writerow([i])
                csvfile.close()
        except Exception as e:
            messagebox.showerror(message=f"No se encontro el directorio 'Archivos salida' se creara en el mismo direcotrio de este programa\n{e}",title='Alerta')
            os.mkdir('Archivos salida')
            self.datosOrdenados(arr)

    def datosAleatorios(self,numerosNombres,flagBubble,cantDatos,cantItera,avance)->df:
        x=0
        files=[]
        cant=[]
        timeT=[]
        timeQ=[]
        timeB=[]
        while x<cantItera:
            if numerosNombres:
                arrT=self.numeros_Aleatorios(cantDatos)
            else:
                arrT=self.palabras_Aleatorias(cantDatos)
            inicioB=0
            finB=0
            arrQ=arrT
            arrB=arrT
            inicioQ=time.time()
            self.quicksort(arrQ)
            finQ=time.time()

            inicioT=time.time()
            self.timsort(arrT)
            finT=time.time()

            if flagBubble:
                inicioB=time.time()
                self.bubblesort(arrB)
                finB=time.time()

            files.append('-----------------')
            cant.append(cantDatos)
            timeT.append(round(finT-inicioT,13))
            timeQ.append(round(finQ-inicioQ,13))
            timeB.append(round(finB-inicioB,13))
            cantDatos+=avance
            x+=1
            self.datosOrdenados(arrT)
        return df({'Archivo':files,'Cantidad Datos':cant,'Tiempo Tim':timeT,'Tiempo Quick':timeQ,'Tiempo Bubble':timeB})
