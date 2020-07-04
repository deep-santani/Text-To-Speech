# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 09:50:43 2020

@author: deep
"""

from tkinter import *
import pyttsx3

root = Tk()
root.title("Text-to-Speech.com")
root.geometry("800x500")
root.iconbitmap('E:/3.Extra Education/Python/Text to speech/fan.ico')

def talk():
    engine = pyttsx3.init()
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0,END)

my_entry = Entry(root, font=("Helvetica", 28))
my_entry.pack(pady=20)

my_button= Button(root, text="Speak", command=talk)
my_button.pack(pady=20)

