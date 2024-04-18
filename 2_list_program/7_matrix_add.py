l1=[[2,3,4],[5,6,7]]
l2=[[1,2,3],[4,5,6]]
result=[[0,0,0],[0,0,0]]
for i in range(len(l1)):
    for j in range(len(l1[0])):
        result[i][j]=l1[i][j]+l2[i][j]
print(result)