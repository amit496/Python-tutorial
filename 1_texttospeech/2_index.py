import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.say('Hello, welcome to Python programming!')
engine.runAndWait()