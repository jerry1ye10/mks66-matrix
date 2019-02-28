from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

matrix = new_matrix()
ident(matrix)
print("testing mulitplication")

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]

print("mult A,B")
matrix_mult(A,B)
print("printing A")
print_matrix(A)
print("")
print("printing B")
print_matrix(B)
print("")
print("mult B,A")
matrix_mult(B,A)
print("printing A")
print_matrix(A)
print("")
print("printing B")
print_matrix(B)
print("")
print("mult IDENT,A")
matrix_mult(matrix,A)
print("printing A")
print_matrix(A)

matrix = new_matrix()
add_edge(matrix, 250, 150, 0, 350, 150, 0)
add_edge(matrix, 350, 150, 0, 350, 250, 0)
add_edge(matrix, 350, 250, 0, 250, 250, 0)
add_edge(matrix, 250, 250, 0, 250, 150, 0)



draw_lines( matrix, screen, color )
display(screen)
