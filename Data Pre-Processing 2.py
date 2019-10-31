#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import datetime as dt
 #add comment

# In[3]:


data = pd.read_csv('nyzseg.csv')


# In[4]:


data.head()


# In[5]:


data['Date'] = pd.to_datetime(data['Date'], format='%B %d, %Y')


# In[6]:


data.head()


# In[10]:


date_filter = (data['Date'] >= '2019-01-01')
filted_data = data.loc[date_filter, :]


# In[11]:


gk = filted_data.groupby(['Account Number'])['Billed Usage'].mean()


# In[12]:


gk.head()


# In[ ]:





# In[ ]:




