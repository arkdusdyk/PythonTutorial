#기초 출력변환
#1031
num = int(input())
print("%o" %num)

#1032,1033
#16를소문자, 대문자로 하는가
num = int(input())
print("%X" %num)

#1034
#8진수 -> 10진수
num = int(input(),8)
print("%d" %num)

#1035
#16진수 -> 8진수
num = int(input(), 16)
print("%o" %num)

#1036
#ASCII to dec
ch = input()
print(ord(ch))

#1037
#dec to ASCII
ch = int(input())
print(chr(ch))
