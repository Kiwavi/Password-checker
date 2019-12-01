#!/usr/bin/python3

""" This is a program that checks whether the password is correct or not using regular expressions. Now I will make it more secure by making sure that the user doesn't """

import re

capital = re.compile(r'[A-Z]')
numerical = re.compile(r'[0-9]')
small_letter = re.compile(r'[a-z]')

password = re.compile(r'[A-Za-z\.\d@=-]+')

user_passwd = input('Enter your password: ')

def Verify(user_passwd):
    capital_count = 0
    numerical_count = 0 
    small_letter_count = 0
    both_count = 0
    user_passwd = list(user_passwd) #Turn into a list first
    for letter in user_passwd:
        if capital.search(letter) != None: #Iterate through each character in the list checking whether there's a capital letter
            capital_count = capital_count + 1 
        if numerical.search(letter) != None:
            numerical_count = numerical_count + 1
        if small_letter.search(letter) != None:
            small_letter_count = small_letter_count + 1
    if capital_count > 0 and  numerical_count > 0 and small_letter_count > 0 and len(user_passwd) > 11 :
        print('The password is valid and apparently safe')
    elif len(user_passwd) >= 12 and small_letter_count > 0 or capital_count > 0:
        print("Password is longer than 13 characters, thus safe")
    else:
        print('The password you entered is incorrect, make sure it has a capital letter, a small letter, a digit, and is longer than 11 characters')

Verify(user_passwd)

