import pyttsx3 as pt
from time import sleep
f = open("sample.txt","r")
file = f.readlines()
start = pt.init()
for i in file:
    start.say(i)
    start.runAndWait()
    sleep(1)

f.close()
