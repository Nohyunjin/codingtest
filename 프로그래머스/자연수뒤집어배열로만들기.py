# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.


def solution(n : int):
    answer = []
    # 자연수를 str로 바꾸고 순서를 뒤집음
    s = reversed(str(n))
    # s에 있는 요소들을 하나씩 리스트에 추가
    for i in s :
        answer.append(int(i))
    return answer


# 다른 사람 풀이
def solution(n):
    return list(map(int, reversed(str(n))))