# CTI-110
# P3LAB - Debugging
# Jonathan Thomas 
# 06/30/2020

A_score = 90
B_score = 80
C_score = 70
D_score = 60
score = int(input('Enter your test score: '))
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')


#Pseudocode:
#Assign letter grades to their number values
#Ask user to enter their test score
#If score is an 90 or above printed result will be an A
#Anything else will move down the chain of code to find the correct letter
#If score is an 80 to 89 printed result will be an B
#Anything else will move down the chain of code to find the correct letter
#If score is an 70 to 79 printed result will be an C
#Anything else will move down the chain of code to find the correct letter
#If score is an 60 to 69 printed result will be an D
#Anything else will move down the chain of code to find the correct letter
#If score is an 59 or below printed result will be an F

            
