from time import ctime
import time
import datetime
import os
import subprocess
import webbrowser
import re
import sys
from speaker import speak

def mind(data):

    if any(c in data for c in ("hi", "hello", "hey")):
        speak("Hi Jayant")

    if any(c in data for c in ("what's up", "whats up", "WhatsApp")):
        speak("nothing much")
    
    if "how are you" in data:
        speak("I am fine")

    if any(c in data for c in ("what can you do", "what to do", "do something")):
        speak("You can ask me to do the following tasks :")
 
    if any(c in data for c in ("what time is it", "what's the time")):
        current_time = time.localtime()
        hour = time.strftime('%H', current_time)
        if(hour=="0"):
            stime = time.strftime('%H:%M %p', current_time)
            speak("It is " + stime)
        else:
            stime = time.strftime('%I:%M %p', current_time)
            speak("It is " + stime)

    if any(c in data for c in ("night", "shift")):
        ##if night_shift.
        speak("night shift is on")

    if any(c in data for c in ("book", "lunch", "at")):
        place = data.split("at ")
        speak("Please wait while I'm booking our lunch at "+place)
        url = "https://www.google.nl/maps/place/" + place + "/&amp;"
        webbrowser.open(url)

    if any(c in data for c in ("book", "tickets", "flight", "from", "to")):
        data1 = data.split("from ")
        fr = data1[1]
        data2 = data.split("to ")
        to = data2[1]
        speak("Please wait while I'm booking our flight")
        url = "https://www.google.com/flights/flights-from-"+fr+"-to-"+to+".html?gl=us"
        webbrowser.open(url)
 
    if "where is" in data:
        data = data.split(" ")
        location = data[-1]
        speak("HPlease hold on, I will show you where " + location + " is.")
        url = "https://www.google.nl/maps/place/" + location + "/&amp;"
        webbrowser.open(url)

    if "what is" in data:
        data = data.split("is ")
        ask = data[1]
        url = "https://www.google.co.in/search?q=" + ask + "&sourceid=chrome&ie=UTF-8"
        webbrowser.open(url)
        speak("I found this on the web for" + ask)

    if any(c in data for c in ("play", "music")):
        ##
        speak("playing"+"music")

    #if any(c in data for c in ("play")):
#        raw = data
#        data = data.split("play ")
#        song = data[1]
#        speak("now playing "+song)
#        url = "https://play.google.com/music/listen?u=0#/sr/"+song
#        webbrowser.open(url)
        
    if "open" in data:
        raw = data
        data = data.split("open ")
        app = data[-1]
        if "open I" in raw:
            app_name = "i" + app
        else:
            app_name = app
        subprocess.Popen(["/usr/bin/open", "-W", "-n", "-a", "/Applications/"+app_name+".app"])
        speak("opening "+app_name)
        time.sleep(0.5)

    if "close" in data:
        raw = data
        data = data.split(" ")
        app = data[-1]
        if any(c in raw for c in ("close I ", "closer")):
            app = app[0].upper() + app[1:]
            app_name = "i" + app
        else:
            app_name = app
        os.system("pkill -9 "+app_name)
        speak("closed "+app_name)
        
    if "shutdown" in data:
        speak("Shutting down")
        sys.exit("Shut Down!")
