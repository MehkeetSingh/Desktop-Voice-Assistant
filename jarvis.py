from email.mime import audio
from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant. Please tell how may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        # r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        speak("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google chrome' in query:
           chrompath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
           speak("opening chrome")
           os.startfile(chrompath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print("Sir, the time is: " + strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open word' in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("opening word")
            os.startfile(path)

        elif 'open powerpoint' in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            speak("opening powerpoint")
            os.startfile(path)

        elif 'say' in query:
            query = query.replace("say", "")
            speak(query)

        elif 'who' in query:
            speak("My creater is Mr Mehkeet Singh. He is a genious person")

        elif 'internet' in query:
            speak("What should I search")
            search = takeCommand()
            webbrowser.open(search)

        elif 'thank you' in query:
            speak("My pleasure")

        elif 'exit' in query:
            speak("Thank you for using me, have a nice day")
            exit()

        elif 'quit' in query:
            speak("Thank you for using me, have a nice day")
            exit()