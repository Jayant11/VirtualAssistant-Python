import time
from recorder import recordAudio
from jarvis import mind
from speaker import speak


# initialization
time.sleep(1)
speak("Hi Jayant!")
while 1:
    data = recordAudio()
    mind(data)

    
