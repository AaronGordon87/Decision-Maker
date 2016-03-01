#!/usr/bin/python3

from collections import Counter
from random import randint
import webbrowser

print('How many of you are there?')
people = input()

destinations = ['the cinema', 'the pub', 'for dinner', 'bowling', 'a drive']
answers = []
results = []
winner = []

print('Please enter your postcode (without spaces).')
postcode = str(input())

for i in range(int(people)):
    i = 0
    while i < 5:
        if i < 1:
            print ('Hello and welcome to the decision maker. What is your name?')
            name = input()
            print('Hello ' + str(name), ', Would you like to go to ' + str(destinations[i]), '?') # the cinema/dinner/bowling/lazer zone/pub.....dictionary/list?
            decision = input()
            while decision not in ("Yes", "yes", "No", "no"):
                print('It must be a yes or no answer.')
                decision = input()
            if decision.lower() == 'yes':
                answers.append((destinations[i]))

        elif i > 0:
             print('Would you like to go to ' + str(destinations[i]), '?') # the cinema/dinner/bowling/lazer zone/pub.....dictionary/list?
             decision = input()
             while decision not in ("Yes", "yes", "No", "no"):
                print('It must be a yes or no answer.')
                decision = input()
             if decision.lower() == 'yes':
                answers.append((destinations[i]))
        i = i + 1


most_common = Counter(answers)
Counter(answers)

highest_number=0
for key in most_common:
    if most_common[key] > highest_number:
        highest_number = most_common[key]


for key in most_common:
    if most_common[key] == highest_number:
        winner.append(key)

        

randchoice = randint(0, len(winner))

print('You choice has been made for you - ' + winner[randchoice],'.')

webbrowser.open('http://www.yelp.com/search?find_desc=' + winner[randchoice] + '&find_loc=' + postcode + '&ns=1')
