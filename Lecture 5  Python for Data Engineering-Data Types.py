#!/usr/bin/env python
# coding: utf-8

# ## Slicing of Strings

# In[6]:


s="arunkumar"
#0 1 2 3 4 5
#-1-2-3-4-5


# In[7]:


s[20]


# In[9]:


s[0:4]


# In[10]:


s[0:3]


# In[11]:


s[4:7]


# In[12]:


a="arun"
a*4


# In[76]:


"arun"+"arun"


# In[13]:


a="nandini"
len(a)


# In[16]:


a="my name is pradeep"
len(a)


# ## Type Casting

# In[ ]:


int -> str
str -> int
float -> int
int ->float


# In[17]:


a=45.67
print(type(a))


# In[19]:


b=int(45.67)
print(type(b))


# In[20]:


int(True)


# In[21]:


int(False)


# In[22]:


a=10
print(type(a))


# In[25]:


a="10"
b=int(a)
print(type(b))
print(b)


# In[26]:


a="arun"
b=int(a)


# In[27]:


a=10
float(a)


# In[28]:


float(True)


# In[29]:


float(False)


# In[30]:


int(True)


# In[31]:


#bool data type
bool(0)


# In[32]:


bool(1)


# In[33]:


bool(5)


# In[34]:


bool("")


# In[35]:


bool(0.0)


# In[36]:


bool(0.1)


# In[39]:


l=["tb1","tb2","tb3"]
for i in l:
    print(i)
    


# ## list data type

# In[43]:


l1=[2,4,6,-4]
print(l1)
print(type(l1))


# In[54]:


#list data type is heterogenous data type
l1=[2,4,6,-4,"ashish","sonu",3,7,8]
print(l1)
print(type(l1))


# In[48]:


l1[0]


# In[49]:


l1[1]


# In[50]:


l1[-1]


# In[52]:


l1[1:4]


# In[53]:


l1[::-1]


# In[55]:


l1[1:7:2]


# In[56]:


len(l1)


# In[ ]:


l1=[2,4,6,-4,"ashish","sonu",3,7,8]


# In[57]:


l1=[2,4,6,-4,"ashish","sonu",3,7,8]
l1[1]


# In[58]:


l1[1]=-6


# In[59]:


l1


# In[ ]:


#list is mutable


# In[60]:


l1=[2,4,6,-4,"ashish","sonu",3,7,8]
l1.append(19)


# In[61]:


l1


# In[63]:


l1.append(7)


# In[64]:


l1


# In[65]:


l1.remove(7)


# In[66]:


l1


# In[67]:


l1.remove(6)


# In[68]:


l1


# In[ ]:


#List is mutable,heterogenous colection of elements in which the insertion order is preserved.
#duplicate elemets are allowed in list. 


# In[ ]:


## Tuple data type
#Q.What is difference between list and tuple?


# In[70]:


t1=(3,5,3,4)
print(type(t1))


# In[ ]:


#Tuple is immutable


# In[71]:


t1.append("sonu")


# In[72]:


t1.remove(3)


# In[74]:


t1=(3,5,3,4,"arun")
print(type(t1))


# In[ ]:




