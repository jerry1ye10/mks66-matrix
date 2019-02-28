"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for e in range(len(matrix[0])):
        for r in range(len(matrix)):
            s += str(matrix[r][e]) + ' '
        s += '\n'
    print(s)
#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(len(matrix)):
        for i in range(len(matrix[0])):
            if i == x:
                matrix[x][i] = 1
            else:
                matrix[x][i] = 0


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    holder = new_matrix(cols=len(m2))
    for r in range(len(m2)):
        for c in range(len(m1[0])):
            for x in range(len(m1)):
                holder[r][c] += m2[r][x] * m1[x][c]
    for r in range(len(holder)):
        for c in range(len(holder[0])):
            m2[r][c] = holder[r][c]



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
