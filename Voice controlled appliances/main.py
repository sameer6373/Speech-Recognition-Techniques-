import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Simulated appliances
appliances = {
    "light": False,
    "fan": False,
    "tv": False,
    "ac": False
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def control_appliance(command):
    for appliance in appliances:
        if f"turn on {appliance}" in command:
            appliances[appliance] = True
            speak(f"{appliance.capitalize()} is now ON.")
            return
        elif f"turn off {appliance}" in command:
            appliances[appliance] = False
            speak(f"{appliance.capitalize()} is now OFF.")
            return
    speak("Command not recognized. Try again.")

if __name__ == "__main__":
    speak("Voice controlled appliance system initiated.")
    while True:
        cmd = listen_command()
        if "exit" in cmd or "stop" in cmd:
            speak("Exiting. Goodbye!")
            break
        control_appliance(cmd)
