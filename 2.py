import speech_recognition as sr
filename = "a.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source,duration=20)
    text = r.recognize_google(audio_data)
print(text)
print("done!")
