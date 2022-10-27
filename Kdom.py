

import numpy as np





def pmat(mat,n):
    val=""
    for iy, ix in np.ndindex(mat.shape):
        num=mat[iy, ix]
        if num==-1:
            num="K"
        else:
            num=str(num)

        if ix==n-1:
            val=val+(num+"  \n")
        else:
            val=val+(num+"  ")
    
    return val




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




import itertools as itr
def kights_dom(n):

    if n<0:
        return "invalid input","invalid input","invalid input"
    k=n*n
    bestk=n*n
    c=0
    bestsol=np.full((n,n),-1)
    while(c<1000):
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

        if c==10:
            r1=pmat(bestsol,n)+"\nThe Number of knights is "+str(bestk)
        if c==100:
            r2=pmat(bestsol,n)+"\nThe Number of knights is "+str(bestk)
        c+=1
        r3=pmat(bestsol,n)+"\nThe Number of knights is "+str(bestk)

    return r1,r2,r3





#print(str(kights_dom(8)[2]))
