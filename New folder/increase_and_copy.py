def increasecopy(high, n):
    #global moves
    for i in range(3, n+1):
        if i <= 1:
            moves[i] = 0
        if(i>high):  
            moves[i] = 1 + min(moves[i-1], moves[i-high])
        else:
            moves[i] = min(moves[i-1], moves[i-high])
    return moves[n]


test = int(input())
for i in range(test):
    
    n = int(input())
    if n == 1:
        print(0)
        continue
    moves = [0]*(n+1)
    moves[0] = 0
    moves[1] = 0
    moves[2] = 1
    print(increasecopy(1, n))
