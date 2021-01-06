#기초 -1d array
#1093
num = int(input())
arr = list(map(int, input().split()))
cnt = [0 for i in range(23)]
for i in range(num):
    cnt[arr[i]-1] = cnt[arr[i]-1]+1
for i in range(23):
    print(cnt[i], end = ' ')

#1094
num = int(input())
arr = list(map(int, input().split()))
arr.reverse()
for i in range(num):
	print(arr[i], end = ' ')

#1095
num = int(input())
arr = list(map(int, input().split()))
min = arr[0]
for i in range(num):
	if(min>arr[i]):
		min = arr[i]
print(min)