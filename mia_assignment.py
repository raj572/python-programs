'''
This is a guessing game that the user plays with the program/computer.
The program generates a random number using the random function.
The user tries to guess it by inputting a value. 
The program then indicates whether the guess is right or not.
If it is wrong, then the program should tell how off the guess was.
If it is right, there should be another positive indicator.
You can place a limit on the number of guesses allowed.
You will also need functions to compare the inputted number with the guessed number,
to compute the difference between the two, and to check whether an actual number was inputted or not.
'''
# import random

# def compare_numbers(num1, num2):
#     return abs(num1 - num2)

# def is_valid_input(input_str):
#     if not input_str.isdigit():
#         print("Invalid input. Please enter a number.")
#         return False
#     return True

# def play_game():
#     num_tries = 6 # Default number of tries
#     random_number = random.randint(1, 100)
#     print("Welcome to the Guessing Game!")
#     print(f"I'm thinking of a number between 1 and 100. You have {num_tries} tries to guess it.")

#     for i in range(num_tries):
#         user_input = input(f"Guess #{i + 1}: ")
#         if not is_valid_input(user_input):
#             continue

#         guess = int(user_input)
#         if guess == random_number:
#             print(f"Congratulations! You guessed the number in {i + 1} tries.")
#             return
#         else:
#             difference = compare_numbers(guess, random_number)
#             if difference < 5:
#                 print("You're very close!")
#             elif difference < 10:
#                 print("You're getting there, but still so far.")
#             else:
#                 print("You're way off, keep trying!")
    
#     print(f"Sorry, you ran out of tries. The number was {random_number}.")

# play_game()

'''
 What's the word?
Similar to 'What's the Number?', this name focuses on the user having to guess the randomly generated word. 
You can create a list from which the word would have to be guessed and also set a cap on the number of guesses allowed.
After this, you can create the rules yourself! When the user inputs the word, 
you can indicate whether the alphabet written appears in this particular position or not.
You will need a function to check if the user is inputting alphabets or numbers and to display
error messages appropriately.
'''

# import random

# # Function to check if the input is valid
# def is_valid_input(input_str):
#     if not input_str.isalpha():
#         print("Invalid input. Please enter only alphabets.")
#         return False
#     if len(input_str) != 1:
#         print("Invalid input. Please enter only one alphabet.")
#         return False
#     return True

# # Function to play the game
# def play_game(word_list):
#     num_tries = 6 # Default number of tries
#     random_word = random.choice(word_list)
#     word_length = len(random_word)
#     guessed_word = ["_"] * word_length
#     print("Welcome to the 'What's the Word?' game!")
#     print(f"I'm thinking of a word with {word_length} letters. You have {num_tries} tries to guess it.")

#     for i in range(num_tries):
#         user_input = input(f"Guess #{i + 1}: ")
#         if not is_valid_input(user_input):
#             continue

#         alphabet = user_input.lower()
#         if alphabet in random_word:
#             for j in range(word_length):
#                 if random_word[j] == alphabet:
#                     guessed_word[j] = alphabet
#             print("You guessed a correct alphabet!")
#             print(" ".join(guessed_word))
#         else:
#             print("Sorry, that alphabet is not in the word.")
    
#         if "".join(guessed_word) == random_word:
#             print(f"Congratulations! You guessed the word '{random_word}' in {i + 1} tries.")
#             return
    
#     print(f"Sorry, you ran out of tries. The word was '{random_word}'.")

# # Prompt the user to input a list of words
# word_list = input("Enter a list of words, separated by commas: ").split(",")
# word_list = [word.strip() for word in word_list]
# print(f"The words you have provided are: {word_list}")

# # Play the game with the user-inputted word list
# play_game(word_list)

'''
 Contact Book
Everyone uses a contact book to save contact details, including name, address, phone number, and even email address. 
The main objective of this project is to generate a contact book using python where users can add a new contact, edit, or delete existing contacts
and view the details of all their contacts.

# '''
# # define a Contact class to hold contact information
# class Contact:
#     def __init__(self, name, address, phone, email):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         self.email = email

# # define a ContactBook class to manage contacts
# class ContactBook:
#     def __init__(self):
#         self.contacts = []

#     def add_contact(self, contact):
#         self.contacts.append(contact)

#     def remove_contact(self, name):
#         for contact in self.contacts:
#             if contact.name == name:
#                 self.contacts.remove(contact)
#                 return True
#         return False

#     def find_contact(self, name):
#         for contact in self.contacts:
#             if contact.name == name:
#                 return contact
#         return None

#     def edit_contact(self, name, field, new_value):
#         contact = self.find_contact(name)
#         if contact is None:
#             return False
#         if field == "name":
#             contact.name = new_value
#         elif field == "address":
#             contact.address = new_value
#         elif field == "phone":
#             contact.phone = new_value
#         elif field == "email":
#             contact.email = new_value
#         else:
#             return False
#         return True

#     def view_contacts(self):
#         for contact in self.contacts:
#             print("Name: ", contact.name)
#             print("Address: ", contact.address)
#             print("Phone: ", contact.phone)
#             print("Email: ", contact.email)
#             print("--------------------------")

# # create an instance of the ContactBook class
# book = ContactBook()

# # loop until the user chooses to exit
# while True:
#     print("1. Add Contact")
#     print("2. Edit Contact")
#     print("3. Remove Contact")
#     print("4. View Contacts")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         name = input("Enter name: ")
#         address = input("Enter address: ")
#         phone = input("Enter phone number: ")
#         email = input("Enter email address: ")
#         contact = Contact(name, address, phone, email)
#         book.add_contact(contact)
#         print("Contact added successfully!")
#     elif choice == 2:
#         name = input("Enter name: ")
#         field = input("Enter field to edit (name, address, phone, or email): ")
#         new_value = input("Enter new value: ")
#         if book.edit_contact(name, field, new_value):
#             print("Contact updated successfully!")
#         else:
#             print("Contact not found.")
#     elif choice == 3:
#         name = input("Enter name: ")
#         if book.remove_contact(name):
#             print("Contact removed successfully!")
#         else:
#             print("Contact not found.")
#     elif choice == 4:
#         book.view_contacts()
#     elif choice == 5:
#         break
#     else:
#         print("Invalid choice. Please try again.")
'''
Password Checker
Online security is essential in this modern world where everything happens online. 
Passwords are the armors that protect our accounts from getting hacked or compromised.
Having said that, creating a strong password is a tedious task. You can build a program that 
intakes some words from the user 
and then generates a random password using those words.
'''
# import random
# import re
# import string

# def password_checker(password):
#     if len(password) < 8:
#         return False
#     if not re.search("[a-z]", password):
#         return False
#     if not re.search("[A-Z]", password):
#         return False
#     if not re.search("[0-9]", password):
#         return False
#     if not re.search("[_@$]", password):
#         return False
#     return True

# def generate_password(words):
#     password = ""
#     for i in range(3):
#         password += random.choice(words).capitalize()
#     for i in range(3):
#         password += random.choice(string.digits)
#     for i in range(2):
#         password += random.choice(string.punctuation)
#     password += random.choice(words)
#     return password

# words = input("Enter some words separated by spaces: ").split()
# password = generate_password(words)
# print("Your new password is:", password)

# if password_checker(password):
#     print("Your password is strong!")
# else:
#     print("Your password is not strong enough.")

#2nd code

# import random

# # Prompt user to enter words
# words = input("Enter some words separated by spaces: ").split()

# # Concatenate words together
# password = ''.join(words)

# # Shuffle the letters of the password
# password = ''.join(random.sample(password, len(password)))

# # Output the password
# print("Your random password is:", password)

'''
Quiz Application
This is one of the interesting python project ideas to create. 
This is a standard quiz application that presents a set of carefully curated
questions to the users (a questionnaire), allows them to answer the same,
and displays the correct answer if they are wrong. 
Each test will display the final score of the user.
'''


questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["Mount Everest", "Mount Kilimanjaro", "Mount Fuji", "Mount Rushmore"],
        "answer": "Mount Everest"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yen", "Dollar", "Euro", "Pound"],
        "answer": "Yen"
    }
]

score = 0

for i, question in enumerate(questions):
    print(f"Question {i+1}: {question['question']}")
    for j, option in enumerate(question['options']):
        print(f"{j+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if question['options'][int(user_answer)-1] == question['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['answer']}")

print(f"Your final score is {score}/{len(questions)}")
