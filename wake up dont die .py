import time
#to do:
#try again things
#check for typos etc
#make it so that you can go back to where you were

def sceneOne():
    print("\nyou wake up to a cold breeze in your room.")
    time.sleep(1.5)
    print("you slowly open your eyes...")
    time.sleep(1.5)
    print("only to see another pair looking at you from your window.")
    time.sleep(1.5)
    print("a dark figure looks down at you.")
    time.sleep(1.5)
    print("he smiles.")
    time.sleep(1.5)
    print("'what are you still doing here?'")
    time.sleep(2)
    print("'wake up.'")
    time.sleep(1.5)
    sceneOneChoices()

def sceneOneChoices():
    sceneOneChoice = input("\n1. stay awake \n2. go back to sleep \n")
    if sceneOneChoice == "1":
        stayAwake()
    if sceneOneChoice == "2":
        goBackToSleep()
    

#branch one
def stayAwake():
    print("\nyou keep your eyes open.")
    time.sleep(1.5)
    print("he smiles wider.")
    time.sleep(1.5)
    print("his eyes get brighter.")
    time.sleep(1.5)
    print("'you're not awake.'")
    time.sleep(1.5)
    print("'but i'm real.'")
    time.sleep(1.5)
    print("'do you want to talk to me?'")
    time.sleep(1.5)
    s1c1choice = input("\n1. nod \n2. go back to sleep \n")
    
    if s1c1choice == "1":
        stayAwakeTHENNod()
    
    if s1c1choice == "2":
        stayAwakeTHENGoBackToSleep()


def stayAwakeTHENNod():
    print("\nsomehow, his smile gets even wider.")
    time.sleep(1.5)
    print("'good! i'm glad.'")
    time.sleep(1.5)
    print("he leans into your room.")
    time.sleep(1.5)
    s1c1c1choice = input("\n1. move back \n2. stay where you are \n")
    
    if s1c1c1choice == "1":
        stayAwakeTHENNodTHENmoveBack()
    
    
    if s1c1c1choice == "2":
        stayAwakeTHENNodTHENstayInPlace()
    

def stayAwakeTHENNodTHENmoveBack():
    print("\nhe frowns slightly.")
    time.sleep(1.5)
    print("he then climbs into your room.")
    time.sleep(1.5)
    print("he stands at the foot of your bed.")
    time.sleep(1.5)
    print("'now i can see you better.'")
    time.sleep(1.5)
    print("'let me talk to you.'")
    time.sleep(1.5)
    talkToHim = input("\n1. nod \n2. close your eyes \n");
    
    if talkToHim == "1":
        stayAwakeTHENNodTHENmoveBackTHENnod()
    
    if talkToHim == "2":
        stayAwakeTHENNodTHENmoveBackTHENcloseYourEyes()
    


def stayAwakeTHENNodTHENmoveBackTHENnod():
    print("\nhe smiles.")
    time.sleep(1.5)
    print("'what do you want to talk about?'")
    time.sleep(1.5)
    talkAbout = input("\n1. him \n2. you \n")
    if talkAbout == "1":
        talkAboutHim()
    if talkAbout == "2":
        talkAboutYou()
    

#ending: lose
def talkAboutHim():
    print("\nhis face becomes expressionless.")
    time.sleep(1.5)
    print("'no.'")
    time.sleep(2)
    print("'you're not supposed to know about me.'")
    time.sleep(1.5)
    print("he looks at you darkly.")
    time.sleep(1.5)
    print("'you don't deserve to wake up.'")
    time.sleep(1.5)
    print("he surges towards you with his mouth wide open.")
    time.sleep(1.5)
    print("his jaw closes around your head.")
    time.sleep(1.5)
    print("\nyou lose. game over.")
    time.sleep(2)
    print("try again?")
    

def talkAboutYou():
    print("\nhe smiles wide.")
    time.sleep(1.5)
    print("he crawls into your room and stands over you.")
    time.sleep(1.5)
    print("'i can tell you something about yourself.'")
    time.sleep(1.5)
    print("'you're not awake. but you're still scared.'")
    time.sleep(1.5)
    print("his eyes become crazed.")
    time.sleep(1.5)
    print("'don't worry. i'm here now.'")
    time.sleep(1.5)
    print("'i'll make sure you wake up.'")
    time.sleep(1.5)
    wakeUp = input("\n1. tell him okay \n2. close your eyes \n")
    if wakeUp == "1":
        letHimWakeYouUp()
    if wakeUp == "2":
        dontLetHimWakeYouUp()
    


#ending: lose
def letHimWakeYouUp():
    print("\nhis smile gets impossibly wider.")
    time.sleep(1.5)
    print("'you've made the right choice.'")
    time.sleep(1.5)
    print("'i'm so glad you'll be joining me.'")
    time.sleep(1.5)
    print("he leans down and pries your eyes further open.")
    time.sleep(1.5)
    print("suddenly everything turns black and cold.")
    time.sleep(1.5)
    print("then there is nothing.")
    time.sleep(1.5)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()

#ending: lose
def dontLetHimWakeYouUp():
    print("\nyou close your eyes tight.")
    time.sleep(1.5)
    print("he becomes enraged.")
    time.sleep(1.5)
    print("'i am trying to do a nice thing for you!'")
    time.sleep(1.5)
    print("'and you ignore me?!'")
    time.sleep(1.5)
    print("he sighs and tries to calm down.")
    time.sleep(1.5)
    print("'you don't know what's good for you.'")
    time.sleep(1.5)
    print("'i'll make you wake up.'")
    time.sleep(1.5)
    print("he smiles. 'don't worry, you'll like it.'")
    time.sleep(1.5)
    print("he pries your eyes open.")
    time.sleep(1.5)
    print("you see his eyes have become red. then suddenly...")
    time.sleep(1.5)
    print("you see nothing.")
    time.sleep(1.5)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()



def stayAwakeTHENNodTHENmoveBackTHENcloseYourEyes():
    print("\nyou close your eyes.")
    time.sleep(1.5)
    print("he frowns more.")
    time.sleep(1.5)
    print("you hear him sigh. he sounds angry.")
    time.sleep(1.5)
    print("suddenly you feel breath against your ear.")
    time.sleep(1.5)
    print("'talk to me.'")
    time.sleep(1.5)
    openOrClose = input("\n1. open your eyes \n2. keep your eyes closed \n")
    if openOrClose == "1":
        openWhileHesMad();
    if openOrClose == "2":
        closeWhileHesMad()
    


def openWhileHesMad():
    print("\nyou open your eyes slowly.")
    time.sleep(1.5)
    print("he visibly calms down.")
    time.sleep(1.5)
    print("'i knew you were smart.'")
    time.sleep(1.5)
    print("'what do you want to talk about?'")
    time.sleep(1.5)
    angryTalkAbout = input("\n1. him \n2. you \n")
    if angryTalkAbout == "1":
        angryTalkAboutHim();
    if angryTalkAbout == "2":
        angryTalkAboutYou()
    

def angryTalkAboutHim():
    print("\nhe looks surprised.")
    time.sleep(1.5)
    print("'aren't you afraid?'")
    time.sleep(1.5)
    afraid = input("\n1. no \n2. yes \n")
    if afraid == "1":
        youreNotAfraid()
    if afraid == "2":
        youreAfraid()
    

#ending: lose
def youreNotAfraid():
    print("\nhe frowns.")
    time.sleep(1.5)
    print("'well, in that case...")
    time.sleep(1.5)
    print("he smiles.")
    print("'i'll show you why you should be afraid.'")
    time.sleep(1.5)
    print("he pulls at your eyelids, forcing them to open farther than was comfortable.")
    time.sleep(2)
    print("his hollow eyes turn red.")
    time.sleep(1.5)
    print("then everything turns black.")
    time.sleep(2)
    print("\nyou did not make it until morning.")
    time.sleep(1.5)
    print("game over. you lose.")
    time.sleep(2)
    tryAgain()


def youreAfraid():
    print("\nhe grins.")
    time.sleep(1.5)
    print("'good. i knew you were smart.'")
    time.sleep(1.5)
    print("'now tell me...'")
    time.sleep(1.5)
    print("he leans forward.")
    time.sleep(1.5)
    print("... do you want to wake up?")
    time.sleep(1.5)
    angryWakeUp = input("\n1. yes \n2. no \n")
    if angryWakeUp == "1":
        youWantToWakeUp()
    if angryWakeUp == "2":
        youDontWantToWakeUp()
    
    

#ending: lose
def youWantToWakeUp():
    print("\n'i'm glad.")
    time.sleep(1.5)
    print("'you'll enjoy it, i promise.'")
    time.sleep(1.5)
    print("'he grabs your eyelids and pushes them open.")
    time.sleep(1.5)
    print("you feel a chill wash over you.")
    time.sleep(1.5)
    print("then everything turns black.")
    time.sleep(2)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()

#ending:lose
def youDontWantToWakeUp():
    print("\nhe pouts.")
    time.sleep(1.5)
    print("for a second, you almost feel bad for saying no.")
    time.sleep(1.5)
    print("then he jeers at you.")
    time.sleep(1.5)
    print("'aww, did you really think you had a choice?'")
    time.sleep(1.5)
    print("he grabs you by your torso and drags you out of bed.")
    time.sleep(1.5)
    print("he stand you up in front of him, his eyes boring into yours.")
    time.sleep(1.5)
    print("his eyes slowly start to glow red.")
    time.sleep(1.5)
    print("your vision fades to black.")
    time.sleep(2)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()


#ending:lose
def angryTalkAboutYou():
    print("\nhe smiles cheekily.")
    time.sleep(1.5)
    print("'i already know everything about you.'")
    time.sleep(1.5)
    print("he grabs your chin.")
    time.sleep(1.5)
    print("'i know you won't tell me no.'")
    time.sleep(1.5)
    print("his grin becomes so wide it stretches his face.")
    time.sleep(1.5)
    print("his eyes start to glow red.")
    time.sleep(1.5)
    print("'you'll let me wake you up, won't you?'")
    time.sleep(1.5)
    print("you try to shake your head no, but the hand on your chin makes you nod.")
    time.sleep(1.5)
    print("'good.'")
    time.sleep(1.5)
    print("your vision fails and you collapse.")
    time.sleep(2)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()

#ending: lose
def closeWhileHesMad():
    print("\nyou close your eyes tighter.")
    time.sleep(1.5)
    print("a few seconds pass in silence.")
    time.sleep(1.5)
    print("you feel him move away from you, and you relax your body.")
    time.sleep(1.5)
    print("suddenly you hear a loud shriek.")
    time.sleep(1.5)
    print("you open your eyes just in time to see his claw-like fingers rushing towards your face.")
    time.sleep(1.5)
    print("then, nothing.")
    time.sleep(2)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()




def stayAwakeTHENNodTHENstayInPlace():
    print("\nyou don't move.")
    time.sleep(1.5)
    print("his face falls slightly.")
    time.sleep(1.5)
    print("'aren't you afraid of me?'")
    time.sleep(1.5)
    afraidOutsideWindow = input("\n1. yes \n2. no \n")
    if afraidOutsideWindow == "1":
        afraidWhileHesOutside()
    if afraidOutsideWindow == "2":
        notAfraidWhileHesOutside()
    


def afraidWhileHesOutside():
    print("\nhe sighs with relief.")
    time.sleep(1.5)
    print("'great! that's perfect.'")
    time.sleep(1.5)
    print("he suddenly appears next to your bed.")
    time.sleep(1.5)
    print("'do you want to be friends?'")
    time.sleep(1.5)
    friends = input("\n1. yes \n2. no \n")
    if friends == "1":
        yesToFriends()
    if friends == "2":
        noToFriends()

#ending
def yesToFriends():
    print("\nhis eyes grow manic.")
    time.sleep(1.5)
    print("'thank you thank you!'")
    time.sleep(1.5)
    print("'you've made this really easy for me.'")
    time.sleep(1.5)
    print("he grabs your face with both hands and leans in close.")
    time.sleep(1.5)
    print("you feel his hands grow impossibly cold.")
    time.sleep(1.5)
    print("your eyes roll back, and then...")
    time.sleep(1.5)
    print("darkness.")
    time.sleep(2)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()

#ending
def noToFriends():
    print("\nhe glowers down at you.")
    time.sleep(1.5)
    print("'no??'")
    time.sleep(1.5)
    print("he huffs.")
    time.sleep(1.5)
    print("'i didn't want to do this, but you give me no choice.'")
    time.sleep(1.5)
    print("he raises one of his hands...")
    time.sleep(1.5)
    print("and slashes you across your eyes.")
    time.sleep(2)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()


#ending
def notAfraidWhileHesOutside():
    print("\nhe raises his eyebrows.")
    time.sleep(1.5)
    print("'oh?'")
    time.sleep(1.5)
    print("he suddenly appears on top of you.")
    time.sleep(1.5)
    print("the pressure of his body is suffocating.")
    time.sleep(1.5)
    print("he grins.")
    time.sleep(1.5)
    print("'are you scared now?'")
    time.sleep(1.5)
    print("you nod furiously.")
    time.sleep(1.5)
    print("his eyes soften.")
    time.sleep(1.5)
    print("'theere you go. thank you for admitting that.'")
    time.sleep(1.5)
    print("he gets off of you.")
    time.sleep(1.5)
    print("'just for that, i'll bring you to the nice place.'")
    time.sleep(1.5)
    print("he smiles and puts his hand over your eyes.")
    time.sleep(1.5)
    print("he leans down and whispers in your ear:")
    time.sleep(1.5)
    print("'wake up.'")
    time.sleep(2)
    print("\nyou did not make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()



#choice 2 from branch 1
def stayAwakeTHENGoBackToSleep():
    print("\nyou close your eyes tight.")
    time.sleep(1.5)
    print("eventually you no longer feel him looking at you.")
    time.sleep(1.5)
    print("you relax, and try to go back to sleep.")
    time.sleep(1.5)
    print("\nsuddenly you feel breath on your skin.")
    time.sleep(1.5)
    print("you open your eyes...")
    time.sleep(1.5)
    print("only to see him leaning above you.")
    time.sleep(1.5)
    print("he smiles.")
    time.sleep(1.5)
    print("'i knew you wouldn't try sleeping again.")
    time.sleep(1.5)
    print("'so, do you want to talk?'")
    time.sleep(1.5)
    s1c1c2choice = input("\n1. nod \n2. shut your eyes")
    if s1c1c2choice == "1":
        stayAwakeTHENGoBackToSleepTHENNod()
    if s1c1c2choice == "2":
        stayAwakeTHENGoBackToSleepTHENshutYourEyes()


def stayAwakeTHENGoBackToSleepTHENNod():
    print("\n'good.'")
    time.sleep(1.5)
    print("'what do you want to talk about?'")
    time.sleep(1.5)
    talkAboutWhileInside = input("\n1. him \n2. you \n")
    if talkAboutWhileInside == "1":
        talkAboutHimInside()
    if talkAboutWhileInside == "2":
        talkAboutYouInside()
    

def talkAboutHimInside():
    print("\nhe sighs forlornly.")
    time.sleep(1.5)
    print("'i have spent so long playing this game.'")
    time.sleep(1.5)
    print("'no one ever wants to wake up.'")
    time.sleep(1.5)
    print("'can't they see how nice it would be?'")
    time.sleep(1.5)
    print("he looks at you.")
    time.sleep(1.5)
    print("'you're different though.'")
    time.sleep(1.5)
    print("'you want to wake up, don't you?'")
    time.sleep(1.5)
    wakeUpInside = input("\n1. yes \n2. no \n")
    if wakeUpInside == "1":
        insideAndUWantToWakeUp()
    if wakeUpInside == "2":
        insideAndYouDontWantToWakeUp()
    

#ending
def insideAndUWantToWakeUp():
    print("\n'i knew you would understand.'")
    time.sleep(1.5)
    print("'i'll help you come with me.'")
    time.sleep(1.5)
    print("he put a hand over your eyes and closed his own.")
    time.sleep(1.5)
    print("his hand grows colder and colder.")
    time.sleep(1.5)
    print("there is a smile in his voice as he says:")
    time.sleep(1.5)
    print("'don't you like how dark it is?'")
    time.sleep(2)
    print("\nyou did not make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()
    

#ending
def insideAndYouDontWantToWakeUp():
    print("\n'no?'")
    time.sleep(1.5)
    print("he clicks his tongue, then shrugs.")
    time.sleep(1.5)
    print("'i thought you were smarter than that.'")
    time.sleep(1.5)
    print("his eyes glow red and his jaw stretches impossibly wide.")
    time.sleep(1.5)
    print("before you can blink, his open mouth crashes down on your chest.")
    time.sleep(1.5)
    print("you black out.")
    time.sleep(2)
    print("\nyou did not make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()


#ending
def talkAboutYouInside():
   print("\nhe gazes at you intently.")
   time.sleep(1.5)
   print("'how... selfish.'")
   time.sleep(1.5)
   print("'i already know everything about you.'")
   time.sleep(1.5)
   print("'but you know nothing about me.'")
   time.sleep(1.5)
   print("'don't you want to know about me?'")
   time.sleep(1.5)
   print("you say nothing.")
   time.sleep(1.5)
   print("'well then, if that's the case...'")
   time.sleep(1.5)
   print("'i'll just show you.'")
   time.sleep(1.5)
   print("he turns your face towards him and forces you to look into his eyes.")
   time.sleep(1.5)
   print("you see everything... ")
   time.sleep(1.5)
   print("and then you see nothing.")
   time.sleep(2)
   print("\nyou did not make it until morning.")
   time.sleep(1.5)
   print("you lose. game over.")
   time.sleep(2)
   tryAgain()

#ending
def stayAwakeTHENGoBackToSleepTHENshutYourEyes():
    print("\nyou shut your eyes.")
    time.sleep(1.5)
    print("you see a red glow in the darkness behind your eyelids.")
    time.sleep(1.5)
    print("you hear laughter, and suddenly...")
    time.sleep(1.5)
    print("everything is dark.")
    time.sleep(2)
    print("\nyou did not make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()


#second branch
def goBackToSleep():
    print("\nyou close your eyes.")
    time.sleep(1.5)
    print("you tell yourself this is just a dream,")
    time.sleep(1.5)
    print("but you can still feel his eyes on you.")
    time.sleep(1.5)
    print("his smile gets slightly angrier.")
    time.sleep(1.5)
    print("'i said...'")
    time.sleep(1.5)
    print("'he smiles nicely again.")
    time.sleep(1.5)
    print("'wake up, please.'")
    time.sleep(1.5)
    s1c2choice = input("\n1. open your eyes \n2. keep your eyes closed \n")
    if s1c2choice == "1":
        youOpenAfterPleaseWakeUp()
    if s1c2choice == "2":
        youKeepClosedAfterPlease()


def youOpenAfterPleaseWakeUp():
    print("\nhe hums upon seeing your eyes open.")
    time.sleep(1.5)
    print("'very good.'")
    time.sleep(1.5)
    print("'now... do you want to play a game?'")
    time.sleep(1.5)
    game = input("\n1. yes \n2. no \n")
    if game == "1":
        gameYesOne()
    if game == "2":
        gameNoOne()
   

#ending
def gameYesOne():
    print("\nhis eyes sparkle.")
    time.sleep(1.5)
    print("he climbs in your room and sits on your bed.")
    time.sleep(1.5)
    print("'i'm glad you said yes.'")
    time.sleep(1.5)
    print("'it'll make this much easier.'")
    time.sleep(1.5)
    print("he leans over and grabs your legs, dragging you off the bed.")
    time.sleep(1.5)
    print("he pulls you outside.")
    time.sleep(1.5)
    print("he grips your face and makes you look at him under the light of the moon.")
    time.sleep(1.5)
    print("he smiles, and the light from the moon disappears.")
    time.sleep(1.5)
    print("his hollow eyes start to glow red.")
    time.sleep(1.5)
    print("you become entranced by the light, until your eyes cross and you fall limp.")
    time.sleep(2)
    print("\nyou did not make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()


def gameNoOne():
    print("\nhe pauses.")
    time.sleep(1.5)
    print("'i'm sorry, i seem to have heard you wrong.'")
    time.sleep(1.5)
    print("'do you want to play a game?'")
    time.sleep(1.5)
    gameTwo = input("\n1. yes \n2. no \n")
    if gameTwo == "1":
        gameYesTwo()
    if gameTwo == "2":
        gameNoTwo()
    

#ending
def gameYesTwo():
    print("\nhis eyes sparkle.")
    time.sleep(1.5)
    print("he climbs in your room and sits on your bed.")
    time.sleep(1.5)
    print("'i'm glad you said yes.'")
    time.sleep(1.5)
    print("'it'll make this much easier.'")
    time.sleep(1.5)
    print("he leans over and grabs your legs, dragging you off the bed.")
    time.sleep(1.5)
    print("he pulls you outside.")
    time.sleep(1.5)
    print("he grips your face and makes you look at him under the light of the moon.")
    time.sleep(1.5)
    print("he smiles, and the light from the moon disappears.")
    time.sleep(1.5)
    print("his hollow eyes start to glow red.")
    time.sleep(1.5)
    print("you become entranced by the light, until your eyes cross and you fall limp.")
    time.sleep(2)
    print("\nyou did not make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()

#ending
def gameNoTwo():
    print("\nhe raises his eyebrows.")
    time.sleep(1.5)
    print("'well, you don't have much of a choice.'")
    time.sleep(1.5)
    print("'this is my game, and i want you to play.'")
    time.sleep(1.5)
    print("he rushes into your room.")
    time.sleep(1.5)
    print("he leans over you, grinning wildly.")
    time.sleep(1.5)
    print("'what a shame... you lose.'")
    time.sleep(1.5)
    print("he slashes a clawed hand across your eyes.")
    time.sleep(2)
    print("\nyou did not make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()


#ending
def youKeepClosedAfterPlease():
    print("\nyou shut your eyes tighter.")
    time.sleep(1.5)
    print("you hear him sigh annoyedly.")
    time.sleep(1.5)
    print("'i don't have time for this.'")
    time.sleep(1.5)
    print("you suddenly feel him on top of you, his weight crushing your ribs.")
    time.sleep(1.5)
    print("then there is a bright flash of red light.")
    time.sleep(1.5)
    print("he reaches for your eyes and pries them open...")
    time.sleep(1.5)
    print("but all you see is dark.")
    time.sleep(2)
    print("\nyou didn't make it until morning.")
    time.sleep(1.5)
    print("you lose. game over.")
    time.sleep(2)
    tryAgain()



def tryAgain():
    print("\ntry again?")
    tryAgain = input("\n1. yes \n2. no \n")
    if tryAgain == "1":
        beginningTwo()
    if tryAgain == "2":
        print("\ngoodnight, then. :)")
    

def beginningTwo():
    print("\nmake it till morning.")
    time.sleep(1.5)
    print("if you let him get you, you lose.")
    time.sleep(1.5)
    ready = input("\n\nare you ready? \n 1. yes \n 2. no \n")
    if ready == "1":
        sceneOne()
    if ready == "2":
        time.sleep(1.5)
        print("you stay asleep.")
        time.sleep(1.5)
        print("when you wake up, it is morning.")
        time.sleep(1.5)
        print("good job! you win.")
        time.sleep(2)
        tryAgain()


#ending: win
def beginning():
    print("wake up")
    time.sleep(2)
    print("\ndirections:")
    time.sleep(1.5)
    print("enter 1 or 2 to choose an option.")
    time.sleep(1.5)
    print("there are 20 endings. there is only one way to win.")
    time.sleep(2)
    print("\nmake it till morning.")
    time.sleep(1.5)
    print("if you let him get you, you lose.")
    time.sleep(1.5)
    ready = input ("\n\nare you ready? \n 1. yes \n 2. no \n")
    if ready == "1" :
        sceneOne()
    if ready == "2":
        time.sleep(1.5)
        print("you stay asleep.")
        time.sleep(1.5)
        print("when you wake up, it is morning.")
        time.sleep(1.5)
        print("good job! you win.")
        time.sleep(2)
        tryAgain()

beginning() 

    

