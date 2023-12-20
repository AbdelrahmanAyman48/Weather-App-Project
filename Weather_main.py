from tkinter import *
from tkinter import messagebox
from Weather_style import Style
from Weather_menu import MMenu
from datetime import datetime
import time
import requests

class Main:
    def __init__(self,root): 
        self.root = root
        self.object_style = Style(self.root)
        self.object_menu = MMenu(self.root)
        
        
        self.url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        # self.API = '06051f3cadead7ba821ba795bf6d124f'
        self.API = '8058cbb5f06ba5c27957afa56f3d21d1'
        
        self.variable_city = StringVar()
        
        #..................................
        self.city_name = Entry(self.root, font=('poppins', 22), bg='#252525',
                            border=0,justify='center', fg='white', textvariable = self.variable_city)
        self.city_name.place(x=220,y=50)
        self.image_get = PhotoImage(file='Weather_png/get_data.png')
        self.button = Button(
                self.root, image=self.image_get, borderwidth=0, bg='#252525', command=self.get_data).place(x=530,y=46)
# https://www.youtube.com/watch?v=urTOBIXII6s
    def get_data(self):
        # request http data
        self.url_api_http = requests.get(self.url.format(self.city_name.get() , self.API))
        print(self.url_api_http)
        print('........................................')
        
        if self.url_api_http.status_code == 200:
        # Handle the successful response
            self.weather_data_json = self.url_api_http.json()  
            # Extract JSON data from the response
            if self.weather_data_json["cod"] != "404" :
                # Process the data further
                # Access weather_data_json attributes as needed
            # convert requested http data to json ad save it variable
                # self.weather_data_json = self.url_api_http.json()
                print(self.weather_data_json)
                print('........................................')
                # get cityname from json
                self.city= self.weather_data_json['name']
                self.country = self.weather_data_json['sys']['country']
                self.temp_kvl = self.weather_data_json['main']['temp']
                self.temp_cel = round(self.temp_kvl - 273.15,2) 
                self.temp_fehr = round(self.temp_kvl - 273.15,2)*9/5+32
                self.weather = self.weather_data_json['weather'][0]['main']
                self.description = self.weather_data_json['weather'][0]['description']
                self.presure = self.weather_data_json['main']['pressure']
                self.humidity = self.weather_data_json['main']['humidity']
                
                self.final_result = (
                    self.city, self.country, self.temp_kvl ,self.temp_cel , 
                    self.temp_fehr ,self.weather ,self.presure  ,self.description 
                    ,self.humidity
                )
                if self.final_result:
                    self.show_data()
            else:
                print("City not found")
        else:
            print("Failed to fetch data. Status code:", self.url_api_http.status_code)

        # if self.weather_data_json["cod"] != "404":
            # main = self.weather_data_json["main"]
            # weather = self.weather_data_json["weather"]
            # current_temperature = round(main["temp"] - 273.15,2) 
            # current humidity = main["humidity"]
            # weather_description = weather[0]["description"] 
            # print("Temperature (in Celsius unit) = " +
                        # f'{current_temperature}' +
                    # "\n humidity (in percentage) = " +
                        # f'{current humidity}%' +
                    # "In description = " +
                        # f'{weather_description}')
        # else:
            # print("City Not Found ")
                
        
        return #messagebox.showerror('Error', 'Error in city name please use name correct')
    
# https://www.youtube.com/watch?v=uDugJX5ZFpw&ab_channel=%D8%B9%D9%84%D8%A7%D8%A1%D8%AC%D8%A7%D8%B3%D9%85%D9%85%D8%AD%D9%85%D8%AF 
    def show_data(self):
        print(self.final_result)

        self.object_style.lbl1['text'] = self.final_result[0]+'-' + self.final_result[1]
        self.object_style.lbl2['text'] = ('{:.0f}°C, {:.0f}°F'.format(self.final_result[3], self.final_result[4]))
        self.object_style.lbl3['text'] = self.final_result[5]
        self.object_style.lbl4['text'] = self.final_result[6]
        self.object_style.lbl5['text'] = self.final_result[7]
        self.object_style.lbl6['text'] = 'Humidity |'
        

        self.label_temp_cel = Label(self.root, font=('poppins', 25),fg='red',text='{:.0f}°C'.format(self.final_result[3]))
        self.label_temp_cel.place(x=500,y=190)
        
        self.current_weather = Label(self.root, text='Current Weather', font=('poppins', 22), fg='#000000').place(x=55,y=140)
        self.label_humidity_value = Label(self.root, text=f'{self.final_result[8]}', font=('poppins', 22), fg='#77c9ee').place(x=650,y=240) 
        
        self.add_time()
        
    def add_time(self):
        self.time = datetime.now()
        self.string_time = self.time.strftime('%H:%M:%S %p')
        
        self.label_time = Label(self.root, text=f'{self.string_time}', fg='#000000', font=('poppins', 22)).place(x=100,y=240) 
        
        self.root.after(1000, self.add_time)


if __name__ == '__main__':
    app = Tk()
    main_class = Main(app) 
    app.mainloop()
    
    # To add menu bar and list
# https://www.youtube.com/watch?v=urTOBIXII6s&ab_channel=%D8%B9%D9%84%D8%A7%D8%A1%D8%AC%D8%A7%D8%B3%D9%85%D9%85%D8%AD%D9%85%D8%AF
# https://www.youtube.com/watch?v=bUju6_99vCw&list=PLhiFu-f80eo_JY4sO_XOB0khGVck2PUkJ&index=19&pp=iAQB&ab_channel=%D8%AA%D9%83%D9%86%D9%88U
# https://www.youtube.com/watch?v=Co8iA-wmOtw&list=PLhiFu-f80eo_JY4sO_XOB0khGVck2PUkJ&index=16&ab_channel=%D8%AA%D9%83%D9%86%D9%88U 

# to exe
# https://www.youtube.com/watch?v=fxhhv-6oftw&list=PLNKBKJ7bHHw7xUQHHppY-W2TPFWSnmVtT&index=5&ab_channel=%D8%B9%D9%84%D8%A7%D8%A1%D8%AC%D8%A7%D8%B3%D9%85%D9%85%D8%AD%D9%85%D8%AF
# https://www.youtube.com/watch?v=Lz2mWUEDJQk&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK
# https://www.youtube.com/watch?v=iCkE84jfveI&ab_channel=Al-MunthirSaffan%28%E2%80%AB%D8%A7%D9%84%D9%85%D9%86%D8%B0%D8%B1%D8%B3%D9%81%D8%A7%D9%86%E2%80%AC%E2%80%8E%29
# https://www.youtube.com/watch?v=XhLX0QIW4ZU&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK