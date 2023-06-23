import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



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
    speak("I am Jeff Sir. Please tell me how may I help you")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kpcool1705@gmail.com','krishpatel@1705')
    server.sendmail('20dcs080@charusat.edu.in',to,content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Please say it again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = 'C:\\Users\\SONY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "20dcs080@charusat.edu.in"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend krish bhai. I am unable to send this email")
        elif 'exit' in query:
            speak("Bye Bye Sir. Have a good day!")
            break;