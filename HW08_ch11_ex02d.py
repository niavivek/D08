#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    #create a list of values for each key
    inverse = dict()
    for key in d:
        val = d[key]
        # returns default value when it already contains the value, else it adds the value to the list
        inverse[val] = inverse.get(val, []) + [key]
    return inverse


def print_hist_newest(d):
    #get only the keys
    d_keys = []
    for key in d:
        d_keys.append(key)
    d_keys.sort()#sort the keys
    for keys in d_keys:#print keys and values
            print(keys,d[keys])

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_old(s):
    d = dict()
    for c in s:
        #d.get(c, 1)
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


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
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
