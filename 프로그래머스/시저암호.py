# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다.
# "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

def solution(s, n):
    low_answer = "abcdefghijklmnopqrstuvwxyz"
    up_answer = low_answer.upper()
    
    result = []
    
    for i in s :
        if i == ' ':
            result.append(" ")
        elif i.islower() is True:
            indx = low_answer.find(i) + n
            result.append(low_answer[indx % 26])
        else:
            indx = up_answer.find(i) + n
            result.append(up_answer[indx % 26])
            
    return "".join(result)