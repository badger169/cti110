# CTI-110
# P3HW1 - Color Mixer
# Jonathan Thomas
# 6/28/2020

color1 = input('Enter your first primary color (red, blue or yellow): ')
color2 = input('Enter your second primary color (red, blue or yellow): ')
if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print( "red & blue makes purple")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print( "red & yellow makes orange")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print( "blue & yellow makes green")
else:
    print("Error invalid color chosen, please enter a primary color of red, blue or yellow")


#Pseudocode:
#User will be asked to enter their first primary color
#User will be asked to enter their second primary color
#The combination or red and blue or vice versa makes purple
#Display the outcome of mixing red and blue
#The combination or red and yellow or vice versa makes orange
#Display the outcome of mixing  red and yellow 
#The combination or blue and yellow or vice versa makes green
#Display the outcome of mixing blue and green
#Error will dislpay if user enters a color that is not primary
