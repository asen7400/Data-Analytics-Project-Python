#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install matplotlib')
get_ipython().system('pip install pandas')
get_ipython().system('pip install seaborn')


# In[6]:


#loading the required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[7]:


fifa= pd.read_csv(r"C:\Users\asen7\Downloads\FIFA_20.csv")


# In[8]:


fifa.head(10)


# In[9]:


for col in fifa.columns:
    print(col)


# In[10]:


fifa.shape


# In[11]:


18278*104


# In[28]:


#by default prints top 10 enrties
fifa['nationality'].value_counts()


# In[13]:


#top five countries
fifa['nationality'].value_counts()[0:5]


# In[14]:


fifa['nationality'].value_counts()[0:5].keys()


# In[15]:


#creating bar plot 1st variable needs to be categorical
plt.figure(figsize=(5,6))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="g")
plt.grid(True)


# In[16]:


player_salary=fifa[['short_name','wage_eur']]


# In[17]:


player_salary.head()


# In[18]:


player_salary=player_salary.sort_values(by=['wage_eur'],ascending=False)


# In[19]:


player_salary.head()


# In[20]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5], list(player_salary['wage_eur'])[0:5], color=["blue","green","red","purple","orange"])
plt.show()


# In[21]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5], list(player_salary['wage_eur'])[0:5], color="blue")
plt.show()


# In[22]:


fifa['nationality']=="Argentina"


# In[23]:


Argentina=fifa[fifa['nationality']=='Argentina']
Argentina.head(10)


# In[24]:


#sorting in ascending order
Argentina.sort_values(by=['height_cm'],ascending=True).head()


# In[25]:


##sorting in decending order##   
Argentina.sort_values(by=['height_cm'],ascending=False).head()


# In[26]:


Argentina[['short_name','wage_eur']].sort_values(by=['wage_eur'], ascending=False).head()


# In[ ]:




