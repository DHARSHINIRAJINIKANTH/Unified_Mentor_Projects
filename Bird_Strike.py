#!/usr/bin/env python
# coding: utf-8

# # Project 1 - Data Visualization of Bird Strikes between 2000 – 2011

# ## Importing the dataset

# In[23]:


import pandas as pd
data=pd.read_excel("Bird_strikes_data.xlsx")


# In[24]:


data.head(20)


# In[25]:


data.info()


# ## Data Cleaning and Preparation

# In[26]:


data=data.drop('Remarks',axis=1)


# In[27]:


data.info()


# In[28]:


data=data.dropna()


# In[29]:


data.info()


# ## Converting the prepared data to excel 

# In[31]:


data.to_excel('Bird_Strike.xlsx', index=False)


# In[ ]:




