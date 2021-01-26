#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:48:10 2020

@author: tuan

https://www.geeksforgeeks.org/timeit-python-examples/
"""

# importing the required modules 
import timeit 

# linear search function 
def linear_search(mylist, find): 
	for x in mylist: 
		if x == find: 
			return True
	return False


# compute linear search time 
def linear_time(): 
	SETUP_CODE = ''' 
from __main__ import linear_search 
from random import randint'''
	
	TEST_CODE = ''' 
mylist = [x for x in range(1000)] 
find = randint(0, len(mylist)) 
linear_search(mylist, find) 
	'''
	# timeit.repeat statement 
	times = timeit.repeat(setup = SETUP_CODE, 
						stmt = TEST_CODE, 
						repeat = 2, 
						number = 10000) 

	# priniting minimum exec. time 
	print('Linear search time: {}'.format(min(times))) 

if __name__ == "__main__": 
	linear_time() 

