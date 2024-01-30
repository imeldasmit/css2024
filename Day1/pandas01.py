# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:19:05 2024

@author: iSmit

@data: country.csv
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)                 # display data stored in csv file

# Pandas useful featuers:

print(file.info())          # (1)
"""
table summary: 
    -number of columns, 
    -their names, 
    -Non-Null Count, and 
    -the Dtype or data type
"""

print(file.describe())        # (2)
"""
The .describe() method is used to generate 
descriptive statistics of a DataFrame or Series. 
It provides a summary of the central tendency, 
dispersion, and shape of the distribution of a dataset. 
It is primarily designed for summarizing numerical data, and 
it provides statistics that are meaningful for quantitative variables.
"""

# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)

# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# Lists indexes start at 0 which has the value of 30
print("First item - age (index 0): ", age[0])
print(age[1])
print("Last item (index 10): ", age[10])

# This will give an error as there is no value at index 11
# print(age[11])                # index access between 0 and 10 for 11 items

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print("Minimum age: ", min(age))
print("Maximum age: ", max(age))
print("Number of items/Length of the list: ", len(age))
print("Sum of ages: ", sum(age))
average = sum(age)/len(age)
print("Average age: ", average)

C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print("First item - gender (index 0): ", gender[0])
print(gender[1])
print(gender[2])
print("Last item - gender (index 11, or -1): ", gender[-1])               
# A nice feature: you can access the last value in the list by setting the index = -1.

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print("First item - country (index 0): ", country[0])
print(country[5])

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]

print(my_list)
"""
We can do many things with lists:
* print all the items in the list using [:]
* we can add items to the end of the list using append()
* add items at specific positions using insert()
* remove an item from the list using the remove() function
* check how many variables are in the list using the len()
* print a range of values using [start:end] – just like in excel!
"""

# More examples
my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])