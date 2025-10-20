from tkinter import *
from geopy.geocoders import Nominatim        # pip install geopy
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder    # pip install timezonefinder
from datetime import *
import requests                               # pip install requests
import pytz                                   # pip install pytz
from PIL import Image, ImageTk                # pip install pillow
import time



class WeatherClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x400+325+150")   
        self.root.title("Weather App")
        self.root.resizable(False, False)
        self.root.config(bg="#f8ea28")
        
           # ----- Background Image -----#
        bg = Image.open("weather.png")
        bg = bg.resize((700, 400))
        self.photo_image = ImageTk.PhotoImage(bg)
        self.lbl_photo_image = Label(self.root, image=self.photo_image, bd=0)
        self.lbl_photo_image.place(x=0, y=0)

        #--- Varaibles-----#
        self.var_city=StringVar()
        self.var.txtcity=StringVar()
        self.var_latitude=StringVar()
        self.var_temprature=StringVar()
        self.var_humididty=StringVar()
        self.var_pressure=StringVar()
        self.var_wind=StringVar()
        self.var_des=StringVar()
        self.var_localtime=StringVar()

        #----Our Datas ----#
        self.var.txtcity=Label(self.root,text="",font=("times 30 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_txtcity.place(x=0,y=70)
        self.var_textcity.focus()

        self.var.latitude=Label(self.root,text="",font=("times 12 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_latitude.place(x=0,y=70)

        self.var.temprature=Label(self.root,text="",font=("times 40 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_temprature.place(x=20,y=150)

        self.var.localtime=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_localtime.place(x=165,y=220,width=150)

        self.var.des=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_des.place(x=90,y=330)
        

        self.var.wind=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_wind.place(x=250,y=330)

        self.var.humididty=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_humididty.place(x=370,y=330)

        self.var.humididty=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_humididty.place(x=370,y=330)

        self.var.pressure=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_pressure.place(x=500,y=330)

        #-----Label------#
        label1=Label(self.root,text="Description",font=("times 14 bold"),fg="white",bg="#4c7b7b").place(x=90, y=20)
        





        


if __name__ == "__main__":
    root = Tk()            
    obj = WeatherClass(root)
    root.mainloop()