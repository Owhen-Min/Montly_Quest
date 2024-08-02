# ############## 주의 ##############
# # 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# # 리스트 메서드 count 를 사용하지 않습니다.
# def count_treasures(treasure_list):
#     # 여기에 코드를 작성하여 함수를 완성합니다.
#     trea_dict = {}
#     # 리턴을 위한 빈 딕셔너리 선언.
#     for treasure in treasure_list:
#         if treasure in trea_dict:
#             trea_dict[treasure] += 1
#         # treasure_list 안에 있는 값 treasure가 trea_dict에 있는 경우 기존의 value에 1을 더한다.
#         else: trea_dict[treasure] = 1
        
#         # treasure_list 안에 있는 값 treasure가 trea_dict에 없는 경우 treasure를 키로 설정하고 값을 1로 설정한다.

#     return trea_dict
    

# # 추가 테스트를 위한 코드 작성 가능
# # 예) print(함수명(인자))

# #####################################################
# # 아래 코드를 삭제하는 경우 
# # 모든 책임은 삭제한 본인에게 있습니다. 
# ############## 테스트 코드 삭제 금지 #################
# print(count_treasures(["gold", "silver", "diamond", "gold", "silver"]))  # {'gold': 2, 'silver': 2, 'diamond': 1}
# print(count_treasures(["pearl"]))  # {'pearl': 1}
# #####################################################
def count_treasures(treasure_list):
    dict = {}
    for key in treasure_list:
        if dict.get(key) == None:
            dict.update( {key : 1})
        else:
            dict.update({key : dict[key]+1})
    return dict

print(count_treasures(["gold", "silver", "diamond", "gold", "silver"]))  # {'gold': 2, 'silver': 2, 'diamond': 1}
print(count_treasures(["pearl"]))  # {'pearl': 1}