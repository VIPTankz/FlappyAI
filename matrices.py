
def calc(matrix1,matrix2):
    answer_matrix = []
    for k in range(len(matrix1)):
        temp_matrix = []
        for i in range(len(matrix2[0])):
            number = 0
            for j in range(len(matrix2)):
                number += matrix1[k][j]*matrix2[j][i]
            temp_matrix.append(number)
        answer_matrix.append(temp_matrix)
    return answer_matrix


if __name__ == "__main__": 
    matrix1 = [[1,2,3,4],[2,3,4,5]]
    matrix2 = [[1,2,3],[4,5,6],[2,3,4],[7,8,9]]

    print(calculate_matrix(matrix1,matrix2))
