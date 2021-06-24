import speech_recognition as sr
import os, subprocess

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    if r.recognize_google(audio).lower() == "notepad":
        os.system("start notepad")
    elif r.recognize_google(audio).lower() == "youtube":
        os.system("start firefox youtube.com")
    else:
        print("Command Not Recognized.")
        print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))