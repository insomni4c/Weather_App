import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

#f3668e0a861f3f155e676393b7a4a2b4
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (in Celcius): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving the weather'

    return final_str

def get_weather(city):
    weather_key = 'f3668e0a861f3f155e676393b7a4a2b4'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root=tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='pic1.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

frame=tk.Frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5, rely=0.03,relwidth=0.55,relheight=0.1,anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button=tk.Button(frame, text="Get Weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0.0,relwidth=0.3,relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5,rely=0.65, relwidth=0.55, relheight=0.2, anchor='n')

label=tk.Label(lower_frame, font=('Lucida Sans', 15), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()