def ops(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def digit(dataset):
	d = dataset[::2]
	op = dataset[1::2]
	d=[float(i) for i in d]
	m = [[0]*(len(d)+1) for _ in range(len(d)+1)]
	M = [[0]*(len(d)+1) for _ in range(len(d)+1)]
	for i in range(1,len(d)+1):
		m[i][i] = M[i][i] = d[i-1]
	n = len(d)
	for s in range(1,n):
		for i in range(1,n-s+1):
			j = i+s
			mini,maxi = float('inf'),float('-inf')
			for k in range(i,j):
				a = ops(M[i][k],M[k+1][j],op[k-1])
				b = ops(M[i][k],m[k+1][j],op[k-1])
				c = ops(m[i][k],M[k+1][j],op[k-1])
				d = ops(m[i][k],m[k+1][j],op[k-1])
				mini = min(mini,a,b,c,d)
				maxi = max(maxi,a,b,c,d)
			m[i][j] = mini
			M[i][j]	= maxi
	return int(M[1][n])

n= input()
print(digit(n))
