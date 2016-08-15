#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports
pledge_histogram = {}

# Body
def print_hist_old(h):
	for c in h:
		print(c, h[c])


def print_hist_new(h):
	#get the key for all the values
	list_keys = []
	for key in h:
		list_keys.append(key)
	#sort the keys
	list_keys.sort()
	# print the keys and values
	for keys in list_keys:
		print(keys,h[keys])


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
# Body


def histogram_new(s):
	d = dict()
	for c in s:
		# returns default value when it already contains the value, else it increases the value by 1
		d[c] = d.get(c, 0) + 1
	return d

def get_pledge_list():
	""" Opens pledge.txt and converts to a list, each item is a word in
	the order it appears in the original file. returns the list.
	"""
	# Your code here.
	pledge_list = []
	with open("pledge.txt",'r') as pledge_file:
		for lines in pledge_file:
			each_word = lines.split()
			for word in each_word:
				pledge_list.append(word)
	return pledge_list
	# return pledge_list (uncomment this)

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():
	""" Calls print_hist_new with the appropriate arguments to print the
	histogram of pledge.txt.
	"""
	print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
	main()
