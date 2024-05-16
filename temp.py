#This is my temperature converter written in Python
welcome1 = "Welcome to Brock's Temperature Converter! " # Welcome message to the user
welcome2 = "What scale are you converting from? (CHOOSE C/F/K)" 
print(welcome1+welcome2) 
input1 = input() # User input for the scale they are converting from. 
#using if statements to figure out the scale the user is converting from
if input1 == "C": # If the user chooses Celsius
        print("You are converting from Celsius!")
        print("What is the temperature in Celsius?")
        temp1 = float(input()) # User input for the temperature in Celsius. Used float so we can divide it.
        temp2 = (temp1 * 9/5) + 32 # Conversion formula from Celsius to Fahrenheit 
        temp3 = temp1 + 273.15 # Conversion formula from Celsius to Kelvin
        print("The temperature in Fahrenheit is", temp2) # Output of the temperature in Fahrenheit
        print("The temperature in Kelvin is", temp3) # Output of the temperature in Kelvin

elif input1 == "F": # If the user chooses Fahrenheit
        print("You are converting from Fahrenheit!")
        print("What is the temperature in Fahrenheit?")
        temp1 = float(input()) # User input for the temperature in Fahrenheit. Used float so we can divide it.
        temp2 = (temp1 - 32) * 5/9 # Conversion formula from Fahrenheit to Celsius
        temp3 = (temp1 - 32) * 5/9 + 273.15 # Conversion formula from Fahrenheit to Kelvin
        print("The temperature in Celsius is", temp2) # Output of the temperature in Celsius
        print("The temperature in Kelvin is", temp3) # Output of the temperature in Kelvin

elif input1 == "K": # If the user chooses Kelvin
        print("You are converting from Kelvin!")
        print("What is the temperature in Kelvin?")
        temp1 = float(input()) # User input for the temperature in Kelvin. Used float so we can divide it.
        temp2 = temp1 - 273.15 # Conversion formula from Kelvin to Celsius
        temp3 = (temp1 - 273.15) * 9/5 + 32 # Conversion formula from Kelvin to Fahrenheit
        print("The temperature in Celsius is", temp2) # Output of the temperature in Celsius
        print("The temperature in Fahrenheit is", temp3) # Output of the temperature in Fahrenheit
