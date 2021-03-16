# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:49:54 2021

@author: Tuan
civic Hanah Hanah
"""
def isPalindrome(s):
    return s == s[::-1]

def findAllPalindrome():
    list_all=list()
    for line in open("Lab08_05.py"):
        words = line.strip().lower().split()
        for x in words:
            if isPalindrome(x):
                list_all.append(x)
    return list_all

palindrome_list = findAllPalindrome()
print("The unique words that are palindrome are:-", set(palindrome_list))