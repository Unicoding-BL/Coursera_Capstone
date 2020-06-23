#!/usr/bin/env python
# coding: utf-8

# ### Get data from Wikipedia

# In[114]:


from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
origin = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(origin, 'lxml')


# ### Creat a table

# In[124]:


table = soup.find('table', class_ = "wikitable sortable")
df = pd.read_html(str(table))[0]
column_name = ['Postal Code','Borough','Neighborhood']
list = df.drop([0])
list.columns = column_name
list


# ### Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned.

# In[116]:


list1 = list[-list.Borough.isin(['Not assigned'])]
list1


# ### If a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough.

# In[125]:


list1['Neighborhood'][list1['Neighborhood'] == 'Not assigned'] = list1['Borough']
list1


# ### Shape of the table

# In[123]:


list1.shape

