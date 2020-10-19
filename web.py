import webbrowser
import random
import datetime
"""welcome to ecommerce chat bot:
1)Firstly the bot greet the user and asks his\her name
2) bot shows the menu to the user 
3)bot opens the website according to user selection 
  1.flipkart big billion days
  2.amazon great indian festival
  3.myntra big fashion festival
  4.end of tasks and quit
4)completion user task and quit
"""
def greet_and_introduction():
    global name
    name=input("Enter your name:  ")
    print("Hello!",name)
    intro=[
        " I am an ecommerce bot.Please select an option to go to an ecommerce website to make festival season wonder full with shoping ",
         " I am here to help you.Select an option to go to an ecoomerce website. "
         ]
    print(random.choice(intro))
def tasks():
    print(f" press 1 if you want to go to the flipkart big billion days website.")
    print(f" press 2 if you want to open the amazon great indian festival website.")
    print(f" press 3 if you want to go the myntra big fashion festival.")
    print(f" press 4 if you want to quit bot.")
def flipkart():
    webbrowser.open("https://www.flipkart.com/big-billion-days-store?gclid=CjwKCAjwz6_8BRBkEiwA3p02VbxVOh4lS6ax73_2IogWceTaJnZEBNWjBA_ohiy7_WM-W3tKDiFjuxoCblwQAvD_BwE&ef_id=CjwKCAjwz6_8BRBkEiwA3p02VbxVOh4lS6ax73_2IogWceTaJnZEBNWjBA_ohiy7_WM-W3tKDiFjuxoCblwQAvD_BwE:G:s&s_kwcid=AL!739!3!473243512766!e!!g!!flipkart%20big%20billion%20day&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_bbdkeywords_goog")
def amazon():
    webbrowser.open("https://www.amazon.in/?ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_CjwKCAjwz6_8BRBkEiwA3p02VVOSRPKsaxxDlM-5NlowZslW8UuKtTBUSQ-q9tsKGfm99qDr2uBQ1BoCONYQAvD_BwE_k_&ext_vrnc=hi&gclid=CjwKCAjwz6_8BRBkEiwA3p02VVOSRPKsaxxDlM-5NlowZslW8UuKtTBUSQ-q9tsKGfm99qDr2uBQ1BoCONYQAvD_BwE&network=g")
def myntra():
    webbrowser.open("https://www.myntra.com/?utm_source=Google&utm_medium=cpc&utm_campaign=Search%20-%20Myntra%20Brand%20(India)&gclid=CjwKCAjwz6_8BRBkEiwA3p02Va01XLT7HLl3OUJKSTStN0A7tlkIJWy-ymNjOgz8TF0F76p1pdgkBBoCtagQAvD_BwE")

greet_and_introduction()
while(True):
    tasks()
    task=int(input("Enter your choice here: "))
    if(task==1):
        flipkart()
    elif(task==2):
        amazon()
    elif(task==3):
        myntra()
    elif(task==4):
        quit=input(f"\n To quit the bot enter yes")
        if(quit=="yes"):
            print(f"\n Thank you for spending your valuable time with me.........!")
            break
        else:
            print(f"\n sorry invalid enter********")
    else:
        print("invalid selection!,please select the options from to 1 to 4")
        break