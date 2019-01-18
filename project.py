cluelist1 = []
x = 0
v = 0
i = 0
import subprocess
from gtts import gTTS
import time

def ttsf(a):
    audio_file = "hello.mp3"
    tts = gTTS(text= a,lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])

audio_file = "hello.mp3"
tts = gTTS(text= 'It was December 13th, 2032. It was a dark and stormy night.Police sirens echo through the streets. Waking up from a nightmare the detective turns on the light.Almost immediately after John gets out of bed the phone rings and it is the captain.He was told he had to come in. It is currently 3 in the morning\n'
'There was a murder. He drives to the police station. His Captain is adressing all the officers. He stated at twelve hundred hours one of our own james blake was murdered by a gunshot. Execution  style in an alley\n'
                 'After the captains adress you are given the evidence from the case. There are three clues. The first is a footprint left at the scene. The second is a note in his pocket and the third is the security footage. What peice of evidence do you want to investigate', lang="en")
tts.save(audio_file)
return_code = subprocess.call(["afplay", audio_file])
time.sleep(0.5)
while x == 0:
    evchoice = input("What piece of evidence do you want to investigate (1,2,3)")
    if evchoice == "1":
        audio_file = "hello.mp3"
        tts = gTTS(text='John drives to the crime scene. It takes him a good hour, traffic is terrible in 2032 even with flying cars. He finaly arrives at the crime scene and breaks down crying. What should he do now. keep crying or toughen up and continue with the investigation.', lang="en")
        tts.save(audio_file)
        return_code = subprocess.call(["afplay", audio_file])
        time.sleep(0.5)
        while i == 0:
            cry = input("What should he do now (keep crying or toughen up and continue with the investigation)")
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
    elif evchoice == "2":
        audio_file = "hello.mp3"
        tts = gTTS(text='You have chosen to investigate the note in his pocket. You walk throught the busy police precinct. You finaly make it to the morge to look at the body and get his belongings. The Doctor hands you his jacket and inside of it there is a white note.\n'
                        ' This note is of course stained with blood but luckely this did not damage the letter. You open it and it simply reads the The Moragino Hotel 12 a clock. This was two hours before he died. You look up the hotel name. you find out that\n'
                        ' there is 10 of these hotels in toronto. What Do You Want To Do. You can visit all the hotels or compare evidence you have so far.',lang="en")
        tts.save(audio_file)
        return_code = subprocess.call(["afplay", audio_file])
        while v == 0:
            choice2 = input("Do you either want to visit all the hotels or compare evidence you have so far")
            if choice2 == "compare evidence you have so far" and "sand" in cluelist1:
                ttsf("As you Look at the sand found at the crime scene You have an incredible Idea. You look at all the hotel properties for sand. James Blake had to be at a hotel that had sand at it. You finaly found one propperty near Yonge and Dundas. This Property is the main building in Toronto and is owned by the Donoli family.\n"
                                 " The Biggest Mob In all of the United Federation of America. Do You Want to Head to the Hotel or report what you have to your captain.")
                caporhot = input("do You Want to head To the hotel Or ceport what You Have to Your captain")
                if caporhot == "head to the hotel":
                    ttsf("You pick up your gun and your badge and head out of the front doors of the police station. You get in your car and fly to the Moragino Hotel. You Exit the car when the sun is setting. It is freezing outside.\n"
                         " You walk into the hotel and are welcomed by magnificent human like AI Robots. You ask one of the Robots to see the owner of the hotel. \n"
                         "They Robot says No Sorry Ms.Donoli does not see random visitors. You then Flash Your Badge and then are let right in. You are lead to a backroom. In the back room you see Ms.Donoli. She is giving an unidentified powder to a robot. She is the head of the mob. You ask her about what she knows about the muder of Detective Blake. She says she knows nothing but you give her the evidence of the sand being found at the scene. You then threaten to have police shut down\n"
                         "the hotel for weeks investigating. She then loses her main money laundering enterprise. She then gives the name of her second in command that commited the murder without the concent of the Donoli crime family. You then see him out of the corner of you eye. You run after him and he runs into a crowd of people. You run after him and eventualy catch him. He is arrested and sent to prison. Congratulations you have gotten the killer. Or Did You. 48 hours after the trial the body of a police officer was found. He was identified as YOU. The Killer Strikes again.")
                elif caporhot == "report what you have to your captain":
                    ttsf("You head to the captains office to tell him your suspicions. You enter to see him taking a nap. You wake him up of course and tell him what you found. He says this is dangerous and asked me who I told. I replied with no one. And he said good, no one can be trusted. He tells me to go home and relax. I said okay as I have been up a while. I go home to my apartment and took a quick nap. I wake up a day later. I guess It was not a quick nap. I decide to watch some television before I go back to the precinct. As I am watching tv my door is broken down and 5 armed guys with full bullet proof vest run into the room.\n"
                         "What Do you do. Jump Out the Window or Surrender. ")
                    choice3 = input("What Do You Do. jump out the window or surrender")
                    if choice3 == "jump out the window":
                        ttsf("You Jump Out the Window Like a lunatic and land on a window washer platform. You cut the rope and come crashing down to the street below. As you run away you are shot in the shoulder and are arrested by the police. You are sent to an interogation room and your captain walks in. He sits down and says that they found your finger prints on Detective blakes body. He also said they found a video of you killing him. You said this is a set up and the captain says he knows he is the one who did it. It all makes sense now. \n"
                             "This is how we never arrested the Donoli family. Our captain is dirty. Captain morgan then stated that his boss killed Detective James. Because he found out Captain Morgan was dirty. Detective James had to be silenced and now so do you. Detective John was then put to death for the murder of detective Blake. "
                             "")
                    elif choice3 == "surrender":
                        ttsf("They HandCuff You. The cold steel sends shivers down your spine. When You arrive back at the Station You are sent to an interogation room. Your captain walks in quickly after you arrive. \n"
                             "He sits down and says that they found your finger prints on Detective blakes body. \n"
                             "He also said they found a video of you killing him. You said this is a set up and the captain says he knows he is the one who did it. It all makes sense now. \n"
                             "This is how we never arrested the Donoli family. Our captain is dirty. Captain morgan then stated that his boss killed Detective James. Because he found out Captain Morgan was dirty. Detective James had to be silenced and now so do you. \n"
                             "Detective John was then put to death for the murder of detective Blake.")

            elif choice2 == "compare evidence you have so far" and "sand" not in cluelist1 and "vid" not in cluelist1:
                print("You Do Not have any evidence.")
            elif choice2 == "compare evidence you have so far" and "vid" in cluelist1:
                ttsf("hi")
            elif choice2 == "visit all the hotels":
                ttsf("You have chosen to visit all of the Moragino hotels. You visit every Moragino hotel in Toronto which takes a good 8 hours. This is what happens when you don't find any clues. You Finaly arrive at one of the buildings at Yonge and Sheppard. This Hotel is known to be owned by the Trigal Crime Family. In Toronto Every Hotel is owned by a different crime family.\n"
                     "You Walk into the hotel and find a group of men that look super sketchy. Do You want to approach them or listen from a distance.")
                choice4 = input("do you want to approach them or listen from a distance?")
                if choice4 == "approach them":
                    ttsf("You Walk up to them and say, Hello Gentlemen My Name is detective john. I am investigating...... One of the guys takes a swing and you. You luckily dodge it and get out of the way He Runs away. You Chase him down. You Chase him up the stairs of the hotel and eventualy you make it to the roof. He is trapped and you finaly tackle him. He says fine I Confess. You Then Tell him he is under arrest for Detective Blake. He Says No I didn't BANG\n" \
                    "He is Dead. He was sniped in the head. You then run for cover. There is no more gunfire. Do You Want to Run from Cover or stay there ")
                    choice5 =input("Do You want to run from cover or stay there ")
                    if choice5 == "run from cover":
                        ttsf("You Run From Cover. You Look for a shooter then Bang. You are shot in the shoulder. As You look up at the sky a person walks in front of you. They say they are getting an ambulance and to hang on. You take a deep breath and die.")
                        exit("You Die and Don't Find the Killer")
                    elif choice5 == "stay there":
                        ttsf("You stay behind the obstacle for 3 hours. You finaly leave the surface and BANG. You are Shot in the HEAD")
                        exit("You Have Died and Have Not Solved the Murder.")
                elif choice4 == "listen from a distance":
                    ttsf("You Listen closely as you here them talk about a murder. They are talking about how some dirty cop was responsible for it. Out of No Where you get hit in the back of the head and you collapse. You wake up in a dirty basement. Tied to a chair. A figure comes towards you. It is your captain. He says congratulations you solved half the case. I'm just the mole not the killer. Suprise.\n"
                         "But now you die. He pulls out a gun and BANG.")
                    exit("Congratulations you found the mole. To Bad You are Dead and No one knows what you found.")
    elif evchoice == "3":
        ttsf("You Have Chosen to investigate the security footage. You plug in the USB with the security footage on your computer. It starts with an open alley. Detective Blake then walks through to meet with a hooded figure. He seems very freindly with him. The man then punches Blake in the face and shoves him to his knees.\n"
             "She then Shoots him in the head. She looks towards the camera and you see her face. Do You Search her face in facial recognition or look at the wanted board.")
        choice6 = input("hi")