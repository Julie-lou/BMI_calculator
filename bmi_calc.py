# create bmi check here, the function name is bmi_check

# START_1 = True
# START_2 = False



# while START_1:
#     def bmi_check(weight, height):
#         result = weight / height
#         if result < 18.5:
#             return  "underweight" , result
#         elif result <= 18.5 and result >= 24.9:
#             return  "normal" , result
#         elif result <= 25 and result >= 29.9:
#             return  "overweight" , result
#         elif result <= 30 and result >= 34.9:
#             return  "obese" , result
#         elif result >= 35:
#             return  "extremely obese" , result
#         elif weight > 635 or height > 2.72:
#             return  "unrealistic information" , "2"
#         else:
#             return  "invalid input" , "1"
    # START_2 = True
    # while START_2:
    #     decision = input("Do you want to continue? Y/N:")
    #     if decision == "y" or "Y":
    #         START_1 = True
    # while decision == "n" or "N":
    #         input("Thank you for using our App, take good care of your health!")
    #         input("Good day sir!")
    #         break




     # '''
        # your bmi function code is here.
        # the heaviest person on earth weight is 635kg
        # the heightest person on earth is 2.72m

        # '''
        # your code here!



def bmi_check(weight,height):
        if type(weight) == str or type(height) == str:
            return('invalid input', 1)
        if type(weight) == float or type(weight) == int or type(height) == float or type(height) == int:
       
            result = float((weight / height) / height)
            if float(weight) > 635 or float(height) > 2.72: 
                return('unrealistic information' , 2)
            elif result < 18.5:
                    return('underweight' , round(result, 2))
            elif result >= 18.5 and result <= 24.9:
                return('normal' , round(result, 2) )
            elif result >= 25 and result <= 29.9:
                return('overweight' , round(result,2)) 
            elif result >= 30 and result <= 34.9:
                return('obese' , round(result,2))  
            elif result >= 35:
                return('extremely obese', round(result,2))
        

 
     
        
        #     print("invalid input") 
    
    
        

           
       
    
   
   