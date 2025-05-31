import pyttsx3
list=["Super Sarah","Able Omkar","Bhati","Sike",""]
engine=pyttsx3.init()
engine.setProperty("rate",150)
voices = engine.getProperty('voices')
# for index ,voice in enumerate(voices):
#     print(f"voice:{index}")
#     print(f"(id:{voice.id})")
engine.setProperty('voice', voices[1].id)
for i in list:
    message=(f"Hello youtuber {i}")
    print(message)
    engine.say(message)
    engine.runAndWait()