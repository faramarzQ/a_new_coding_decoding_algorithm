import math

def do(base_table, string):
    """encrypt the given string using the base table letters

    Args:
        base_table ([dict]): [maps letters to integers]
        string ([string]): [the string given to encode]

    Returns:
        [list]: [encrypted 2d array]
    """

    # convert the given string to array of integers
    list_of_integers = ConvertStringToInteger(base_table, string)

    # create matrix from mapped list
    matrix = createMatrix(base_table, list_of_integers)

    #split the matrix into blocks of size 4
    blocks = splitMatrix(matrix)

    # calculate determinant of each block
    determinants = calculateDeterminantOfBlocks(blocks)

    # create the final encoded matrix
    final_matrix = makeFinalMatrix(determinants, blocks)

    return final_matrix
pass

def ConvertStringToInteger(base_table, given_string):
    """convert the given string into array of integers using the base table

    Args:
        base_table ([dict]): [maps letters to integers]
        given_string ([string]): [the string given to encode]

    Returns:
        [list]: [list of mapped chars of string into integers]
    """

    # blocks count is the number of divided blocks in the matrix, paper mentioned it as 'n'
    temp = math.ceil(math.sqrt(len(given_string)))
    if( temp % 2  == 1):
        temp += 1
    blocks_count = int(pow(temp/2, 2))

    # calculating the b variable, mentioned in the paper
    if(blocks_count <= 3):
        n = 3
    else:
        n = blocks_count

    # replace spaces with zeros
    given_string = given_string.replace(' ', '0')

    letters = list(given_string)

    # map letters to their integers
    for i in range(len(letters)):
        if(letters[i] in base_table):
            # add b to each value of the base table
            letters[i] = base_table[letters[i]] + n

    return letters
pass

def createMatrix(base_table, integer_list):
    """create the n*n matrix from the list of integers

    Args:
        base_table ([dict]): [maps letters to integers]
        integer_list ([list]): [list of mapped string into integers]

    Returns:
        [list]: [2d matrix]
    """

    letters = list(integer_list)

    # blocks count is the number of divided blocks in the matrix, paper mentioned it as 'n'
    item_per_row = math.ceil(math.sqrt(len(integer_list)))
    if( item_per_row % 2  == 1):
        item_per_row += 1
    blocks_count = int(pow(item_per_row/2, 2))

    # calculating the b variable, mentioned in the paper
    if(blocks_count <= 3):
        n = 3
    else:
        n = blocks_count

    # making the 2d matrix, filling it with zeros (mapped value of it), putting list of mapped char in it
    matrix = [ [ (base_table['0']+n) for i in range(item_per_row) ] for j in range(item_per_row) ]
    for i in range(item_per_row):
        for j in range(item_per_row):
            if(len(letters) > 0):
                letter = letters.pop(0)
                if( letter != ' '):
                    matrix[i][j] = letter

    return matrix
pass

def splitMatrix(matrix):
    """split matrix into blocks of size 4

    Args:
        matrix ([list]): [2d matrix]

    Returns:
        [list]: [2d matrix of blocks]
    """

    blocks_count = int(pow(len(matrix)/2, 2))

    # creating 2d list of blocks filled with zeros, finding proper block for each item in the matrix
    blocks =[ [ [ 0 for i in range(2) ] for j in range(2) ]  for j in range(blocks_count) ]

    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):

            row_of_block = (i - (i % 2)) / 2
            col_of_block = (j - (j % 2)) / 2
            position_of_block = int((row_of_block * math.ceil(math.sqrt(blocks_count)) ) + col_of_block)
            block_row = int(i % 2)
            block_col = int(j % 2)
            blocks[position_of_block][block_row][block_col] = matrix[i][j]

    return blocks
pass

def calculateDeterminantOfBlocks(blocks):
    """calculating determinant of each block

    Args:
        blocks ([list]): [list of blocks]

    Returns:
        [list]: [determinant of each block]
    """

    determinants =[0]*len(blocks)

    # for each block, calculate the determinant
    for i in range(len(blocks)):
        determinants[i] = blocks[i][0][0]*blocks[i][1][1] - blocks[i][0][1]*blocks[i][1][0]

    return determinants
pass

def makeFinalMatrix(determinants, blocks):
    """create final encoded matrix from blocks and determinants

    Args:
        determinants ([list]): [a list of determinants of each blocks]
        blocks ([list]): [2d array of blocks]

    Returns:
        [list]: [2d encoded matrix]
    """

    # crete and fill the 2d matrix and encode the values in it
    final_matrix = [ [ 0 for i in range(4) ] for j in range(len(blocks)) ]
    for i in range(len(blocks)):
        final_matrix[i][0] = determinants[i]
        final_matrix[i][1] = blocks[i][0][0]
        final_matrix[i][2] = blocks[i][0][1]
        final_matrix[i][3] = blocks[i][1][1]

    return final_matrix
pass
