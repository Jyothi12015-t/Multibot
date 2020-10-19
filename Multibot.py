"""
1. Greetings from the bot and ask user names
2.Displaying the Menu card that the bot can do
3.Move with fascinated choice
4.It can choose BMI , Snake_Game ,Web-Browse.
"""
import random
def greet_intro():
    responses=[" Happy to see you here.I am Multibot. May i know your name? "]
    print(random.choice(responses))
def welcome(name):
    print(" Hello !",name)
def menu_card():
    print("These are the tasks that my mster Learned me...")
    print("1. Find BMI of a person")
    print("2. Play Snake_Game ")
    print("3. Web_Browser")
    print("4. End the conversation")
    try:
        return(int(input("Enter your Choice : ")))
    except:
         print("Sorry, I'm not Understanding")

def bot():
    greet_intro()
    name=input("Name: ")
    welcome(name)
    choice=menu_card()
    while choice != 4 :
        if choice==1:
         from bmi2 import str
        elif  choice==2:
         from game import reaching
        elif choice==3:
         from web import greet_and_introduction
        choice=menu_card()
bot()
    

    
