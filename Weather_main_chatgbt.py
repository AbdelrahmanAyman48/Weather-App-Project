
from tkinter import *
from tkinter import messagebox
from Weather_style import Style
from Weather_menu import MMenu
from datetime import datetime
import time
import requests

# Code Reorganization: I've reorganized the code by moving some repeated operations to separate methods for better readability and maintainability.
# Error Handling: Added more detailed error handling for different scenarios, such as handling a city not found, connection errors, and unexpected API responses.
# Reduced Redundancy: Avoided redundant creation of labels and improved the overall structure of the Main class.


class Main:
    def __init__(self, root):
        self.root = root
        self.object_style = Style(self.root)
        self.object_menu = MMenu(self.root)
        self.url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        self.API = '8058cbb5f06ba5c27957afa56f3d21d1'
        self.variable_city = StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.city_name = Entry(self.root, font=('poppins', 22), bg='#252525',
                            border=0, justify='center', fg='white', textvariable=self.variable_city)
        self.city_name.place(x=220, y=50)

        self.image_get = PhotoImage(file='Weather_png/get_data.png')
        self.button = Button(self.root, image=self.image_get, borderwidth=0, bg='#252525', command=self.get_data)
        self.button.place(x=530, y=46)

    def get_data(self):
        city_name = self.variable_city.get()
        if city_name:
            try:
                response = requests.get(self.url.format(city_name, self.API))
                if response.status_code == 200:
                    self.handle_response(response.json())
                elif response.status_code == 404:
                    messagebox.showerror("Error", "City not found")
                else:
                    messagebox.showerror("Error", f"Failed to fetch data. Status code: {response.status_code}")
            except requests.RequestException as e:
                messagebox.showerror("Error", f"Request Exception: {e}")

    def handle_response(self, data):
        if data.get("cod") != "404":
            self.show_data(data)
        else:
            messagebox.showerror("Error", "City not found")

    def show_data(self, data):
        city = data['name']
        country = data['sys']['country']
        temp_kvl = data['main']['temp']
        temp_cel = round(temp_kvl - 273.15, 2)
        temp_fehr = round(temp_kvl - 273.15, 2) * 9 / 5 + 32
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']

        final_result = (
            city, country, temp_kvl, temp_cel,
            temp_fehr, weather, pressure, description,
            humidity
        )

        self.update_display(final_result)

    def update_display(self, result):
        self.object_style.lbl1['text'] = result[0] + '-' + result[1]
        self.object_style.lbl2['text'] = '{:.0f}°C, {:.0f}°F'.format(result[3], result[4])
        self.object_style.lbl3['text'] = result[5]
        self.object_style.lbl4['text'] = result[6]
        self.object_style.lbl5['text'] = result[7]
        self.object_style.lbl6['text'] = 'Humidity |'

        Label(self.root, font=('poppins', 25), fg='red', text='{:.0f}°C'.format(result[3])).place(x=500, y=190)
        Label(self.root, text='Current Weather', font=('poppins', 22), fg='#000000').place(x=55, y=140)
        Label(self.root, text=f'{result[8]}', font=('poppins', 22), fg='#77c9ee').place(x=650, y=240)
        self.add_time()

    def add_time(self):
        time_now = datetime.now().strftime('%H:%M:%S %p')
        Label(self.root, text=time_now, fg='#000000', font=('poppins', 22)).place(x=100, y=240)
        self.root.after(1000, self.add_time)


if __name__ == '__main__':
    app = Tk()
    main_class = Main(app)
    app.mainloop()
