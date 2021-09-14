#!/usr/bin/env python
# coding: utf-8

# ## Lecture 2

# In[ ]:


#PYTHON
USES:-
    Web development(flask,django)
    Automation
    Scripting
    Machine Learning(sklearn)
    AI
    Data Engineering
    Data Analysis(pandas,numpy,matplotlib)


# In[ ]:


Python-1989-1991
inventor-Guido van Rossum
open source language
Python 3.9.0


# In[ ]:





# In[ ]:


#Operator->symbols in python that perform any operation
1.Arithematic Operator
2.Relational Operator
3.Logical Operator
4.Bitwise Operator
5.Assignment Operator
6.Special Operators


# In[ ]:


a=5
b=3
c=a+b
print(c)


# In[ ]:


##Arithematic Operator
Addition Operator-> +
Substarction Operator-> -
Multiplication -> *
Division -> /
Modulous Operator -> %
Floor Division Opearot -> //
Exponent Opearator -> ** 


# In[ ]:


#Addition Operator-> +
a=5
b=3
c=a+b
print(c)


# In[ ]:


a="pavan"
b="adnan"
c=a+b
print(c)


# In[ ]:


#Substarction Operator-> -
a=5
b=3
c=a-b
print(c)


# In[ ]:


a="pavan"
b="adnan"
c=a-b
print(c)


# In[ ]:


#Multiplication -> *
a=5
b=3
c=a*b
print(c)


# In[ ]:


a="pavan"
b="adnan"
c=a*b
print(c)


# In[ ]:


#Division -> /
a=5
b=3
c=a/b
print(c)


# In[ ]:


#Modulous Operator -> %
a=5
b=3
c=a%b
print(c)


# In[ ]:


#Floor Division Opearotor -> //
a=5
b=3
c=a//b
print(c)


# In[ ]:


a=5
b=2
c=a//b
print(c)


# In[ ]:


#Exponent Opearator -> ** 
a=5
b=2
c=a**b
print(c)


# In[ ]:


#Relational Operator
>,<,=,>=,<=


# In[ ]:


a=1
b=2
print(a>b)


# In[ ]:


a=1
b=2
print(a<b)


# In[ ]:


a=1
b=2
print(a=b)


# In[ ]:


a="arun"
b="gautam"
print(a<b)


# In[ ]:


#3.Logical Operator
and-->if both the arguments are true only then result will be true
or-->if at least one argument is true only then result will be true
not->complement


# In[ ]:


True and True


# In[ ]:


True or True


# In[ ]:


True or False


# In[ ]:


False or False


# In[ ]:


not


# In[ ]:


#Assignment Operator
a=5
b=3
c=a+b
print(c)


# In[ ]:


a=5
b=3
a += b 
print(a)


# In[ ]:


a=5
b=3
a=a+b 
print(a)


# In[ ]:


x=5
x*=10
print(x)


# ## Ternary Operator

# In[ ]:


x=firstValue if condition else secondValue #Ternary Operator 


# In[ ]:


a=5
b=10
print(a)
print(b)


# In[ ]:


a,b=5,10
a,b=b,a
print(a)
print(b)


# In[ ]:


a,b=20,10
x=30 if a<b else 40 # Ternary operator
print(x)


# In[ ]:


a,b=20,10
if a<b:
    print(30)
else:
    print(40)


# In[23]:


#Program to find minimum of 3 numbers
a=int(input("enter first number"))


# In[24]:


print(a)


# In[25]:


print(type(a))


# In[31]:


a=int(input("enter first number"))
b=int(input("enter second number"))


# In[32]:


c=a+b
print(c)


# In[33]:


a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
min=a if a<b and a<c else b if b<c else c
print("minimum value:",min)


# ## SPECIAL OPERATOR

# In[ ]:


1.IDENTITY OPERATORS
2.MEBERSHIP OPERATOR


# In[ ]:


1.IDENTITY OPERATORS
a)is--> is opeartor is used for address comparision and "==" compares values
b)is not


# In[37]:


a=10
b=10
c=10
print(a is b is c)


# In[35]:


x=True
y=True
print(x is y)


# In[39]:


a=10
b=10
print(id(a))
print(id(b))
print(a is not b)


# In[ ]:


2.MEBERSHIP OPERATOR
a)in
b)not in


# In[43]:


#in

x="my name is arun"
print('n' in x)
print('z' in x)
print('n'not in x)


# In[ ]:




