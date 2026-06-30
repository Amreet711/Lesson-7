# ord() function returns character value to ASCII value

#Output: 65
print(ord('A'))
#Output: 97
print(ord('a'))
#Output: 48
print(ord('0')) 
#Output: 64
print(ord('@'))         

# chr() function returns ASCII value to character value

#Output: @
print(chr(64))
#Ouput: a
print(chr(97))

#User Input
char=input("Please enter one character:")

#Validate: Check that the input is valid
if type(char) is str and len(char)==1:
    print("VALID ENTERY!")
else:
    print("INVALID ENTERY!\n Please restart the code and entery exactly ONE character")

#Get ASCII value
ascii_val=ord(char)

#Display the result
print(f"Chacacter: {char}")
print(f"ASCII Value: {ascii_val}")

#Identify character type using ASCII ranges
if ascii_val >= 65 and ascii_val <=90:
    print(ascii_val,"Type: Uppercase Letter")
elif ascii_val >= 97 and ascii_val <= 122:
    print(char,"Type: Lowercase")
elif ascii_val >= 48 and ascii_val <= 57:
    print(char,"Type: Digit")
elif ascii_val == 32:
    print(char,"Type: Space")
else:
    print(char,"Type: Special Character")