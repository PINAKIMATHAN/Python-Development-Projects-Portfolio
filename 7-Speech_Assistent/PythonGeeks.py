import speech_recognition as sr

import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk


class assistance_gui:
    def __init__(self,root):
        self.root = root
        self.root.title("Pinaki Voice Assistant")
        self.root.geometry('600x600')
        self.root.config(bg='#76EEC6')

        self.bg = ImageTk.PhotoImage(file="images/background.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="images/frame_image.png")
        left = Label(self.root, image=self.centre).place(x=100, y=100, width=400, height=400)

        start = Button(self.root, text='START', bg='#010b3d', fg='#f7c705', font = ("times new roman bold", 14), command=self.start_option).place(x=150, y=520)

        close = Button(self.root, text='CLOSE', bg='#fa342d', fg='#f7c705', font = ("times new roman bold", 14), command=self.close_window).place(x=350, y=520)

    def start_option(self):
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def start():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                wish = "Good Morning!"
            elif hour >= 12 and hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            speak('Hello Sir,' + wish+' I am your voice assistant. Please tell me how may I help you')

        def take_command():
            try:
                with sr.Microphone() as data_taker:
                    print("Say Something")
                    voice = listener.listen(data_taker)
                    instruction = listener.recognize_google(voice)
                    instruction = instruction.lower()
                    return instruction
            except:
                pass

        def run_command():
            instruction = take_command()
            print(instruction)
            try:
                if 'who are you' in instruction:
                    speak('I am your personal voice Assistant')

                elif 'what can you do for me' in instruction:
                    speak('I can play songs, tell time, and help you go with wikipedia')

                elif 'current time' in instruction:
                    time = datetime.datetime.now().strftime('%I: %M')
                    speak('current time is' + time)

                elif 'what is your name' in instruction:
                    speak('I have no name I am your personal voice Assistant')

                elif 'do you have any siblings' in instruction:
                    speak('Yes I have one sister')

                elif 'have you fed your pets or animals today' in instruction:
                    speak('Yes I fed my pets this morning before leaving the house')

                elif 'how was your weekend' in instruction:
                    speak('It was good thanks for asking. How about yours')

                elif 'have you taken a walk or been outside today' in instruction:
                    speak('Yes I went for a walk during my break to get some fresh air')

                elif 'thank you so much I appreciate it' in instruction:
                    speak('You re welcome glad to help')
   
                elif 'open google' in instruction:
                    speak('Opening Google')
                    webbrowser.open('google.com')

                elif 'open youtube' in instruction:
                    speak('Opening Youtube')
                    webbrowser.open('youtube.com')

                elif 'open facebook' in instruction:
                    speak('Opening Facebook')
                    webbrowser.open('facebook.com')

                elif 'open python geeks' in instruction:
                    speak('Opening PythonGeeks')
                    webbrowser.open('pythongeeks.org')

                elif 'open linkedin' in instruction:
                    speak('Opening Linkedin')
                    webbrowser.open('linkedin.com')

                elif 'open gmail' in instruction:
                    speak('Opening Gmail')
                    webbrowser.open('gmail.com')

                elif 'open stack overflow' in instruction:
                    speak('Opening Stack Overflow')
                    webbrowser.open('stackoverflow.com')

                elif 'what is your favorite TV show?' in instruction:
                    speak('My favorite TV show is Game of Thrones')

                elif 'would you like a cup of coffee' in instruction:
                    speak('Yes please Thank you')

                elif 'have you smiled or laughed today' in instruction:
                    speak('Yes I smiled and laughed during a conversation with a colleague')

                elif 'did you express gratitude for something or someone today' in instruction:
                    speak('Yes I expressed gratitude for having a supportive family and friends during a conversation')

                elif 'how old are you' in instruction:
                    speak('I am a robot I am alive till you dont disturb')

                elif 'whats your favorite mobile' in instruction:
                    speak('My favorite movie is iPhone 11')

                elif 'how is your day going so far' in instruction:
                    speak('Its going pretty well thanks for asking How about yours')

                elif 'have you checked the weather forecast for the day' in instruction:
                    speak('Yes I checked the weather forecast this morning to know what to expect for the day')

                elif 'shutdown' in instruction:
                    speak('I am shutting down')
                    self.close_window()
                    return False
                else:
                    speak('I did not understand, can you repeat again')
            except:
                speak('Waiting for your response')
            return True

        start()

        while True:
            if run_command():
                run_command()
            else:
                break


    def close_window(self):
        self.root.destroy()

root = Tk()


obj=assistance_gui(root)

root.mainloop()
