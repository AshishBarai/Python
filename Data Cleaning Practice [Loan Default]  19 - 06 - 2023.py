#!/usr/bin/env python
# coding: utf-8

# ## Loan Default

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv(r"A:\Loan Default Practice\Loan_Default.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# ## Missing Value Treatment

# In[5]:


df.isnull().sum() ##count of how many null/missing values are present in each column


# In[6]:


df.isnull().sum()*100/len(df)


# In[7]:


def check_missing(x):
    x = x.isnull().sum()*100/len(x)
    x = x[x > 0]
    x = x.sort_values(ascending = False)
    return x

check_missing (df)


# In[8]:


df.Upfront_charges[:10]


# In[34]:


sns.distplot(df['Upfront_charges'])


# In[10]:


df['Upfront_charges'].median()


# In[11]:


df.Upfront_charges = df.Upfront_charges.fillna(2596.45)


# In[12]:


sns.distplot(df['Upfront_charges'])


# In[13]:


check_missing(df)


# In[14]:


df.Interest_rate_spread


# In[15]:


sns.displot(df.Interest_rate_spread)


# In[16]:


df.Interest_rate_spread.mean()


# In[19]:


df.Interest_rate_spread.median()


# In[20]:


df.Interest_rate_spread = df.Interest_rate_spread.fillna(df.Interest_rate_spread.mean())


# In[21]:


check_missing(df)


# In[22]:


sns.boxplot(df.rate_of_interest)


# In[23]:


df.rate_of_interest = df.rate_of_interest.fillna(df.rate_of_interest.mean())


# In[30]:


check_missing(df)


# In[26]:


sns.distplot(df.income)


# In[27]:


df.income = df.income.fillna(df.income.median())


# In[29]:


sns.distplot(df.income)


# In[31]:


check_missing(df)


# In[32]:


df.dtir1 = np.where(df.dtir1.isnull(),df['loan_amount']/df['income'],df.dtir1)
## replaced non values with calculated dtir ratio based on loan_amount and income


# In[33]:


check_missing(df)


# In[35]:


df.Secured_by.unique()


# In[37]:


df[df.property_value.isnull()]['Secured_by'].unique()


# In[44]:


prop_value_dict = dict(df.groupby('Region').property_value.median())


# In[45]:


prop_value


# In[46]:


df.property_value = df.apply(lambda x : prop_value_dict[x.Region] if np.isnan(x.property_value) else x.property_value, axis=1)


# In[47]:


check_missing(df)


# In[48]:


df.LTV = np.where(df.LTV.isnull(),df.loan_amount*100/df.property_value,df.LTV)
## loan-to-value(LTV) is ratio is an assessment of leanding risk


# In[49]:


check_missing(df)


# In[52]:


df.loan_limit.unique()


# In[53]:


df.loan_limit.mode()


# In[54]:


pd.pivot_table(df,index = 'loan_limit',columns = 'loan_type',aggfunc = 'count',values = 'ID')


# In[55]:


df.loan_limit = df.loan_limit.fillna('cf')


# In[56]:


check_missing(df)


# In[60]:


df.approv_in_adv


# In[61]:


df.approv_in_adv.mode()


# In[63]:


df.approv_in_adv = df.approv_in_adv.fillna('nopre')


# In[64]:


check_missing(df)


# In[66]:


df.age.mode()


# In[69]:


df.age = df.age.fillna('45-54')


# In[70]:


check_missing(df)


# In[71]:


df.submission_of_application.mode()


# In[72]:


df.submission_of_application = df.submission_of_application.fillna('to_inst')


# In[74]:


check_missing(df)


# In[76]:


df.loan_purpose.mode()


# In[77]:


df.loan_purpose = df.loan_purpose.fillna('p3')


# In[83]:


100 - len(df.dropna())*100/len(df)


# In[84]:


df = df.dropna()


# In[85]:


check_missing(df)


# In[87]:


df.head()


# In[ ]:




