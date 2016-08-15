"""Program to implement the game - Bulls and cows: the program generates a random number 
with number of digits equal to length. If the command line argument length is not provided,
 the default value is 3. This means that, by default, the random number is in the range of 000 and 999. 
The program will establish a maximum number of rounds, maxrounds, equal to (2^length) + length. 
For example, if length = 3, then maxrounds = 11.
The program prompts the user to type in a guess, informing the user of the number of digits expected.
 The program will then read the user input, and provide 'bulls and cows' feedback to the user. 
 A matching digit in the correct position will result in a 'bull', while a matching digit in the
  wrong position will result in a 'cow'. For example, if the correct answer is '123', 
  and the guess is '324', then the feedback will be one bull (for the digit '2') 
  and one cow (for the digit '3')."""
import random
from sys import argv
#method to find the cows and bulls
def cow_bull(guess, expected, num_digits):
	#initialize values for cows and bulls variable
	cows = 0
	bulls = 0
	guess = "{:0>{}}".format(guess, num_digits) # pad 0's to the guess number as that is in int format
	guess = list(guess)
	expected = list(str(expected))
	b_indx = 0
	while b_indx < len(guess): # continue till all digits are visited
		if guess[b_indx] == expected[b_indx]: # if values at same index are equal, it's bulls
			bulls += 1
			guess.pop(b_indx)# pop the values, so they dont appear for cows evaluation
			expected.pop(b_indx)
		else:
			b_indx += 1 # increase counter if there was no pop
	c_indx = 0
	while c_indx < len(guess): # continue till all digits are visited
		if guess[c_indx] in expected: # if the digit is anywhere in the expected number
			cows += 1 #increment cow counter
		c_indx += 1 #increment index
	return cows, bulls
#method to get random number based on number of digits
def gen_rand_num(num_digits):
	end = 10**int(num_digits)#get ending digit
	random_num = random.randrange(0,end)#generate random number
	# if random number of length less than the required digits, pad 0's
	if (len(str(random_num)) < num_digits):
		random_num = "{:0>{}}".format(random_num, num_digits)	
	return random_num
#main game
def cows_and_bulls():
	# default value for digits
	num_digits = 3
	try:
		num_digits = int(argv[1]) # check if command line input for digits is integer
	except:
		num_digits = 3
	random_num = gen_rand_num(num_digits)
	max_round = (2**num_digits) + num_digits#calculate maximum number of guesses allowed
	guess = ''#initialize guess
	num_guess = 1 # counter for number of guesses
	print("Let's play the mimsmind1 game. You have {} guesses.".format(max_round))
	print("Guess a {} digit number: ".format(num_digits),end="")
	#continue till max guesses or till if guess is correct
	while (guess != int(random_num)) and (num_guess <= max_round):
		try:
			guess = input()
			#check for length of guess = length of required digits
			if len(str(guess)) == num_digits:
				#convert guess to integer
				guess = int(guess)
			else:
			#error for invalid number of digits in guess
				print("Invalid input. Try again: ",end="")
				continue
		except:
		#exception for non-integer values
			print("Invalid input. Try again: ",end="")
		else:
		#if input is valid, check for equality
			if int(random_num) == guess:
				print ("Congratulations. You guessed the correct number in {} tries.".format(num_guess))
				break
			else:
			#check for cows and bulls
				cow, bull = cow_bull(guess, random_num, num_digits)
				print ("{} bull(s), {} cow(s). Try again: ".format(bull, cow),end="")
				num_guess += 1
		
	#if maximum guesses is reached, print the result
	if (num_guess > max_round):
		print("Sorry. You did not guess the number in {} tries. The correct number is {}.".format(max_round, random_num))

def main():
	cows_and_bulls()

if __name__ == '__main__':
	main()	
