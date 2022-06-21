#로또의 최고 순위와 최저 순위
# def solution(lottos, win_nums):
#     cnt=0
#     ZeroCnt=0
#     for i in lottos:
#         if i in win_nums:
#             cnt+=1
#         elif i == 0:
#             ZeroCnt+=1

#     answer = []
#     if cnt>=2:
#         answer.append(7-(cnt+ZeroCnt))
#         answer.append(7-cnt)
#     elif cnt == 0 and ZeroCnt ==0:
#         answer=[6,6]
#     else:
#         answer.append(7-(cnt+ZeroCnt))
#         answer.append(6)
         
#     return answer

#짝수와 홀수
# def solution(num):
#     answer = ''
#     if num%2==0:
#         answer="Even"
#     else:
#         answer="Odd"
#     return answer

#x만큼 간격이 있는 n개의 숫자
# def solution(x, n):
#     answer = []
#     plus=0
#     for i in range(1,n+1):
#         plus = x*i
#         answer.append(plus)  
#     return answer

# 행렬의 덧셈
# def solution(arr1, arr2):
#     answer = arr1
#     for i in range(len(arr1)):
#         for j in range(len(arr2[i])):
#             answer[i][j]=arr1[i][j]+arr2[i][j]
#     return answer

#하샤드 수
# def solution(x):
#     answer = True
#     hab=0 
#     for i in str(x):
#         hab+=int(i)
#     if x%hab==0:
#         answer=True
#     else:
#         answer=False
#     return answer

#평균 구하기
# def solution(arr):
#     answer = 0
#     hab=0
#     for i in arr:
#         hab+=int(i)
#     answer=hab/len(arr)
#     return answer

#직사각형 별찍기
# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     for j in range(a):
#         print('*',end='')
#     print()

#최대공약수와 최소공배수
# def solution(n, m):
#     a = n
#     b = m
#     if n>m:
#         n, m = m, n
#     while m%n:
#         r = m%n
#         m = n
#         n = r
#     return [n, a*b/n]

#휴대폰 번호 가리기
# def solution(phone_number):
#     answer = ''
#     for i in range(len(phone_number)-4):
#         answer += "*"
#     for i in range(len(phone_number)-4,len((phone_number))):
#         answer += phone_number[i]
#     return answer

#서울에서 김서방 찾기
# def solution(seoul):
#     answer = ''
#     for i in range(len(seoul)): 
#         if seoul[i] =="Kim":
#             answer = "김서방은 {}에 있다".format(i)
#     return answer

#두 정수의 합
# def solution(a, b):
#     answer = 0
#     if a<=b:
#         for i in range(a,b+1):
#             answer+=i
#     else:
#         c=b
#         d=a
#         for i in range(c,d+1):
#             answer+=i
#     return answer

#이상한 문자 만들기
# def solution(s):
#     answer =''
#     nanu=s.split(' ')
#     for i in nanu:
#         for j in range(len(i)):
#             if j%2==0:
#                 answer+=i[j].upper()
#             else:
#                 answer+=i[j].lower()
#         answer+= ' '
#     return answer[0:-1]

#자릿수 더하기
# def solution(n):
#     answer = 0
#     n=str(n)
#     for i in n:
#         answer += int(i)

#     return answer

#자연수 뒤집어 배열로 만들기
# def solution(n):
#     answer = []
#     n=str(n)
#     for i in n:
#         answer.insert(0,int(i))
#     return answer

#콜라스추측
# def solution(num):
#     answer = 0
#     if num==1:
#         return answer
#     while num != 1:
#         if answer > 500:
#             return -1
#             break
#         elif num%2==0:
#             answer+=1
#             num = num/2
#         elif num%2!=0:
#             answer+=1
#             num = num*3+1
#     return answer

#제일 작은수 제거하기
# def solution(arr):
#     if len(arr)==1:
#         return [-1]
#     arr.remove(min(arr))
#     return arr

#정수 내림차순 배치하기
# def solution(n):
#     k = list(str(n))
#     k.sort(reverse=True)
#     answer=''
#     for i in k:
#         answer+=str(i)
#     return int(answer)

#수박수박수 문제
def solution(n):
    answer = ''
    for i in range(n):
        if i%2==0:
            answer+='수'
        else:
            answer+='박'
    return answer
