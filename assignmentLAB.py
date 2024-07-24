'''Assignment:
1. Declare a div() function with two parameters. Then call the function and pass two
numbers and display their division.
2. Declare a square() function with one parameter.Then call the function and pass
one number and display the square of that number .
3. Using max() and min() functions display the maximum and minimum of 5 random
numbers.
4. Accept a name from the user and display that in lower case using lower()
function'''



'''#1. Declare a div() function with two parameters. Then call the function and pass two numbers and 
# display their division.'''


def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."

# Calling the function with two numbers
result = div(10, 2)
print("The result of division is:", result)




'''#2. Declare a square() function with one parameter.Then call the function and pass
one number and display the square of that number .'''



def square(a):
    if(a>0):
       return a*a
    else:
       return "enter posivite number"
    
a=int(input("enter the number"))
result=square(a)
print("square is :", result)




'''  3. Using max() and min() functions display the maximum and minimum of 5 random
numbers.'''


import random

# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated random numbers
print("Random numbers:", random_numbers)

# Find the maximum and minimum numbers
max_number = max(random_numbers)
min_number = min(random_numbers)

# Display the maximum and minimum numbers
print("Maximum number:", max_number)
print("Minimum number:", min_number)





'''4. Accept a name from the user and display that in lower case using lower()
function'''


str=input(" ENTER THE NAME IN UPPER CASE :")
lower_case=str.lower()
print(lower_case)







'''Assignment:
1. Write a Python program to count the occurrences of each word in a
given sentence
string = “To change the overall look of your document. To change the look
available in the gallery”
2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n"
3. Write a Python program to reverse words in a string
String = “Deeptech Python Training”
4. Write a Python program to count and display the vowels of a given
text
String=”Welcome to python Training”
'''



'''1. Write a Python program to count the occurrences of each word in a
given sentence
string = “To change the overall look of your document. To change the look
available in the gallery”'''


def count_word_occurrences(input_string):
    # Convert the string to lower case to ensure case insensitivity
    input_string = input_string.lower()
    
    # Split the string into words
    words = input_string.split()
    
    # Create a dictionary to store word counts
    word_count = {}
    
    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Example usage
input_string = "To change the overall look of your document. To change the look available in the gallery"
word_counts = count_word_occurrences(input_string)

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")








'''2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n"'''


def remove_newlines(input_string):
    # Replace newline characters with an empty string
    return input_string.replace('\n', '')

# Example usage
input_string = "\nBest \nDeeptech \nPython \nTraining\n"
cleaned_string = remove_newlines(input_string)

print(cleaned_string)





'''3. Write a Python program to reverse words in a string
String = “Deeptech Python Training”'''


def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed list of words into a single string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

# Example usage
input_string = "Deeptech Python Training"
reversed_string = reverse_words(input_string)

print(reversed_string)






'''4. Write a Python program to count and display the vowels of a given
text
String=”Welcome to python Training”'''


def count_and_display_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    vowel_list = []
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)
    
    return vowel_count, vowel_list
    
# Example usage
input_string = "Welcome to python Training"
vowel_count, vowel_list = count_and_display_vowels(input_string)

print(f"Number of vowels: {vowel_count}")
print(f"Vowels: {' '.join(vowel_list)}")





'''Assignment:
 1. Write a Python program to Count all letters, digits, and special
 symbols from the given string
 Input = “P@#yn26at^&i5ve”
 Output: Chars = 8 Digits = 2 Symbol = 3
 2. Write a Python program to remove duplicate characters of a given
 string.
 Input = “String and String Function”
 Output: String and Function
 3. Write a Python program to count Uppercase, Lowercase, special
 character and numeric values in a given string
 Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
 Output:
 UpperCase : 5
 LowerCase : 18
 NumberCase : 5
 SpecialCase : 11
 4. Write a Python Count vowels in a string
 input= “Welcome to Python Assignment”
 Output: Total vowels are: 8'''







''' 1. Write a Python program to Count all letters, digits, and special
 symbols from the given string
 Input = “P@#yn26at^&i5ve”
 Output: Chars = 8 Digits = 2 Symbol = 3 '''


def count_characters(input_string):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    
    for char in input_string:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    
    return char_count, digit_count, symbol_count

# Input string
input_string = "P@#yn26at^&i5ve"

# Get counts
chars, digits, symbols = count_characters(input_string)

# Output results
print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")








'''2. Write a Python program to remove duplicate characters of a given
 string.
 Input = “String and String Function”
 Output: String and Function'''


def remove_duplicates(input_string):
    result = ""
    for char in input_string:
        if char not in result:
            result += char
    return result

input_string = "String and String Function"
output_string = remove_duplicates(input_string)
print("Input:", input_string)
print("Output:", output_string)

    






'''3. Write a Python program to count Uppercase, Lowercase, special
 character and numeric values in a given string
 Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
 Output:
 UpperCase : 5
 LowerCase : 18
 NumberCase : 5
 SpecialCase : 11'''


def count_characters(input_string):
    upper_case = 0
    lower_case = 0
    number_case = 0
    special_case = 0
    
    for char in input_string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        elif char.isdigit():
            number_case += 1
        else:
            special_case += 1
    
    return upper_case, lower_case, number_case, special_case

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper_case, lower_case, number_case, special_case = count_characters(input_string)

print("Input:", input_string)
print("UpperCase:", upper_case)
print("LowerCase:", lower_case)
print("NumberCase:", number_case)
print("SpecialCase:", special_case)







'''4. Write a Python Count vowels in a string
 input= “Welcome to Python Assignment”
 Output: Total vowels are: 8'''


def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in input_string:
        if char in vowels:
            count += 1
            
    return count

input_string = "Welcome to Python Assignment"
vowel_count = count_vowels(input_string)

print("Input:", input_string)
print("Total vowels are:", vowel_count)
