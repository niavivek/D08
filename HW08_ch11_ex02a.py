#!/usr/bin/env python3
# HW08_ch11_ex02a
# This is discussed in ThinkPython2 but not formally an exercise.
# Dictionaries have a method called 'get' that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
###############################################################################
# Imports


# Body
pledge_histogram = {}


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
    # read the file and split the lines into words and return them as a list
    with open("pledge.txt",'r') as pledge_file:
        for lines in pledge_file:
            each_word = lines.split()
            for word in each_word:
                pledge_list.append(word)
    return pledge_list
    # return pledge_list (uncomment this)


###############################################################################
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
