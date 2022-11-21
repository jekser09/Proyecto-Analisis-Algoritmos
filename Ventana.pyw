from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import BOLD
from Demostracion import *
from tkinter import ttk
from tkinter import *
import webbrowser as wb


class Ventana():

    def __init__(self) -> None:

        #Crear ventana donde se posicionaran todos los componentes
        self.__ventana=Tk()
        self.__ventana.title("Analisis de algoritmos")
        self.__ventana.resizable(False,False)
        self.__ventana.iconbitmap("Iconos/ordenado.ico")
        self.__wventana=int(self.__ventana.winfo_screenwidth()*0.75)
        self.__hventana=int(self.__ventana.winfo_screenheight()*0.90)
        self.__pwidth = (self.__ventana.winfo_screenwidth()//2)-(self.__wventana//2)
        self.__pheight = (self.__ventana.winfo_screenheight()//2)-(self.__hventana//2)
        #Crear menubar
        self.__menubar=Menu(self.__ventana)
        self.__ventana.config(menu=self.__menubar)
        self.__mInicio=Menu(self.__menubar,tearoff=0)
        self.__mInicio.add_command(label='<--',command=lambda:[self.cambiar_Frames(1)])
        self.__mInicio.add_separator()
        self.__mSort=Menu(self.__menubar,tearoff=0)
        self.__mSort.add_command(label='Ordenar',command=lambda:[self.cambiar_Frames(2)])
        self.__menubar.add_cascade(label='Inicio',menu=self.__mInicio)
        self.__mInicio.add_command(label='Salir',command=self.__ventana.quit)
        self.__menubar.add_cascade(label='Demostracion',menu=self.__mSort)
        self.ventana_Inicio()
        self.ventana_Sort()
        self.cambiar_Frames(1)
        self.__ventana.geometry(f'{self.__wventana}x{self.__hventana}+{self.__pwidth}+{self.__pheight}')
        self.__ventana.mainloop()

    def ventana_Inicio(self)->None:
        self.__iniImg1=PhotoImage(file="Iconos/ordenado.png")
        self.__timImg=PhotoImage(file="Iconos/timsort.png")
        self.__quickImg=PhotoImage(file="Iconos/quicksort.png")
        self.__bubbleImg=PhotoImage(file="Iconos/bubblesort.png")

        #Paneles Tim
        self.__iniFrame=Frame(relief='groove',bd=6,bg='#908174',width=self.__wventana,height=self.__hventana)
        self.__iniFrame.columnconfigure(0,weight=7)
        self.__iniFrame.columnconfigure(1,weight=1)
        self.__iniFrame.columnconfigure(2,weight=7)
        self.__iniFrame.rowconfigure(0,weight=1)
        self.__iniFrame.rowconfigure(1,weight=1)
        self.__iniFrame.rowconfigure(2,pad=55,weight=1)
        self.__iniFrame.rowconfigure(3,weight=1)
        self.__iniFrame.rowconfigure(4,weight=1)
        self.__iniFrame.rowconfigure(5,weight=1)
        self.__iniFrame.rowconfigure(6,weight=1)
        self.__iniFrame.rowconfigure(7,weight=1)
        self.__iniFrame.rowconfigure(8,weight=1)

        self.__titulo=Label(self.__iniFrame,text='Analisis de algoritmos',bg='#A9DE18',font=('Cambria',20,BOLD),)
        self.__titulo.grid(row=0,column=0,columnspan=3,sticky=S+N+E+W)

        self.__subTitulo=Label(self.__iniFrame,text='Alagoritmos de ordenamiento',bg='#A9DE18',font=('Cambria',20,BOLD))
        self.__subTitulo.grid(row=1,column=0,columnspan=3,sticky=S+N+E+W)

        self.__lblImg1=Label(self.__iniFrame,image=self.__iniImg1,bg='#908174')
        self.__lblImg1.rowconfigure(0,weight=1)
        self.__lblImg1.grid(row=2,column=0,sticky=S+N+E+W)
        self.__lblImg2=Label(self.__iniFrame,image=self.__iniImg1,bg='#908174')
        self.__lblImg2.rowconfigure(0,weight=1)
        self.__lblImg2.grid(row=2,column=2,sticky=S+N+E+W)

        self.__frames = [PhotoImage(file="Gif/sort.gif", format='gif -index %i' %(i)) for i in range(99)]
        self.__iniCanvas=Canvas(self.__iniFrame,width=450,height=260)
        self.__iniCanvas.grid(row=2,column=1,sticky=EW)

        Label(self.__iniFrame,text='TimSort',relief='solid',bd=1,bg='#0EE7EB',font=('Cambria',10,BOLD)).grid(row=3,column=0,sticky=S+N+E+W)
        Label(self.__iniFrame,text='QuickSort',relief='solid',bd=1,bg='#0EE7EB',font=('Cambria',10,BOLD)).grid(row=3,column=1,sticky=S+N+E+W)
        Label(self.__iniFrame,text='BubbleSort',relief='solid',bd=1,bg='#0EE7EB',font=('Cambria',10,BOLD)).grid(row=3,column=2,sticky=S+N+E+W)

        Button(self.__iniFrame,image=self.__timImg,bg='#C4AE9C',bd=2,command=lambda:[wb.open(r'https://docs.google.com/presentation/d/1Fzru9vMW9SrbZx2Ep7Yv2TM14xN862Dd/edit#slide=id.p1',new=1,autoraise=True)]).grid(row=4,column=0,rowspan=2,sticky=S+N+E+W)
        Button(self.__iniFrame,image=self.__quickImg,bg='#C4AE9C',bd=2,command=lambda:[wb.open(r'https://www.genbeta.com/desarrollo/implementando-el-algoritmo-quicksort',new=1,autoraise=True)]).grid(row=4,column=1,rowspan=2,sticky=S+N+E+W)
        Button(self.__iniFrame,image=self.__bubbleImg,bg='#C4AE9C',bd=2,command=lambda:[wb.open(r'https://www.include-poetry.com/Code/C++/Metodos/Ordenamientos/Bubble-sort/',new=1,autoraise=True)]).grid(row=4,column=2,rowspan=2,sticky=S+N+E+W)

        Label(self.__iniFrame,text='Universidad Central',bg='#F5C40F',font=('Cambria',16,BOLD)).grid(row=6,column=0,columnspan=3,sticky=S+N+E+W)
        Label(self.__iniFrame,text='Autor: Johand Esteban Castro Rodriguez',bg='#F5C40F',font=('Cambria',16,BOLD)).grid(row=7,column=0,columnspan=3,sticky=S+N+E+W)
        Label(self.__iniFrame,text='Docente: Giovanny Alexander Briceño Riveros',bg='#F5C40F',font=('Cambria',16,BOLD)).grid(row=8,column=0,columnspan=3,sticky=S+N+E+W)
        Label(self.__iniFrame,text='16/11/2022',bg='#F5C40F',font=('Cambria',14,BOLD)).grid(row=9,column=0,columnspan=3,sticky=S+N+E+W)

        self.__ventana.after(0,self.update_Ini,0)

    def update_Ini(self,ind)->None:
            frame = self.__frames[ind]
            ind += 1
            if ind == 99:
                ind = 0
            self.__iniCanvas.create_image(0, 0, image=frame, anchor=NW)
            self.__ventana.after(120, self.update_Ini, ind)

    def ventana_Sort(self)->None:

        self.__imgPlay=PhotoImage(file='Iconos/play.png')
        self.__imgCrear=PhotoImage(file='Iconos/crear.png')
        self.__imgSubir=PhotoImage(file='Iconos/subir.png')
        self.__imgDecor1=PhotoImage(file='Iconos/formacion.png')
        self.__imgDecor2=PhotoImage(file='Iconos/grafico.png')
        self.__imgDecor3=PhotoImage(file='Iconos/tabla.png')

        self.__cantDatos=IntVar()
        self.__cantDatos.set(1000)
        self.__iteraciones=IntVar()
        self.__iteraciones.set(10)
        self.__avance=IntVar()
        self.__avance.set(20)
        self.__checkNum=BooleanVar()
        self.__checkNum.set(True)
        self.__checkPal=BooleanVar()
        self.__checkPal.set(False)

        self.__sortFrame=Frame(relief='groove',bd=6,bg='#C2705C',width=self.__wventana,height=self.__hventana)
        self.__sortFrame.grid_propagate(False)
        self.__sortFrame.rowconfigure(0,weight=1)
        self.__sortFrame.rowconfigure(1,weight=1)
        self.__sortFrame.rowconfigure(2,weight=1)
        self.__sortFrame.rowconfigure(3,weight=1)
        self.__sortFrame.rowconfigure(4,weight=1)
        self.__sortFrame.rowconfigure(5,weight=1)
        self.__sortFrame.rowconfigure(6,weight=1)
        self.__sortFrame.rowconfigure(7,weight=1)
        self.__sortFrame.rowconfigure(8,weight=1)
        self.__sortFrame.rowconfigure(9,weight=1)
        self.__sortFrame.rowconfigure(10,weight=1)
        self.__sortFrame.rowconfigure(11,weight=1)
        self.__sortFrame.rowconfigure(12,weight=1)
        self.__sortFrame.rowconfigure(13,weight=1)
        self.__sortFrame.rowconfigure(14,weight=1)
        self.__sortFrame.rowconfigure(15,weight=1)
        self.__sortFrame.rowconfigure(16,weight=1)
        self.__sortFrame.rowconfigure(17,weight=1)
        self.__sortFrame.rowconfigure(18,weight=1)
        self.__sortFrame.columnconfigure(2,weight=1)
        self.__sortFrame.columnconfigure(3,weight=1)
        self.__sortFrame.columnconfigure(4,weight=1)
        Label(self.__sortFrame,text="DATOS ALEATORIOS",bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=0,column=0,columnspan=2)
        Label(self.__sortFrame,text="_Cantidad Datos_",bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=1,column=0,columnspan=2)
        Entry(self.__sortFrame,textvariable=self.__cantDatos,bg='#764437',relief='groove',font=('Cambria',12,BOLD)).grid(row=2,column=0,columnspan=2)
        Label(self.__sortFrame,text="_Iteraciones_",bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=3,column=0,columnspan=2)
        Entry(self.__sortFrame,textvariable=self.__iteraciones,bg='#764437',relief='groove',font=('Cambria',12,BOLD)).grid(row=4,column=0,columnspan=2)
        Label(self.__sortFrame,text="_Avance_",bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=5,column=0,columnspan=2)
        Entry(self.__sortFrame,textvariable=self.__avance,bg='#764437',relief='groove',font=('Cambria',12,BOLD)).grid(row=6,column=0,columnspan=2)
        Label(self.__sortFrame,text="_Tipo De Datos_",bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=7,column=0,columnspan=2)
        Checkbutton(self.__sortFrame,text="Numeros",command=lambda:[self.check_Bot(1)],bg='#C2705C',font=('Cambria',12,BOLD),variable=self.__checkNum,).grid(row=8,column=0)
        Checkbutton(self.__sortFrame,text="Palabras",command=lambda:[self.check_Bot(0)],bg='#C2705C',font=('Cambria',12,BOLD),variable=self.__checkPal,).grid(row=8,column=1)
        Button(self.__sortFrame,image=self.__imgPlay,command=lambda:[self.pintar_Grafica(True)],bg='#CE8573',bd=2).grid(row=9,column=0,columnspan=2,sticky=EW)
        ttk.Separator(self.__sortFrame,orient='horizontal',).grid(row=10,column=0,columnspan=2,sticky=EW)
        Label(self.__sortFrame,text="ARCHIVOS",bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=11,column=0,columnspan=2)
        Label(self.__sortFrame,text="_Crear Archivos_",bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=12,column=0,columnspan=2)
        self.__spnCantArchivos=ttk.Spinbox(self.__sortFrame,state='readonly',from_=1,to=1000,font=('Cambria',10,BOLD))
        self.__spnCantArchivos.set(1)
        self.__spnCantArchivos.grid(row=13,column=0,columnspan=2)
        Button(self.__sortFrame,image=self.__imgCrear,command=lambda:[self.crear_Csvs()],bg='#CE8573',bd=2).grid(row=14,column=0,columnspan=2,sticky=EW)
        Label(self.__sortFrame,text="_Cargar Archivos_",bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=15,column=0,columnspan=2)
        Button(self.__sortFrame,image=self.__imgSubir,bg='#CE8573',bd=2,command=self.dir_carpeta).grid(row=16,column=0,columnspan=2,sticky=EW)
        Button(self.__sortFrame,image=self.__imgPlay,command=lambda:[self.pintar_Grafica(False)],bg='#CE8573',bd=2).grid(row=17,column=0,columnspan=2,sticky=EW)
        Label(self.__sortFrame,image=self.__imgDecor1,bg='#C2705C',font=('Cambria',15,BOLD)).grid(row=18,column=0,columnspan=2)
        Button(self.__sortFrame,image=self.__imgDecor2,command=lambda:[self.graf_Tabla(1)],bg='#CE8573',bd=2,).grid(row=18,column=2,padx=5,sticky=EW)
        ttk.Separator(self.__sortFrame,orient='vertical',).grid(row=18,column=3,sticky=NS)
        Button(self.__sortFrame,image=self.__imgDecor3,command=lambda:[self.graf_Tabla(0)],bg='#CE8573',bd=2,).grid(row=18,column=4,padx=5,sticky=EW)
        #Grafica
        self.fig=Figure()
        self.plot=self.fig.add_subplot()
        self.plot.set_title(r"|TimSort:$O(n*\log{n})$|QuickSort: $O(n*\log{n})$|BubbleSort: $O(n^{2})$|"+
                            "\n(Verde)----------(Morado)----------(Rojo)")
        self.plot.set_ylabel('Tiempo Ordenamiento [ms]')
        self.plot.set_xlabel('Cantidad Datos')
        self.plot.grid()
        self.canvas=FigureCanvasTkAgg(self.fig,master=self.__sortFrame,)
        self.canvas.get_tk_widget().grid(row=0,column=2,columnspan=3,rowspan=18,padx=5,pady=5,sticky=S+N+E+W)
        self.canvas.draw()

        #Tabla
        self.__tbFrame=Frame(self.__sortFrame,relief='groove',bd=3,bg='#764437')
        self.__tv = ttk.Treeview(self.__tbFrame,columns=('col1','col2','col3','col4','col5'))
        self.__tv.column("#0",width=10,anchor=CENTER)
        self.__tv.column("col1",width=100, anchor=CENTER)
        self.__tv.column("col2",width=50, anchor=CENTER)
        self.__tv.column("col3",width=80, anchor=CENTER)
        self.__tv.column("col4",width=80, anchor=CENTER)
        self.__tv.column("col5",width=80, anchor=CENTER)
        self.__tv.heading("#0", text="#", anchor=CENTER)
        self.__tv.heading("col1", text="Archivo", anchor=CENTER)
        self.__tv.heading("col2", text="Cantidad Datos", anchor=CENTER)
        self.__tv.heading("col3", text="Tiempo Tim ms", anchor=CENTER)
        self.__tv.heading("col4", text="Tiempo Quick ms", anchor=CENTER)
        self.__tv.heading("col5", text="Tiempo Bubble ms", anchor=CENTER)
        self.__tv.insert("",END,text='0',values=('-----',0,0,0,0))
        self.__tv.pack(expand=True,fill=BOTH)

    def cambiar_Frames(self,change)->None:
        self.__iniFrame.pack_forget()
        self.__sortFrame.pack_forget()
        if change==1:
            self.__iniFrame.pack(fill=BOTH,expand=True)
        elif change==2:
            self.__sortFrame.pack(fill=BOTH,expand=True)
        else:
            print("Error inesperado al cambiar ventanas")

    def check_Bot(self,x)->None:
        if x==1:
            self.__checkNum.set(True)
            self.__checkPal.set(False)
        else:
            self.__checkNum.set(False)
            self.__checkPal.set(True)

    def graf_Tabla(self,x)->None:
        self.canvas.get_tk_widget().grid_forget()
        self.__tbFrame.grid_forget()
        if x==1:
            self.canvas.get_tk_widget().grid(row=0,column=2,columnspan=3,rowspan=18,padx=5,pady=5,sticky=S+N+E+W)
        else:
            self.__tbFrame.grid(row=0,column=2,columnspan=3,rowspan=18,padx=5,pady=5,sticky=S+N+E+W)

    def pintar_Grafica(self,flag)->None:
        try:
                self.plot.clear()
                self.plot.set_title(r"|TimSort:$O(n*\log{n})$|QuickSort: $O(n*\log{n})$|BubbleSort: $O(n^{2})$|"+
                            "\n(Verde)----------(Morado)----------(Rojo)")
                self.plot.set_ylabel('Tiempo Ordenamiento [ms]')
                self.plot.set_xlabel('Cantidad Datos')
                self.plot.grid()
                flagB=messagebox.askyesno(message='Desea incluir el algoritmo\n Bubble Sort en la grafica?',title='Informacion')
                if flag:
                    if self.__cantDatos.get()>=1000 and self.__iteraciones.get()>=10 and self.__avance.get()>=20:
                        self.__infoSort=Demostracion().datosAleatorios(self.__checkNum.get(),flagB,self.__cantDatos.get(),
                                                            self.__iteraciones.get(),self.__avance.get())
                        self.plot.plot(self.__infoSort.iloc[:,1],self.__infoSort.iloc[:,2],color='#258A21')
                        self.plot.plot(self.__infoSort.iloc[:,1],self.__infoSort.iloc[:,3],color='#62217E')
                        if flagB: self.plot.plot(self.__infoSort.iloc[:,1],self.__infoSort.iloc[:,4],color='#D20404')
                        self.canvas.draw()
                        self.llenar_Tabla()
                    else:
                        messagebox.showinfo(message="Valores minimos permitidos:\nCantidad datos: 1000\n"+
                                                    "Cantidad iteraciones: 10\n"+
                                                    "Avance: 20",title="Informacion")
                else:
                    if self.__ruta!='' and self.__ruta!=None:
                        self.__infoSort=Demostracion().ordenarArchivos(self.__ruta,flagB)
                        self.plot.plot(self.__infoSort.iloc[:,1],self.__infoSort.iloc[:,2],color='#258A21')
                        self.plot.plot(self.__infoSort.iloc[:,1],self.__infoSort.iloc[:,3],color='#62217E')
                        if flagB: self.plot.plot(self.__infoSort.iloc[:,1],self.__infoSort.iloc[:,4],color='#D20404')
                        self.canvas.draw()
                        self.llenar_Tabla()
                    else:
                        messagebox.showerror(message='No se pudo encontrar la ruta',tittle='Error')
        except Exception as e:
            messagebox.showerror(message=f'Por favor solo introduzca numeros de tipo entero\nerror: {e}')

    def llenar_Tabla(self)->None:
        self.__tv.delete(*self.__tv.get_children())
        for i in range(len(self.__infoSort.iloc[:])):
            self.__tv.insert("",END,text=str(i+1),values=(self.__infoSort.iloc[i][0],self.__infoSort.iloc[i][1],
                                                          self.__infoSort.iloc[i][2],self.__infoSort.iloc[i][3],
                                                          self.__infoSort.iloc[i][4]))

    def dir_carpeta(self)->None:
        self.__ruta=filedialog.askdirectory()

    def crear_Csvs(self)->None:
        try:
            x=int(self.__spnCantArchivos.get())
            if x>0 and x<1000:
                if Demostracion().crearArchivos(x):
                    messagebox.showinfo(message="Archivos creados en la carpeta 'Archivos entrada'",title='Confirmacion')
                else:
                    pass
            else:
                messagebox.showwarning(message="Error inesperado comuniquese con su distribuidor",title="Alerta")
        except:
            messagebox.showwarning(message="Solo valores numericos por favor",title="Alerta")

if __name__=='__main__':
    Ventana()
