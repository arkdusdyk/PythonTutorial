#기초-종합

#1078
num = int(input())
sum=0
while(num>0):
    if(num%2==0):
        sum+=num
    num-=1
print(sum)

#1079
ch = list(input().split())
i=0
while(True):
	print(ch[i])
	if(ch[i]=='q'):
		break
	i+=1

#1080
num = int(input())
i=1
sum=0
while(True):
	sum+=i
	if(sum>=num):
		print(i)
		break
	i+=1

#1081
num1, num2 = map(int, input().split())
for i in range(0,num1):
	for j in range(0, num2):
		print(i+1, j+1)

#1082
a = int(input(),16)
for i in range (1, 16):
	print(("%X"%a)+'*'+("%X" %i) + '=' + ('%X'%(a*i)))

#1083
a = int(input())
for i in range(1, a+1):
	if(i%3==0):
		print("X", end = ' ')
	else:
		print(i, end = ' ')

#1084
num = list(map(int, input().split()))
count=0
for i in range(num[0]):
	for j in range(num[1]):
		for k in range(num[2]):
			print(i,j,k)
			count+=1
print(count)

#1085
h, b, c, s, = map(int, input().split())
store = round(h*b*c*s/8/1024/1024,1)
print(store , "MB")

#1086
w, h, b = map(int, input().split())
store = round(w*h*b/8/1024/1024, 2)
print("%.2f MB" %store)

#1087
num = int(input())
sum=0
i=1
while(True):
	sum += i
	if(sum>=num):
		print(sum)
		break
	i+=1

#1088
num = int(input())
i=1
while(num>=i):
	if(i%3==0):
		pass
	else:
		print(i, end = ' ')
	i+=1

#1089
arr = list(map(int, input().split()))
print((arr[2]-1)*arr[1] + arr[0])

#1090
arr = list(map(int, input().split()))
print(arr[0]*(arr[1]**(arr[2]-1)))

#1091
arr = list(map(int, input().split()))
for i in range(1, arr[3]):
	arr[0] *= arr[1]
	arr[0] += arr[2]
print(arr[0])

#1092
num = list(map(int, input().split()))
i=1
while(True):
	if(i%num[0]==0 and i%num[1]==0 and i%num[2]==0):
		print(i)
		break
	else:
		i+=1