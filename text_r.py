import pyttsx3 as tx

buddy = tx.init()

voices = buddy.getProperty('voices')
buddy.setProperty('voice', voices[1].id)

text = input('Enter Your Text Here =>')
buddy.say(text)

buddy.runAndWait()
buddy.stop()