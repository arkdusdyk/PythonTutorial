#기초 조건, 반복실행
#1065~1066
#짝수 홀수 조건
num = list(map(int, input().split()))
for i in range(3):
    if(num[i]%2==0):
        print("even")
    else:
        print("odd")

#1067
num = int(input())
if(num>0):
    print("plus")
else:
    print("minus")
if(num%2==0):
    print("even")
else:
    print("odd")

#1068
num = int(input())
if(num>=90):
	print("A")
elif(num>=70):
	print("B")
elif(num>=40):
	print("C")
else:
	print("D")

#1069
ch = input()
if(ch=="A"):
	print("best!!!")
elif(ch=="B"):
	print("good!!")
elif(ch=="C"):
	print("run!")
elif(ch=="D"):
	print("slowly~")
else:
	print("what?")

#1070
num = int(input())
if(num==12 or num==1 or num==2):
	print("winter")
elif(num==3 or num==4 or num==5):
	print("spring")
elif(num==6 or num==7 or num==8):
	print("summer")
else:
	print("fall")

#1071
num = list(map(int, input().split()))
i=0
while(i<len(num)):
	if(num[i]==0):
		break
	print(num[i])
	i+=1

#1072
cnt = int(input())
num = list(map(int, input().split()))
i=0
while(i<cnt):
	print(num[i])
	i+=1

#1073 == 1071

#1074
num = int(input())
while(num>0):
	print(num)
	num-=1

#1075
num = int(input())
num-=1
while(num>=0):
	print(num)
	num-=1

#1076
ch = input()
num = ord('a')
while(num <= ord(ch)):
	print(chr(num), end=' ')
	num+=1

#1077
num = int(input())
i=0
while(num>=i):
	print(i)
	i+=1
