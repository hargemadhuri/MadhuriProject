#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


import requests


# In[3]:


pip install bs4


# In[4]:


from bs4 import BeautifulSoup


# In[8]:


import pandas as pd


# In[5]:


url="https://www.flipkart.com/search?q=5g+smart+phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
r=requests.get(url)


# In[6]:


r


# In[9]:


soup=BeautifulSoup(r.content,"html.parser")


# In[10]:


soup


# In[12]:


Name=[]
Rating=[]
Price=[]
Discount=[]
Description=[]
for i in range(1,49):# this code only works till page 49 after that it showes an error as NoneType object has no attribute "find"
    url="https://www.flipkart.com/search?q=mobile+phone+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+phone+5g%7CMobiles&requestId=9fc04ba5-8a69-4780-88c6-565feaeb2a44&as-searchtext=mobile+&page="+str(1)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div", class_="_1YokD2 _3Mn1Gg")
    names=box.find_all("div", class_="_4rR01T")
# print(names)
    for i in names:
        name=i.text
        Name.append(name)
#     print(Name)
#     print(len(Name))
    names=box.find_all("div", class_="_3LWZlK")
    # print(names)
    for i in names:
        name=i.text
        Rating.append(name)
#     print(Rating)
#     print(len(Rating))
    names=box.find_all("div", class_="_30jeq3 _1_WHN1")
    # print(names)
    for i in names:
        name=i.text
        Price.append(name)
#     print(Price)
#     print(len(Price))
    names=box.find_all("div", class_="_3Ay6Sb")
    # print(names)
    for i in names:
        name=i.text
        Discount.append(name)
# #     print(Discount)
# #     print(len(Discount))
    names=box.find_all("div", class_="col col-7-12")
#     print(names)
    for i in names:
        name=i.text
        Description.append(name)
#     print(Description)
#     print(len(Description))
df=pd.DataFrame({"Product_name":Name,"Reviews":Rating,"Prices":Price,"Discount":Discount,"Description":Description})
print(df)
    

#     print(soup)


# In[13]:


df=pd.read_csv("C:/Users/Mayur/Documents/Anaconda/Python Projects/Flipkar_5G_mobiles_Data1.csv")
df


# **Import and Reading Data**

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use("ggplot")


# In[15]:


df=pd.read_csv("C:/Users/Mayur/Documents/Anaconda/Python Projects/Flipkar_5G_mobiles_Data1.csv")
df


# **Step 1: Data Understanding**
# 
# 

# In[16]:


df.shape #This method shows number of row and column respectively 1152 rows and 6 columns


# In[17]:


df.head() # head will show us first few rows


# In[18]:


df.columns # will return you the list of columns present


# In[19]:


df.dtypes # datatype of each column


# In[20]:


df.drop(["Unnamed: 0"],axis=1,inplace=True) # here axis 1 represent column and inplace is to remove then and there


# In[21]:


df


# In[27]:


# rename column
df=df.rename(columns={"Prices":"Prices_Rupees","Discount":"Discount_%"})


# In[22]:


df


# In[23]:


# this command is use to see missing value
#there is no missing value
df.isna().sum()


# In[24]:


df.loc[df.duplicated()]


# In[25]:


df.query("Product_name=='APPLE iPhone 14 (Purple, 128 GB)'")


# In[28]:


df['Prices_Rupees'] = df['Prices_Rupees'].str.split('₹').str[1].str.replace(',', '').astype(int)
# herewe first use the str.split() method to split the 'Prices_Rupees' column based on the '₹' string. 
# This returns a pandas Series of lists, with each list containing the two parts of the string before and after the "₹" string.
# Next, we use the .str[1] to get the second part of each list, which is the numerical value but have comma inbetween after the rupee sign.
# so now we usethe str.replace() method to remove commas from the 'Prices_Rupees' column after splitting the string based on
# '₹'. This ensures that the resulting strings only contain numerical characters that can be converted to integers
# Finally, we use the astype() method to convert this numerical string to an integer datatype.
df


# In[29]:


#converted string to int
df['Discount_%'] = df['Discount_%'].str.split('% off').str[0].astype(int) 
df


# In[30]:


df.dtypes 


# In[31]:


unique_df = df.nunique()
print(unique_df)


# In[32]:


df.describe()


# In[33]:


df.info()


# **DATA VISUALIZATION**

# In[34]:


import seaborn as sns


# In[35]:


sns.countplot(x='Discount_%', data=df) #from this countplot we can conclude that maximum 17% of discount is given


# In[36]:


sns.countplot(x='Product_name', data=df)
plt.xticks(rotation=90)


# In[37]:


sns.countplot(x='Prices_Rupees', data=df)
plt.xticks(rotation=70) # this command is for the label of bar


# In[38]:


# plt.figure(figsize=(6,6))
sns.boxplot(x="Product_name", y="Reviews",data=df)
plt.xticks(rotation=90)


# In[39]:


df.loc[~df.duplicated(subset=["Product_name","Prices_Rupees","Description"])]


# In[40]:


print(df.Product_name.unique())


# In[46]:


import matplotlib.pyplot as plt


# In[55]:


plt.figure(figsize=(8,7))
sns.countplot(x='Reviews',data=df,hue = 'Prices_Rupees')
plt.legend(loc="upper right")
plt.show()

