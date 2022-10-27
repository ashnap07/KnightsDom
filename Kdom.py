

import numpy as np




#function to print the matrix as a chess with K instead of -1
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



#function checks if the cell at x,y is attacked by one knight at least
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

#function checks if all tragets of a knight is still attacked after its removal including its location
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

    #returns invalid input if the user enterd a negative number
    if n<0:
        return "invalid input","invalid input","invalid input"
    
    #k is the starting number of knights.
    k=n*n
    #bestk is to save the chessboard with lowest number of knights 
    bestk=n*n
    #counter of itreations
    c=0
    #matrics to save the best chessboard solution
    bestsol=np.full((n,n),-1)

    #starting point of the algorithm
    while(c<1000):
        #broadcasting -1 to the matrics to start the search
        bd=np.full((n,n),-1)
        
        #filling p with all possible indexs of the chessboard
        arr1=list(range(n))
        L=arr1+arr1
        p=list(itr.permutations(L,2))

        #starting point of the local search and knights removel
        while(len(p)>0): 
            idx=np.random.randint(len(p))
            x,y=p[idx][0],p[idx][1]
            del p[idx]
            if attacked(bd,x,y):
                bd[x][y]=0
            if not nibattacked(bd,x,y):
                bd[x][y]=-1            

        #checks if all cells are attacked and put -1 on them if otherwise
        for iy, ix in np.ndindex(bd.shape):     
            at=attacked(bd,iy,ix)
            if not at:
                bd[iy][ix]=-1
        
        #count the number of knights 
        k=0 
        for iy, ix in np.ndindex(bd.shape):
                if bd[iy, ix]==-1:
                    k+=1
        #keep track of the best solution
        if k<bestk:
            bestsol=bd
            bestk=k
        #keep track of the best solution after 10 itreations
        if c==10:
            r1=pmat(bestsol,n)+"\nThe Number of knights is "+str(bestk)
        #keep track of the best solution after 100 itreation
        if c==100:
            r2=pmat(bestsol,n)+"\nThe Number of knights is "+str(bestk)
        
        c+=1
        #saves the best solution after 1k itreations
        r3=pmat(bestsol,n)+"\nThe Number of knights is "+str(bestk)

    return r1,r2,r3





#print(str(kights_dom(8)[2]))
