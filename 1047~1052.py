#기초 bitshift, 비교연산
#1047
a = int(input())
print(a<<1)

#1048
a,b = map(int,input().split(' '))
print(a<<b)

#1049~1052
#비교연산의 차이일뿐 모두 같은 유형
a,b = map(int, input().split(' '))
if(a>b):
    print(1)
else:
    print(0)
