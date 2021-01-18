#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:07:46 2020

@author: tuan
"""

n = int(input())
for i in range(n):
    print(' '*(n-i-1), end="")
    print('#'*(i+1))