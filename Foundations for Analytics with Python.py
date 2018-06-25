#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:10:57 2018

@author: martin
"""

#June 12, 2018
import re
# lower(), upper(), capitalize()
string8 = "here is WHAT Happens when YoU USE Capitalize."
print("Output #36: {0:s}".format(string8.capitalize()))
string8_list = string8.split()
print("Output #37 (on each word):")
for word in string8_list:
    print("{0:s}".format(word.capitalize()))

#Regular Expressions / Pattern Matching
#Count the number of times a pattern appears in a string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count = count+1
print("Output #38 : {0:d}".format(count))

#Print the pattern each time it is found in the string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r'(?P<word_match>The)', re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group("word_match")))

#Substitute the letter "a" for the word "the" in the string
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {0:s}".format(pattern.sub("a", string)))

#June 13, 2018
#Dates
#Print today's date, as well as the year, month, and day element
from datetime import date, time, datetime, timedelta
today = date.today()
print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))

#Calculate a new date using a timedelta
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: Yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s}, {1!s}".format(eight_hours.days, eight_hours.seconds))

#Calculate the amount of time between two dates and grab the first element,
#the number of days
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))
#%%
#Create a string with a specific format from a data object
print("Output #50: {:s}".format(today.strftime("%m/%d/%Y")))
print("Output #51: {:s}".format(today.strftime("%b %d, %Y")))
print("Output #52: {:s}".format(today.strftime("%y-%m-%d")))
print("Output #53: {:s}".format(today.strftime("%B %d, %Y")))
      
#June 14, 2018
#%%
#Create a datetime object with a specific format
#from a string representing a date
date1 = today.strftime("%m/%d/%Y")
date2 = today.strftime("%b %d, %Y")
date3 = today.strftime("%Y-%m-%d")
date4 = today.strftime("%B %d, %Y")

#Two datetime objects and two date objects
#based on four strings that have different date formats
print("Output #54: {!s}".format(datetime.strptime(date1, "%m/%d/%Y")))
print("Output #55: {!s}".format(datetime.strptime(date2, "%b %d, %Y")))

#Show the date portion only
print("Output #56: {!s}".format(datetime.date(datetime.strptime(date3,\
      "%Y-%m-%d"))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime(date4, \
      "%B %d, %Y"))))

#June 15, 2018
#%%
#List
#Use square brackets to create a list
#len() counts the number of elements in a list
#max() and min() find the maximum and minimum numbers in numeric lists
#count() counts the number of times a value appears in a list
a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list has {} elements.".format(len(another_list)))
print("Output #64: 5 in another_list appears {} time.".format \
      (another_list.count(5)))

#June 19, 2018
#%%
#Use list indices to access specific values in a list
#[0] is the first value; [-1] is the last value
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))

#Use list slices to access a subset of list of values
#Do not include the starting indice to start from the beginning
#Do not include the ending indice to go all of the way to the end
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))

# =============================================================================
#June 21, 2018
# =============================================================================
#%%
#Use [:] to make a copy of a list
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))

#Use + to add two or more lists together
a_longer_list = a_list + another_list    #to add lists together
print("Output #78: {}".format(a_longer_list))
      
#Use 'in' and 'not in' to check whether specific values are or are not in a list
a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
    print("Output #80: 2 is in {}".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Output #82: 6 is not in {}".format(a_list))

#Use append() to add additional value to the end of the list
#Use remove() to remove specific values from the list
#Use pop() to remove values from the end of the list
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))
      
#Use reverse() to reverse a list, in place, meaning it change the list
#To reverse a list without changeing the original list, make a copy first
a_list.reverse()
print("Output #86: {}".format(a_list))
a_list_copy = a_list[:]
a_list_copy.reverse()
print("Output #87: {}".format(a_list_copy))
  
# Use sort() to sort a list, in-place, meaning it changes the list
# To sort a list without changing the original list, make a copy first      
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

# =============================================================================
#June 22, 2018 
# =============================================================================
#%%
# Use sorted() to sort a collection of lists by a position in the list
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))

# Use itemgetter() to sort a collection of lists by two index positions
from operator import itemgetter
my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678], \
[578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))

# Tuples
# Use parentheses to create a tuple
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my_tuple has {} elements".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print("Output #96: {}".format(longer_tuple))

# Unpack tuples with the left-hand side of an assignment operator
one, two, three = my_tuple
print("Output #97: {0} {1} {2}".format(one, two, three))
var1 = 'red'
var2 = 'Robbin'
print("Output #98: {} {}".format(var1, var2))
# Swap values between variables
var1, var2 = var2, var1
print("Output #99: {} {}".format(var1, var2))

# Covert tuples to lists and lists to tuples
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print("Output #100: {}".format(tuple(my_list)))
print("Output #101: {}".format(list(my_tuple)))

# =============================================================================
# June 25, 2018
# =============================================================================
# Dictionaries
# Use curly braces to create a dictionary
# Use a colon between keys and values in each pair
#len() counts the number of key-value pairs in a dictionary
#%%
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements".format(len(another_dict)))

# Use keys to access specific values in a dictionary
#%%
print("Output #106: {}".format(a_dict['two']))