#Name: Brock Jenkinson
# Date: 05/21/2024
# Instructor: Snehasis Mukhopadhyay
# This is my temperature converter written in Python
welcome1 = "Welcome to Brock's Temperature Converter! "
welcome2 = "What scale are you converting from? Choose 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin: "
welcome_msg = (welcome1 + welcome2)
# Showing welcome message to the user
print(welcome_msg)  

# Boolean variable for input validation
valid_input = True

# User inputs an integer for the scale they are converting from.
scale_choice = int(input())  

# If the user chooses Celsius
if scale_choice == 1:  
        print("You are converting from Celsius!")
        print("What is the temperature in Celsius?")
        # User input for the temperature in Celsius. Used float so we can divide it.
        temp1 = float(input())  
        # Conversion formula from Celsius to Fahrenheit
        temp2 = (temp1 * 9/5) + 32  
        # Conversion formula from Celsius to Kelvin
        temp3 = temp1 + 273.15  
        # Output of the temperature in Fahrenheit
        print("The temperature in Fahrenheit is " + str(temp2) + ",this was found by using the formula of 'F = (C * 9/5) + 32' ")  
        # Output of the temperature in Kelvin
        print("The temperature in Kelvin is " + str(temp3) + ",this was found by using the formula of 'K = C + 273.15'")  

elif scale_choice == 2:  # If the user chooses Fahrenheit
        print("You are converting from Fahrenheit!")
        print("What is the temperature in Fahrenheit?")
        # User input for the temperature in Fahrenheit. Used float so we can divide it.
        temp1 = float(input())  
        # Conversion formula from Fahrenheit to Celsius
        temp2 = (temp1 - 32) * 5/9  
        # Conversion formula from Fahrenheit to Kelvin
        temp3 = (temp1 - 32) * 5/9 + 273.15  
        # Output of the temperature in Celsius
        print("The temperature in Celsius is " + str(temp2) + ",this was found by using the formula of 'C = (F-32) * 5/9'")
         # Output of the temperature in Kelvin 
        print("The temperature in Kelvin is " + str(temp3) + ",this was found using the formula of 'K = C + 273.15'") 

# If the user chooses Kelvin
elif scale_choice == 3:  
        print("You are converting from Kelvin!")
        print("What is the temperature in Kelvin?")
        # User input for the temperature in Kelvin. Used float so we can divide it.
        temp1 = float(input()) 
        # Conversion formula from Kelvin to Celsius
        temp2 = temp1 - 273.15  
         # Conversion formula from Kelvin to Fahrenheit
        temp3 = (temp1 - 273.15) * 9/5 + 32 
        # Output of the temperature in Celsius
        print("The temperature in Celsius is " + str(temp2) + ", this was found using the formula of 'C = K - 273.15'")  
        # Output of the temperature in Fahrenheit
        print("The temperature in Fahrenheit is " + str(temp3) + ", this was found by using the formula of 'F = C * 9/5 + 32'")  

# If the user inputs an invalid scale
else:  
        print("Invalid scale! Please choose 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin.")
        # Output of the invalid scale messaged
        print("Please restart the program and try again.")  