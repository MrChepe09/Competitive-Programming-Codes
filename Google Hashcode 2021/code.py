from random import randint
fin = open("c.txt")
fout = open("output.txt", "w")

inpKeys = list(map(int, fin.readline().rstrip('\n').split()))
streetTime = {}
streetIntersections = {}
carPath = []
pathExist = {}
streetCount = {}
for i in range(inpKeys[2]):
    streetLine = list(fin.readline().rstrip('\n').split())
    streetIntersections[streetLine[2]] = [int(streetLine[0]), int(streetLine[1])]
    streetTime[streetLine[2]] = streetLine[3]
for i in range(inpKeys[3]):
    carLine = list(fin.readline().rstrip('\n').split())
    for i in range(1, len(carLine)):
        if(carLine[i] in streetCount):
            streetCount[carLine[i]]+=1
        else:
            streetCount[carLine[i]] = 1
        pathExist[carLine[i]] = True
    carPath.append(carLine)

ans = 0
done = []
for i in pathExist:
    if(streetIntersections[i][1] not in done):
        ans+=1
        done.append(streetIntersections[i][1])


fout.write(str(ans) + '\n')
curr = 0
while(curr<inpKeys[1]):
    rm = randint(1, 50%inpKeys[0])
    res = []
    maxi = 0
    resm = 0
    for i in streetIntersections:
        if(streetIntersections[i][1] == curr and (i in pathExist)):
            res.append(i)
        
    if(len(res) != 0):
        fout.write(str(curr)+'\n')
        fout.write(str(len(res)) + '\n')
        for i in streetCount:
            if(streetIntersections[i][1] == curr and streetCount[i]>maxi):
                maxi = streetCount[i]
                resm = i
    for i in res:
        if(i == resm):
            fout.write(i+" "+str(rm)+'\n')
        else:
            fout.write(i+" "+str(1)+'\n')
    curr+=1

fin.close()
fout.close()