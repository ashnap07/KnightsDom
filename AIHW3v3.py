#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def pmat(mat):
    for iy, ix in np.ndindex(mat.shape):
        if ix==n-1:
            print(mat[iy, ix])
        else:
            print(mat[iy, ix],end="")


# In[3]:


def attacked(bd,x,y):
    n=len(bd[0])

    if not(x>=0 and x<n and y>=0 and y <n):
        return True
    
    attacked=False
    
    if bd[x][y]== -1:
        attacked=True
    if x+1 < n and y + 2 < n:
        if bd[x+1][y+2]== -1:
            attacked=True
    if (x+2) < n and (y + 1) < n:
        if bd[(x+2)][(y+1)]== -1:
            attacked=True
    if (x+2) < n and y - 1 >=0:
        if bd[x+2][y-1]== -1:
            attacked=True
    if x+1 < n and y - 2 >=0:
        if bd[x+1][y-2]== -1:
            attacked=True
    if x-1 >=0 and y + 2 <n:
        if bd[x-1][y+2]== -1:
            attacked=True
    if x-2 >=0 and y + 1 <n:
        if bd[x-2][y+1]== -1:
            attacked=True
    if x-2 >=0 and y -1 >=0:
        if bd[x-2][y-1]== -1:
            attacked=True
    if x-1 >=0 and y -2 >=0:
        if bd[x-1][y-2]== -1:
            attacked=True
            
    return attacked

def nibattacked(bd,x,y):
    if not attacked(bd,x+1,y+2):
        return False
    elif not attacked(bd,x+2,y+1):
        return False
    elif not attacked(bd,x+2,y-1):
        return False
    elif not attacked(bd,x+1,y-2):
        return False
    elif not attacked(bd,x-1,y+2):
        return False
    elif not attacked(bd,x-2,y+1):
        return False
    elif not attacked(bd,x-2,y-1):
        return False
    elif not attacked(bd,x-1,y-2):
        return False
    else:
        return True


# In[31]:


import itertools as itr
n=20
if n<0:
    print("invalid input")
    exit()
k=n*n
c=0
bestk=n*n
bestsol=np.full((n,n),-1)
while(c<=1000):
    bd=np.full((n,n),-1)
    arr1=list(range(n))
    L=arr1+arr1
    p=list(itr.permutations(L,2))


    while(len(p)>0): 
        idx=np.random.randint(len(p))
        x,y=p[idx][0],p[idx][1]
        del p[idx]
        if attacked(bd,x,y):
            bd[x][y]=0
        if not nibattacked(bd,x,y):
            bd[x][y]=-1            

    
    for iy, ix in np.ndindex(bd.shape):     
        at=attacked(bd,iy,ix)
        if not at:
            bd[iy][ix]=-1
    k=0 
    for iy, ix in np.ndindex(bd.shape):
            if bd[iy, ix]==-1:
                k+=1
    
    if k<bestk:
        bestsol=bd
        bestk=k
        
    c+=1


# In[32]:


print(bestsol)
print(bestk)


# In[ ]:





# In[ ]:




