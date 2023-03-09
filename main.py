from random import randrange
import random
import time
from ssl import Purpose


def getPlayerName(name):
 print("Hello, what is your name?")
 name = input()
 print("Why hello there " + name)
print("Are you here for a fortune or a reading?")
purpose = input()

smart = ["Someone is looking up to you. Don't let that person down."," When in anger sing the alphabet.","You are not illiterate","Your friends sectreltly agree your head is the wrong size for your body","You should try LSD","you will be hungry again in one hour.","Always borrow money from a pessimist; they don't expect to be paid back.","If PLAN A fails, all is not lost; There are 25 more letters in the alphabet", "Those who limit the past limit their future.","Better late than never but never late is better","A goal without a plan is just a wish.","a person that aims at nothing is sure to hit it.","Expecting the unexpected makes the unexpected expected."]
 
if purpose== "fortune":
 
   print("thinking..." )
   time.sleep(random.randrange(0,5))
   print(random.choice(smart))
  
for i in range(1):
   print((randrange(0,13)))

Cards = ["Perhaps you feel that everything you have known is falling apart. Unexpected changes and turmoil, end of a job, end of a career, divorce or end of a relationship, recovering from a bereavement of fear or bereavement. Try not to worry too much: this time of absolute endings heralds a brand new beinning, a period of great transformation.", 
"The spirits suggest that at this time you desire comfort, security and hapiness and may well need some emotional support and reassurance.If you are considering having a baby the desire will be very strong at this time, or perhaps you are already pregnant and you have some concerns. If male, perhaps you are considering fatherhood with someone but have concerns.Things will turn out fine, just know that you are loved and that there are people around you who care.", 
"The word failure isn't in your vocabulary. You are worried things are more of a struggle than you expected, with more delays and frustrations.Things aren't going according to plan at all - just chill out, calm that mind of yours and you'll find the strength to battle on until you succeed. This is a period of movement and change and conflicts ending in victory.",
 "Brand new potential, an opportunity which once given must not be ignored, a new project, decision or relationship that could affect the rest of your life - all are indicated here. You will enjoy success and enjoyment for past efforts, events will pick up a pace and the outcome will be quicker than expected.", 
 "A run of bad luck here, perhaps already evident or there are certainly signs that things are not going your way.The responsibility of important decisions weighs heavy with you where there are choices to make. Trust your intuition, and even if you have to make the painful decision to give up something in order to move on, then have the courage to do it.",
 "Justice will be done. Decisions will go in your favour, particularly regarding partnerships or legal matters. Now is the time for some good luck and reward for your good deeds in the past.", 
 "You feel a sense of purpose and the willpower to get things done. Self-empowerment is the key word here. Any new enterprises in love or career show great potential. You feel that you have the ability to think on your feet and, faced with opposition, the appearance of The Magician is an excellent omen of success. Time to believe in yourself and go for it!", 
 "You are about to enter a period of peace and harmony in your relationship, career or life in general.", 
 "You will find a way of handling difficult circumstances with calm confidence. Life is flowing at this time - enjoy it.", 
 "Your negativity and lack of self-control are your real enemies. If you are finding certain addictions in your life are taking a hold, be it smoking or drinking for example, look inward for your heart's true strength and self-belief. Change your attitude and be positive and you will reap great rewards.", "Expect life to change - and quickly. Fate, destiny or synchronicity, call it what you like, positive change and good fortune is evident here. If you have important choices to make trust your intuition. Do you feel that events seem to be evolving without much input from you? If so trust it and go with the flow."


]
if purpose== "reading":
   pass
print("sensing your energy...")
time.sleep(random.randrange(0,5))
print