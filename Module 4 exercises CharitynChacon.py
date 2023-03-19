#!/usr/bin/env python3

#1. What is a variable?
#A variable is a value that can change, depending on conditions

#2. What is a constant?
#Is a fixed value in an equation that is not affected by any changes in the variable.


# 3. Can a variable be changed once assigned?
# No,in python once a variable is assigned we can not change it, but we can reassign it if we want a different value.


#4. Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount by which to count.

print( "Welcome, let's count!")
start= int(input("\nEnter the starting number: " ))
end= int(input("Enter the ending number: "))
amount= int(input("Enter the amount by which to count: "))

for number in range (start,end,amount):
	print(number, end=" ")


##5 Create a program that gets a message from the user and then prints it out backwards.

message= input("\n\nNow, give me a short message: ")
print ("Your message will be given backwards: ",message[::-1])
print(input("\nPress enter key to keep with the next exercise"))


#6. Create a game where the computer picks a random word and the player has to guess that word. The computer tells the player how many letters are in the word. Then the player gets five chances to ask if a letter is in the word. The computer can only respond with “yes” or “no”. Then, the player must guess the word.

import random  

print("\n\nNow, You have to guess a word that I picked randomly for you...")
list_of_words= ["computer","phone", "television","watch"]

#pick a word randomly

word= random.choice(list_of_words)
answer= word

#program tells the player how many letter contains the word

print("The word that I choose for you has", len(word),"letters")

print("\nYou have 5 chances to ask me if a letter is in the word")

chance=5

while chance>0:
	guess= input("Give me a letter: ")
	chance -=1
	
	for letter in guess:
		if letter.lower() in word:
			print("Yes")
		else:
				print("No")
				
				print("\nYou have", chance, "more chances to guess the letters")
				
answer=input("\nCan you guess the word?: ")
if answer==word:
	print("\nCONGRATULATIONS! you guessed the word, the correct answer is: ", word)
else:
	print("\nSorry!! You have lost, the correct answer is: ", word)
#
#
#	

