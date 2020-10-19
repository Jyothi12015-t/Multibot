def start():
    def BMI(height, weight): 
        bmi = weight/(height**2) 
        if (bmi < 18.5): 
            return "underweight"
        elif ( bmi >= 18.5 and bmi < 24.9): 
            return "Healthy"
        elif ( bmi >= 24.9 and bmi < 30): 
            return "overweight" 
        elif ( bmi >=30): 
            return "Suffering from Obesity"
        
    def val(height,weight):
        bmi = weight/(height**2) 
        return bmi

    def str(ans):
        if ans.lower()=="yes":
            start()
        elif ans.lower()=='no':
            print("Bye,Thank you for using this bot")
        else:
            print("Please enter yes or no for calculating BMI")
            s=input()
            str(s)
        
    print("What is your height(in meters)?")
    height = float(input())


    print("What is your weight(in kg)?")
    weight = int(input())

    bmi = val(height, weight) 
    status = BMI(height,weight)
    print("Your BMI is","{:.2f}".format(bmi),"kg/m^2.")
    print("So,you are",status)
    
    if status=="underweight":
        print("you may need to put on some weight. You are recommended to ask your doctor or a dietitian for advice.")
    elif status=="Healthy":
        print("This indicates that you are at a healthy weight for your height. By maintaining a healthy weight, you lower your risk of developing serious health problems.")
    elif status=="overweight":
        print("You may be advised to lose some weight for health reasons. You are recommended to talk to your doctor or a dietitian for advice.")
    elif status=="Suffering from Obesity":
        print(" Your health may be at risk if you do not lose weight. You are recommended to talk to your doctor or a dietitian for advice.")
    
    print("enter yes if you want to calculate another bmi else enter no ")
    an_re=input()
    
    str(an_re)


def str(ans):
    if ans.lower()=="yes":
        start()
    elif ans.lower()=='no':
        print("This bot is for only calculating BMI")
        print("Enter yes for calculating BMI")
        b=input()
        str(b)
    else:
        print("Please enter yes or no for calculating BMI")
        s=input()
        str(s)

print("Hello,I am BMI Calculator.")
print("What is your name ?")
name = input()
import datetime
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    print('Good morning',name)
elif 12 <= currentTime.hour < 18:
    print('Good afternoon',name)
else:
    print('Good evening',name)

print("Do you want to calculate your BMI ?(yes/no) ")
ans=input()
str(ans)
