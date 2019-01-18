import subprocess
from gtts import gTTS
import time
cry =""
def ttsf(a):
    audio_file = "hello.mp3"
    tts = gTTS(text= a,lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])
from tkinter import *
master = Tk()


def closewindow(choice):
    global cry
    if choice==1:
        cry = "keep crying"
    if choice==2:
        cry = "toughen up and continue with the investigation"
    ttsf("Hello World")
        while i == 0:
             button = Button(master, text="What should he do now (keep crying or toughen up and continue with the investigation)", command=closewindow(1))
             button.pack()
             mainloop()
            cry = get_Cry()
            if cry == "keep crying":
                audio_file = "hello.mp3"
                tts = gTTS(text="You walk out of the alley and continue to cry. Finaly after 20 minutes you get it together and walk back into the alley. But in those 20 minutes someone came in and wiped up the boot print. You don't get any evidence and return back to the station", lang="en")
                tts.save(audio_file)
                return_code = subprocess.call(["afplay", audio_file])
            elif cry == "toughen up and continue with the investigation":
                audio_file = "hello.mp3"
                tts = gTTS(text='You slap yourself in the face and get yourself together. You then put on your rubber gloves and look at the bootprint. You conclude that the shoe is a size 12 mens. The print is uneven though which could mean that the person who wore the shoe has a smaller foot. In the crevices he found sand. Thats strange sand is extremely rare in 2032 Toronto. You then head back to the Police Station. The Clue has been added to your inventory',lang="en")
                tts.save(audio_file)
                return_code = subprocess.call(["afplay", audio_file])
                print("Congratulations You have Unlocked a Clue")
                cluelist1.append("sand")
                print(cluelist1)
                break



