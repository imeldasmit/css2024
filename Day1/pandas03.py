# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:19:05 2024

@author: iSmit

Excercises
"""

import pandas

"""
Problem: Dirty data, no column names
"""

column_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

file = pandas.read_csv("housing_data.csv", names = column_names, sep = ";")

# file = pandas.read_csv("housing_data.csv")

print(file)           # display data stored in housing file

print(file.info())

print(file.describe())

"""
Problem: Dirty data, no column names
"""

column_names = ["A", "B", "C", ...]

file = pandas.read_csv("housing_data.csv", names = column_names)


"""
Files in a sub directory
file = pandas.read_csv("chatfiles/air_traffic.csv")
"""
