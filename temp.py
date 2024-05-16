#This is a temperature converter written in Python
welcome1 = "Welcome to Brock's Temperature Converter! " # Welcome message to the user
welcome2 = "What scale are you converting from? (CHOOSE C/F)"
print(welcome1+welcome2) 
input1 = input() # User input for the scale they are converting from. 
#using if statements to determine the scale the user is converting from
if input1 == "C": # If the user chooses Celsius
        print("You are converting from Celsius.")
        print("What is the temperature in Celsius?")
        temp1 = float(input()) # User input for the temperature in Celsius
        temp2 = (temp1 * 9/5) + 32 # Conversion formula from Celsius to Fahrenheit
        print("The temperature in Fahrenheit is", temp2) # Output of the temperature in Fahrenheit




