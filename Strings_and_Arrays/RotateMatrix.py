__author__ = 'vokidah'

'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
'''

def rotate_matrix(arr, n):
     for i in range(0, int(n/2)):
         for j in range(i, n-i-1):
             temp = arr[i][j]
             arr[i][j] = arr[n-j-1][i]
             arr[n-j-1][i] = arr[n-i-1][n-j-1]
             arr[n-i-1][n-j-1] = arr[j][n-i-1]
             arr[j][n-i-1] = temp
     for each in arr:
         print(each)

array = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15 ,16]]
rotate_matrix(array, len(array))
print()
array = [[1,2],
         [3,4]]
rotate_matrix(array, len(array))
print()
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
rotate_matrix(array, len(array))
