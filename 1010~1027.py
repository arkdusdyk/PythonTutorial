#기초 입출력
#1010
num = int(input())
print(num)

#1011
alp = input()
print(alp)

#1012
alp = float(input())
print("%f" %alp)

#1013
num1,num2 = map(int, input().split())
print(num1, num2)

#1014
ch1, ch2 = input().split()
print(ch2, ch1)

#1015
f1 = float(input())
print("%.2f" %f1)

#1017
n1 = int(input())
print(n1,n1,n1,sep=' ')

#1018
num1, num2 = map(int, input().split(':'))
print("{0}:{1}".format(num1,num2))
#print(f'{num1}:{num2}') -> python3.6 이상만 지원

#1019
num1,num2,num3 = map(int,input().split('.'))
print("%4d.%02d.%02d"%(num1,num2,num3))

#1020
num1,num2 = map(int, input().split('-'))
print("%06d%07d" %(num1,num2))

#1021
str = input()
print(str)

#1022
print(input())  #사실상 이전 문제와 같음

#1023
num1, num2 = map(int,input().split('.'))
print(num1)
print(num2)

#1024
str = input()
for letter in str:
    print('\'%s\'' %letter)

#1025
arr = []
num = int(input())
digit=10000
while(num>0):
    arr.append(num%10)
    num= num//10
arr.reverse()
for i in arr:
    print('[%d]' %(i*digit))
    digit = digit//10
#could also try:
#num = input()
#for i in range(len(num)):
    #print("[%d]" %(int(num[i])*10**(len(num)-(i+1))))

#1026
hr,mn,sc = map(int, input().split(':'))
print(mn)

#1027
yr,mn,dy = map(int, input().split('.'))
print("%02d-%02d-%04d" %(dy,mn,yr))
