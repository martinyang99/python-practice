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
print("Output #56: {!s}".format(datetime.date(datetime.strptime(date3, "%Y-%m-%d))))
