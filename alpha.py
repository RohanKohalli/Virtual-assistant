import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import wolframalpha
import json
from urllib.request import urlopen
import time
import requests

engine = pyttsx3.init()

# wolframalpha_app_id = "KKX4RG-UEJRYEGAKX"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# current time
def time_():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(time)


# current date
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 11:
        speak("Good morning rohan")
    elif 12 <= hour <= 15:
        speak("Good afternoon rohan")
    elif 16 <= hour <= 19:
        speak("Good Evening rohan")
    else:
        speak("Good night rohan")
    speak("Alpha, At your service. Please tell me how can i help you today?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say again please....")
        return "none"
    return query


# battery details
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def whoami():
    speak("I am alpha,automated bot made by rohan")


def task():
    speak('I can take screenshot search on ecosia, youtube and browse wikipedia.'
          'I can read news for you and also i can open any application for you')


def joke():
    speak(pyjokes.get_joke())
    print(pyjokes.get_joke())


def screenshot():
    img = pyautogui.screenshot()
    speak('What name should i give to file')
    file_name = input("Enter the file name with extension(.jpg,.png,.jpeg):")
    img.save(file_name)


if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand().lower()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'search web' in query:
            speak('what should i search?')
            wbpath = 'C:/Program Files(%86)/Firefox.exe %s'
            search = takecommand().lower()
            wb.get(wbpath).open_new_tab(search + '.com')

        elif 'search youtube' in query:
            speak('what should i search?')
            search_term = takecommand().lower()
            speak("searching in youtube...")
            wb.open("https://www.youtube.com/results?search_query=" + search_term)

        elif 'search ecosia' in query:
            speak("what should i search?")
            search_term = takecommand().lower()
            speak("searching...")
            wb.open("https://www.ecosia.org/search?q=" + search_term)

        elif 'who are you' in query:
            whoami()

        elif 'what can you do' in query:
            task()

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'close' in query:
            speak('going offline')
            quit()

        elif 'telegram' in query:
            speak('opening telegram')
            telegram = r'C:\Users\rohan\AppData\Roaming\Telegram Desktop\Telegram.exe'
            os.startfile(telegram)

        elif 'whatsapp' in query:
            speak('opening whatsapp..')
            whatsapp = r"C:\Users\rohan\AppData\Local\WhatsApp\WhatsApp.exe"
            os.startfile(whatsapp)

        elif 'zoom' in query:
            speak('opening zoom..')
            zoom = r"C:\Users\rohan\AppData\Roaming\Zoom\bin\Zoom.exe"
            os.startfile(zoom)

        elif 'write a note' in query:
            speak("what should i write?")
            note = takecommand()
            file = open('note.txt', 'a')
            speak("should i include date and time")
            ans = takecommand()
            if 'yes' in ans or 'sure' in ans:
                strtime = datetime.datetime.strftime("%H:%M:%S")
                file.write(strtime)
                file.write(":-")
                file.write(note)
                speak("done taking notes?")
            else:
                file.write(note)

        elif 'show note' in query:
            speak("showing notes")
            file = open('note.txt')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            speak('taking screenshot..')
            screenshot()

        elif 'remember' in query:
            speak('what should i remember?')
            memory = takecommand()
            speak('you asked me to remember that' + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember' in query:
            remember = open('memory.txt', 'r')
            speak("you asked me to remember that" + remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=46e1aede2ab7413190d392"
                                  "22f9f5dfb6")
                data = json.load(jsonObj)
                i = 1

                speak('Here are some of the top news from techcrunch')
                print("##########TOP HEADLINES##############" + "\n")
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("you have asked to locate" + location)
            wb.open_new_tab("https://maps.mapmyindia.com/search=" + location)

        elif 'calculate' in query:
            client = wolframalpha.Client("KKX4RG-UEJRYEGAKX")
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("the answer is" + answer)
            speak("the answer is " + answer)

        elif 'what is' in query or 'define' in query:
            client = wolframalpha.Client("KKX4RG-UEJRYEGAKX")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("no results")

        elif 'stop listening' in query:
            speak('for how many seconds you want me to stop listening')
            ans = int(takecommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
