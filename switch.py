# from wordhoard import Antonyms,Synonyms
from pydictionary import Dictionary # https://pypi.org/project/Py-Dictionary/
import speech_recognition as sr
import threading
import pyttsx3


engine=pyttsx3.init()
#engine.say('speak')
engine.runAndWait()
r=sr.Recognizer()
filename="b.wav"
with sr.AudioFile(filename) as source:
    audio=r.listen(source,phrase_time_limit=3)
    text=r.recognize_google(audio)
    print("the query is printed='", text, "'")


def choice():
    print('What do u want say 1 for antonym 0 for synonym')
    # engine.say('What do u want say 1 for antonym 0 for synonym')
    r=sr.Recognizer()
filename="b.wav"
with sr.AudioFile(filename) as source:
    audio=r.listen(source,phrase_time_limit=3)
    text=r.recognize_google(audio)
    print("the query is printed='", text, "'")


# threading.Thread(target=choice)
# threading.Thread(target=speak_to_inform)


def antonym(text):
    dict = Dictionary(str(text))
    antonyms_list = dict.antonyms()
    print(antonyms_list)
    #Audio---------------------------
    engine=pyttsx3.init()
    engine.say(antonyms_list)
    engine.runAndWait()

def synonym(text):
    dict = Dictionary(str(text))
    meanings_list = dict.meanings()
    print(meanings_list)  
    #Audio---------------------------
    engine=pyttsx3.init()   
    engine.say(meanings_list)
    engine.runAndWait()    


# threading.Thread(synonym)
if choice()==1:
    antonym(text)
else:
    synonym(text)
