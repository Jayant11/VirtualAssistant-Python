import pyttsx3

def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)
    engine.setProperty('rate',120)
    engine.setProperty('volume',0.9) 
    engine.runAndWait()
 
