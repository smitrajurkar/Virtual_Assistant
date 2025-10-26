#importing required modules
import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser

#create enginr for text to speech
engine = pyttsx3.init()
engine.setProperty('rate',175)


#speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


#command taking function
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio) #audio to text 
            command = command.lower()
            print("You said:", command)
            return command
        except:
            return ""

#create run assistant function
def run_assistant():
    command = take_command()

    #in command it have time word
    if "time" in command:
        time = datetime.datetime.now().strftime("%I : %M : %P")
        speak(f"The current time {time}")
    #date in command returns the current date 
    elif "date" in command:
        date = datetime.date()
        speak(f"Today date is {date}")
#open notepad
    elif "open notepad" in command:
        speak("opening notepad")
        os.system('notepad')
    elif "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
    #search for any query
    elif "hey siri" in command:
        query = command.replace("hey siri","")
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Looking for {query}")
            webbrowser.open(url)
    elif "bye" in command or "stop" in command:
        speak("Ok bye")
        exit()
    else:
        speak("I am here to assist you, ask to open youtube, open notepad, time or date")

#main function
if __name__=="__main__":
    speak("Hey Buddy hi,today i am here to assists youn in opening youtube opening notepad like any query")
    while True:
        run_assistant()