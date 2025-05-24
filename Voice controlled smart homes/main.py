import speech_recognition as sr
import pyttsx3
from home_config import home

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)
        return command
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def control_home(command):
    for room, appliances in home.items():
        for appliance in appliances:
            if f"turn on {appliance} in {room}" in command:
                home[room][appliance] = True
                speak(f"{appliance} in {room} turned on.")
                return
            elif f"turn off {appliance} in {room}" in command:
                home[room][appliance] = False
                speak(f"{appliance} in {room} turned off.")
                return
    if "status" in command:
        for room, devices in home.items():
            for device, state in devices.items():
                status = "on" if state else "off"
                speak(f"{device} in {room} is {status}.")
        return
    speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Smart Home system activated.")
    while True:
        command = listen_command()
        if "exit" in command or "stop" in command:
            speak("Exiting Smart Home system.")
            break
        control_home(command)
