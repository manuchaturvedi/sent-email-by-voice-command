import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("and the current time is")
    speak(Time)


def date_():
    year =datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)
    time_()


def wishme():
    speak("welcome back mach!")
    date_()    
    
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<=12:
        speak("good morning sir!")
    elif hour>=12 and hour<=18:
        speak("good afternoon sir!")
    elif hour>=18 and hour<=24:
        speak("good evening sir!")
    else:
        speak("good night sir")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        speak("listening")

        r.pause_threshold = 1 
        audio=r.listen(source)

    try:
        print("Recognizing... " )
        speak("Recognizing ...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
        speak(query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "None"
    return query

def sendmail(to,content):
    server=smtplib.SMTP('smtp.email.com',587, timeout=120)
    server.ehlo()
    server.starttls()
    server.login('28manuchaturvedi@gmail.com','9893941930')
    server.sendmail('28manuchaturvedi@gmail.com',to,content)
    server.close()

if __name__=="__main__":


    while True:
        query= takeCommand().lower()
         
        #All commands will be stored in lower case in query
        #for easy recognition

        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak("searching...")
            query=query.replace('wikipedia...','')
            result=wikipedia.summary(query,sentences=3)
            speak('according to wikipedia')
            print(result)

        elif 'send email' in query:
            try:
                speak("what should i write?")
                content=takeCommand()
                #provide reciever email address
                reciever='manuchaturvedi28mc@gmail.com'
                sendmail(reciever,content)
                speak(content)
                speak('email has been sent.')
            except Exception as e:
                print(e)
                speak("unable to send email.")
                



    