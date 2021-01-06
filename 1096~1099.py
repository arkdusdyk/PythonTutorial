#기초-2d array
#1096
num = int(input())
arr = [[0 for i in range(19)] for j in range(19)]
for k in range(num):
    i,j = map(int, input().split())
    arr[i-1][j-1] = 1
for i in range(19):
    for j in range(19):
        print(arr[i][j], end = ' ')
    print()

#1097
arr = [0 for i in range(19)]
for i in range(19):
	arr[i] = list(map(int, input().split()))
num = int(input())
for k in range(num):
	i,j = map(int, input().split())
	for l in range(19):
		if(arr[i-1][l]==0):
			arr[i-1][l]=1
		else:
			arr[i-1][l]=0
	for l in range(19):
		if(arr[l][j-1]==0):
			arr[l][j-1]=1
		else:
			arr[l][j-1]=0
for i in range(19):
	for j in range(19):
		print(arr[i][j], end = ' ')
	print()

#1098
i,j = map(int, input().split())
arr = [[0 for k in range(j)] for l in range(i)]
n = int(input())
for k in range(n):
	l,d,x,y = map(int, input().split())
	if(d==0):
		for m in range(l):
			arr[x-1][y-1+m] =1
	else:
		for m in range(l):
			arr[x-1+m][y-1] = 1
for k in range(i):
	for l in range(j):
		print(arr[k][l], end = ' ')
	print()

#1099
arr = [0 for i in range(10)]
for i in range(10):
	arr[i] = list(map(int, input().split()))
x,y = 1,1
while(True):
	if(arr[x][y]==2):
		arr[x][y]=9
		break
	arr[x][y]=9
	if(arr[x][y+1]!=1):
		y+=1
	else:
		if(arr[x+1][y]==1):
			break
		x+=1
for i in range(10):
	for j in range(10):
		print(arr[i][j], end = ' ')
	print()