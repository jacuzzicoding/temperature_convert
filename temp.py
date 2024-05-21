#Name: Brock Jenkinson
# Date: 05/21/2024
# 
# This is my temperature converter written in Python
welcome1 = "Welcome to Brock's Temperature Converter! "
welcome2 = "What scale are you converting from? Choose 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin: "
print(welcome1 + welcome2)

input1 = int(input())  # User inputs an integer for the scale they are converting from.

if input1 == 1:  # If the user chooses Celsius
        print("You are converting from Celsius!")
        print("What is the temperature in Celsius?")
        temp1 = float(input())  # User input for the temperature in Celsius. Used float so we can divide it.
        temp2 = (temp1 * 9/5) + 32  # Conversion formula from Celsius to Fahrenheit
        temp3 = temp1 + 273.15  # Conversion formula from Celsius to Kelvin
        print("The temperature in Fahrenheit is", temp2)  # Output of the temperature in Fahrenheit
        print("The temperature in Kelvin is", temp3)  # Output of the temperature in Kelvin

elif input1 == 2:  # If the user chooses Fahrenheit
        print("You are converting from Fahrenheit!")
        print("What is the temperature in Fahrenheit?")
        temp1 = float(input())  # User input for the temperature in Fahrenheit. Used float so we can divide it.
        temp2 = (temp1 - 32) * 5/9  # Conversion formula from Fahrenheit to Celsius
        temp3 = (temp1 - 32) * 5/9 + 273.15  # Conversion formula from Fahrenheit to Kelvin
        print("The temperature in Celsius is", temp2, "this was found by using the formula of 'C = (F-32) * 5/9'")  # Output of the temperature in Celsius
        print("The temperature in Kelvin is", temp3, "this was found using the formula of 'K = C +273.15'")  # Output of the temperature in Kelvin

elif input1 == 3:  # If the user chooses Kelvin
        print("You are converting from Kelvin!")
        print("What is the temperature in Kelvin?")
        temp1 = float(input())  # User input for the temperature in Kelvin. Used float so we can divide it.
        temp2 = temp1 - 273.15  # Conversion formula from Kelvin to Celsius
        temp3 = (temp1 - 273.15) * 9/5 + 32  # Conversion formula from Kelvin to Fahrenheit
        print("The temperature in Celsius is", temp2)  # Output of the temperature in Celsius
        print("The temperature in Fahrenheit is", temp3)  # Output of the temperature in Fahrenheit

else:  # If the user inputs an invalid scale
        print("Invalid scale! Please choose 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin.")
        print("Please restart the program and try again.")  # Output of the invalid scale messaged