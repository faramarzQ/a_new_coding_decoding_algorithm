
import encode
import decode

base_table = {'A':12, 'a':13, 'B':14, 'b':15, 'C':16, 'c':17, 'D':18, 'd':19, 'E':20, 'e':21, 'F':22, 'f':23, 'G':24, 'g':25, 'H':26, 'h':27, 'I':28, 'i':29, 'J':30, 'j':31, 'K':32, 'k':33, 'L':34, 'l':35, 'M':36, 'm':37, 'N':38, 'n':39, 'O':40, 'o':41, 'P':42, 'p':43, 'Q':44, 'q':45, 'R':46, 'r':47, 'S':48, 's':49, 'T':50, 't':51, 'U':52, 'u':53, 'V':54, 'v':55, 'W':56, 'w':57, 'X':58, 'x':58, 'Y':59, 'y':60, 'Z':61,'z':62}

string = "hello world"
matrix = encode.do(base_table, string)

string = decode.do(base_table, matrix)
