#!/usr/bin/env python
# coding: utf-8

# # Numpy Example 1
# 
# 
# 

# In[1]:


import numpy 
i=numpy.array([10,20,30,40,50])
print(i)


# # Alternative Names (ALIAS)
# 

# In[2]:


import numpy as np
i=np.array([10,20,30,40,50])
print(i)


# 
# # Check Numpy Version

# In[3]:


import numpy as np
print(np.__version__)


# # Type() Function (NDARRAY)

# In[4]:


import numpy as np
i=np.array([1,2,3,4,5])
print(i)
print(type(i))


# # Example With Tuple

# In[5]:


import numpy as np
i=np.array((1,2,3,4,5))
print(i)


# # Dimensions of Array in Numpy
# 

# 0D Array

# In[6]:


import numpy as np
i=np.array(10)
print(i)


# 1 D Array

# In[7]:


import numpy as  np
i=np.array([10,20,30,40,50])
print(i)


# 2D Array

# In[8]:


import numpy as np
i=np.array([
    [10,20,30,50],
    [60,70,80,90]
])
print(i)


# 3D Array

# In[9]:


import numpy as np
i=np.array([
    [[10,20,30,40,50],[60,70,80,90,100]],
    [[110,120,130,140,150],[160,170,180,190,200]],
    [[10,20,30,40,50],[60,70,80,90,100]]
])
print(i)


# # Ndim Atrribute

# In[10]:


import numpy as np
i=np.array(10)
j=np.array([10,20,30])
k=np.array([
    [10,20,30,40,50],
    [60,70,80,90,100]
])
l=np.array([
    [[10,20,30,40,50],[60,70,80,90,100]],
    [[110,120,130,140,150],[160,170,180,190,200]]
])
print(i)
print(i.ndim)
print()
print(j)
print(j.ndim)
print()
print(k)
print(k.ndim)
print()
print(l)
print(l.ndim)


# # Ndmin Argument

# In[11]:


import numpy as np
i=np.array([10,20,30,40],ndmin=5)
print(i)
print(i.ndim)


# # Access Element

# In[12]:


import numpy as np


# In[13]:


i=np.array([10,20,30,40,50])
print(i[1])


# In[14]:


i=np.array([
    [10,20,30,40,50],
    [60,70,80,90,100]
])
print(i[0,2])


# In[15]:


print(i[1,4])


# In[16]:


i= np.array([  
    [[10, 20, 30], [40, 50, 60]],  
    [[70, 80, 90], [100, 110, 120]]
])
print(i[0, 1, 2])


# In[17]:


print(i[1,1,2])


# In[18]:


print(i[1,-1,-1])


# In[19]:


print(i[1,-2,-1])


# In[20]:


i=np.array([10,20,30,40,50])
print(i[-1])


# # Slicing

# In[21]:


import numpy as np
i=np.array([10,20,30,40,50,60,70,80])
print(i[0:4])


# In[22]:


print(i[3:6])


# End Index

# In[23]:


print(i[1:])


# Start Index

# In[24]:


print(i[:4])


# # Neagative Slicing Index

# In[25]:


import numpy as np
i=np.array([10,20,30,40,50,60,70,80])
print(i[-4:-2])


# In[26]:


print(i[-3:-1])


# In[27]:


print(i[2:-3])


# # Slicing With Step

# In[28]:


import numpy as np
i=np.array([10,20,30,40,50,60,70,80,90,100])
print(i[1:9:2])


# In[29]:


print(i[0:8:3])


# In[30]:


print(i[::])


# In[31]:


print(i[::2])


# # Slicing With 2D Array

# In[32]:


import numpy as np
i=np.array([
    [10,20,30,40,50],
    [60,50,80,90,100],
    [110,120,130,140,150],
    [1,2,3,4,5,]
])
print(i[0,1:3])


# In[33]:


print(i[1,0:4])


# In[34]:


print(i[1,1:3])


# In[35]:


print(i[2, 1:4])


# In[36]:


print(i[2,0:4])


# In[37]:


print(i[0:2,3])


# In[38]:


print(i[0:3,4])


# In[39]:


print(i[0:3,0:3])


# In[40]:


print(i[0:3,-4:-1])


# # Data Type in Numpy

# In[41]:


import numpy as np
i=np.array([1,2,3,4,5])
print(i.dtype)


# In[42]:


import numpy as np
i=np.array([1,2,3,4,5])
j=i.astype('f')
print(j)
print(j.dtype)


# In[43]:


import numpy as np
i=np.array([10,0,12,0,11,1,0,3,0])
j=i.astype('bool')
print(j)
print(j.dtype)


# # Copy Data And View Data
# 

# Copy Data

# In[44]:


import numpy as np
i=np.array([1,2,3,4,5]) #Original Data
j=i.copy()  #copy data
i[0]=10
i[1]=20
print(i)
print(j)


# View Data
# 

# In[45]:


import numpy as np
i=np.array([1,2,3,4,5]) #original data
j=i.view() #view data
i[2]=30
i[3]=40
print(i)
print(j)


# Changes in Copy  Data
# 

# In[46]:


import numpy as np
i=np.array([1,2,3,4,5]) #Original Data
j=i.copy()  #copy data
j[0]=10
j[1]=20
print(i)
print(j)


# Changes in View Data

# In[47]:


import numpy as np
i=np.array([1,2,3,4,5]) #original data
j=i.view() #view data
j[2]=30
j[3]=40
print(i)
print(j)


# # Base Atrribute

# In[48]:


import numpy as np
i=np.array([1,2,3,4,5,6,7,8,9,10])
j=i.view()
j[1]=10
j[2]=20
print(i)
print(j)

print()
print(i.base)
print(j.base)


# # Numpy Shape

# In[49]:


# 1 D Example
import numpy as np
i=np.array([1,2,3,4,5,6,7,8])
print(i.shape)


# In[50]:


# 2 D Example
import numpy as np
i=np.array([
    [1,2,3,4,5,6,7,8,9,10],
    [11,22,33,44,55,66,77,88,99,111]
])
print(i.shape)


# In[53]:


#3 D Example
import numpy as np
i=np.array([
    [[1,2,3,4,5],[6,7,8,9,10]],
    [[11,12,13,14,15],[16,17,18,19,20]]
])
print(i.shape)


# # Numpy Reshape

# In[54]:


import numpy as np
i = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
j = i.reshape(5,2)
print(j)


# In[55]:


import numpy as np
i = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
j = i.reshape(4,3)
print(j)


# In[56]:


import numpy as np
i = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 113])
j = i.reshape(4,3)
print(j)


# In[57]:


import numpy as np
i = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,150, 160])
j = i.reshape(2,2,4)
print(j)


# In[58]:


import numpy as np
i = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,150, 160])
j = i.reshape(2,4,2)
print(j)


# In[59]:


import numpy as np
i = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,150])
j = i.reshape(2,4,2)
print(j)


# In[60]:


import numpy as np
i = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,150,160])
j = i.reshape(2,4,-1)
print(j)


# In[63]:


import numpy as np
i=np.array([
    [[1,2,3,4,5],[6,7,8,9,10]],
    [[11,22,33,44,55],[66,77,88,99,100]],
    [[12,13,14,15,16],[17,18,19,20,21]]
])
j=i.reshape(-1)
print(i.ndim)
print(j)


# In[64]:


import numpy as array
i=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
j=i.reshape(-1)
print(i.ndim)
print(j)


# # Access Elements

# In[65]:


import numpy as np
i=np.array([1,2,3,4,5,6,7,8,9,10])
for j in i:
    print(j)


# In[66]:


import numpy as np
i=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
for j in i:
    print(j)


# In[67]:


import numpy as np
i=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
for j in i:
    for k in j:
        print(k)


# In[70]:


import numpy as np
i=np.array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[11,12,13],[14,15,16],[17,18,19]],
    [[21,22,23],[24,25,26],[27,28,29]]
])
print(i.shape)
for j in i:
    for k in j:
        for m in k:
            print(m)


# # Random Number in Numpy

# In[75]:


from numpy import random
i=random.randint(100)
print(i)


# In[78]:


from numpy import random 
i=random.rand()
print(i)


# In[79]:


from numpy import random 
i=random.rand(10)
print(i)


# In[80]:


from numpy import random
i=random.randint(100,size=(10))
print(i)


# In[81]:


from numpy import random
i=random.randint(100,size=(2,5))
print(i)


# In[82]:


from numpy import random
i=random.randint(100,size=(6,6))
print(i)


# In[83]:


from numpy import random
i=random.randint(100,size=(4,3,5))
print(i)


# In[84]:


from numpy import random 
i=random.rand(5,2)
print(i)


# In[85]:


from numpy import random 
i=random.rand(3,3,3)
print(i)


# # Choice Method

# In[86]:


from numpy import random
i=[1,2,3,4,5,6,7,8,9,10]
j=random.choice(i)
print(j)


# In[87]:


from numpy import random
i=[1,2,3,4,5,6,7,8,9,10]
j=random.choice(i,size=(2,5))
print(j)


# In[88]:


from numpy import random
i=[1,2,3,4,5,6,7,8,9,10]
j=random.choice(i,size=(2,5,3))
print(j)


# In[ ]:




