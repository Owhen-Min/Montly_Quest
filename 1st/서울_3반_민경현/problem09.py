############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_number_sum(word):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    num_sum = 0
    num_string = ''
    # 합을 구하기 위해 변수값 선언.
    for i in range(len(word)):
        if word[i].isdigit() == True:
            num_string += word[i]
            # word의 i번째 값이 숫자라면, num_string에 word의 i번째 값 추가.
            if i==(len(word)-1):
                num_sum += int(num_string)
            # 만약 i가 word의 마지막 글자라면, 현재까지의 숫자 string을 num_sum에 추가
        elif num_string != '': 
            # num_string이 빈칸이 아닐 경우를 추가하지 않으면 오류 발생.
            num_sum += int(num_string) 
            # 이어지는 글자가 숫자가 아닌 경우, 현재까지의 숫자를 num_sum에 추가.
            num_string =''
            # num_string 초기화
    return num_sum



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_number_sum('ab123cd45ef6'))     # 174
print(calculate_number_sum('0a1s2d3f4'))        # 10
print(calculate_number_sum('ssafy10gi2good4560')) # 4572
#####################################################
