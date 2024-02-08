import speech_recognition as sr
import pyttsx3


listener=sr.Recognizer()
engine=pyttsx3.init()
engine.say("hai sir")
engine.runAndWait()
engine.say("how can i help you")
engine.runAndWait()

try:
      with sr.Microphone() as source:
        print("start speaking dude!")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)  # type: ignore
        command =command.lower()
        if '' in command :
            print(command)
            
except:
    pass   