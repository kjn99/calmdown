from wordhoard import Antonyms
from wordhoard import Synonyms
from pydictionary import Dictionary
#from englisttohindi.englisttohindi import EngtoHindi
import pyttsx3
import speech_recognition as sr
r=sr.Recognizer()
filename="b.wav"
with sr.AudioFile(filename) as source:
    audio=r.listen(source,phrase_time_limit=3)
    text=r.recognize_google(audio)
    print("the query is printed='", text, "'")


dict=Dictionary(text)
synonym=Synonyms(text)
antonym=Antonyms(text)
#d=pydictionary()
print(f'Meaning of word{dict.meanings()[0]}')
print(f'Synonyms of given :- {synonym.find_synonyms()[0]}')
print(f'Antonyms of given:-{antonym.find_antonyms()[0]}')
#dict.meanings
engine=pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.say(dict.meanings()[0])
engine.say(synonym.find_synonyms()[0])
engine.say(antonym.find_antonyms()[0])
engine.runAndWait()
