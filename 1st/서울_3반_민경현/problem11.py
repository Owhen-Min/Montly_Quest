############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    N = len(matrix)
    # 문제에서 정사각 행렬이라고 주어졌으므로 len(matrix)를 가져와 N by N의 행렬로 생각할 수 있음.
    matrix_with_zero = []
    for i in range(N+2):
        ls = []
        for j in range(N+2):
            ls.append(0)
        matrix_with_zero.append(ls)
        # 주변 영역이 행열의 범위를 벗어나는 경우 해당 방향은 제외하는 대신 0을 씌워 값에 영향이 없고, 오류도 나지 않게 함.
    for i in range (N):
        for j in range(N):
            matrix_with_zero[i+1][j+1] = matrix[i][j]
            # matrix_with_zero의 가운데에 기존 matrix을 배치.

    
    max_sum = matrix_with_zero[0][1]+matrix_with_zero[1][1] + matrix_with_zero[2][1] + matrix_with_zero[1][0] + matrix_with_zero[1][2]
    # matrix가 음수로만 이루어져있을 경우 max_sum의 값을 0으로 설정했을 때 올바른 값이 나오지 않을 수 있음. 따라서 비교하려는 값의 제일 처음 값을 max_sum의 기준으로 놓음.
    
    for i in range(N):
        for j in range(N):
            sum = matrix_with_zero[i][j+1]+matrix_with_zero[i+1][j+1] + matrix_with_zero[i+2][j+1] + matrix_with_zero[i+1][j] + matrix_with_zero[i+1][j+2]
            # matrix_with_zero에서 십자 형태로 숫자를 더함.
            if sum > max_sum:
                max_sum = sum
            # 그 값들을 비교하여 가장 큰 값이 max_sum에 남아 있도록 조작.

    return max_sum




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

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
