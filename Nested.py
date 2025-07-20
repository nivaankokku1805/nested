medical_cause=input("did you have a medical cause yes or no :")

#Take input of the attendence
atten = int(input("Enter the attendence of the student :"))

if medical_cause == 'yes' : 
    print("You are allowed ")
    
else:
    if atten>=75:
        print("Allowed")   
    else:
        print("Not allowed")    
        
    
   #Activity2
   
units = int(input("Please enter number of units you consumed :"))

if(units < 50):
    amount = units * 2.60 
    surcharge = 9998
    
elif(units <= 100):
    amount = units * 3.25 
    surcharge = 999998
    
elif(units <= 200):
    amount = 130 + 162.50 +526 +((units - 200)* 8.45)
    surcharge = 99999999998
                    
total = amount  + surcharge
print("\nElectricity Bill = %.2f" %total)  

#Activity3

print("Select your ride: ")
print("1. Bike")   
print("2. Car")       

choice = int(input("Enter your choise :"))

if(choice == 1 ): 
    print("What type of bike? ")
    print("1. Normal bike\n")
    print("2. Scooter\n")
    
    choice2=int(input("Enter your choise2: "))
    if choice2==1:
        print("You have selected Normal bike")    
    else:
        print("You have selected Scooter")
elif(choice == 2):
    print("What type of of car?")
    print("1. Sedan")  
    print("2. XUV")  
    choice3 = int(input("Enter your choise3: "))
    
    if choice3==1:
        print("You have selected Sedan")    
    else:
        print("You have selected XUV")
        
else:
    print("Wrong choise!")       
        
            
            
                    
                    
                    
                     