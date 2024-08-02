# 보물의 가격 표
treasure_prices = {
    "gold": 100,
    "silver": 50,
    "diamond": 200,
    "ruby": 150,
    "emerald": 120,
    "sapphire": 180,
    "pearl": 80,
    "coin": 1
}

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_total_value(treasure_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    t_value = 0
    # 총가치 (total value)를 구하기 위한 초기값 변수 0 선언.
    for trea in treasure_list:
        t_value += treasure_prices[trea]
        # treasure_list 안의 값 trea마다, treasure_prices에서 키값으로 value를 호출하여 t_value에 더해준다.

    return t_value
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_total_value(["gold", "silver", "diamond", "gold", "silver"]))  # 500
print(calculate_total_value(["pearl"]))  # 80
#####################################################
