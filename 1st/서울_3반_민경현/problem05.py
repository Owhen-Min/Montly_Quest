############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 set을 사용하지 않습니다.
def remove_duplicates(lst):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    unique_list = []
    # 빈 리스트 선언
    for item in lst:
        if item not in unique_list:
            unique_list.append(item) 
        # lst를 선회하며 lst의 아이템이 unique_list에 존재하지 않을 경우, item을 unique_list에 추가한다.
    return unique_list


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(remove_duplicates([4, 5, 6, 4, 3, 2, 1, 2, 3]))  # [4, 5, 6, 3, 2, 1]
print(remove_duplicates(['a', 'b', 'c', 'a', 'd', 'b']))  # ['a', 'b', 'c', 'd']
print(remove_duplicates([4, 5, 'a', 4, 'b', 2, 'a', 3, 2, 3]))  # [4, 5, 'a', 'b', 2, 3]