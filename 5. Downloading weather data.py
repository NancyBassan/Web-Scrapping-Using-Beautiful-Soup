#!/usr/bin/env python
# coding: utf-8

# #### Import necessary library

# In[1]:


import requests
from bs4 import BeautifulSoup


# #### Download the web page containing the forecast and Create a BeautifulSoup class to parse the page.

# In[2]:


page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')


# #### Find the div with id seven-day-forecast, and assign to seven_day

# In[3]:


seven_day = soup.find(id="seven-day-forecast")


# #### Inside seven_day, find each individual forecast item.

# In[4]:


forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())


# #### Extract and print the first forecast item

# In[5]:


period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)


# In[6]:


img = tonight.find("img")
desc = img['title']
print(desc)


# #### Extracting all the information from the page

# In[7]:


#Select all items with the class period-name inside an item with the class tombstone-container in seven_day
period_tags = seven_day.select(".tombstone-container .period-name")

#Use a list comprehension to call the get_text method on each BeautifulSoup object.
periods = [pt.get_text() for pt in period_tags]
periods


# In[8]:


short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)


# #### Combining our data into a Pandas Dataframe

# In[9]:


import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
weather


# In[ ]:




