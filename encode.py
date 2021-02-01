import math
import numpy

def do(base_table, string):
    converted_string = convertStringToInteger(base_table, string)
    string_matrix = createStringMatrix(base_table, converted_string)
    print(string_matrix)
    blocks = splitStringMatrix(string_matrix)
    determinants = calculateDeterminantOfBlocks(blocks)

    final_matrix = makeFinalMatrix(determinants, blocks)

    return final_matrix
"""
create the init matrix of the given string
"""
def createStringMatrix(base_table, given_string):
    letters = list(given_string)

    blocks_count = math.ceil(math.sqrt(len(given_string)))
    if( blocks_count % 2  == 1):
        blocks_count += 1

    matrix = [ [ 0 for i in range(blocks_count) ] for j in range(blocks_count) ]
    print(given_string)
    for i in range(blocks_count):
        for j in range(blocks_count):
            if(len(letters) > 0):
                letter = letters.pop(0)
                if( letter != ' '):
                    matrix[i][j] = letter

    return matrix

def splitStringMatrix(matrix):
    blocks_count = pow(int(len(matrix) / 2), 2)

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

def convertStringToInteger(base_table, given_string):
    # n is the variable named by the paper
    n = math.ceil(math.sqrt(len(given_string)))

    # a simple condition to bind the n variable
    if(n <= 3):
        b = 3
    else:
        b = n

    letters = list(given_string)

    # map letters to their number
    for i in range(len(letters)):
        if(letters[i] in base_table):
            if(letters[i] == ''):
                continue
            letters[i] = base_table[letters[i]] + b
    print(letters)
    return letters

def calculateDeterminantOfBlocks(blocks):
    determinants =[0]*len(blocks)

    # for each block, calculate the determinant
    for i in range(len(blocks)):
        determinants[i] = blocks[i][0][0]*blocks[i][1][1] - blocks[i][0][1]*blocks[i][1][0]

    return determinants

def makeFinalMatrix(determinants, blocks):
    final_matrix = [ [ 0 for i in range(4) ] for j in range(len(blocks)) ]

    for i in range(len(blocks)):
        final_matrix[i][0] = determinants[i]
        final_matrix[i][1] = blocks[i][0][0]
        final_matrix[i][2] = blocks[i][0][1]
        final_matrix[i][3] = blocks[i][1][1]

    return final_matrix
