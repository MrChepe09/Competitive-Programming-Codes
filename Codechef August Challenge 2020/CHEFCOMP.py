from collections import defaultdict
def chefcomp(n, p, a, b):
    global graph
    print(graph)
    day = [-1 for _ in range(n+1)]
    for i in range(1, n+1):
        visited = [0 for _ in range(n+1)]
        curr = p[i]
        stack = []
        stack.append(curr)

        while(len(stack)!=0):
            s = stack[-1]
            stack.pop()

            if(visited[s]):
                continue
            else:
                visited[s] = 1
                b[s] = b[s]-min(a[curr], b[s])
                if(b[s]<=0 and day[s]==-1):
                    day[s] = i
            print(graph)
            for c in graph[s]:
                print(c, graph[s])
                if(c and (visited[c] ==0 )):
                    stack.append(i)

            for c in graph[curr]:
                graph[curr][c] = 0
                graph[c][curr] = 0

            print(day)


test = int(input())
for i in range(test):
    n = int(input())
    graph = defaultdict(defaultdict)
    for i in range(1, n+1):
        graph[i] = {}
        for j in range(1, n+1):
            graph[i][j] = 0
    for i in range(n-1):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(chefcomp(n, p, a, b))   
