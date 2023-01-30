import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not understand..")

def speechtxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if "hello joy" in sptext().lower():
        while True:
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is joy"
                speechtxt(name)
            elif "how old are you" in data1:
                age = "i am two year old"
                speechtxt(age)
            elif 'now time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtxt(time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'linkedin' in data1:
                webbrowser.open("https://www.linkedin.com/in/neelesh-vaishnav-b6109b1a6/")
            elif 'jokes' in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtxt(joke_1)
            elif "exit" in data1:
                speechtxt("thankyou")
                break
            time.sleep(6)
    else:
        speechtxt("thanks")



