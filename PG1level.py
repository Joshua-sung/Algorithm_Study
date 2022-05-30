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
def solution(x, n):
    answer = []
    plus=0
    for i in range(1,n+1):
        plus = x*i
        answer.append(plus)  
    return answer