import random

##################################################
# Student Name: Augie Krueger
# Course: CS2
# Date: September 30, 2026
# Project: String Functions
##################################################

def reverser(string):
    '''
    Summary: reverses inputed string

    Paramaters: string

    Output: prints reversed string
    '''
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string  
    print(reversed_string)

def count_vowels(string):
    '''
    Summary: counts the vowels in a string
    
    Paramaters: string
    
    Output: returns the total vowels
    '''
    v_count = 0
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for char in string:
        if char in vowels:
            v_count += 1
    return v_count

def count_consonants(string):
    '''
    Summary: counts the consonants in a string
            
    Paramaters: string
            
    Output: returns total consonats
    '''
    c_count = 0
    consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    for char in string:
        if char in consonants:
            c_count += 1
    return c_count

def first_name(full_name):
    '''
    Summary: seperates your first name from your full name
            
    Paramaters: full_name
            
    Output: prints your first name
    '''
    print(f"your first name is {full_name.split(' ')[0]}")

def middle_name(full_name):
    '''
    Summary: seperates your middle name from your full name
            
    Paramaters: full_name
            
    Output: prints your middle name
    '''
    print(f"your last name is {full_name.split(' ')[1]}")
def last_name(full_name):
    '''
    Summary: seperates your last name from your full name
            
    Paramaters: last_name
            
    Output: prints your last name
    '''
    print(f"your last name is {full_name.split(' ')[2]}")

def name_hyphen_detector(full_name):
    '''
    Summary: determines whether the your name has a hyphen
            
    Paramaters: name
            
    Output: returns whether the name has a hyphen
    '''
    for char in full_name:
        if char == "-":
            hyphen = True
            break
        else:
            hyphen = False
    print(hyphen)

def uppercase(string):
    '''
    Summary: converts a string to all uppercase
            
    Paramaters: string
            
    Output: prints the new string
    '''
    lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_string = []
    letter_dictionary = {}
    for i in range(len(lowercase_letters)):
        letter_dictionary[lowercase_letters[i]] = uppercase_letters[i]
    for letter in string:
        new_string.append(letter_dictionary.get(letter, letter))
    print(new_string)

def lowercase(string):
    '''
    Summary: converts a string to all lowercase
            
    Paramaters: string
            
    Output: prints the new string
    '''
    lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_string = []
    letter_dictionary = {}
    for i in range(len(uppercase_letters)):
        letter_dictionary[uppercase_letters[i]] = lowercase_letters[i]
    for letter in string:
        new_string.append(letter_dictionary.get(letter, letter))
    print(new_string)

def name_generator(length):
    '''
    Summary: generates a random name
            
    Paramaters: length of the name
            
    Output: returns the name
    '''
    charecters = list("abcdefghijklmnopqrstuvwxyz")
    name = ""
    
    for i in range(length):
        name += random.choice(charecters)
    return(name)

def is_palindrome(string):
    '''
    Summary: determines whether a string is a palindrom
            
    Paramaters: string
            
    Output: returns true or false
    '''
    reversed_string = reverser(string)
    if string == reversed_string:
        return True
    else:
        return False

def intitials(full_name):
    '''
    Summary: gets your initials from your name
            
    Paramaters: full name
            
    Output: prints the initials
    '''
    f_name = first_name(full_name)
    m_name = middle_name(full_name)
    l_name = last_name(full_name)
    first_initial = f_name[0]
    middle_initial = m_name[0]
    last_initial = l_name[0]
    intitials = first_initial + middle_initial + last_initial
    print(intitials)

def name_title_detector(full_name):
    '''
    Summary: sees whether a name has a title
            
    Paramaters: full name
            
    Output: returns true or false
    '''
    lower_name = full_name.lower
    for char in lower_name:
        if char == "dr":
            title = True
            break
        elif char =="sir":
            title = True
            break
        elif char =="esq":
            title = True
            break
        elif char =="ph.d":
            title = True
            break
        else:
            title = False
    return(title)

while True:
    def main():
        print("input numbers 1-x"
        "1) reverser" \
        "2) count_vowels" \
        "3) count_consonats"
        "4) first_name" \
        "5) middle_name" \
        "6) last_name"
        "7) name_hyphen_detector" \
        "8) uppercase" \
        "9) lowercase" \
        "10) name_generator" \
        "11) is_palindrome" \
        "12) initials" \
        "13) name_title_detector"
        )
        function = input("what function would you like to do")
        function = input("what is your string")
        if function == 1:
            string = input("what string do you want to reverse")
            reverser(string)
        elif function == 2:
            string = input("what is your string")
            count_vowels(string)
        elif function == 3:
            string = input("what is your string")
            count_consonants(string)
        elif function == 4:
            name = input("what is your name")
            first_name(name)
        elif function == 5:
            pass
        elif function == 6:
            name = input("what is your name")
            last_name(name)
        elif function == 7:
            name = input("what is your name")
            name_hyphen_detector(name)
        elif function == 8:
            string = input("what is your string")
            uppercase(string)
        elif function == 9:
            string = input("what is your string")
            lowercase(string)
        elif function == 10:
            length = ("what is the length")
            name_generator(length)
        elif function == 11:
            string = ("what is the string")
            is_palindrome(string)
        elif function == 12:
            full_name = input("what is your fullname")
            intitials(full_name)
        elif function == 13:
            full_name = input("what is your full name")
            name_title_detector(full_name)
