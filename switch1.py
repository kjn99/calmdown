# from wordhoard import Antonyms,Synonyms
from pydictionary import Dictionary # https://pypi.org/project/Py-Dictionary/
import speech_recognition as sr
import threading
import pyttsx3


engine=pyttsx3.init()
engine.say('speak')
engine.runAndWait()
r=sr.Recognizer()
with sr.Microphone() as source:
    audio= r.listen(source,phrase_time_limit=3)
    text = r.recognize_google(audio)#,language="hi-IN")
    print(text)


def choice():
    print('What do u want say 1 for antonym 0 for synonym')
    # engine.say('What do u want say 1 for antonym 0 for synonym')
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source,phrase_time_limit=3)
        text1 = r.recognize_google(audio)#,language="hi-IN")
        print("your choice",text1)
        return int(text1)


# threading.Thread(target=choice)
# threading.Thread(target=speak_to_inform)


def antonym(text):
    dict = Dictionary(str(text))
    antonyms_list = dict.antonyms()
    print(antonyms_list[0])
    #Audio---------------------------
    engine=pyttsx3.init()
    engine.say(antonyms_list[0])
    engine.runAndWait()

def synonym(text):
    dict = Dictionary(str(text))
    meanings_list = dict.synonyms()
    print(meanings_list[1])  
    #Audio---------------------------
    engine=pyttsx3.init()   
    engine.say(meanings_list[1])
    engine.runAndWait()    


# threading.Thread(synonym)
if choice()==1:
    antonym(text)
else:
    synonym(text)
