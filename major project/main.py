import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d093053d72bc40248998159804e0e67d"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif  "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif  "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif  "open harsh channel" in c.lower():
        webbrowser.open("https://www.youtube.com/@harsh_dalal")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 
        
if __name__ == "__main__":
    speak("Initializing harshit....")
    while True:
        # Listen for the wake word "harshit"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "harshit"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                  print("harshit active....")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)

                  processcommand(command)
       
       
        except Exception as e:
          print("error; {0}".format(e))
            