from pydictionary import Dictionary
import pyttsx3
import speech_recognition as sr
import os
#d=Dictionary()

#print(d.meaning("college"))
#a=dict(d.meaning("school"))
#print(a["Noun"])
#b=list(a["Noun"])
#print(b[0])

r=sr.Recognizer()
with sr.Microphone() as source:
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print("the query is printed='", text, "'")
dict=Dictionary(text)
#dict.meanings()
engine=pyttsx3.init()
meaning=dict.meanings()
print(meanings[0])
engine.say(meaning)
engine.runAndWait()
