def do(base_table, matrix):
    q_matrix = calculateQMatrix(matrix)
    first_element_matrix = calculateFirstElementMatrix(q_matrix, matrix)
    second_element_matrix = calculateSecondElementMatrix(q_matrix, matrix)
    findLatentIndexes(matrix, first_element_matrix, second_element_matrix, q_matrix)

def calculateQMatrix(matrix):
    n = len(matrix)
    q_matrix = [0]*4
    q_matrix = [fibonacci(n+1), fibonacci(n), fibonacci(n), fibonacci(n-1)]
    return q_matrix

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calculateFirstElementMatrix(q_matrix, matrix):
    element_matrix = [0]*len(matrix)
    for i in range(len(element_matrix)):
        element_matrix[i] = q_matrix[0]*matrix[i][0] + q_matrix[2]*matrix[i][1]

    return element_matrix

def calculateSecondElementMatrix(q_matrix, matrix):
    element_matrix = [0]*len(matrix)
    for i in range(len(element_matrix)):
        element_matrix[i] = q_matrix[1]*matrix[i][0] + q_matrix[3]*matrix[i][1]

    return element_matrix

def findLatentIndexes(matrix, first_element_matrix, second_element_matrix, q_matrix):
    n = len(matrix)
    latent_indexes = [0]*4
    for i in range(len(matrix)):
        temp_x = 0
        while True:
            if(pow(-1, n)*matrix[i][0] == ( first_element_matrix[i]*( q_matrix[1]*temp_x +  q_matrix[3]*matrix[i][3]) ) - ( second_element_matrix[i]*( q_matrix[0]*temp_x + q_matrix[2]*matrix[i][3] ) ) ):
                print('s')

            print(temp_x)
            temp_x +=1
