#!/usr/bin/env python
# coding: utf-8

# # Identifiers

# In[2]:


#A name(variable name,class name,function name,module name) in python is identifier.


# In[13]:


a=5
print(a)


# In[ ]:


#Rules to define identifiers:-
    alphabet symbols(lower case or upper case)
    digits(0 to 9)
    underscore symbol(_)
    
    Identifiers should not start with digits.
    
    Identifiers are case sensitive(Python is case sensitive)
    
    Reserverd keywords cannot be identifiers.
    


# In[18]:


arun_6=7
print(arun_6)


# In[15]:


ar$un=5
print(ar$un)


# In[19]:


78arun=9
print(78arun)


# In[20]:


arun78=9
print(arun78)


# In[22]:


arun=7
ARUN=9
print(ARUN)


# ##Reserved Keywords
# There are 33 reserved keywords in python.
# 
# True,False,None->only these 3 keywords have capital letter.
# and,or,not,is
# if,elif,else
# while,for,break,continue,return,in,yield
# try,except,finally,raise,assert
# import,from,as,class,def,pass,global,nonlocal,lamda,del,with
# 

# In[25]:


return=4
print(return)


# # Data Types

# In[ ]:


#based on the vlaues provided,teh data type is automatically assigned to the variables.Hence,python is Dynamically Typed Language.


# In[26]:


a=5
print(type(a))


# In[28]:


a="rahul"
print(type(a))


# In[29]:


a='rahul'
print(type(a))


# In[ ]:


#Python has following inbuild data types:-
   1.int
    


# In[37]:


#int data type->to represent whole numbers(integer values)
a=10
print(a)
print(type(a))
   
   


# In[33]:


#float data type->to represent decimal values
a=2.456
print(a)
print(type(a))


# In[38]:


#Complex data type
a=2+6j
print(a)
print(type(a))


# In[43]:


#bool data type->to represent boolena values
#True->1 oR False->0

a=True
print(type(a))


# In[46]:


a=False
print(type(a))


# In[48]:


a=10
b=20
c=a<b
print(c)
print(type(c))


# In[50]:


#string data type->represented by str->written either in single quotes or double quotes
a="rahul"
print(a)
print(type(a))


# In[51]:


a='rahul'
print(a)
print(type(a))


# In[57]:


a="""rahul 
is a
good
coder"""
print(a)
print(type(a))


# In[58]:


a='''rahul 
is a
good
coder'''
print(a)
print(type(a))


# In[ ]:


to comment or uncomment multiple lines simutaneoulsy->ctrl+question mark
# adnaan is a good boy
# pradee is excellent person


# In[ ]:


#Slicing of Strings

