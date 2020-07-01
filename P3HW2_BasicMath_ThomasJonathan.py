# CTI-110
# P3HW2 - BasicMath
# Jonathan Thomas
# 6/30/2020


value1 = float(input('Enter your first number: '))
value2 = float(input('Enter your second number: '))

def add(value1, value2):
    return value1 + value2
def subtract(value1, value2):
    return value1 - value2
def multiply(value1, value2):
    return value1 * value2
print("-------Menu-------")
print("1)Add Numbers")
print("2)Multiply Numbers")
print("3)Subtract Numbers")
print("4)Exit")
choice = input("Enter choice 1,2,3 or 4: ")

if choice == '1':
    print(value1, "+", value2, "=", add(value1,value2))
elif choice=='2':
     print(value1, "*", value2, "=", multiply(value1,value2))
elif choice=='3':
    print(value1, "-", value2, "=", subtract(value1,value2))
elif choice=='4':
    print("Program will Terminate")
else:
    print ("an incorrect choice was entered")



#Pseudocode:
#Prompt the user to type in their first chosen number
#Prompt the user to type in their second chosen number
#Define functions to perform
#Display a choice menu of addition, multiplication, subtraction and exit
#Instruct user to make a make an option
#Display added results if user chooses 1
#Display multiplied results if user chooses 2
#Display subtracted results if user chooses 3
#Display a terminate message if user chooses 4
#Cover all other invalid entries with an error message
