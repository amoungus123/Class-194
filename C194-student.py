#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name :")
print("We will learn about bubble plot today and find some intresting facts about prodution of movies their revenue")


# # Activity 1 - Which movies has collected more than Four hundred million dollors in box office

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

disney_movies = pd.read_csv('disney_movies.csv')
disney_movies


# In[3]:


#Find list of movies who has collected more then Four hundred million dollors in box office
movies_collection = disney_movies.loc[disney_movies['total_gross'] > 400000000]
movies_collection


# In[4]:


#Plot a bubble graph to show which movies who has collected more then Four hundred million dollors in box office
plt.figure(figsize=(12, 8))
plt.xticks(rotation='vertical')

rgb = np.random.rand(3)
print(rgb)

plt.scatter(movies_collection['movie_title'], movies_collection['total_gross'], 
                  c=[rgb],label = 'Total Gross', 
                 alpha=0.5,
                 s = movies_collection['total_gross']/1000000)

plt.legend()
plt.xlabel("Movies", size=14)
plt.ylabel("Total Gross", size=14)


# Conclusion - Star wars Ep 7: The Force Awakers and The Avengers are 2 movies which made the most in box office till now
# 

# # Activity 2 - Find the total number of movies per year and plot a bubble chart, to find out in which year the maximum  movies were produced
# 
# 
# 

# In[5]:


#Import libraries and read csv 'movie_update.csv'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movie_update = pd.read_csv('movie_update.csv')
movie_update


# In[6]:


#Group by year column and find total number of movies released each year 
group_year = movie_update.groupby('Year')['Title'].count().reset_index()
group_year


# In[7]:


#Plot a bubble graph to show total number of movies released each year
plt.figure(figsize=(20, 8))
plt.scatter(group_year [ 'Year'], group_year [ 'Title'], 
             color='lilac', label='Number of movies', 
             alpha=0.5, 
             s=group_year['Title']*3 )

plt.xticks (rotation='vertical')
plt.legend()
plt.xlabel("Years", size=14)
plt.ylabel("Number of movies", size=14)


# Conclusion - 

# # Activity 3 - Find which category of movie has the maximum income as per you.
# 
# 
# 

# In[8]:


#Read 'disney_movies.csv'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('disney_movies.csv') = df

#Put a condition as per you to find out which category of movie has the maximum income
movies = df.loc[df['total_gross'] > 300000000] 
movies


# In[9]:


#Group by genre and sum the total income of the movies
group_by_genre = movies.groupby('genre')['total_gross'].sum().reset_index() 
group_by_genre


# In[10]:


#Plot a pie chart as per the genre and fetch which category of movie to make for making the maximum profit
value=group_by_genre['total_gross'] 
label=group_by_genre['genre'] 
plt.pie(value, labels-label, autopct='%0.2f%%', radius=2) 
plt.show()


# Conclusion : 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




