#!/usr/bin/python3

""" This is a program that checks whether the password is safe or not using regular expressions. """

import re

capital = re.compile(r'[A-Z]')
numerical = re.compile(r'[0-9]')

user_passwd = input('Please enter your password: ')

def Verify(user_passwd):
    capital_count = 0
    numerical_count = 0 
    user_passwd = list(user_passwd) #Turn into a list first
    for letter in user_passwd:
        if capital.search(letter) != None: #Iterate through each character in the list checking whether there's a capital letter
            capital_count = capital_count + 1 
        if numerical.search(letter) != None:
            numerical_count = numerical_count + 1
    if capital_count > 0 and numerical_count > 0:
        print('The password is valid and apparently safe')
    else:
        print('The password you entered is incorrect, make sure it has a capital letter, a digit, and is longer than 8 characters')

Verify(user_passwd)

