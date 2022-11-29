import speech_recognition as sr
from translate import Translator
r=sr.Recognizer()
filename="b.wav"
with sr.AudioFile(filename) as source:
    audio=r.listen(source,phrase_time_limit=3)
    text=r.recognize_google(audio)
    print("the query is printed='", text, "'")
translator =Translator(to_lang="hi")
translation = translator.translate(text)
print(translation)
