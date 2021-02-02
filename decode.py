import math

def do(base_table, matrix):

    q_matrix = calculateQMatrix(matrix)
    first_element_matrix = calculateFirstElementMatrix(q_matrix, matrix)
    second_element_matrix = calculateSecondElementMatrix(q_matrix, matrix)
    latent_indexes = findLatentIndexes(matrix, first_element_matrix, second_element_matrix, q_matrix)
    reshaped_blocks = reshapeBlocksWithLatentIndexes(latent_indexes, matrix)
    reconstructed_matrix = reconstructMatrix(base_table, reshaped_blocks)
    string = convertNumberMatrixToString(reconstructMatrix)

def calculateQMatrix(matrix):

    if(len(matrix) <= 3):
        n = 3
    else:
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
        element_matrix[i] = q_matrix[0]*matrix[i][1] + q_matrix[2]*matrix[i][2]

    return element_matrix

def calculateSecondElementMatrix(q_matrix, matrix):
    element_matrix = [0]*len(matrix)
    for i in range(len(element_matrix)):
        element_matrix[i] = q_matrix[1]*matrix[i][1] + q_matrix[3]*matrix[i][2]

    return element_matrix

def findLatentIndexes(matrix, first_element_matrix, second_element_matrix, q_matrix):
    n = len(matrix)
    latent_indexes = [0]*len(matrix)
    for i in range(len(matrix)):
        temp_x = 0
        while True:
            if(pow(-1, n)*matrix[i][0] == ( first_element_matrix[i]*( q_matrix[1]*temp_x +  q_matrix[3]*matrix[i][3]) ) - ( second_element_matrix[i]*( q_matrix[0]*temp_x + q_matrix[2]*matrix[i][3] ) ) ):
                break;
            temp_x +=1
        latent_indexes[i] = temp_x

    return latent_indexes

def reshapeBlocksWithLatentIndexes(latent_indexes, matrix):
    reshaped_blocks = [ [ 0 for i in range(len(matrix[0])) ] for j in range(len(matrix)) ]

    for i in range(len(matrix)):
        reshaped_blocks[i][0] = matrix[i][1]
        reshaped_blocks[i][1] = matrix[i][2]
        reshaped_blocks[i][2] = latent_indexes[i]
        reshaped_blocks[i][3] = matrix[i][3]

    return reshaped_blocks

def reconstructMatrix(base_table, reshaped_blocks):

    blocks_per_row = int(math.sqrt(len(reshaped_blocks)))
    blocks = blocks_per_row * 2

    reconstructed_matrix = [ [ (base_table['0']+blocks) for i in range(blocks) ] for j in range(blocks) ]

    for i in range(len(reshaped_blocks)):
        for j in range(4):
            row = int( 2*math.floor(i/blocks_per_row) + math.floor(j/2) )
            col = int( 2*math.floor(i%blocks_per_row) + math.floor(j%2) )
            reconstructed_matrix[row][col] = reshaped_blocks[i][j]

    return reconstructed_matrix

