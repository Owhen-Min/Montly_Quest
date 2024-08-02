############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
def reverse_string(s):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if len(s) == 0:
        return s
    # 재귀함수가 무한으로 돌지 않도록 입력값의 길이가 1일 경우 주어진 s를 반환하고 재귀를 멈춘다.
    return reverse_string(s[1:]) + s[0]
    # 주어진 s의 첫 글자를 제일 뒤에 배치하고, 나머지 글자들은 다시 reverse_string 함수에 집어넣는다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(reverse_string("hello"))  # "olleh"
print(reverse_string("world"))  # "dlrow"
print(reverse_string("python"))  # "nohtyp"
#####################################################

s = 'odddda'
lst =list(s)
print(len(s))
print(s[100:])
print(lst[100:])
# print(lst[-1:len(s): -1])

print(s[len(s):-1:-1]) # 음수 인댁수
