x=[[0,0,0,0,0]]
def con(m):
    if(m==0):
        return 1
    else:
        return 0
for i in range(3):
    x.append([0]+list(map(int,input().split()))+[0])
x.append([0,0,0,0,0]) 
 
y=[]
for i in range(5):
    a=[]
    for j in range(5):
        a.append(1)
    y.append(a)    
for i in range(1,4):
    for j in range(1,4):
        if(x[i][j]%2!=0):
             
            y[i][j]=con(y[i][j])
            y[i][j-1]=con(y[i][j-1])
            y[i][j+1]=con(y[i][j+1])
            y[i-1][j]=con(y[i-1][j])
            y[i+1][j]=con(y[i+1][j])
for i in range(1,4):
    for j in range(1,4):
        print(y[i][j],end="")
    print()    