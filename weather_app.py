import tkinter
from tkinter import *
import requests
import datetime
import json
import urllib.request
r = requests.get(url='http://api.openweathermap.org/data/2.5/weather?q=delhi&mode=json&units=metric&APPID=2efd491f1f84e0b152d447db126f55ca')
json_data= r.json()
def fetch_data():
    city_name = city_entry.get()
    data_output(data_organizer(data_fetch(url_builder(city_name))))
def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
    return converted_time
def url_builder(city_name):
    user_api = '2efd491f1f84e0b152d447db126f55ca'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?q='  # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz
    full_api_url = api + str(city_name) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url
# http://api.openweathermap.org/data/2.5/weather?id=1273294&mode=json&units=metric&APPID=2efd491f1f84e0b152d447db126f55ca
def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    print(output)
    raw_api_dict = json.loads(output)
    #print(raw_api_dict)
    url.close()
    return raw_api_dict
def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    '''print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')'''
    city_lab = Label(frame, text="City:",font='Helvetica 16 bold italic')
    city_lab.grid(row=5,column=0)
    city_data.config(text=data['city'])
    city_data.grid(row=5,column=1)
    country_data.config(text=data['country'])
    country_data.grid(row=5, column=2)
    sky_lab = Label(frame, text="Sky",bg='white',font='Times')
    sky_lab.grid(row=6, column=0)
    sky_data.config(text=str(data['sky']))
    sky_data.grid(row=6, column=1)
    temp_max_lab = Label(frame, text="Max.Temp.",bg='white',font='Times')
    temp_max_lab.grid(row=7, column=0)
    temp_max.config(text=str(data['temp_max'])+m_symbol)
    temp_max.grid(row=7, column=1)
    temp_min_lab=Label(frame, text="Min.Temp.",bg='white',font='Times')
    temp_min_lab.grid(row=8, column=0)
    temp_min.config(text=str(data['temp_min'])+m_symbol)
    temp_min.grid(row=8, column=1)
    humidity_lab = Label(frame, text="Humidity",bg='white',font='Times')
    humidity_lab.grid(row=9, column=0)
    humidity_data.config(text=str(data['humidity']))
    humidity_data.grid(row=9,column=1)
    pressure_lab = Label(frame, text="Pressure",bg='white',font='Times')
    pressure_lab.grid(row=10, column=0)
    pressure_data.config(text=str(data['pressure']))
    pressure_data.grid(row=10,column=1)
    sunrise_lab = Label(frame, text="Sunrise",bg='white',font='Times')
    sunrise_lab.grid(row=11, column=0)
    sunrise_data.config(text=str(data['sunrise']))
    sunrise_data.grid(row=11, column=1)
    sunset_lab = Label(frame, text="Sunset",bg='white',font='Times')
    sunset_lab.grid(row=12, column=0)
    sunset_data.config(text=str(data['sunset']))
    sunset_data.grid(row=12, column=1)
    wind_lab = Label(frame, text="Wind",bg='white',font='Times')
    wind_lab.grid(row=13, column=0)
    wind_data.config(text=str(data['wind']))
    wind_data.grid(row=13, column=1)
    cloudiness_lab = Label(frame, text="Cloudiness",bg='white',font='Times')
    cloudiness_lab.grid(row=14, column=0)
    cloudiness_data.config(text=str(data['cloudiness']))
    cloudiness_data.grid(row=14, column=1)

m = Tk(className=' Weather Forecast')
frame = Frame(m, bg='white')
frame.pack()
#w = Canvas(frame, width=200, height=100, bg='lavender')
#w.pack(side=TOP)
#T = Text(frame, height=20, width=30, bg='white')
#T.pack()
# T.insert(END, fetch_data())
city_label = Label(frame,text="Enter city: ", bg='white')
city_label.grid(row=0,column=0)
city_entry = Entry(frame)
city_entry.grid(row=0,column=1)
show = Button(frame,text="Show Weather", bg='white',fg='black',activeforeground='grey', command=fetch_data)
show.grid(row=1, column=1)
city=Label(frame)
city_data = Label(frame)
country_data= Label(frame)
temp_max = Label(frame)
temp_min = Label(frame)
humidity_data = Label(frame)
pressure_data = Label(frame)
sky_data = Label(frame)
sunrise_data = Label(frame)
sunset_data = Label(frame)
wind_data = Label(frame)
cloudiness_data = Label(frame)
m.mainloop()
