# print('\"!@#$%^&*()\'')
# print('\"C:\\Download\\\'hello\'.py\"')
# print("print(\"Hello\\nWorld\")")

#6013
# userin13a=input()
# userin13b=input()
# print(userin13b)
# print(userin13a)

# #6014
# userin14f=float(input())
# print(userin14f)
# print(userin14f)
# print(userin14f)

# #6015
# userin15a, userin15b= input().split(' ')
# print(userin15a)
# print(userin15b)

#6016
# userin16a, userin16b= input().split(' ')
# print(userin16b+' '+userin16a)

#6017
# userin17 = input()
# print(userin17, userin17, userin17)

#6018
# userin18a, userin18b = input().split(':')
# print(userin18a, userin18b, sep=':')

# #6019
# year,mon,day= input().split('.')
# print(f"{day}-{mon}-{year}")

# #6020
# firstid,lastid=input().split('-')
# print(f"{firstid}{lastid}")

#6027
# a = input()
# n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
# print('%x'% n)  n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

#6028
# a28 = input()
# n28 = int(a28) 
# print('%X' % n28)  #n28에 저장되어있는 값을 16진수 대문자 형태 문자열로 출력

#6029
# a29 = input()
# n29 = int(a29, 16)      #입력된 a29를 16진수로 인식해 변수 n에 저장
# print('%o' % n29)  #n29에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

#6030
# n30 = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
# print(n30)

#6031
# c = int(input())
# print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 

#6043
# a,b = input().split(' ')
# c=float(a)/float(b)
# print(format(c,".3f"))

#6044
# a,b = input().split(' ')
# a44=int(a)
# b44=int(b)
# print(a44+b44)
# print(a44-b44)
# print(a44*b44)
# print(a44//b44)
# print(a44%b44)
# print(format(a44/b44,".2f"))

#6045
# a,b,c = input().split(' ')
# a45 = int(a)
# b45 = int(b)
# c45 = int(c)
# hab = a45+b45+c45
# avg = hab/3
# print(hab,format(avg,".2f"))

#6048
# a,b=input().split(' ')
# print(int(a)<int(b)) # true가 출력됨

#6052
# n=int(input())
# print(bool(n))

#6055
# a, b = input().split()
# print(bool(int(a)) or bool(int(b)))

#6059
# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)
# ** 비트단위(bitwise) 연산자는,
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)
# 가 있다.

#6060
# a,b=input().split(' ')
# print(int(a)&int(b))

#6064
# print((a if a<b else b) if ((a if a<b else b)<c) else c)

#6066
# def check(x):
#     if x%2==0 :
#         print("even")
#     else :
#         print("odd")
# a, b, c = map(int,input().split(' '))
# check(a)
# check(b)
# check(c)

#6074 알파벳 출력
# 알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
# chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.
# c = ord(input())
# t = ord('a')
# while t<=c :
#   print(chr(t), end=' ')
#   t += 1

#6078
# while True:
#     usrin = input()
#     print(usrin)
#     if usrin =="q":
#         break

#6080
# n , m = map(int,input().split( ))
# for i in range(1, n+1) :
#   for j in range(1, m+1) :
#     print(i, j)

#6081
# print('%X'%n) #n에 저장되어있는 값을 16진수로 출력
# n = int(input(), 16)
# for i in range(1, 16) :
#   print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#6082
a = int(input())
for i in range(1,a+1):
    if (i%10==3 or i%10==6 or i%10==9):
        print('X',end=' ')
        continue    
    print(i,end=' ')