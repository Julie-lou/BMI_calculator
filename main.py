from bmi_calc import bmi_check

# call bmi_calc function
# and build your bmi interface
# your code is here


# print("Welcome to Free BMI Calculation App, Where health is matter!")
# name = input("Enter your name: ")
# weight = input("Enter your weight in (kg): ")
# height = input("Enter your height in (meter): ")

# print(f"{name} is {bmi_check(weight,height)} BMI")

START_1 = True
START_2 = False
START_3 = True
# print("Welcome to Free BMI Calculation App, Where health is matter!")
# name = input("Enter your name: ")
# weight =eval(input("Enter your weight in (kg): "))
# height =eval(input("Enter your height in (meter): "))

while START_1 == True:  
    print("Welcome to Free BMI Calculation App, Where health is matter!")
    name = input("Enter your name: ")
    weight =eval(input("Enter your weight in (kg): "))
    height =eval(input("Enter your height in (meter): "))    
    print(f"{name} is {bmi_check(weight,height)} BMI") 
    
     
        
        #     print("invalid input") 
    
    
        

           
       
    
   
    START_1 = False
    START_2 = True

    while START_2:
        decision = input("Do you want to continue? Y/N:")
        if decision == "Y":
         START_3 = True
        elif decision == "N":   
                START_2 = False
                print("Thank you for using our App, take good care of your health!")
                print("Good day sir!")
                break
        while START_3 == True: 
            name = input("Enter your name: ")
            weight = eval(input("Enter your weight in (kg): "))
            height = eval(input("Enter your height in (meter): "))  
            START_1 = True
            START_3 = False
            START_2 = False 


       
            
            
                 
        # while START_3 == True: 
        #     name = input("Enter your name: ")
        #     weight = float(input("Enter your weight in (kg): "))
        #     height = float(input("Enter your height in (meter): "))  
        #     START_1 = True
        #     START_3 = False
        #     START_2 = False 

       
        