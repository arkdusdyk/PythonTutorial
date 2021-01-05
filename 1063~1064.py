#기초 삼항연산

#1063
num1, num2 = map(int, input().split())
print(num1 if num1>num2 else num2)

#1064
num = list(map(int, input().split()))
if(num[0]<num[1]):
    if(num[0]< num[2]):
        min = num[0]
    else:
        min = num[2]
else:
    if(num[1] < num[2]):
        min = num[1]
    else:
        min = num[2]
print(min)
