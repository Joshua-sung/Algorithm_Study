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
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*',end='')
    print()