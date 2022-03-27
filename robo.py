import pyttsx3 as pyt
import random 
#write some functions here
def addition(first_number, second_number):
    robo_voice.say(float(first_number)+float(second_number))
    robo_voice.runAndWait()
random_number = random.randint(0, 100)
robo_voice = pyt.init()
#intro
askRobo = ["what is your name", "pick me a random number", "add 2 numbers"]
print("Ask me like:")
print(askRobo)
print("Spelling mistake can cause no responses!")
name = input("What is your name:")
robo_voice.say("Hello" +name)
robo_voice.runAndWait()
active = True
#this is where robot replys
while active == True:
    user = input(name+ ":")
    if user == askRobo[2]:
        firAdd = float(input("Enter your first number:"))
        secAdd = float(input("Enter your second number:"))
        print(firAdd+secAdd)
        addition(firAdd, secAdd)
    if user == askRobo[0]:
        robo_voice.say("My name is robo")
        robo_voice.runAndWait()
    if user == askRobo[1]:
        robo_voice.say("Here is a random number from 0 to 100")
        robo_voice.say(random_number)
        print(random_number)
        robo_voice.runAndWait()
robo_voice.runAndWait()