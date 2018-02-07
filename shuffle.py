#!/usr/bin/python

# A GENERAL-PURPOSE SHUFFLER 
# This shuffling tool picks up the set of items to be shuffled 
# from a textfile and suggests a randomly re-ordered sequence 
# Use cases: 
# Restaurants to visit, dress clothes for the week, meal recipes, etc 

import random
itemList = []

fptr = open("items.conf", "r")
for line in fptr:
    itemList.append(line.strip('\n'))

random.shuffle(itemList)
print itemList 
