from tkinter import *
from PIL import Image
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning sir") 
        window.update()
        speak("Good Morning sir")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon sir!")
        window.update()
        speak("Good Afternoon sir!")
    else:
        var.set("Good Evening sir")
        window.update()
        speak("Good Evening sir!")
    speak("I am Anu ! How may I help you sir") 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()

        if 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            var.set('opening google sir')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            var.set('opening facebook sir')
            window.update()
            speak("opening facebook sir")
            webbrowser.open("facebook.com")

        elif 'open blogger' in query:
            var.set('opening blogger sir')
            window.update()
            speak("opening blogger sir")
            webbrowser.open("blogger.com")

        elif 'open gmail' in query:
            var.set('opening gamil sir')
            window.update()
            speak("opening gmail sir")
            webbrowser.open("gmail.com")

        elif 'hello' in query:
            var.set("Hello Sir ! How may i help you ?")
            window.update()
            speak("Hello Sir ! How may i help you ?")
			
        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby;Born on 18 Jan 2020")
            window.update()
            speak("I am a little baby;Born on 18 Jan 2020")

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" 
            os.startfile(path)

        elif 'open project ppt' in query:
            var.set("opening your project ppt sir")
            window.update()
            speak("opening your project ppt sir")
            path = "C:\\Users\\lenovo\\Desktop\\virtual assistant\\my desktop assistant.pptx"
            os.startfile(path)
            
        elif 'close ppt' in query:
            speak("closing ppt sir")
            path="C:\\Users\\lenovo\\Desktop\\virtual assistant\\my desktop assistant.pptx"
            os.system('TASKKILL /F /IM my desktop assistant')

        elif 'your name' in query:
            var.set("Myself Anu007 Sir")
            window.update()
            speak('myself Anu007 sir')

        elif 'who is your creator' in query:
            var.set('My Creator is Mr. Abhijit Dusane')
            window.update()
            speak('My Creator is Mr. Abhijit Dusane')

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Jarvis')
            window.update()
            speak('Hello Everyone! My self Anu007')

        elif 'open code' in query:
            speak("opening code for you sir")
            codepath = "C://Users//lenovo//AppData//Local//Programs//Microsoft VS Code//Code.exe"
            os.startfile(codepath)
        
        elif 'close code' in query:
            speak("closing code sir")
            codepath = "C://Users//lenovo//AppData//Local//Programs//Microsoft VS Code//Code.exe"
            os.system('/F /IM code.exe')

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe" 
            os.startfile(path)

        elif 'close chrome' in query:
            speak("closing chrome sir")
            path="C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
            os.system('TASKKILL /F /IM chrome.exe')

        elif 'open firefox' in query:
            speak("opening firefox sir")
            firefoxpath="C://Program Files (x86)//Mozilla Firefox//firefox.exe"
            os.startfile(firefoxpath)
        elif 'close firefox' in query:
            speak("closing firefox sir")
            firefoxpath="C://Program Files (x86)//Mozilla Firefox//firefox.exe"
            os.system('TASKKILL /F /IM firefox.exe')
        
        
        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'G://music' 
            songs = os.listdir(music_dir)
            n = random.randint(0,20)
            os.startfile(os.path.join(music_dir, songs[n]))
     
        elif 'play movies' in query:
            var.set('playing movies for you sir')
            window.update
            speak("playing movies for you sir ")
            movies_dir = 'H://movies'
            movies = os.listdir(movies_dir)
            n = random.randint(0,78)
            os.startfile(os.path.join(movies_dir,movies[n]))

        elif 'open photos' in query:
            var.set('opening photos sir')
            window.update()
            speak("opening photos sir")
            photos_dir = 'D://photos'
            photos= os.listdir(photos_dir)
            n = random.randint(0,3)
            os.startfile(os.path.join(photos_dir,photos[n]))

        elif 'stop' in query:
            var.set("Good bye sir ! Have a good day !")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Good bye sir ! Have a good day ! ")
            break

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Impact", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Impact", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='G:/virtual assistant/Assistant.gif', format = 'gif -index %i' %(i)) for i in range(100)]  
window.title('MY PERSONAL ASSISTANT')

label = Label(window,width = 420 , height = 450,highlightcolor = '#ff6600',)
label.pack()
window.after(0, update, 0)
btn0 = Button(text = 'WISH ME',width =50, command = wishme, bg = '#0099e6')
btn0.config(font=("Impact", 14))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 50,command = play, bg = '#ff6600')
btn1.config(font=("Impact", 14) )
btn1.pack()
btn2 = Button(text = 'EXIT',width = 50, command = window.destroy, bg = '#0099e6')
btn2.config(font=("Impact", 14))
btn2.pack()


window.mainloop()
