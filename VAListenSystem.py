import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio
import audioop
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

class ListenSystem:
    def __init__(self):
        self.engine=pyttsx3.init('sapi5')
        self.engine.setProperty('rate',150)
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)
        self.listening=False
        self.working=False
        self.query=""
        self.greetings=[
            "Hello!",
            "Hi!",
            "Nice to meet you!",
            "Hey!"
        ]
        # Might use task stack tasks self.task=[]#queue the number of task to work on string

    def speak(self,audio):    
        self.engine.say(audio)
        self.engine.runAndWait()

        
    def takeCommand(self):
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source=source)
            print("Listening")
            audio = r.listen(source,timeout=5)
        
        try:
            self.query = str(r.recognize_google(audio, language ='en-in')).lower()
            self.response=True
    
        except Exception as e:
            print(e)
            self.query= "None"
       
        
    
    def intro(self):
        self.speak(random.choice(self.greetings))
        self.speak("What can I help you with?")
    def time(self):
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            self.speak("Good Morning!")
    
        elif hour>= 12 and hour<18:
            self.speak("Good Afternoon!")   
    
        else:
            self.speak("Good Evening!")  
    
        #assname =("My name is Beta version 0.01")
        #self.speak(assname)
        #self.speak("I am your Assistant... May I assist you with anything")
    
    def StopCopyingMe(self):
        self.speak(self.query)
    def testStatement(self):
        self.speak("The quick brown fox jumps over the lazy dog.")
        
    def wikiSearch(self):
        self.speak('Searching Wikipedia...')
        query = self.query.replace("wikipedia", "")
        results = wikipedia.summary(self.query, sentences = 3)
        self.speak("According to Wikipedia")
        self.speak(results)
 
    def process_action(self):
        if "hi" in self.query or "hello" in self.query:
            self.intro()            
        elif "time" in self.query:
            self.time()
        elif "wikipedia" in self.query:
            self.wikiSearch()
    


if __name__ in "__main__":
    pass

