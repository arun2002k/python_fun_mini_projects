import pyttsx3
import wikipedia
import voice 

voice = pyttsx3.init()
In = input("Searching -/-.... : ")
res = wikipedia.summary(In, sentences = 10)
print(res)
voice.say(res)
voice.runAndWait()
