#기초 산술연산
#1038,1039
num1, num2 = map(int, input().split(' '))
print(num1+num2)

#1040
num = int(input())
print(-1*num)

#1041
ch = input()
num = ord(ch)
print(chr(num+1))

#1042,1043
#연산의 차이만 있음
num1, num2 = map(int, input().split(' '))
print(num1%num2)

#1044
print((int(input()))+1)

#1045
a,b = map(int, input().split(' '))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("%.2f" %(a/b))

#1046
a,b,c = map(int, input().split(' '))
print(a+b+c)
print("%.1f" %((a+b+c)/3))
