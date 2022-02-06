import tkinter as tk
import numpy as np
import random
import time
import datetime
import threading
import Adafruit_DHT
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

pin = 2
sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)


lcd1 = 12
lcd2 = 7
lcd3 = 8
lcd4 = 25
lcd5 = 24
lcd6 = 23

lcd = LCD.Adafruit_CharLCD(lcd1,lcd2,lcd3,lcd4,lcd5,lcd6,0,16,2)

def tick():

    time3=time.strftime('%H:%M:%S')
    clock.config(text=time3)
    clock.after(200,tick)


def get_data():

    threading.Timer(5, get_data).start()

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        l_display.config(text = temperature)
        l_display1.config(text = humidity)
        l_t2=tk.Label(mainwindow, text="OK",font=("Arial",25),bg="green")
        l_t2.grid(row=3,column=1, padx=10, pady=0, sticky="nsew")
              
        lcd.clear()
        lcd.message('Temp={0:0.1f}*C  \nHumidity={1:0.1f}%'.format(temperature, humidity))
        time.sleep(1)
        #lcd.message("Temp: " + str(temperature) + "c\nHumidity: "+ str(humidity) + "%")
    else:
       print('Failed to get reading. Try again!')
       l_t2=tk.Label(mainwindow, text="Fault",font=("Arial",25),bg="red")
       l_t2.grid(row=3,column=1, padx=10, pady=0, sticky="nsew")
       
       lcd.clear()
       lcd.message("Fault")             
       time.sleep(1)
       


    return temperature
    return humidity
       



mainwindow = tk.Tk()
mainwindow.geometry('640x340')
mainwindow.title("Sensor Data Live Feed ")

clock=tk.Label(mainwindow,font=("Arial",30), bg='azure',fg="black")
clock.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

l_m=tk.Label(mainwindow,text="Sensor Data ",font=("Arial",30),fg="Black")
l_m.grid(row=0,column=1, padx=10, pady=10, sticky="nsew")

l_t=tk.Label(mainwindow, text="Temperature C",font=("Arial",25),bg='honeydew3')
l_t.grid(row=1,column=0, padx=10, pady=0, sticky="nsew")


l_display=tk.Label(mainwindow,font=("Arial",25),fg="red")
l_display.grid(row=1,column=1, padx=10, pady=10, sticky="nsew")

l_t1=tk.Label(mainwindow, text="Humidity",font=("Arial",25))
l_t1.grid(row=2,column=0, padx=10, pady=10, sticky="nsew")

l_display1=tk.Label(mainwindow,font=("Arial",25),fg="green")
l_display1.grid(row=2,column=1, padx=10, pady=10, sticky="nsew")


Status=tk.Label(mainwindow, text="Status",font=("Arial",25),bg='honeydew3')
Status.grid(row=3,column=0, padx=10, pady=0, sticky="nsew")


tick()
get_data()



#lcd = LCD.Adafruit_CharLCD(lcd1,lcd2,lcd3,lcd4,lcd5,lcd6,0,16,2)

#humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 2)
#lcd.clear()
#lcd.message("Temp: " + str(temperature) + "c\nHumidity: "+ str(humidity) + "%")
#time.sleep(1)
#print("Temp: " + str(temperature) + "c\nHumidity: "+ str(humidity) + "%")


mainwindow.mainloop()
