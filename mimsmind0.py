"""Program to implement the game - guessing a number based on the number of digits
from the command line"""
import random
from sys import argv

#default num_digits if none provided
num_digits = 1
try:
	#if the command line has the number of digits - assign it to the variable
	num_digits = int(argv[1])
except:
	num_digits = 1
#get the last number for the entered digits
end = 10**int(num_digits)
#get a random number
random_num = random.randrange(0, end)
#if the length of random number is less than expected digits - pad 0's
if (len(str(random_num)) < num_digits):
	random_num = "{:0>{}}".format(random_num, num_digits) # random_num is a string
#initialize guess
guess = ''
num_guess = 1 # counter for numer of guesses

print("Let's play the mimsmind0 game.")
print("Guess a {} digit number: ".format(num_digits),end="")
#repeat until guess is correct
while guess != int(random_num):
	try:
		guess = input() # get an input
		if len(str(guess)) == num_digits: # validate the length to number of digits expected
			guess = int(guess)	#check if it is an integer
		else:#error message for invalid number of digits
			print("Invalid Input. Try again: ",end="")
			continue
	except:#exception for non-integer
		print("Invalid Input. Try again: ",end="")
	else: # continue if no exception
	#if values are equal - success
		if int(random_num) == guess:
			print ("Congratulations. You guessed the correct number in {} tries.".format(num_guess))
			break
			#else say higher or lower
		elif int(random_num) < guess:
			print ("Try again. Guess a lower number: ",end="") 
		else:
			print ("Try again. Guess a higher number: ",end="")
		num_guess += 1 # increment guess counter