from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import time


class WeatherClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x400+325+150")
        self.root.title("Weather App")
        self.root.resizable(False, False)
        self.root.config(bg="#f8ea28")

        # ----- Background Image ----- #
        bg = Image.open("weather.png")
        bg = bg.resize((700, 400))
        self.photo_image = ImageTk.PhotoImage(bg)
        self.lbl_photo_image = Label(self.root, image=self.photo_image, bd=0)
        self.lbl_photo_image.place(x=0, y=0)

        # --- Variables ----- #
        self.var_city = StringVar()
        
        self.var_city.set("Badulla")   # seting Default Location as a Badulla
        self.var_txtcity = StringVar()
        self.var_latitude = StringVar()
        self.var_temprature = StringVar()
        self.var_humididty = StringVar()
        self.var_pressure = StringVar()
        self.var_wind = StringVar()
        self.var_des = StringVar()
        self.var_localtime = StringVar()

        # ---- Output Labels ---- #
        self.var_txtcity = Label(self.root, text="", font=("times 30 bold"), fg="black", bg="#00C9E2", justify="center")
        self.var_txtcity.place(x=0, y=70)

        self.var_latitude_lbl = Label(self.root, text="", font=("times 12 bold"), fg="black", bg="#00C9E2", justify="center")
        self.var_latitude_lbl.place(x=0, y=40)

        self.var_temprature_lbl = Label(self.root, text="", font=("times 40 bold"), fg="black", bg="#00C9E2", justify="center")
        self.var_temprature_lbl.place(x=20, y=120)

        self.var_localtime_lbl = Label(self.root, text="", font=("times 14 bold"), fg="black", bg="#00C9E2" ,justify="center")
        self.var_localtime_lbl.place(x=220, y=220, width=100)

        self.var_des_lbl = Label(self.root, text="", font=("times 14 bold"), fg="black", bg="#00C9E2", justify="center")
        self.var_des_lbl.place(x=90, y=300)

        self.var_wind_lbl = Label(self.root, text="", font=("times 14 bold"), fg="black", bg="#00C9E2", justify="center")
        self.var_wind_lbl.place(x=250, y=300)

        self.var_humididty_lbl = Label(self.root, text="", font=("times 14 bold"), fg="black", bg="#00C9E2", justify="center")
        self.var_humididty_lbl.place(x=370, y=300)

        self.var_pressure_lbl = Label(self.root, text="", font=("times 14 bold"), fg="black", bg="#00C9E2", justify="center")
        self.var_pressure_lbl.place(x=500, y=300)

        # ----- Static Labels ------ #
        Label(self.root, text="Description", font=("times 14 bold"), fg="white", bg="#202930").place(x=90, y=270)
        Label(self.root, text="Wind", font=("times 14 bold"), fg="white", bg="#202930").place(x=250, y=270)
        Label(self.root, text="Humidity", font=("times 14 bold"), fg="white", bg="#202930").place(x=370, y=270)
        Label(self.root, text="Pressure", font=("times 14 bold"), fg="white", bg="#202930").place(x=500, y=270)

        # ---- City Entry ----- #
        textfield = Entry(
            self.root,
            textvariable=self.var_city,
            justify="center",
            font=("Segoe UI", 14, "bold"),
            bg="#313f46",
            fg="white",
            relief="flat",
            insertbackground="white",
        )
        textfield.place(x=380, y=38, width=220, height=35)
        textfield.focus()

        # ---- Search Button ---- #
        search_img = Image.open("search.png")
        search_img = search_img.resize((35, 35), Image.LANCZOS)  # match height of textfield
        self.search_icon = ImageTk.PhotoImage(search_img)

        self.myimage_icon = Button(
            self.root,
            image=self.search_icon,
            borderwidth=0,
            cursor="hand2",
            command=self.getweather,
            bg="#313f46",
            activebackground="#313f46",
        )
        self.myimage_icon.image = self.search_icon
        self.myimage_icon.place(x=605, y=38)

    # ---------- WEahther Funtion ----------
    def getweather(self):
        try:
            city = self.var_city.get().strip()
            if not city:
                messagebox.showwarning("Weather App", "Please enter a city name.")
                return

            geolocator = Nominatim(user_agent="geoapiExercise")
            location = geolocator.geocode(city)
            if location is None:
                messagebox.showerror("Weather App", "City not found. Try another name.")
                return

            # Timezone
            tzfinder = TimezoneFinder()
            tzname = tzfinder.timezone_at(lng=location.longitude, lat=location.latitude)

            # Longtiutde and Latitude
            self.var_txtcity.config(text=tzname if tzname else "Timezone not found")
            self.var_latitude_lbl.config(
                text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E"
            )
             # ----- Local time ----- #
            if tzname:
             home = pytz.timezone(tzname)
             local_time = datetime.now(home)
             current_time = local_time.strftime("%I:%M %p")
             self.var_localtime_lbl.config(text=current_time)
             # print(f"Current time in {city}: {current_time}")
             
             #request Weather Data
             api="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=b30ecf098d3f39d6da3dda6fe3aae334"
             weather_data=requests.get(api).json()
             
             condition=weather_data['weather'][0]['main']
             description=weather_data['weather'][0]['description']
             temprature=(weather_data['main']['temp'] -273.15)
             pressure=weather_data['main']['pressure']
             humidity=weather_data['main']['humidity']
             wind = weather_data['wind']['speed']
             
             
             #----main data----#
              
             self.var_temprature_lbl.config(text=f"{condition}\n{round(temprature, 2)}°C")
             self.var_des_lbl.config(text=description.capitalize())
             self.var_wind_lbl.config(text=f"{wind} m/s")
             self.var_humididty_lbl.config(text=f"{humidity}%")
             self.var_pressure_lbl.config(text=f"{pressure} hPa")
             
             #----icons-----#
                
            if condition == 'Rain':
                weather_img = Image.open('icons/rain.png')
                weather_img = weather_img.resize((50, 50), Image.LANCZOS)
                self.weather_image = ImageTk.PhotoImage(weather_img)
                self.weather_icon_label = Label(self.root, image=self.weather_image, bg='#202930')
                self.weather_icon_label.place(x=450, y=100)

            elif condition == 'Clouds':
                weather_img = Image.open('icons/cloudy.png')
                weather_img = weather_img.resize((100, 100), Image.LANCZOS)
                self.weather_image = ImageTk.PhotoImage(weather_img)
                self.weather_icon_label = Label(self.root, image=self.weather_image, bg='#202930')
                self.weather_icon_label.place(x=450, y=100)

            elif condition == 'Clear':
                weather_img = Image.open('icons/cleansky.png')
                weather_img = weather_img.resize((100, 100), Image.LANCZOS)
                self.weather_image = ImageTk.PhotoImage(weather_img)
                self.weather_icon_label = Label(self.root, image=self.weather_image, bg='#202930')
                self.weather_icon_label.place(x=450, y=100)

            elif condition in ['Thunderstorm', 'Lightning', 'Storm']:
                weather_img = Image.open('icons/rain_light.png')
                weather_img = weather_img.resize((50, 50), Image.LANCZOS)
                self.weather_image = ImageTk.PhotoImage(weather_img)
                self.weather_icon_label = Label(self.root, image=self.weather_image, bg='#202930')
                self.weather_icon_label.place(x=450, y=100)

            else:
                # fallback default
                weather_img = Image.open('icons/cleansky.png')
                weather_img = weather_img.resize((50, 50), Image.LANCZOS)
                self.weather_image = ImageTk.PhotoImage(weather_img)
                self.weather_icon_label = Label(self.root, image=self.weather_image, bg='#202930')
                self.weather_icon_label.place(x=450, y=100)
        
        except Exception as e:
            messagebox.showerror("Weather App", f"Invalid Entry...!\n{e}")


if __name__ == "__main__":
    root = Tk()
    obj = WeatherClass(root)
    root.mainloop()
