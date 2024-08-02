############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    day = 0
    current_water = evaporation_amount
    # 물탱크를 가득 채웠는지의 기준은 물이 증발하기 이전인 물을 채운 이후. 따라서 첫 날 오후 기준부터로 계산하기 위해서는 evaporation_amount만큼을 보정해줘야 한다.
    while current_water < tank_capacity:
        # 현재 물의 양이 탱크보다 적을 경우 반복
        day += 1
        current_water += fill_amount-evaporation_amount
        # 현재의 물양에 채우는 양을 더하고 전날 증발한 양을 빼서 오후 시간 기준으로 총 물량을 계산한다.
    
    return day




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_days_to_fill_tank(100, 20, 5))  # 7
print(calculate_days_to_fill_tank(1000, 100, 10))  # 11
print(calculate_days_to_fill_tank(100, 10, 1))  # 11
#####################################################
