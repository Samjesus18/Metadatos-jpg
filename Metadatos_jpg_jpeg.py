import exifread
import tkinter as tk
from tkinter import filedialog

ruta_imagen = ""
datos = ""
ll = datos

def obtener_metadatos_imagen():
    global ruta_imagen
    global datos
    ruta_imagen = tk.filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo", filetypes=(("Archivos jpg","*jpg"),("Archivos jpeg","*jpeg"),("Todos los archivos","*.*")))
    with open(ruta_imagen, 'rb') as imagen:
        tags = exifread.process_file(imagen)
        datos = ""
        for tag, value in tags.items():
            datos += f'{tag}: {value}\n'
    imprimir()


def guardar_informacion():

    ruta_archivo = tk.filedialog.asksaveasfilename(initialdir="/", title="Guardar archivo", filetypes=(("Archivo txt","*txt"),("Todos los archivos","*.*")))
    if ruta_archivo:
        if not ruta_archivo.endswith(".txt"):
            ruta_archivo += ".txt"
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(datos)

def imprimir ():

    texto1.delete(1.0, tk.END)
    texto1.insert(tk.END, datos)

    



#------------------------------------Interfaz grafica--------------------------
ventana = tk.Tk()
ventana.title("Metadatos JPG y JPEG")
#ventana.geometry("300x400")

frame1 = tk.Frame(ventana)
frame1.pack()

boton_cargar = tk.Button(frame1, text="Cargar", command=obtener_metadatos_imagen)
boton_cargar.grid(row=0, column=0)

label1 = tk.Label(frame1, text="Lectura y analisis")
label1.grid(row=0, column=1)

boton_cargar2 = tk.Button(frame1, text="Guardar", command=guardar_informacion)
boton_cargar2.grid(row=0, column=2)


texto1 = tk.Text(frame1)
texto1.grid(row=1, column=0, columnspan=3)
texto1.bind('<Control-x>', lambda e: texto1.event_generate('<<Cut>>'))
texto1.bind('<Control-c>', lambda e: texto1.event_generate('<<Copy>>'))
texto1.bind('<Control-v>', lambda e: texto1.event_generate('<<Paste>>'))


ventana.mainloop()

