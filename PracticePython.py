import random
# Exercise 1

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# user = input('Enter your user name ')
# age = int(input('Enter your age '))
# referenceYear = 2023

# futureAge = referenceYear + (100 - age)

# print(f"You will be 100 years old in {futureAge}")



# EXTRAS

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.

# Print out that many copies of the previous message on separate lines.

# user = input('Enter your user name ')
# age = int(input('Enter your age '))
# referenceYear = 2023
# number_copies = int(input('Enter the number of copies you want '))

# futureAge = referenceYear + (100 - age)

# for _ in range(number_copies):
#     print(f"You will be 100 years old in {futureAge} \n")

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 2

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# number = int(input("Enter a number "))

# if number % 2 == 0:
#     print (f"{number} is even")
# else:
#     print(f"{number} is odd")



# EXTRAS

# If the number is a multiple of 4, print out a different message.

# number = int(input("Enter a number "))

# if number % 4 == 0:
#     print(f"{number} is multiple of 4")
# elif number % 2 == 0:
#     print (f"{number} is even")
# else:
#     print(f"{number} is odd")



# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# num = int(input('Enter a number to check '))
# divide = int(input('Enter a number to divide '))

# if (num / divide) % 2 == 0:
#     print ('The result is even')
# elif (num / divide) % 2 == 1:
#     print ('The result is odd')
# else:
#     print ('The result is a float')

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 3

# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for element in a:
#     if element < 5:
#         print(element)



# EXTRAS

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = []

# for element in a:
#     if element < 5:
#         b.append(element)

# print(b)



# Write this in one line of Python.

# print( [ element for element in a if element <5 ] )



# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = []

# number = int(input('Enter a number '))

# for element in a:
#     if element < number:
#         b.append(element)

# print(b)

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 4

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# number = int(input('Enter a number '))

# list = []

# for i in range(1, i+1):
#     if number % i == 0:
#         list.append(i)

# print(f'The divisors of {number} are {list}')

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 5

# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# c = []

# for element in a:
#     if element in b and element not in c:
#         c.append(element)

# print(c)



# Extras

# Randomly generate two lists to test this

# list1 = []
# list2 = []

# length1 = random.randint(1, 10)
# length2 = random.randint(1, 10)

# for i in range(length1):
#     i = random.randint(1, 100)
#     list1.append(i)

# for i in range(length2):
#     i = random.randint(1, 100)
#     list2.append(i)

# print(f'Im list1 {list1}')
# print(f'Im list2 {list2}')

# resultList = []

# for element in list1:
#     if element in list2 and element not in resultList:
#         resultList.append(element)

# print(resultList)


# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# print( [e for e in a if e in b] )

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 6

# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# string = input('Enter a word ')

# reverse_string = string[::-1]

# if string == str(reverse_string):
#     print(f'{string} is a palindrome')
# else:
#     print(f'{string} is not a palindrome')

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 7

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# b = [ element for element in a if element % 2 == 0 ]

# print(b)

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 8

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# new_game = True

# while new_game == True:
#     player1 = input('Rock, Paper or Scissor? ')
#     player2 = input('Rock, Paper or Scissor? ')

#     if player1 == player2:
#         print('Draw')
#     elif player1 == 'Rock' and player2 == 'Paper':
#         print('Player two wins')
#     elif player1 == 'Rock' and player2 == 'Scissor':
#         print('Player one wins')
#     elif player2 == 'Rock' and player1 == 'Paper':
#         print('Player two wins')
#     elif player2 == 'Rock' and player1 == 'Scissor':
#         print('Player one wins')

#     question = input('Press y if you want a new game or n if you want to quit')

#     if question != 'y':
#         new_game = False

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 9

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# random_number = random.randint(1, 9)

# number = int(input('Guess the number between 1 and 9 '))

# if number == random_number:
#     print('Thats it!')
# elif number > random_number:
#     print('Too high!')
# elif number < random_number:
#     print('Too low!')
# else:
#     print('Error')



# EXTRAS

# Keep the game going until the user types “exit”

# exit = False

# while exit == False:
#     random_number = random.randint(1, 9)

#     number = int(input('Guess the number between 1 and 9 '))

#     if number == random_number:
#         print('Thats it!')
#     elif number > random_number:
#         print('Too high!')
#     elif number < random_number:
#         print('Too low!')
#     else:
#         print('Error')

#     question = input("Type 'exit' if you want to quit ")

#     if question == 'exit':
#         exit = True



# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# exit = False
# guesses = 0

# while exit == False:
#     random_number = random.randint(1, 9)

#     number = int(input('Guess the number between 1 and 9 '))

#     if number == random_number:
#         print('Thats it!')
#     elif number > random_number:
#         print('Too high!')
#     elif number < random_number:
#         print('Too low!')
#     else:
#         print('Error')
    
#     guesses += 1

#     question = input("Type 'exit' if you want to quit ")

#     if question == 'exit':
#         exit = True

# print(f'The user has taken {guesses} guesses')

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 10

# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

# The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

# print( [e for e in a if e in b] )



# EXTRAS

# Randomly generate two lists to test this

# a = random.sample(range(100), random.randint(1, 20))
# b = random.sample(range(100), random.randint(1, 20))

# print(a)
# print(b)
# print( [e for e in a if e in b] )

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 11

# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). Take this opportunity to practice using functions,

# def get_integer(help_text):
#   return int(input(help_text))

# def get_divisor_list(number):
#   list = []

#   for i in range(1, number+1):
#     if number % i == 0:
#       list.append(i)
  
#   return list

# def is_prime():
#   number = get_integer('Write a number ') 
#   divisors = get_divisor_list(number) 

#   if len(divisors) == 2:
#     print('The number is prime')
#   elif len(divisors) > 2:
#     print('The number is not prime')
#   else:
#     print('Error')

# is_prime()

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 12

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

# def first_and_last(list):
#   return ([list[0], list[-1]])

# print(first_and_last([5, 10, 15, 20, 25]))

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 13

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

# def get_integer(help_text):
#   return int(input(help_text))

# def get_fibonacci():
#   number = get_integer('Write the amount of Fibonacci numbers you want \n >>>')
#   list = [1, 1]

#   if number == 0:
#     print('Error')
#   elif number == 1:
#     print([1])
#   elif number == 2:
#     print(list)
#   else:
#     for _ in range(2, number):
#       new_number = list[-1] + list[-2]
#       list.append(new_number)
#     print(list)

# get_fibonacci()

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 14

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# def remove_duplicates(unfiltered_list):
#   unfiltered_list = set(unfiltered_list)
#   return (list(unfiltered_list))

# print(remove_duplicates([1,1,1,2,3,4,5,5,5,5]))


# EXTRAS

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

# def remove_duplicates(unfiltered_list):
#   filtered_list = []

#   for element in unfiltered_list:
#     if element not in filtered_list:
#       filtered_list.append(element)
  
#   return filtered_list

# print(remove_duplicates([1,1,1,2,3,4,5,5,5,5]))


# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Write the solution for this in a different function.

# def get_common_numbers(list1, list2):
#   return (set([e for e in a if e in b]))

# print(get_common_numbers(a, b))



# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 15

# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

# " My name is Michele "

# Then I would see the string:

# " Michele is name My "

# shown back to me.

# def get_reverse_order(sentence):
#   split_sentence = sentence.split()
#   reversed = []
#   for element in split_sentence:
#     reversed.insert(0, element)
  
#   return " ".join(reversed)

# print(get_reverse_order('The sun is shining'))

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 16

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# def generate_character_list():
#   string_list = 'abcdefghijklmnopqrstuvwxyz'
#   upper_string_list = string_list.upper()
#   number_list = '1234567890'
#   symbol_list = '!"#$%&/()=?¡¿¨*[];,:._-'

#   return (string_list + number_list + symbol_list + upper_string_list)

# def password_generator():
#   security_level = int(input('How many characters do you want the password to have? TIP: More characters make up for a strong password'))
#   character_list = generate_character_list()
#   password = ''
#   for _ in range (security_level):
#     index = random.randint(0, len(character_list))
#     password += character_list[index]

#   return password

# print(password_generator())

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 17



# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 18

# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

# Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.

# def cows_and_bull():
# 	guess = False
# 	random_number = str(random.randint(1000, 9999))
# 	print(random_number)

# 	while guess == False:
# 		bulls = 0
# 		cows = 0
    
# 		user_number = input('Enter a 4-digit: \n')

# 		for i in range(0, 4):
# 			if random_number.find(user_number[i]) != -1:
# 				if random_number[i] == user_number[i]:
# 					cows += 1
# 				else:
# 					bulls += 1
    
# 		if cows == 4:
# 			print('That\'s the correct number')
# 			guess = True
# 		else:
# 			print(f'{cows} cows, {bulls} bulls \nTry Again!')

# if __name__=="__main__":
#   cows_and_bull()

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 19


# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 20

# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

a = [1, 3, 5, 30, 42, 43, 500]

# def is_in_list(number):
#   for i in a:
#     if i == number:
#       return True
  
#   return False

# if __name__=="__main__":
#   user_number = int(input('Enter a number: \n>>> '))
#   if is_in_list(user_number):
#     print('The number is in the list')
#   else:
#     print('The number is not in the list')


# EXTRAS

# Use binary search.

# WITHOUT RECURSION

# def is_in_list(number):
#   new_list = a.copy()
#   half_list_index = round(len(new_list) / 2)
#   founded = False  

#   while founded == False:
#     if number == new_list[half_list_index]:
#       return True
#     elif len(new_list) == 1:
#       return False
#     elif number < new_list[half_list_index]:
#       new_list = new_list[0:half_list_index]
#       half_list_index = round(len(new_list) / 2)
#     else:
#       new_list = new_list[half_list_index:]
#       half_list_index = round(len(new_list) / 2)

# if __name__=="__main__":
#   user_number = int(input('Enter a number: \n>>> '))
#   if is_in_list(user_number):
#     print('The number is in the list')
#   else:
#     print('The number is not in the list')


# WITH RECURSION

# def is_in_list(number, list):
#   half_list_index = round(len(list) / 2)

#   if number == list[half_list_index]:
#     return True
#   elif half_list_index == 0:
#     return False
#   elif number < list[half_list_index]:
#     return is_in_list(number, list[0:half_list_index])
#   else:
#     return is_in_list(number, list[half_list_index:])
  
# if __name__=="__main__":
#   user_number = int(input('Enter a number: \n>>> '))
#   if is_in_list(user_number, a):
#     print('The number is in the list')
#   else:
#     print('The number is not in the list')



# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 21



# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 22



# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 23



# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 24

# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. 

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 

# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

# Remember that in Python 3, printing to the screen is accomplished by

#  print("Thing to show on screen")
#%%

def draw_game_board(num_cells):
  for cell in range(0, num_cells):
    print(" ---" * num_cells + "\n" + "|   " * num_cells + "|")
    if cell == num_cells - 1:
      print(" ---" * num_cells)

draw_game_board(4)

# - - - - - - - - - - - - - - - - - - - - - - - - 

# Exercise 24

# %%

import random

def guessing_number():
  guessed = False  
  min = 0
  max = 100
  while guessed == False:
    computer_number = random.randint(0, 100)
    print(f'Is {computer_number}')



# %%

