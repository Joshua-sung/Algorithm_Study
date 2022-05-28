#로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    cnt=0
    ZeroCnt=0
    for i in lottos:
        if i in win_nums:
            cnt+=1
        elif i == 0:
            ZeroCnt+=1

    answer = []
    if cnt>=2:
        answer.append(7-(cnt+ZeroCnt))
        answer.append(7-cnt)
    elif cnt == 0 and ZeroCnt ==0:
        answer=[6,6]
    else:
        answer.append(7-(cnt+ZeroCnt))
        answer.append(6)
         
    return answer