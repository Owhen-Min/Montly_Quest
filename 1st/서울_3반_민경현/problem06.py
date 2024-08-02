############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    length_list = []
    # 길이를 저장하기 위한 빈 리스트 선언
    for string in str_list:
        count = 0
        # string의 길이를 측정하기 위한 변수 0 선언.
        for char in string:
            count += 1
            # 글자 하나마다 count를 1씩 더함.
        length_list.append(count)
        # 차례대로 총 글자수를 length_list에 추가해줌.
    return str_list[length_list.index(max(length_list))]
# length_list 중 가장 큰 숫자의 index를 str_list에서 index로 호출할 경우 길이가 가장 긴 문자열을 반환할 수 있다.
# index로 호출할 경우 길이가 같은 문자열 속에서 가장 먼저 찾은 문자열을 반환하게 된다.



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"