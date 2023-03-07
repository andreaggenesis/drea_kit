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

if purpose:
   pass