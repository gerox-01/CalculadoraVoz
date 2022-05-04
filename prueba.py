import gtts 
from win32com.client import Dispatch
import speech_recognition as sr

r = sr.Recognizer()
def speak(str):
    speak = Dispatch.Dispatch("SAPI.SpVoice")
    speak.Speak(f'Okay. Answer is {str}')

def listen():
    print('listening...')
    with sr.Microphone() as source:
        audio = r.listen(source)
        MyText = r.recognize_google(audio)
        print(MyText)
        return MyText

if __name__ == '__main__':
    words = listen()
    x = words.split()

    if(x[1] == '+'):
        num1 = float(x[0])
        num2 = float(x[2])
        print(num1 + num2)
        speak(num1 + num2)
    elif(x[1] == '-'):
        num1 = float(x[0])
        num2 = float(x[2])
        print(num1 - num2)
        speak(num1 - num2)
    elif(x[1] == '*'):
        num1 = float(x[0])
        num2 = float(x[2])
        print(num1 * num2)
        speak(num1 * num2)
    elif(x[1] == '/'):
        num1 = float(x[0])
        num2 = float(x[2])
        print(num1 / num2)
        speak(num1 / num2)
    else:
        print('Invalid operation')
        speak('Invalid operation')