#Title
print("ASCII Value Checker")
#Creating a seperation
print("-" * 40)
#Getting user input
char=input("Please enter one character:")
#Validate input
if type(char) is str and len(char) > 1:
    print("ENTERY IS INVALID! \n Please enter ONE character")
#Get ASCII Value
ascii_val= ord(char)
#Display results
print(f"\nCharacter:'{char}'")
print(f"ASCII Value: {ascii_val}")
#Identify character type
if ascii_val >= 65 and ascii_val <= 90:
    print("\nUppercase Letter")
elif ascii_val >= 97 and ascii_val <= 122:
    print("\nLowercase Letter")
elif ascii_val >= 48 and ascii_val <= 57:
    print("\nDigit")
elif ascii_val == 32:
    print("\nSpace")
else:
    print("\nSpecial Character")