import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk() 
window.wm_title("SISTEMA DE ENROLAMIENTO")
window.config(bg="gray")


miFrame=tk.Frame()
miFrame.pack(fill="y", expand="True")
miFrame.config(bg="gray")
miFrame.config(width="1500", height="1500")
miLabel=tk.Label(miFrame, text="RECONOCIMIENTO-FACIAL", font=("Helvetica Neue", 15))
miLabel.place(x=500, y=35)


imageFrame = tk.Frame(miFrame, width=1500, height=1500)
imageFrame.place(x=70, y=100)
imageFrame.config(cursor="hand1")


miLabel1=tk.Label(miFrame, text="INFORMACION PERSONAL", font=("Helvetica Neue", 10))
miLabel1.place(x=940, y=100)
#----------------------------------------------------------------------------------
cedula=tk.Label(miFrame, text="Cedula:", font=("Helvetica Neue", 10))
cedula.place(x=940, y=140)

cuadrotexto0=tk.Entry(miFrame)
cuadrotexto0.place(x=940, y=160)
#-----------------------------------------------------------------------------------
primernombre=tk.Label(miFrame, text="Primer nombre:", font=("Helvetica Neue", 10))
primernombre.place(x=940, y=200)

cuadrotexto1=tk.Entry(miFrame)
cuadrotexto1.place(x=940, y=220)
#----------------------------------------------------------------------------------
segundonombre=tk.Label(miFrame, text="Segundo nombre:", font=("Helvetica Neue", 10))
segundonombre.place(x=940, y=260)

cuadrotexto2=tk.Entry(miFrame)
cuadrotexto2.place(x=940, y=280)
#----------------------------------------------------------------------------------
primerapellido=tk.Label(miFrame, text="Primer apellido:", font=("Helvetica Neue", 10))
primerapellido.place(x=940, y=320)

cuadrotexto3=tk.Entry(miFrame)
cuadrotexto3.place(x=940, y=340)
#----------------------------------------------------------------------------------
segundoapellido=tk.Label(miFrame, text="Segundo apellido:", font=("Helvetica Neue", 10))
segundoapellido.place(x=940, y=380)

cuadrotexto4=tk.Entry(miFrame)
cuadrotexto4.place(x=940, y=400)
#----------------------------------------------------------------------------------
fechadenacimiento=tk.Label(miFrame, text="Fecha de nacimiento:", font=("Helvetica Neue", 10))
fechadenacimiento.place(x=940, y=440)

cuadrotexto5=tk.Entry(miFrame)
cuadrotexto5.place(x=940, y=460)
#----------------------------------------------------------------------------------
ciudadania=tk.Label(miFrame, text="Ciudadania:", font=("Helvetica Neue", 10))
ciudadania.place(x=940, y=500)

cuadrotexto6=tk.Entry(miFrame)
cuadrotexto6.place(x=940, y=520)
#-----------------------------------------------------------------------------------
genero=tk.Label(miFrame, text="Genero:", font=("Helvetica Neue", 10))
genero.place(x=940, y=560)

cuadrotexto7=tk.Entry(miFrame)
cuadrotexto7.place(x=940, y=580)
#-------------------------------------------------------------------------------------
btn = tk.Button(miFrame, text="Iniciar registro", fg="green")
btn.pack(side="bottom", padx=10, pady=10)
btn.config(width="15", height="3")
btn.place(x=940, y=630)
#--------------------------------------------------------------------------------------

capture0 = cv2.VideoCapture(0)
capture1 = cv2.VideoCapture(1)
capture2 = cv2.VideoCapture(2)
capture3 = cv2.VideoCapture(3)

def show_frame():

#--------------------------------------------------------------
    _, frame0 = capture0.read()
    cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
    img0 = Image.fromarray(cv2image0)
    imgtk0 = ImageTk.PhotoImage(image=img0)
#--------------------------------------------------------------
    _, frame1 = capture1.read()
    cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
    img1 = Image.fromarray(cv2image1)
    imgtk1 = ImageTk.PhotoImage(image=img1)
#--------------------------------------------------------------
    _, frame2 = capture2.read()
    cv2image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
    img2 = Image.fromarray(cv2image2)
    imgtk2 = ImageTk.PhotoImage(image=img2)
#--------------------------------------------------------------
    _, frame3 = capture3.read()
    cv2image3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGBA)
    img3 = Image.fromarray(cv2image3)
    imgtk3 = ImageTk.PhotoImage(image=img3)
#---------------------------------------------------------------

    display1.imgtk = imgtk0 
    display1.configure(image=imgtk0)
#---------------------------------------------------------------
    display2.imgtk = imgtk1
    display2.configure(image=imgtk1)
#---------------------------------------------------------------    
    display3.imgtk = imgtk2
    display3.configure(image=imgtk2)
#---------------------------------------------------------------
    display4.imgtk = imgtk3 
    display4.configure(image=imgtk3)
#---------------------------------------------------------------    
    window.after(10, show_frame) 
#---------------------------------------------------------------

display1 = tk.Label(imageFrame, width=250, height=250)
display1.grid(row=1, column=2, padx=10, pady=5)
display2 = tk.Label(imageFrame, width=250, height=250)
display2.grid(row=2, column=1, padx=10, pady=5)
display3 = tk.Label(imageFrame, width=250, height=250)
display3.grid(row=2, column=2, padx=10, pady=5)
display4 = tk.Label(imageFrame, width=250, height=250)
display4.grid(row=2, column=3, padx=10, pady=5) 


show_frame() 
window.mainloop() 