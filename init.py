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
# print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

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
a,b = input().split(' ')
c=float(a)/float(b)
print(format(c,".3f"))
