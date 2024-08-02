############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    N = len(matrix)
    max_num = matrix[0][0]
    max_position = []
    # 빈 변수 할당하기
    for i in range(N):
        for j in range(N):
            if(matrix[i][j] > max_num):
                max_num = matrix[i][j]
    # 가장 큰 숫자를 찾기
    for i in range(N):
        for j in range(N):
            if(matrix[i][j] == max_num):
                max_position.append([i,j])
    # 가장 큰 숫자의 위치를 리스트시켜 저장. 행이 우선적으로 적은 index부터 탐색하고, 열이 그 다음으로 적은 index부터 탐색하므로 index 0번을 호출할 경우 별도의 조작이 필요하지 않음.
    
    return max_position[0]




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################
