from tkinter import *
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk 
import requests

class Style:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600+400+100') 
        self.master.title('WeatherApp')
        self.master.resizable(width=False, height=False) 
        self.master.iconbitmap('Weather_png/icon_weather.ico')

        # Load Images
        self.image_city = PhotoImage(file='Weather_png/search1.png')
        self.logo_image = PhotoImage(file='Weather_png/logo.png')
        self.box_image = PhotoImage(file='Weather_png/box.png')

        # Create Labels with Images
        self.label_city = Label(self.master, image=self.image_city)
        self.label_city.place(x=200, y=40)
        
        self.label_logo = Label(self.master, image=self.logo_image)
        self.label_logo.place(x=280, y=120)
        
        self.label_box = Label(self.master, image=self.box_image)
        self.label_box.place(x=100, y=450)
        
        # Entry for City Name
        self.city_name = Entry(self.master, font=('Bold', 22), bg='#404040', border=0, justify='center', fg='white')
        self.city_name.place(x=220, y=50)
        
        # Add Titles
        self.add_titles()
        
        # Create Labels for Weather Information
        self.create_labels()

    def add_titles(self):
        labels_data = [
            ('Location', 120), ('Temperature', 240), ('Weather', 390),
            ('Pressure', 500), ('Description', 620)
        ]

        for title, x_position in labels_data:
            label = Label(self.master, text=title, bg='#99D9EA', font=('poppins', 12, 'bold'), fg='white')
            label.place(x=x_position, y=460)

    def create_labels(self):
        self.lbl1 = Label(self.master, text="....", font=('poppins', 16, 'bold'), bg='#99D9EA', fg='#000000')
        self.lbl1.place(x=120, y=490)
        
        self.lbl2 = Label(self.master, text='....', font=('poppins', 16, 'bold'), bg='#99D9EA', fg='#000000')
        self.lbl2.place(x=240, y=490)
        
        self.lbl3 = Label(self.master, text='...', font=('poppins', 16, 'bold'), bg='#99D9EA', fg='#000000')
        self.lbl3.place(x=400, y=490)
        
        self.lbl4 = Label(self.master, text="....", font=('poppins', 16, 'bold'), bg='#99D9EA', fg='#000000')
        self.lbl4.place(x=510, y=490)
        
        self.lbl5 = Label(self.master, text="....", font=('poppins', 16, 'bold'), bg='#99D9EA', fg='#000000')
        self.lbl5.place(x=620, y=490)
        
        self.lbl6 = Label(self.master, text="....", font=('poppins', 22, 'bold'), fg='#000000')
        self.lbl6.place(x=500, y=240)

if __name__ == '__main__':
    root = tk.Tk()
    style = Style(root)
    root.mainloop()
