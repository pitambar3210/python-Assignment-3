#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1st problem
# write a python program to implement your owm myreduce()function which works exactly like python's built in function reduce()


# In[2]:


def myreduce(fun,val):
    result = val[0]
    for i in range(1,len(val)):
        result = fun(result,val[i])
    return result


# In[3]:


def fun(a,b):
    return a*b


# In[6]:


myreduce(fun,[1,2,3,4,5,6])


# In[7]:


# second problem
#write a python program to implement your own myfilter() function which works exactly like python's built-in- filter


# In[11]:


def myfilter(func,val):
    result=[]
    for i in range(len(val)):
        if func(val[i]):
            result.append(val[i])
    return result
            


# In[12]:


def func(x):
    return x%2 != 0


# In[13]:


myfilter(func,[1,2,3,4,5])


# In[14]:


# third problem
# using list comprehensions


# In[19]:


list1 = [i*j for i in ['x','y','z'] for j in range(1,5)]


# In[20]:


list2 = [j*i  for j in range(1,5) for i in ['x','y','z']]


# In[24]:


list3 =[[i+j] for i in  [2,3,4]for j in [0,1,2]]
list3


# In[25]:


list4 = [[i+j  for i in [2,3,4,5]] for j in [0,1,2,3]]


# In[27]:


list5 = [(j,i) for i in [1,2,3] for j in [1,2,3]]


# In[ ]:




