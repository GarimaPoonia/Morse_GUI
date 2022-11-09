## AUTHOR : Garima
## TASK : 5.3D (To build a GUI interface on raspberry pi which takes input as text from the user, and the led blinks the text in morse code )

#imports specified libraries
from ast import keyword  
from tkinter import *
import tkinter.font
from gpiozero import LED
import time
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

#defining the dimensions of window
window = Tk()
window.title("Morse Code Calculator")
window.geometry("280x170")
myFont = tkinter.font.Font(family = 'Helvetica', size = 10, weight = 'bold')
led = LED(17)

Code = {'A' : '.-' ,'B' : '-...' ,'C' : '-.-.' ,'D' : '-..' ,'E' : '.' ,
'F' : '..-.' ,'G' : '--.' ,'H' : '....' ,'I' : '..' ,'J' : '.---' ,
'K' : '-.-' ,'L' : '.-..' ,'M' : '--' ,'N' : '-.' ,'O' : '---' ,
'P' : '.--.' ,'Q' : '--.-' ,'R' : '.-.' ,'S' : '...' ,'T' : '-' ,
'U' : '..-' ,'V' : '...-' ,'W' : '.--' ,'X' : '-..-' ,'Y' : '-.--' ,'Z' : '--..'}

def Dash():
    led.on()
    time.sleep(0.9)   # the ratio for dot and dash is 1:3
    led.off()
    time.sleep(0.3)
    print("Dash")
    
def Dot():
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
    print("Dot")

#takes input from user in form of text and calculates its morse code  
def MorseCode():
    text = Text_Box.get('1.0','end-1c')
    if len(text) > 12 or len(text) < 0:      #limiting the word length
        led.off()
        print("Please enter a shorter text.")
        print("Word limit - ") 
        return
    else:
        print("Calculating morse code...")
        time.sleep(1)
    for alphabet in text:
        for dot_dash in Code[alphabet.upper()]:
            if dot_dash == '-':
                Dash()
            elif dot_dash == '.':
                Dot()
            else:
                time.sleep(0.13)
        time.sleep(1) 

# closes the current opened window
def exit():
    window.destroy()

Label(window, text = 'Enter name', bg = 'bisque2', font = myFont, height = 1, width = 35).grid(row = 0, column = 1)

Text_Box = Text(window, height = 1, width = 30, bg = 'grey')
Text_Box.grid(row = 1, column = 1, padx = 20, pady = 10)

submitButton = Button(window, text = 'Submit', font = myFont, command = MorseCode, bg = 'white')
submitButton.grid(row = 3, column = 1)

Exit_Button = Button(window, text = 'Exit', font = myFont, command = exit, height = 1, width = 6)
Exit_Button.grid(row = 4, column = 1)

window.mainloop()
