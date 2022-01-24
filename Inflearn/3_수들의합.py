import sys
sys.stdin = open("inflearn\input.txt", 'r')
n, m=map(int, input().split())
a=list(map(int, input().split()))

cnt = 0
left = 0
right = 1
sum_ = a[0]

while True:
    if sum_ < m: # 더한 값이 m보다 작을경우 다음 단계로 진행
        if right < n: # 오른쪽 값이 총 길이보다는 작아야 함
            sum_ += a[right] # 시작값의 오른쪽을 더함
            right += 1 # 다음 값 진행
        else: # 총 길이보다 커지면
            break # 빠져나오게
    elif sum_ == m: # 더한 값이 m이랑 같을 경우 cnt 1증가 후 시작값을 빼주기
        cnt += 1 # 경우의 수 1 증가
        sum_ -= a[left] # 시작값 빼고 다시 시작
        left += 1 # 시작값 조정
    else : # 더한 값이 m보다 클 경우 시작값 빼고 다시 시작
        sum_ -= a[left]
        left += 1
print(cnt)
