import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk() 
window.wm_title("SISTEMA DE ENRROLAMIENTO")
window.config(bg="gray")

imageFrame = tk.Frame(window, width=1000, height=700)
imageFrame.grid(row=10, column=0, padx=10, pady=2)

capture0 = cv2.VideoCapture(0)
capture1 = cv2.VideoCapture(1)
capture2 = cv2.VideoCapture(2)
capture3 = cv2.VideoCapture(3)


def show_frame():

#---------------------------------------------------------------
    _, frame0 = capture0.read()
    cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
    img0 = Image.fromarray(cv2image0)
    imgtk0 = ImageTk.PhotoImage(image=img0)
#--------------------------------------------------------------
    _, frame1 = capture1.read()
    cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
    img1 = Image.fromarray(cv2image1)
    imgtk1 = ImageTk.PhotoImage(image=img1)
#---------------------------------------------------------------
    _, frame2 = capture2.read()
    cv2image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
    img2 = Image.fromarray(cv2image2)
    imgtk2 = ImageTk.PhotoImage(image=img2)
#---------------------------------------------------------------
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


display1 = tk.Label(imageFrame, width=250, height=320)
display1.grid(row=1, column=2, padx=10, pady=5)
display2 = tk.Label(imageFrame, width=250, height=320)
display2.grid(row=2, column=1, padx=10, pady=5)
display3 = tk.Label(imageFrame, width=250, height=320)
display3.grid(row=2, column=2, padx=10, pady=5)
display4 = tk.Label(imageFrame, width=250, height=320)
display4.grid(row=2, column=3, padx=10, pady=5) 


sliderFrame = tk.Frame(window, width=950, height=100)
sliderFrame.grid(row = 800, column=0, padx=10, pady=2)
sliderFrame.config(background="gray")

show_frame() 
window.mainloop() 