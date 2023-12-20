
from tkinter import *
from tkinter import messagebox 
from PIL import Image,ImageTk 
import requests

class Style:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600+400+100') 
        self.master.title('WeatherApp')
        self.master.resizable (width=False, height=False) 
        self.master.iconbitmap('Weather_png/icon_weather.ico')

# .................Add Image Search.........
        self.image_city = PhotoImage(file='Weather_png/search1.png')
        self.label_city = Label(self.master, image=self.image_city).place(x=200,y=40)
        
        
        self.logo_image = PhotoImage(file='Weather_png/logo.png')
        self.label_logo = Label(self.master, image=self.logo_image). place (x=280,y=120)
        
        self.box_image = PhotoImage(file="Weather_png/box.png")
        self.label_box = Label(self.master, image=self.box_image).place(x=100,y=450)
        
        self.city_name = Entry(self.master, font=('Bold',22) , bg='#404040' , border= 0,justify='center', fg='white' ).place(x=220,y=50)
        # self.city_name.config(width=30) 
        
        # ........................Add Labels Description .....................
        self.add_titles()
        
    def add_titles(self):
        self.location = Label(self.master, text='Location',bg='#99D9EA', font=('poppins', 12, 'bold'), fg='white').place(x=120,y=460) 
        self.temperuature = Label(self.master, text="Temperuatur",bg='#99D9EA', font=('poppins', 12, 'bold'), fg='white').place(x=240,y=460) 
        self.weather = Label(self.master, text='Weather', bg='#99D9EA', font=('poppins', 12, 'bold'), fg='white').place(x=390,y=460)
        self.pressure = Label(self.master, text='Pressure' ,bg='#99D9EA',font=('poppins', 12, 'bold'), fg='white').place(x=500,y=460) 
        self.description = Label(self.master, text="Description",bg='#99D9EA', font=('poppins', 12, 'bold'), fg='white').place(x=620,y=460)
        
        #.....................................................
        
        self.lbl1 = Label(self.master, text="....", font=('poppins', 16, 'bold'), bg='#99D9EA',fg='#000000') 
        self.lbl1.place(x=120,y=490)
        
        self.lbl2 = Label(self.master, text='....', font=('poppins',16, 'bold'), bg='#99D9EA',fg='#000000') 
        self.lbl2.place(x=240,y=490)
        
        self.lbl3 = Label(self.master, text='...', font=('poppins', 16, 'bold'), bg='#99D9EA', fg='#000000')
        self.lbl3.place(x=400,y=490)
        
        self.lbl4 = Label(self.master, text="....", font=('poppins', 16, 'bold'), bg='#99D9EA',fg='#000000') 
        self.lbl4.place(x=510,y=490)
        
        self.lbl5 = Label(self.master, text="....", font=('poppins', 16, 'bold'), bg='#99D9EA',fg='#000000') 
        self.lbl5.place(x=620,y=490)
        
        self.lbl6 = Label(self.master, text="....", font=('poppins', 22, 'bold'),fg='#000000') 
        self.lbl6.place(x=500,y=240)