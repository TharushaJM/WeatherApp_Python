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
        self.var_txtcity=StringVar()
        self.var_latitude=StringVar()
        self.var_temprature=StringVar()
        self.var_humididty=StringVar()
        self.var_pressure=StringVar()
        self.var_wind=StringVar()
        self.var_des=StringVar()
        self.var_localtime=StringVar()

        #----Our Datas ----#
        self.var_txtcity=Label(self.root,text="",font=("times 30 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_txtcity.place(x=0,y=70)
      

        self.var_latitude=Label(self.root,text="",font=("times 12 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_latitude.place(x=0,y=40)

        self.var_temprature=Label(self.root,text="",font=("times 40 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_temprature.place(x=20,y=120)

        self.var_localtime=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_localtime.place(x=165,y=220,width=150)

        self.var_des=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_des.place(x=90,y=300)
        

        self.var_wind=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_wind.place(x=250,y=300)

        self.var_humididty=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_humididty.place(x=370,y=300)

      
        self.var_pressure=Label(self.root,text="",font=("times 14 bold"),fg="black",bg="#08f7f7",justify="center")
        self.var_pressure.place(x=500,y=300)

        #-----Label ------#
        label1=Label(self.root,text="Description",font=("times 14 bold"),fg="white",bg="#4c7b7b").place(x=90, y=270)
        label2=Label(self.root,text="WInd",font=("times 14 bold"),fg="white",bg="#4c7b7b").place(x=250, y=270)
        label3=Label(self.root,text="Humidity",font=("times 14 bold"),fg="white",bg="#4c7b7b").place(x=370, y=270)
        label4=Label(self.root,text="Presure",font=("times 14 bold"),fg="white",bg="#4c7b7b").place(x=500, y=270)
        
       
        #----city entry -----#
        textfield = Entry( self.root,textvariable=self.var_city,
        justify="center",font=("Segoe UI", 14, "bold"),bg="#313f46",fg="white",
        relief="flat",
        insertbackground="white")
        
        textfield.place(x=380, y=38, width=220, height=35)
        textfield.focus()
                    
        # ---- Search Button ---- #
        search_img = Image.open("search.png")
        search_img = search_img.resize((35, 35), Image.LANCZOS)   # match height of textfield
        self.search_icon = ImageTk.PhotoImage(search_img)

        self.myimage_icon = Button(
        self.root,
        image=self.search_icon,
        borderwidth=0,
        cursor="hand2",
        command=self.getweather
        bg="#313f46",
        activebackground="#313f46"
        )
        self.myimage_icon.image = self.search_icon
        self.myimage_icon.place(x=605, y=38) 
        
        def getweather(self):
            try:
                city=self.var_city.get()
                geolocater=Nominatim(user_agent="geoapiExercise")
                location=geolocater.geocode(city)
                obj=Timezonefinder()
                
                #---longtitude and Latitude ----#
                result=obj.timezone_at(lng=location.longtitude,lat=location.latitude)
                self.var_
                
                
            except Exception as e:
                messagebox.showerror("Weather App","Invalid Entry...!")
        
        
        
if __name__ == "__main__":
    root = Tk()            
    obj = WeatherClass(root)
    root.mainloop()
    
    