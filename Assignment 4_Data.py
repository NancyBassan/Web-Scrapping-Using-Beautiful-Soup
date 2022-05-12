#!/usr/bin/env python
# coding: utf-8

# # Importing Python Libraries

# In[18]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
pd.set_option('display.max_colwidth', 500)
import time
import random


# # Collecting and Parsing a Web Page

# In[19]:


# Collect first page of artists’ list
page1 = requests.get('https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html')
page2 = requests.get('https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html/2')

# Create a BeautifulSoup object
soup1 = BeautifulSoup(page1.text, 'html.parser')
soup2 = BeautifulSoup(page2.text, 'html.parser')


# # Check whether the page is downloaded

# In[20]:


page1.status_code


# In[21]:


page2.status_code


# # Pulling Text From a Web Page inside the Class post for page1 and page2

# # Pulling Quotes on Page1

# In[22]:


# Navigating the soup for Page1
quotes1 = soup1.find(class_='post')
quotes = []
# looking for content inside the <li> tag
for h in quotes1.findAll('li'):
    quotes1 = h.text
    quotes.append(quotes1)


# # List of Quotes on Page1

# In[23]:


print(quotes)


# # Pulling Authors mentioned on page1

# In[24]:


# Navigating the soup for Page 1
author1 = soup1.find(class_='post')
# looking for em tag inside the <a> tag
authors = []
for h in author1.findAll('a'):  
    author1 = h.find('em')
    if author1 == None :
        continue
    authors.append(next(author1.children).strip())


# # List of Authors on Page1

# In[25]:


print(authors)


# # Pulling Quotes on Page2

# In[26]:


# Navigating the soup for Page 2
quotes2 = soup2.find(class_='post')
# looking for content inside the <li> tag
k=0
quote = []
for h in quotes2.findAll('li'):
    if k < 20 :
        quotes2 = h.text
        k = k+1
        quote.append(quotes2)
    


# # List of Quotes on Page2

# In[27]:


print(quote)


# # Pulling Authors mentioned on page2

# In[28]:


# Naavigating the soup for Page 2
author2 = soup2.find(class_='post')
# looking for em tag inside the <a> tag
author = []
l=0
for h in author2.findAll('a'):  
    author2 = h.find('em')
    if author2 == None :
        continue
    author2 = next(author2.strings).strip()
    l=l+1
    author.append(author2)


# # List of Authors on Page2

# In[29]:


# combine 18 and 19
author[18] = author [18] + ',' + author [19]
author[19]= author [20]
del author[20]
print(author)


# # Combine the results of two Pages

# In[30]:


Authors = authors + author
Quotes = quotes + quote


# # Avoiding Web Scraping Detection

# In[31]:


# List for Randomizing our request rate
rate = [i/10 for i in range(10)]
# Randomizing our request rate    
time.sleep(random.choice(rate))


# # Print the Quotes and their Respective Author Name in Dataframe

# In[32]:


famous_quotes = pd.DataFrame({
    "Quotes": Quotes,
    "Authors": Authors 
})
famous_quotes


# In[ ]:




