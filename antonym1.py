import pyttsx3
import speech_recognition as sr
from wordhoard import Antonyms

#d=Dictionary()
#print(d.meaning("college"))
#a=dict(d.meaning("school"))
#print(a["Noun"])
#b=list(a["Noun"])
#print(b[0])

r=sr.Recognizer()
filename="b.wav"
with sr.AudioFile(filename) as source:
    audio=r.listen(source,phrase_time_limit=3)
    text=r.recognize_google(audio)
    print("the query is printed='", text, "'")
antonym=Antonyms(text)
print(antonym.find_antonyms())
#dict.meanings()
#engine=pyttsx3.init();
#engine.say(antonym.find_antonyms()[0]);
#engine.runAndWait();
