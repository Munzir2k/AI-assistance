import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am JAMES Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        quary = takeCommand().lower()
        if 'wikipedia' in quary:
            speak('Searching Wikipedia....')
            quary = quary.replace("wikipedia", "")
            result = wikipedia.summary(quary, sentences=2)
            speak("According to results ")
            print(result)
            speak(result)
        elif 'open google' in quary:
            webbrowser.get('chrome').open("google.com")
        elif 'open youtube' in quary:
            webbrowser.get('chrome').open("youtube.com")
        elif 'open instagram':
            webbrowser.get('chrome').open("instagram.com")
        else:
            speak("Try again")
