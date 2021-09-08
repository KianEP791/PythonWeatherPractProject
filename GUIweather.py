# We will need to use "tkinter" snd "requests" packages in order to build this program

import tkinter as tkn
import requests

#############################################################

MainWindow = tkn.Tk()  # Creating the main window
MainWindow.geometry("800x550")  # Styling the main window

CityName = tkn.Entry()  # creating text field for entering the city name

txt_city_not_found = tkn.Label(master = MainWindow)  # creating a label to be displayed when city not found

txt_lbl = tkn.Label(master = MainWindow, text = "Please enter the city name below")

temperature_lbl = tkn.Label(master = MainWindow)  # a label to display the temperature we get

descript_lbl = tkn.Label(master = MainWindow)     # a label to display the description of weather

TempMin = tkn.Label(master = MainWindow)     # a label to display minimum temperature
TempMax = tkn.Label(master = MainWindow)     # a label to display maximum temperature

TempFeel= tkn.Label(master = MainWindow)     # a label to display how weather feels like

########################################################################################


def funzero():  # defining the function for a button to load the current weather data
    city = CityName.get()
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="

    api_key = 'd6256ce734c49539d7d962c79c6ac9a1'

    url = base_url + city + "&appid=" + api_key

    weather_datazero = requests.get(url)
    weather_data = weather_datazero.json()

    # If city not found/city name is not correct >>>> we get 404 error
    # If we get error 404 " Oops! City Not Found" will be displayed
    # else the data will be displayed

    if weather_data["cod"] == "404":

        txt_city_not_found.config(text=" Oops! City Not Found")
        txt_city_not_found.pack()

    else:

        b = weather_data['weather'][0]['description']
        a = weather_data['main']
        feels = round(a['feels_like']-273,1)
        min = round(a['temp_min']-273,1)
        max = round(a['temp_max']-273,1)
        temperature = a['temp']
        temperature_in_c = round(temperature - 273, 1)

        temperature_lbl.config(text="tempreture : " + str(temperature_in_c))

        temperature_lbl.pack()

        TempFeel.config(text="it feels like:" + str(feels))
        TempFeel.pack()
        TempMin.config(text=" Minimum temperature today is :" + str(min))
        TempMin.pack()

        TempMax.config(text=" Maximum temperature today is :" + str(max))
        TempMax.pack()


        descript_lbl.config(text=b)

        descript_lbl.pack()


##############################################################################


Current_Weather_Button = tkn.Button(master=MainWindow, text="Current Weather", command=funzero)

# These codes keep displaying the widgets

txt_lbl.pack()
CityName.pack()
Current_Weather_Button.pack()

MainWindow.mainloop()
