import math

def do(base_table, matrix):
    """encoded the given matrix into a string

    Args:
        base_table ([dict]): [maps letters to integers]
        matrix ([list]): [2d encoded matrix]

    Returns:
        [string]: [decoded string]
    """
    # print(fibonacci(34))
    # find the Q-matrix for the problem
    q_matrix = calculateQMatrix(matrix)
    # calculate the E1 matrix
    first_element_matrix = calculateFirstElementMatrix(q_matrix, matrix)

    # calculate the E2 matrix
    second_element_matrix = calculateSecondElementMatrix(q_matrix, matrix)

    # find the latent indexes in the encoded matrix
    latent_indexes = findLatentIndexes(matrix, first_element_matrix, second_element_matrix, q_matrix)

    # reshape each blocks using the latent indexes
    reshaped_blocks = reshapeBlocksWithLatentIndexes(latent_indexes, matrix)

    # reconstruct the matrix of integers using the reshaped blocks
    reconstructed_matrix = reconstructMatrix(base_table, reshaped_blocks)

    # map back the integers into string of chars
    string = convertNumberMatrixToString(base_table, reconstructed_matrix)

    return string
pass

def calculateQMatrix(matrix):
    """calculates the Q-Matrix for the problem

    Args:
        matrix ([list]): [2d encoded matrix]

    Returns:
        [list]: [q-matrix]
    """

    # the condition mentioned in the paper
    if(len(matrix) <= 3):
        n = 3
    else:
        n = len(matrix)

    solved_fibonacci = {}
    fibonacci(n+1, solved_fibonacci)

    # create and fill the matrix with zeros
    q_matrix = [0]*4
    q_matrix = [solved_fibonacci[n+1], solved_fibonacci[n], solved_fibonacci[n], solved_fibonacci[n-1]]

    return q_matrix
pass

def fibonacci(n, solved_fibonacci):
    """a recursive fibonacci function using dynamic programming

    Args:
        n ([integer]): [an integer]

    Returns:
        [integer]: [fibonacci of the given integer]
    """
    if n == 1 or n == 2:
        return 1
    else:
        if(n in solved_fibonacci):
            return solved_fibonacci[n]
        else:
            solved_fibonacci[n] = fibonacci(n-1, solved_fibonacci) + fibonacci(n-2, solved_fibonacci)
            return solved_fibonacci[n]
pass

def calculateFirstElementMatrix(q_matrix, matrix):
    """finds the E1 matrix of the encoded matrix mentioned in the paper

    Args:
        q_matrix ([list]): [Q-matrix]
        matrix ([list]): [the encoded matrix]

    Returns:
        [list]: [the E1 matrix]
    """
    # create and fill the matrix with zeros, then calculate it using the mentioned formula
    element_matrix = [0]*len(matrix)
    for i in range(len(element_matrix)):
        element_matrix[i] = q_matrix[0]*matrix[i][1] + q_matrix[2]*matrix[i][2]

    return element_matrix
pass

def calculateSecondElementMatrix(q_matrix, matrix):
    """finds the E2 matrix of the encoded matrix mentioned in the paper

    Args:
        q_matrix ([list]): [Q-matrix]
        matrix ([list]): [the encoded matrix]

    Returns:
        [list]: [the E2 matrix]
    """
    # create and fill the matrix with zeros, then calculate it using the mentioned formula
    element_matrix = [0]*len(matrix)
    for i in range(len(element_matrix)):
        element_matrix[i] = q_matrix[1]*matrix[i][1] + q_matrix[3]*matrix[i][2]

    return element_matrix
pass

def findLatentIndexes(matrix, first_element_matrix, second_element_matrix, q_matrix):
    """find latent indexes in the blocks using the mentioned formula in the paper

    Args:
        matrix ([list]): [the encoded matrix]
        first_element_matrix ([list]): [E1 matrix]
        second_element_matrix ([list]): [E2 matrix]
        q_matrix ([list]): [Q-matrix]

    Returns:
        [list]: [list of latent indexes for each block]
    """

    # create and fill a list with zeros, the calculate the latent indexes using the formula
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
pass

def reshapeBlocksWithLatentIndexes(latent_indexes, matrix):
    """reshape the encoded matrix and put the latent indexes in their proper positions

    Args:
        latent_indexes ([list]): [list of latent indexes for each blocks]
        matrix ([list]): [2d encoded matrix]

    Returns:
        [list]: [2d matrix, reshaped blocks]
    """

    # create and fill a 2d matrix, and reshape it
    reshaped_blocks = [ [ 0 for i in range(len(matrix[0])) ] for j in range(len(matrix)) ]
    for i in range(len(matrix)):
        reshaped_blocks[i][0] = matrix[i][1]
        reshaped_blocks[i][1] = matrix[i][2]
        reshaped_blocks[i][2] = latent_indexes[i]
        reshaped_blocks[i][3] = matrix[i][3]

    return reshaped_blocks
pass

def reconstructMatrix(base_table, reshaped_blocks):
    """reconstruct the matrix by reshaped blocks

    Args:
        base_table ([dict]): [maps letters to integers]
        reshaped_blocks ([list]): [reshaped blocks]

    Returns:
        [list]: [the reconstruced 2d matrix]
    """
    blocks_per_row = int(math.sqrt(len(reshaped_blocks)))
    blocks = blocks_per_row * 2

    # create and fill a matrix with zeros, put reshaped blocks in their proper position
    reconstructed_matrix = [ [ (base_table['0']+blocks) for i in range(blocks) ] for j in range(blocks) ]
    for i in range(len(reshaped_blocks)):
        for j in range(4):
            row = int( 2*math.floor(i/blocks_per_row) + math.floor(j/2) )
            col = int( 2*math.floor(i%blocks_per_row) + math.floor(j%2) )
            reconstructed_matrix[row][col] = reshaped_blocks[i][j]

    return reconstructed_matrix
pass

def convertNumberMatrixToString(base_table, matrix):
    """mapp the reconstruced matrix of integers into characters using the base table

    Args:
        base_table ([dict]): [maps letters to integers]
        [list]: [the reconstruced 2d matrix]

    Returns:
        [string]: [decoded string]
    """
    # calculate n variable mentioned in the paper
    # n = math.ceil(math.sqrt(len(matrix))*2)

    blocks_count = int(pow(len(matrix)/2, 2))
    if(blocks_count <= 3):
        n = 3
    else:
        n = blocks_count

    # declare and map back the integers in matrix to string of characters
    string = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            string += str(list(base_table.keys())[list(base_table.values()).index( matrix[i][j] - n )])

    # replace the zeros with spaces
    string = string.replace('0', ' ')

    return string
pass