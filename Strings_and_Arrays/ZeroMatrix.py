__author__ = 'vokidah'

'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
'''



def zero_matrix(matrix):
    for each in matrix:
        print(each)
    j = []
    for array in matrix:
        flag = False
        for i in range(0, len(array)):
            if array[i] == 0:
                flag = True
                j.append(i)
        if flag:
            for i in range(0, len(array)):
                array[i] = 0
    for each in j:
        for i in range(0, len(matrix)):
            matrix[i][each] = 0
    print()
    for each in matrix:
        print(each)

zero_matrix([[1,2,3,4],[0,6,0,8],[9,10,11,12]])