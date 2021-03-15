#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
df = pd.read_csv('annual-buisness-csv.csv')
df.head(50)
df['year']


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.plot.scatter(x='hp',y='mpg')


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.plot.scatter(x='hp',y='mpg')


# In[5]:


import pandas as pd
df = pd.read_csv('annual-buisness-csv.csv')
df.head(50)
x = df[['year']]

print(x)


# In[ ]:





# In[24]:


import pandas as pd
df = pd.read_csv('annual-buisness-csv.csv')
df.head()
#df.loc[4,'Variable_name']


# In[21]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan'],'Age':[21,17,23]})
df.head()
#df.loc[2,'Age'] # data collect from data frame


# In[27]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan'],'Age':[21,17,23]})
#df.head()
df.loc[2,'Age'] # data collect from data frame


# In[26]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan'],'Age':[21,17,23]})
df.iloc[1,2]


# In[31]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan'],'Age':[21,17,23]})
df.head()
df.iloc[1,0]


# In[39]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan'],'Age':[21,17,23]})
df.head()
df.loc[0:2,'Name':'Age']


# In[5]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan','Halima','Punnota','Rakib','Nayeem','Sayed'],'Age':[21,17,23,31,35,15,45,26]})
df.head()
df.iloc[0:3,0:2]

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot.scatter(x='Name',y='Age')


# In[9]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan','Halima','Punnota','Rakib','Nayeem','Sayed'],'Age':[21,17,23,31,35,15,45,26]})
df.head()
df.iloc[0:9,0:2]


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.plot.scatter(x='Name',y='Age')


# In[12]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan','Halima','Punnota','Rakib','Nayeem','Sayed'],'Age':[21,17,23,35,35,15,45,45]})
df.head()
df['Age'].unique()# just unique number nibe


# In[33]:


import pandas as pd

df=pd.DataFrame({'Name':['ayon','omee','rehan','Halima','Punnota','Rakib','Nayeem','Sayed'],'Age':[21,17,23,35,35,15,45,45]})
df.head()
df1 = df[df['Age']>=23]
df1


# In[25]:


df1.to_csv('New-data.csv')


# In[32]:


import pandas as pd
df = pd.read_csv('New-data.csv')
df.head()
df.loc[3,'Age']


# In[34]:


import pandas as pd
df = pd.read_csv('New-data.csv')
df.head()
df.loc[3,'Name']


# In[37]:


import pandas as pd
df = pd.read_csv('New-data.csv')
df.head()
df.iloc[3,1]


# In[38]:


import pandas as pd
df = pd.read_csv('New-data.csv')
df['Age']==35


# In[39]:


import pandas as pd
df = pd.read_csv('New-data.csv')
df2 = df[df['Age']==35]
df2


# In[40]:


df2.to_excel('New-data2.xlsx')


# In[11]:


import pandas as pd
df = pd.DataFrame({'Temp(c)':[25,27,35,45,10],'Sell($)':[20,25,30,35,5]})
df.head()


# In[ ]:





# In[15]:


import pandas as pd
df = pd.DataFrame({'Temp(c)':[25,27,35,45,10],'Sell($)':[20,25,30,35,5]})
df.head()
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot.scatter(x='Temp(c)',y='Sell($)')


# In[16]:


import pandas as pd
df = pd.DataFrame({'Temp(c)':[25,27,35,45,10],'Sell($)':[20,25,30,35,5]})
df.head()


# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.plot.scatter(x='Temp(c)',y= 'Sell($)')


# In[23]:


import pandas as pd
calories = {'DAY1':300,'DAY2':500,'DAY3':100,'DAY4':200,'DAY5':600}
c  = pd.Series(calories)
c.index['DAY2']
print(c)


# In[24]:


import pandas as pd
calories = {'DAY1':300,'DAY2':500,'DAY3':100,'DAY4':200,'DAY5':600}
c  = pd.Series(calories)
c(calories,index=['DAY2'])
print(c)


# In[26]:


import pandas as pd
calories = {'DAY1':300,'DAY2':500,'DAY3':100,'DAY4':200,'DAY5':600}
c  = pd.Series(calories)
print(c)


# In[29]:


df = pd.Series(calories,index=['DAY2'])
print(df)


# In[37]:


import pandas as pd
df = pd.read_csv('New-data.csv')
print(df.to_string())# full data frame show kore


# In[38]:


import pandas as pd
df = pd.read_csv('New-data.csv')
df.head()# First 5 ta show kore


# In[40]:


import pandas as pd
df = pd.read_csv('annual-buisness-csv.csv')
print(df)# FiRST 5 ta & last 5 ta show kore


# In[46]:


import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60,
    "6":60,
    "7":45,
    "8":30,
    "9":60,
    "10":60,
    "11":60,
    "12":60,
    "13":60,
    "14":60,
    "15":60,
    "16":60,
    "17":45,
    "18":60,
    "19":45,
    "20":60,
    "21":45,
    "22":60,
    "23":45,
    "24":60,
    "25":60,
    "26":60,
    "27":60,
    "28":60,
    "29":60,
    "30":60,
    "31":45,
    "32":60,
    "33":60,
    "34":60,
    "35":60,
    "36":60,
    "37":60,
    "38":60,
    "39":45,
    "40":45,
    "41":60,
    "42":60,
    "43":60,
    "44":60,
    "45":60,
    "46":60,
    "47":45,
    "48":45,
    "49":60,
    "50":60,
    "51":80,
    "52":60,
    "53":60,
    "54":30,
    "55":60,
    "56":60,
    "57":45,
    "58":20,
    "59":45,
    "60":210,
    "61":160,
    "62":160,
    "63":45,
    "64":20,
    "65":180,
    "66":150,
    "67":150,
    "68":20,
    "69":300,
    "70":150,
    "71":60,
    "72":90,
    "73":150,
    "74":45,
    "75":90,
    "76":45,
    "77":45,
    "78":120,
    "79":270,
    "80":30,
    "81":45,
    "82":30,
    "83":120,
    "84":45,
    "85":30,
    "86":45,
    "87":120,
    "88":45,
    "89":20,
    "90":180,
    "91":45,
    "92":30,
    "93":15,
    "94":20,
    "95":20,
    "96":30,
    "97":25,
    "98":30,
    "99":90,
    "100":20,
    "101":90,
    "102":90,
    "103":90,
    "104":30,
    "105":30,
    "106":180,
    "107":30,
    "108":90,
    "109":210,
    "110":60,
    "111":45,
    "112":15,
    "113":45,
    "114":60,
    "115":60,
    "116":60,
    "117":60,
    "118":60,
    "119":60,
    "120":30,
    "121":45,
    "122":60,
    "123":60,
    "124":60,
    "125":60,
    "126":60,
    "127":60,
    "128":90,
    "129":60,
    "130":60,
    "131":60,
    "132":60,
    "133":60,
    "134":60,
    "135":20,
    "136":45,
    "137":45,
    "138":45,
    "139":20,
    "140":60,
    "141":60,
    "142":45,
    "143":45,
    "144":60,
    "145":45,
    "146":60,
    "147":60,
    "148":30,
    "149":60,
    "150":60,
    "151":60,
    "152":60,
    "153":30,
    "154":60,
    "155":60,
    "156":60,
    "157":60,
    "158":60,
    "159":30,
    "160":30,
    "161":45,
    "162":45,
    "163":45,
    "164":60,
    "165":60,
    "166":60,
    "167":75,
    "168":75
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102,
    "6":110,
    "7":104,
    "8":109,
    "9":98,
    "10":103,
    "11":100,
    "12":106,
    "13":104,
    "14":98,
    "15":98,
    "16":100,
    "17":90,
    "18":103,
    "19":97,
    "20":108,
    "21":100,
    "22":130,
    "23":105,
    "24":102,
    "25":100,
    "26":92,
    "27":103,
    "28":100,
    "29":102,
    "30":92,
    "31":90,
    "32":101,
    "33":93,
    "34":107,
    "35":114,
    "36":102,
    "37":100,
    "38":100,
    "39":104,
    "40":90,
    "41":98,
    "42":100,
    "43":111,
    "44":111,
    "45":99,
    "46":109,
    "47":111,
    "48":108,
    "49":111,
    "50":107,
    "51":123,
    "52":106,
    "53":118,
    "54":136,
    "55":121,
    "56":118,
    "57":115,
    "58":153,
    "59":123,
    "60":108,
    "61":110,
    "62":109,
    "63":118,
    "64":110,
    "65":90,
    "66":105,
    "67":107,
    "68":106,
    "69":108,
    "70":97,
    "71":109,
    "72":100,
    "73":97,
    "74":114,
    "75":98,
    "76":105,
    "77":110,
    "78":100,
    "79":100,
    "80":159,
    "81":149,
    "82":103,
    "83":100,
    "84":100,
    "85":151,
    "86":102,
    "87":100,
    "88":129,
    "89":83,
    "90":101,
    "91":107,
    "92":90,
    "93":80,
    "94":150,
    "95":151,
    "96":95,
    "97":152,
    "98":109,
    "99":93,
    "100":95,
    "101":90,
    "102":90,
    "103":90,
    "104":92,
    "105":93,
    "106":90,
    "107":90,
    "108":90,
    "109":137,
    "110":102,
    "111":107,
    "112":124,
    "113":100,
    "114":108,
    "115":108,
    "116":116,
    "117":97,
    "118":105,
    "119":103,
    "120":112,
    "121":100,
    "122":119,
    "123":107,
    "124":111,
    "125":98,
    "126":97,
    "127":109,
    "128":99,
    "129":114,
    "130":104,
    "131":107,
    "132":103,
    "133":106,
    "134":103,
    "135":136,
    "136":117,
    "137":115,
    "138":113,
    "139":141,
    "140":108,
    "141":97,
    "142":100,
    "143":122,
    "144":136,
    "145":106,
    "146":107,
    "147":112,
    "148":103,
    "149":110,
    "150":106,
    "151":109,
    "152":109,
    "153":150,
    "154":105,
    "155":111,
    "156":97,
    "157":100,
    "158":114,
    "159":80,
    "160":85,
    "161":90,
    "162":95,
    "163":100,
    "164":105,
    "165":110,
    "166":115,
    "167":120,
    "168":125
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127,
    "6":136,
    "7":134,
    "8":133,
    "9":124,
    "10":147,
    "11":120,
    "12":128,
    "13":132,
    "14":123,
    "15":120,
    "16":120,
    "17":112,
    "18":123,
    "19":125,
    "20":131,
    "21":119,
    "22":101,
    "23":132,
    "24":126,
    "25":120,
    "26":118,
    "27":132,
    "28":132,
    "29":129,
    "30":115,
    "31":112,
    "32":124,
    "33":113,
    "34":136,
    "35":140,
    "36":127,
    "37":120,
    "38":120,
    "39":129,
    "40":112,
    "41":126,
    "42":122,
    "43":138,
    "44":131,
    "45":119,
    "46":153,
    "47":136,
    "48":129,
    "49":139,
    "50":136,
    "51":146,
    "52":130,
    "53":151,
    "54":175,
    "55":146,
    "56":121,
    "57":144,
    "58":172,
    "59":152,
    "60":160,
    "61":137,
    "62":135,
    "63":141,
    "64":130,
    "65":130,
    "66":135,
    "67":130,
    "68":136,
    "69":143,
    "70":129,
    "71":153,
    "72":127,
    "73":127,
    "74":146,
    "75":125,
    "76":134,
    "77":141,
    "78":130,
    "79":131,
    "80":182,
    "81":169,
    "82":139,
    "83":130,
    "84":120,
    "85":170,
    "86":136,
    "87":157,
    "88":103,
    "89":107,
    "90":127,
    "91":137,
    "92":107,
    "93":100,
    "94":171,
    "95":168,
    "96":128,
    "97":168,
    "98":131,
    "99":124,
    "100":112,
    "101":110,
    "102":100,
    "103":100,
    "104":108,
    "105":128,
    "106":120,
    "107":120,
    "108":120,
    "109":184,
    "110":124,
    "111":124,
    "112":139,
    "113":120,
    "114":131,
    "115":151,
    "116":141,
    "117":122,
    "118":125,
    "119":124,
    "120":137,
    "121":120,
    "122":169,
    "123":127,
    "124":151,
    "125":122,
    "126":124,
    "127":127,
    "128":125,
    "129":151,
    "130":134,
    "131":138,
    "132":133,
    "133":132,
    "134":136,
    "135":156,
    "136":143,
    "137":137,
    "138":138,
    "139":162,
    "140":135,
    "141":127,
    "142":120,
    "143":149,
    "144":170,
    "145":126,
    "146":136,
    "147":146,
    "148":127,
    "149":150,
    "150":134,
    "151":129,
    "152":138,
    "153":167,
    "154":128,
    "155":151,
    "156":131,
    "157":120,
    "158":150,
    "159":120,
    "160":120,
    "161":130,
    "162":130,
    "163":140,
    "164":140,
    "165":145,
    "166":145,
    "167":150,
    "168":150
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5,
    "6":374.0,
    "7":253.3,
    "8":195.1,
    "9":269.0,
    "10":329.3,
    "11":250.7,
    "12":345.3,
    "13":379.3,
    "14":275.0,
    "15":215.2,
    "16":300.0,
    
    "18":323.0,
    "19":243.0,
    "20":364.2,
    "21":282.0,
    "22":300.0,
    "23":246.0,
    "24":334.5,
    "25":250.0,
    "26":241.0,
    
    "28":280.0,
    "29":380.3,
    "30":243.0,
    "31":180.1,
    "32":299.0,
    "33":223.0,
    "34":361.0,
    "35":415.0,
    "36":300.5,
    "37":300.1,
    "38":300.0,
    "39":266.0,
    "40":180.1,
    "41":286.0,
    "42":329.4,
    "43":400.0,
    "44":397.0,
    "45":273.0,
    "46":387.6,
    "47":300.0,
    "48":298.0,
    "49":397.6,
    "50":380.2,
    "51":643.1,
    "52":263.0,
    "53":486.0,
    "54":238.0,
    "55":450.7,
    "56":413.0,
    "57":305.0,
    "58":226.4,
    "59":321.0,
    "60":1376.0,
    "61":1034.4,
    "62":853.0,
    "63":341.0,
    "64":131.4,
    "65":800.4,
    "66":873.4,
    "67":816.0,
    "68":110.4,
    "69":1500.2,
    "70":1115.0,
    "71":387.6,
    "72":700.0,
    "73":953.2,
    "74":304.0,
    "75":563.2,
    "76":251.0,
    "77":300.0,
    "78":500.4,
    "79":1729.0,
    "80":319.2,
    "81":344.0,
    "82":151.1,
    "83":500.0,
    "84":225.3,
    "85":300.1,
    "86":234.0,
    "87":1000.1,
    "88":242.0,
    "89":50.3,
    "90":600.1,
    "91":201,
    "92":105.3,
    "93":50.5,
    "94":127.4,
    "95":229.4,
    "96":128.2,
    "97":244.2,
    "98":188.2,
    "99":604.1,
    "100":77.7,
    "101":500.0,
    "102":500.0,
    "103":500.4,
    "104":92.7,
    "105":124.0,
    "106":800.3,
    "107":86.2,
    "108":500.3,
    "109":1860.4,
    "110":325.2,
    "111":275.0,
    "112":124.2,
    "113":225.3,
    "114":367.6,
    "115":351.7,
    "116":443.0,
    "117":277.4,
    "119":332.7,
    "120":193.9,
    "121":100.7,
    "122":336.7,
    "123":344.9,
    "124":368.5,
    "125":271.0,
    "126":275.3,
    "127":382.0,
    "128":466.4,
    "129":384.0,
    "130":342.5,
    "131":357.5,
    "132":335.0,
    "133":327.5,
    "134":339.0,
    "135":189.0,
    "136":317.7,
    "137":318.0,
    "138":308.0,
    "139":222.4,
    "140":390.0,
 
    "142":250.4,
    "143":335.4,
    "144":470.2,
    "145":270.8,
    "146":400.0,
    "147":361.9,
    "148":185.0,
    "149":409.4,
    "150":343.0,
    "151":353.2,
    "152":374.0,
    "153":275.8,
    "154":328.0,
    "155":368.5,
    "156":270.4,
    "157":270.4,
    "158":382.8,
    "159":240.9,
    "160":250.4,
    "161":260.4,
    "162":270.0,
    "163":280.9,
    "164":290.8,
    "165":300.4,
    "166":310.2,
    "167":320.4,
    "168":330.4
  }
}
df = pd.DataFrame(data)
print(df.info())


# In[47]:


print(df.head())#if the number of rows is not specified, the head() method will return the top 5 rows.


# In[51]:


print(df.tail())#if the number of rows is not specified, the tail() method will return the last 5 rows.From the bottom.


# In[49]:


print(df)


# In[56]:


print(df.to_string())


# In[57]:


df.corr()


# In[60]:


df["Duration"].plot(kind = 'hist')


# In[ ]:





# In[69]:


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('New-data.csv')
df.plot.hist()


# In[70]:


print(df.to_string())


# In[35]:


import pandas as pd
df = pd.read_csv('dirtydata (1).csv')
print(df.to_string()) # Return full Data Frame with empty/null cells


# In[37]:


import pandas as pd
df = pd.read_csv('dirtydata (1).csv')
new_df = df.dropna() # Return a new Data Frame with no empty cells....By default the dropna() method returns a new DataFrame, and will not change the original.
print(new_df)


# In[24]:


import pandas as pd
df = pd.read_csv('dirtydata (1).csv')
df.dropna(inplace=True)
print(df.to_string())# Now the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.

df.to_csv('new_csv_without_null.csv')



# In[38]:


import pandas as pd
df = pd.read_csv('dirtydata (1).csv')
df.fillna(130,inplace= True) # Replace NULL values with the number 130
print(df.to_string())


# In[33]:


#The example above replaces all empty cells in the whole Data Frame.
#To only replace empty values for one column, specify the column name for the DataFrame.


import pandas as pd
df = pd.read_csv('dirtydata (1).csv')
df['Date'].fillna('2020/12/22',inplace= True)# Replace NULL values for Date column.
df['Calories'].fillna(350.5,inplace= True)#Replace NULL values for Calories column.

print(df.to_string())


# In[39]:


import pandas as pd
df = pd.read_csv('dirtydata (1).csv')

x = df['Calories'].mean() # same median().
df['Calories'].fillna(x,inplace=True)

y = df['Date'].mode()[0]
df['Date'].fillna(y,inplace=True)

print(df.to_string())


# In[45]:


import pandas as pd

df = pd.read_csv('dirtydata (1).csv')

df['Date']= pd.to_datetime(df['Date'])

print(df.to_string())


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
from sklearn.linear_model import LinearRegression

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.style

plt.style.use('classic')

import seaborn as sns

mpg_df = pd.read_csv("car-mpg.csv")
mpg_df.head(50)


# In[10]:


mpg_df = mpg_df.drop('car_name',axis=1)


# In[9]:


mpg_df


# In[11]:


mpg_df['origin'] = mpg_df['origin'].replace({1:'america',2:'europe',3:'asia'})


# In[12]:


mpg_df


# In[13]:


mpg_df = pd.get_dummies(mpg_df, columns=['origin'])


# In[14]:


mpg_df


# In[15]:


mpg_df.describe()


# In[16]:


mpg_df.describe().transpose()


# In[17]:


temp = pd.DataFrame(mpg_df.hp.str.isdigit())
temp[temp['hp'] == False ]


# In[18]:


mpg_df = mpg_df.replace('?',np.nan)


# In[20]:


mpg_df[mpg_df.isnull().any(axis=1)]


# In[ ]:





# In[ ]:





# In[9]:


import numpy as np

print(np.cos(np.pi))
print(np.sqrt(4))
print(np.log(2))
print(np.log(np.exp(5)))


# In[15]:


a = np.array([1,5,9])
print(a)
mat= np.array([[1,5,9],[5,9,7],[10,23,5]])
print(mat)
print(mat.T)


# In[26]:


b = np.arange(1,10+1)

print(b)
print(b.reshape(5,2))


# In[28]:


v = np.random.randn(15)
print(v)
print(v[-1])


# In[29]:


print(v[np.arange(0,3)])


# In[34]:


sub_mat2=v[0:2,0:3].copy()

print(sub_mat2)
print(v)


# In[ ]:




