############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min, max, sorted 함수 리스트 메서드 sort 를 사용하지 않습니다.
def population_difference(population_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    max_pop = population_list[0]
    min_pop = population_list[0]
    # 비교를 위한 기준점을 잡기 위해 변수 선언. 해당 문제의 경우 0 미만의 인구수는 존재하지 않으므로 두 변수 모두 0으로 선언할 수 있지만, 다른 문제에서 실수하지 않게 해당 리스트의 첫 값으로 선언함.
    for pop in population_list:
        if pop > max_pop:
            max_pop = pop
        elif pop < min_pop:
            min_pop = pop
    # pop이 현재까지의 max_pop보다 큰 경우 max_pop의 값을 갱신하고, pop이 현재까지의 min_pop과 작은 경우 min_pop의 값을 갱신한다. pop이 max_pop보다 크면서 min_pop보다 작을 경우는 없기 때문에 elif로 작성.

    return max_pop - min_pop
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(population_difference([100, 200, 300, 400, 500]))  # 400
print(population_difference([50, 150, 250]))  # 200
print(population_difference([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # 90
#####################################################
