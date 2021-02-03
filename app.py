
import encode
import decode

base_table = {'0':-1, 'A':0, 'a':26, 'B':1, 'b':27, 'C':2, 'c':28, 'D':3, 'd':29, 'E':4, 'e':30, 'F':5, 'f':31, 'G':6, 'g':32, 'H':7, 'h':33, 'I':8, 'i':34, 'J':9, 'j':35, 'K':10, 'k':36, 'L':11, 'l':37, 'M':12, 'm':38, 'N':13, 'n':39, 'O':14, 'o':40, 'P':15, 'p':41, 'Q':16, 'q':42, 'R':17, 'r':43, 'S':18, 's':44, 'T':19, 't':45, 'U':20, 'u':46, 'V':21, 'v':47, 'W':22, 'w':48, 'X':23, 'x':49, 'Y':24, 'y':50, 'Z':25,'z':51}

string = "testing NUMBER OnE"

matrix = encode.do(base_table, string)
print(matrix)
string = decode.do(base_table, matrix)
print(string)
