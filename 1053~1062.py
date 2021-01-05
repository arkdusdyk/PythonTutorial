#기초논리연산, 비트단위

#1053~1058
#비교문의 산술연산자의 차이만 남
num1,num2 = map(int,input().split(' '))
if(num1==False and num2==False):
    print(1)
else:
    print(0)

#1059
num = int(input())
print(~(num))

#1060~1062
#비트연산자의 차이만 있음
num1, num2 = map(int, input().split())
print(num1 & num2)

