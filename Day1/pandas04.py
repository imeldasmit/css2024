# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:19:05 2024

@author: iSmit

Excercises
"""

import pandas

file = pandas.read_csv("insurance_data.csv", skiprows = 5)
"""
Error message "ParserError: Error tokenizing data. C error: Expected 1 fields in line 7, saw 2":
    Pandas expect consistent columns
    Meta data in this files causes the problem
    SOLUTION: Skip rows <TIP: Look for Pandas User Guide> 
"""

print(file)                     # display data stored in insurance file

print(file.info())

print(file.describe())

