# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:19:05 2024

@author: iSmit

Excercises
"""

import pandas

file = pandas.read_csv("iris.csv")

print(file)              # display data stored in iris file

print(file.info())

print(file.describe())