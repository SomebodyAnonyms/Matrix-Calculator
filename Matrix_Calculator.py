import random

Matrix_1_row, Matrix_1_column = 0, 0
Matrix_2_row, Matrix_2_column = 0, 0
Matrix_1, Matrix_2 = [], []
Number_range_1, Number_range_2 = 0, 0


Numbers_type = input("Numbers type >> Random(R) or Manually(M): ")
if Numbers_type == "R" or Numbers_type == "r":
    Number_range_1, Number_range_2 = int(input("Enter first range number: ")), int(input("Enter second range number: "))
    Matrix_1_row, Matrix_1_column = int(input("Matrix 1 row: ")), int(input("Matrix 1 column: "))
    Matrix_2_row, Matrix_2_column = int(input("Matrix 2 row: ")), int(input("Matrix 2 column: "))

    for i in range(Matrix_1_column * Matrix_1_row):
        Matrix_1.append(random.randint(Number_range_1, Number_range_2))
    for i in range(Matrix_2_column * Matrix_2_row):
        Matrix_2.append(random.randint(Number_range_1, Number_range_2))
elif Numbers_type == "M" or Numbers_type == "m":
    Matrix_1_row, Matrix_1_column = int(input("Matrix 1 row: ")), int(input("Matrix 1 column: "))
    Matrix_2_row, Matrix_2_column = int(input("Matrix 2 row: ")), int(input("Matrix 2 column: "))
    for i in range(Matrix_1_row * Matrix_1_column):
        Matrix_1.append(int(input("Matrix 1, Number " + str(i + 1) + ": ")))
    for i in range(Matrix_2_row * Matrix_2_column):
        Matrix_2.append(int(input("Matrix 2, Number " + str(i + 1) + ": ")))
else:
    print("")





def get_matrix(matrix_name, column_number, row_number):
    inserted_number_1 = 0
    for row in range(row_number):
        number = ""
        for column in range(column_number):
            if column_number == 1:
                number += "| " + str(matrix_name[inserted_number_1]) + " |"
            elif column == 0:
                number += "| " + str(matrix_name[inserted_number_1])
            elif column == column_number - 1:
                number += "  " + str(matrix_name[inserted_number_1]) + " |"
            else:
                number += "  " + str(matrix_name[inserted_number_1])
            inserted_number_1 += 1
        print(number)
get_matrix(Matrix_1, Matrix_1_column, Matrix_1_row)
print("")
get_matrix(Matrix_2, Matrix_2_column, Matrix_2_row)





def plus_matrix():
    matrix_answer = []
    for i in range(len(Matrix_1)):
        matrix_answer.append(Matrix_1[i] + Matrix_2[i])
    get_matrix(matrix_answer, Matrix_1_column, Matrix_1_row)
def minus_matrix():
    matrix_answer = []
    for i in range(len(Matrix_1)):
        matrix_answer.append(Matrix_1[i] - Matrix_2[i])
    get_matrix(matrix_answer, Matrix_1_column, Matrix_1_row)
def multiplication_matrix():
    matrix_1_int_1 = 0
    matrix_answer = []
    for a in range(Matrix_1_row):
        matrix_2_int_1 = 0
        for b in range(Matrix_2_column):
            sum_multiplication = 0
            matrix_2_int_2 = 0
            for c in range(matrix_1_int_1, matrix_1_int_1 + Matrix_1_column):
                sum_multiplication += Matrix_1[c] * Matrix_2[matrix_2_int_1 + matrix_2_int_2]
                matrix_2_int_2 += Matrix_2_column
            matrix_answer.append(sum_multiplication)
            matrix_2_int_1 += 1
        matrix_1_int_1 += Matrix_1_column
    get_matrix(matrix_answer, Matrix_2_column, Matrix_1_row)

print("\n")
Matrix_operation = input("Enter operation: ")

if Matrix_1_column == Matrix_2_column and Matrix_1_row == Matrix_2_row:
    if Matrix_operation == "+":
        plus_matrix()
    if Matrix_operation == "-":
        minus_matrix()
    elif Matrix_operation == "*":
        multiplication_matrix()
elif Matrix_1_column == Matrix_2_row:
    if Matrix_operation == "*":
        multiplication_matrix()
    else:
        print("The elements can't be match")
else:
    print("The elements can't be match")


input("\nPress enter to exit...")
