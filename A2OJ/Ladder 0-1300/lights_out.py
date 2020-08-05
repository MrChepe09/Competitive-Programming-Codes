def lights(a):
    light = [[1 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if(a[i][j]%2==1):
                if(i==0 and j==0):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i+1][j] = (light[i+1][j]+1) % 2
                    light[i][j+1] = (light[i][j+1]+1) % 2
                elif(i==0 and j==1):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i+1][j] = (light[i+1][j]+1) % 2
                    light[i][j+1] = (light[i][j+1]+1) % 2
                    light[i][j-1] = (light[i][j-1] + 1) % 2
                elif(i==0 and j==2):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i+1][j] = (light[i+1][j]+1) % 2
                    light[i][j-1] = (light[i][j-1] + 1) % 2
                elif(i==1 and j==0):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i+1][j] = (light[i+1][j]+1) % 2
                    light[i][j+1] = (light[i][j+1]+1) % 2
                    light[i-1][j] = (light[i-1][j] + 1) % 2
                elif(i==1 and j==1):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i+1][j] = (light[i+1][j]+1) % 2
                    light[i][j+1] = (light[i][j+1]+1) % 2
                    light[i-1][j] = (light[i-1][j] + 1) % 2
                    light[i][j-1] = (light[i][j-1] + 1) % 2
                elif(i==1 and j==2):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i-1][j] = (light[i-1][j]+1) % 2
                    light[i][j-1] = (light[i][j-1]+1) % 2
                    light[i+1][j] = (light[i+1][j] + 1)%2
                elif(i==2 and j==0):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i+1][j] = (light[i+1][j]+1) % 2
                    light[i][j+1] = (light[i][j+1]+1) % 2
                    light[i-1][j] = (light[i-1][j] + 1) % 2
                elif(i==2 and j==1):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i-1][j] = (light[i-1][j]+1) % 2
                    light[i][j-1] = (light[i][j-1]+1) % 2
                    light[i][j+1] = (light[i][j+1] + 1)%2
                elif(i==2 and j==2):
                    light[i][j] = (light[i][j]+1) % 2
                    light[i-1][j] = (light[i-1][j]+1) % 2
                    light[i][j-1] = (light[i][j-1]+1) % 2
    return light



a = []
for i in range(3):
    arr = list(map(int, input().split()))
    a.append(arr)
res = lights(a)
for i in res:
    print(''.join(map(str, i)))