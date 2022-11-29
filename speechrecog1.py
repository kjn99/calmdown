import speech_recognition as sr
#from PyDictionary import PyDictionary
from pydictionary import Dictionary
import pyttsx3
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    text = r.recognize_google(audio)
print("done...")
dict =Dictionary(text)
antonyms_list = dict.antonyms()
t=dict.print_antonyms()
engine = pyttsx3.init()
engine.say(t)
engine.runAndWait()

