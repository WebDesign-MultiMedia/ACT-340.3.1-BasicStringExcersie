# Problem 1 : Create a string and print it
string1 = "Everything is an Object in Python!!!"
print(string1)
print(string1.upper(), 'Upper')
print(string1.lower(), 'Lower')
print(string1.capitalize(), 'Capitalize')
print(' ')
## Using Variables in Strings
first_name = "Julio" 
last_name = "Salas" 
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
print(' ')
## stripping white spaces
phrase = " Python is a great language "
print(phrase.rstrip())
print(phrase.lstrip())
print(phrase.strip())
print(' ')


# Problem 2 
Famous = "Julio"
Quote = "Ptience, young grasshopper"
print(f"{Famous} once said, '{Quote}'")
print("{} once said, '{}.'".format(Famous, Quote))
print(' ')

## String Indexing and Slicing
course = "Per Scholas"
print(course[0])
print(course[1])    
print(course[2])
print(course[-5])
print(' ')

## Slicing
String1 = "Slicing strings is easy !"
print(String1[0:3])
print(String1[1:6:2])
print(String1[-1: -8: -2])
print(String1[::-1])
print(' ')

# Problem 3
stringTest1 = "Hello World ! "
print(stringTest1[::-1], ': Reverse String') # Reversing a string
print(stringTest1[12], ': last character') # Accessing the last character
print(stringTest1[:], ': All characters') # Accessing all characters
print(stringTest1[3], ': 4th character') # Accessing the 4th character
print(stringTest1[-9], ': 4th character from the end') # Accessing the 4th character from the end
print(stringTest1[-7], ': 7th from the end')  # Accessing the 7th character from the end

