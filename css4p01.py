# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 08:40:32 2024

@author: Imelda Smit
         --> I made use of the notes I made while attending CSS
         --> I also enquired chatGPT (free version) to guide me
         
Project:
As a researcher, you are tasked to do use ETL and EDA skills on a 
movie dataset to extract certain insights.
Using Pandas, use the "movie_dataset.csv" found in the "Week 1" 
section of Canvas.
"""

"""
Use pandas
Get familiarised with data
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")

print(df)                 # display data stored in csv file movie_dataset

print(df.info())          # table summary: -number of columns, -their names, -Non-Null Count, and -the Dtype or data type

print(df.describe())      # generate descriptive statistics of a DataFrame or Series. 

"""  
Some columns have missing values and it would be best to either 
fill or drop where appropriate those missing values to prevent a bias.
Load and clean the data, make reasonable assumptions.
"""

"""
df.dropna(inplace = True) # remove NAN rows (a cell with no data)
This resulted in incorrect answers, so NAN rows were retained, and average values used to fill NANs
"""

# Replace empty values for Revenue and Metascore with mean values - 
#    using fillna method
revMean = df['Revenue (Millions)'].mean().round(2)
df['Revenue (Millions)'].fillna(revMean, inplace=True)

metaMean = df['Metascore'].mean().round(2)
df['Metascore'].fillna(metaMean, inplace=True)

"""
# Not getting the correct answer in Q4, try
# Convert 'Year' column to integer
df['Year'] = df['Year'].astype(int)
# see if there are unexpected values or formatting issues
print(df['Year'].unique())
"""

"""
Question 1 --> 1 pt
What is the highest rated movie in the dataset?
o	Rogue One   o	Trolls   o	The Dark Knight *    o	Jason Bourne
"""

# Learn the column names
print(df.columns.tolist())

# Find the row with the highest rating
max_rating_row = df[df['Rating'] == df['Rating'].max()]

# Extract the title of the movie with the highest rating
highest_rated_title = max_rating_row['Title'].values[0]

# Print or use the result
print(f"Q1: The highest-rated movie is '{highest_rated_title}' with a rating of {df['Rating'].max()}")

"""
Question 2 --> 1 pt
What is the average revenue of all movies in the dataset? 
    Note, since the answer will be effected by how you dealt with missing 
    values, a range has been provided. 
o	Between 70 and 100 Million *   o	Between 120 and 140 Million
o	More than 200 Million          o	Between 100 and 120 Million
"""

# Calculate the average revenue
average_revenue = df['Revenue (Millions)'].mean()

# Print or use the result
print(f"Q2: The average revenue of all movies is: ${average_revenue:.2f} Million")

"""
Question 3 --> 1 pt
What is the average revenue of movies from 2015 to 2017 in the dataset?
    Note, since the answer will be effected by how you dealt with missing
    values, a range has been provided. 
o	Less than 40 Million         o	More than 120 Million
o	Between 50 and 80 Million *  o	Between 100 and 120 Million
"""

# Filter the DataFrame for movies released from 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

# Print or use the result
print(f"Q3: The average revenue of movies from 2015 to 2017 is: ${average_revenue_2015_to_2017:.2f} Million")

"""
Question 4 --> 1 pt
How many movies were released in the year 2016?
o	301     o	297 *      o	113     o	287
"""

# Filter the DataFrame for movies released in the year 2016
movies_2016 = df[df['Year'] == 2016]

# Get the number of movies released in 2016
num_movies_2016 = len(movies_2016)

# Print or use the result
print(f"Q4: The number of movies released in 2016 is: {num_movies_2016}")

"""
Question 5 --> 1 pt
How many movies were directed by Christopher Nolan?
o	6       o	5 *     o	7       o	4
"""

# Filter the DataFrame for movies directed by Christopher Nolan
director_CN = df[df['Director'] ==  "Christopher Nolan"]

# Get the number of movies directed by Christopher Nolan
num_movies_directed_CN = len(director_CN)

# Print or use the result
print(f"Q5: The number of movies directed by Christopher Nolan is: {num_movies_directed_CN}")

"""
Question 6 --> 1 pt
How many movies in the dataset have a rating of at least 8.0?
o	45       o	98       o	78 *    o	81
"""

# Filter the DataFrame for movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

# Get the number of with a rating of at least 8.0
num_movies_rating_8_plus = len(high_rated_movies)

# Print or use the result
print(f"Q6: Movies with a rating of at least 8.0: {num_movies_rating_8_plus}")

"""
Question 7 --> 1 pt 
What is the median rating of movies directed by Christopher Nolan?
o	6.9     o	9.1    o	8.6 *   o	7.4
"""

# Filter the DataFrame for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating for Christopher Nolan's movies
median_rating_CN_movies = director_CN['Rating'].median()

# Print or use the result
print(f"Q7: The median rating of movies directed by Christopher Nolan is: {median_rating_CN_movies:.2f}")

""" 
Question 8 --> 1 pt
Find the year with the highest average rating?
o	2008    o	2007 *  o	2016    o	2006
"""

# Group the DataFrame by 'Year' and calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_avg_rating = average_rating_by_year.idxmax()

# Print or use the result as needed
print(f"Q8: The year with the highest average rating is {year_highest_avg_rating}")

"""
Question 9 --> 1 pt
What is the percentage increase in number of movies made between 2006 and 2016?
o	57      o	421     o	575 *   o	210
"""

# Filter the DataFrame for movies released in 2006 and 2016
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

# Get the number of movies made in 2006 and 2016
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

# Print or use the result as needed
print(f"Q9: The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")

"""
Question 10	--> 3 pts
Find the most common actor in all the movies?
    Note, the "Actors" column has multiple actors names.
    You must find a way to search for the most common actor in all the movies.
o	Bradley Cooper             o	Mark Wahlberg *
o	Matthew McConaughey        o	Chris Pratt
"""

# import counter
from collections import Counter

# Combine all actors' names into a single list
all_actors = [actor for actors_list in df['Actors'].str.split(', ') for actor in actors_list]

# Use Counter to count the occurrences of each actor
actors_counter = Counter(all_actors)

# Find the most common actor
most_common_actor = actors_counter.most_common(1)[0][0]

# Print or use the result as needed
print(f"Q10: The most common actor in all the movies is: {most_common_actor}")

"""
Question 11	--> 3 pts
How many unique genres are there in the dataset?
    Note, the "Genre" column has multiple genres per movie. 
    You must find a way to identify them individually.
o	20      o	15      o	207 *   o	30
"""

# Split the "Genre" column into individual genres and create a set of unique genres
unique_genres = set(genre for genres_list in df['Genre'].str.split(', ') for genre in genres_list)

# Get the count of unique genres
num_unique_genres = len(unique_genres)

# Print or use the result as needed
print(f"Q11: The number of unique genres in the dataset is: {num_unique_genres}")

""" 
Question 12	--> 10 pts
Do a correlation of the numerical features, what insights can you deduce?
Mention at least 5 insights.
And what advice can you give directors to produce better movies?
"""

# Selecting only the numerical columns 
# (Rank, Runtime (min), Rating, Votes, Revenue (mil), Metascore)
numerical_columns = df.select_dtypes(include=['int64', 'float64'])

# Calculating the correlation matrix
correlation_matrix = numerical_columns.corr()

# Displaying the correlation matrix
print("Q12: ", correlation_matrix)

# The values range from -1 to 1, where:
# 1 indicates a perfect positive correlation,
# -1 indicates a perfect negative correlation, and
# 0 indicates no correlation.

# High positive correlation between 
#   Votes and Revenue (0.64); 
#   Rating and metascore (0.67);
#   Votes and Runtime (0.4);
#   Rating and Runtime (0.37)
# High negative correlation between
#   None

""" 
Question 13	--> 1 pt
Once you have completed the Quiz questions, create a GitHub repository and
upload a single python file called "css4p01.py" to it.
Share the url ink for your python file below.
The code must show all the code used to load, analyse and clean the data, 
as well as how you answered the Quiz questions.
Make reasonable assumptions.
"""
print("Q13: ")