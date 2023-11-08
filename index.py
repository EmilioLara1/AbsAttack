import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import paramiko
from tkterm import Terminal
from test import *
#from pycomm.ab_comm import LogixDriver



#SSH conexion
#Colocar aqui las credenciales, ip de la maquina a conectar y el comando
user = ""
password = ""
ip=""
comm="ls"





def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_main_window_resize(event):
    frame.update_idletasks()
    canvas.itemconfig(frame_id, width=canvas.winfo_width(), height=canvas.winfo_height())

main_screen = tk.Tk()
main_screen.title("AbsAttack")
#main_screen.geometry ("860x560")
#permite pantalla fullscreen
main_screen.attributes('-fullscreen', True)
main_screen.bind("<Configure>", on_main_window_resize)

# URL de la imagen
URL = "https://img2.helpnetsecurity.com/posts2021/assetcentre-attack.jpg"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
im.thumbnail((400, 400))  
photo = ImageTk.PhotoImage(im)

main_screen.iconphoto(True, photo)

main_screen.config(background="black")

# Crear una ventana con scroll
canvas = Canvas(main_screen, borderwidth=0, background="black")
vsb = Scrollbar(main_screen, orient="vertical", command=canvas.yview)
hsb = Scrollbar(main_screen, orient="horizontal", command=canvas.xview)
canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
canvas.pack(side="left", fill="both", expand=True)
vsb.pack(side="right", fill="y")
hsb.pack(side="bottom", fill="x")

frame = Frame(canvas, background="black")
frame_id = canvas.create_window((4, 4), window=frame, anchor="nw")

canvas.bind("<Configure>", on_frame_configure)

# Columna de botones a la izquierda
def def_attack1():
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Defensa de ataque 1")
    messageWindow.geometry("860x560")
    Label(messageWindow, text="Esta es la defensa del ataque 1").pack()
    main_screen.withdraw()

    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()

    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)
defattack1 = tk.Button(frame, text="Defender ataque 1", bg="black", fg="white", command= def_attack1)
defattack1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

def def_attack2():
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Defensa de ataque 2")
    messageWindow.geometry("860x560")
    Label(messageWindow, text="Esta es la defensa del ataqu 2").pack()
    main_screen.withdraw()

    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()

    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)

defattack2 = tk.Button(frame, text="Defender ataque 2", bg="black", fg="white", command= def_attack2)
defattack2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

def def_attack3():
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Defensa de ataque 3")
    messageWindow.geometry("860x560")
    Label(messageWindow, text="Esta es la defensa del ataque 3").pack()
    main_screen.withdraw()

    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()

    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)
defattack3 = tk.Button(frame, text="Defender ataque 3", bg="black", fg="white", command= def_attack3)
defattack3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

reset = tk.Button(frame, text="reiniciar", bg="black", fg="white")
reset.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# Espacio de imagen
image_label = Label(frame, image=photo, bg="black")
image_label.grid(row=0, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")



# Columna de botones a la derecha
def attack1():
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Ataque nivel 1")
    #messageWindow.geometry("860x560")
    #permite pantalla fullscreen
    messageWindow.attributes('-fullscreen', True)
    messageWindow.config(background="black")
    tit = Label(messageWindow, text="Este es el ataque de nivel 1", font="Helvetica 20 bold", bg="black", fg="white")
    tit.pack(pady=50)
    sub = Label(messageWindow, text="Listado de directorio", font="Helvetica 20", bg="black", fg="white")
    sub.pack(side=TOP)


    #Descomentar para agregar boton si no pasa ssh
    """ #Regresar a menu principal
    btn_back= Button(messageWindow, text="Regresar", font=12, height=4, width=30,bg="black", fg="white", command=lambda: main_screen.tkraise()).pack()
    btn_back.grid(row=0, column=1,padx=10, pady=10, sticky="nsew") """


    #Conexion ssh
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    #Se ejecuta comando
    _stdin, _stdout,_stderr = client.exec_command("ls")
    #print(_stdout.read().decode())
    string = str(_stdout.read().decode())
    #print(type(string))
    t = Label(messageWindow, text=string, bg="black", fg="white", font="Helvetica 12")
    t.pack(side=TOP)
    client.close()


###### Conexion a PLC
    """  with LogixDriver('192.168.1.1') as plc:
        plc.open()
        if plc.read_tag('Tag1'):
            print('Lectura exitosa')
        plc.close() """

    ###### Botones
    #Regresar a menu principal
    btn_back= Button(messageWindow, text="Regresar", font=12, height=4, width=30,bg="black", fg="white", command=lambda: main_screen.tkraise()).pack()
    btn_back.grid(row=0,column=1,padx=10, pady=10, sticky="nsew")
    
    main_screen.withdraw()

    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()
    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)

atk1 = tk.Button(frame, text="Prueba de ataque 1", bg="black", fg="white", command=attack1)
atk1.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

def attack2():
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Ataque nivel 2")
    messageWindow.geometry("860x560")
    Label(messageWindow, text="Este es el ataque de nivel 2").pack()
    main_screen.withdraw()

    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()

    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)

atk2 = tk.Button(frame, text="prueba de ataque 2", bg="black", fg="white", command=attack2)
atk2.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

def attack3():
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Ataque nivel 3")
    messageWindow.geometry("860x560")
    Label(messageWindow, text="Este is el ataque de nivel 3").pack()
    main_screen.withdraw()

    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()

    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)

atk3 = tk.Button(frame, text="prueba de ataque 3", bg="black", fg="white", command=attack3)
atk3.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

def done():
    main_screen.destroy()

dne = tk.Button(frame, text="Salir", bg="black", fg="white", command=done)
dne.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")



# resize automatico
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)

for i in range(3):
    frame.grid_columnconfigure(i, weight=1)

main_screen.mainloop()
