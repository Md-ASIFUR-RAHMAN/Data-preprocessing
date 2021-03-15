#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv('car-mpg.csv')
df


# In[5]:


df.head(5)


# In[6]:


df.tail(5)


# In[11]:


df['car_name']
df1 = df.drop(['car_name'],axis =1)
df1


# In[12]:


df1.describe()


# In[13]:


df1.info()


# In[15]:


df1[['mpg','cyl']]


# In[31]:



df1


# In[43]:


df1.loc[[5,6]]


# In[56]:


df1.iloc[[0,3],[2,3]]


# In[61]:


df1.loc[(df1.mpg>20.00)]


# In[48]:


df1.loc[(df1.mpg>20.00 )& ('car_type'==1)]


# In[51]:


df1.loc[(df1.mpg>20.00 ) & (df1.car_type==1)]


# In[59]:


df1.loc[(df1.yr>70),['mpg','hp']]


# In[64]:


# we can assign new names to the index


df5= df.head(4)
df5['new name'] = ['This','is','the','row']
df5


# In[67]:


data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 
  
# Declare a list that is to be converted into a column 
address = [] 
for i in range(4):
    n = input()
    address.append(n)
  
# Using 'Address' as the column name 
# and equating it to the list 
df['Address'] = address 
  
# Observe the result 
df


# In[72]:


df.Height.min()


# In[73]:


df.Height.max()


# In[74]:


df.Height.mean()


# In[75]:


df.Height.mode()


# In[76]:


df.Height.median()


# In[92]:


import random
height2 = []
for i in range(4):
    n = df.Height.median()
    height2.append(n)
print(height2 )

df['H'] = height2 
df

    


# In[87]:


df.Height.sum()


# In[91]:


df.corr()


# In[101]:


df.insert(2, "Age",height2 , True)
df


# In[97]:


df6 = pd.read_csv('dirtydata (1).csv')
df6


# In[110]:


df7 = df['H']


# In[109]:


df6.insert(2,'asedfgdfg',df7,True)
df6


# In[111]:


df6.insert(2,'asedfgdfg',df7,True)
df6


# In[112]:


df8 = df6.dropna()
df8


# In[118]:


x = df6['Pulse'].mode() 
df6.fillna(x,inplace=True)
df6


# In[122]:



df6.fillna(12,inplace=True)
df6


# In[125]:


df9 = pd.read_csv('dirtydata (1).csv')
x = df9['Duration'].mode()
df9['Duration'].fillna(x,inplace=True)
df9


# In[138]:


df9.loc[(df9.Duration>40),['Duration','Pulse']]=100
df9


# In[2]:


import pandas as pd

d='2015-01-08 22:44:09' 
date=pd.to_datetime(d).date()
print(date)


# In[ ]:




