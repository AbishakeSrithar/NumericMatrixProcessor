import copy
def multiplyMatrixConstant():
    # Dimensions of First Matrix as string.
    my_dimensions_1 = input("Enter size of first matrix: ")
    my_dimensions_1 = my_dimensions_1.split()
    rows_1 = []

    # Storing First matrix as string.
    print("Enter matrix:")
    for _ in range(int(my_dimensions_1[0])):
        my_row = input()
        my_row = my_row.split()
        rows_1.append(my_row)

    # Storing our constant.
    CONSTANT = float(input("Enter constant: "))

    # Working out answer.
    ans = [[None]*int(my_dimensions_1[1]) for x in range(int(my_dimensions_1[0]))]
    for i in range(int(my_dimensions_1[0])):
        for j in range(int(my_dimensions_1[1])):
            ans[i][j] = float(rows_1[i][j]) * CONSTANT

    # Print ans in required format.
    final_ans = "" 
    for x in ans:
        for y in x:
            final_ans = f"{final_ans}{str(y)} "
        final_ans = f"{final_ans}\n"
    final_ans = f"The result is:\n{final_ans}"

    return final_ans

def addMatrices():
    # Dimensions of First Matrix as string.
    my_dimensions_1 = input("Enter size of first matrix: ")
    my_dimensions_1 = my_dimensions_1.split()
    rows_1 = []

    # Storing First matrix as string.
    print("Enter first matrix:")
    for _ in range(int(my_dimensions_1[0])):
        my_row = input()
        my_row = my_row.split()
        rows_1.append(my_row)

    # Dimensions of Second Matrix as string.
    my_dimensions_2 = input("Enter size of second matrix: ")
    my_dimensions_2 = my_dimensions_2.split()
    rows_2 = []

    # Storing second matrix as string.
    print("Enter second matrix:")
    for _ in range(int(my_dimensions_2[0])):
        my_row = input()
        my_row = my_row.split()
        rows_2.append(my_row)

    # If dimensions are not equal, print error.
    if my_dimensions_1 != my_dimensions_2:
        return "The operation cannot be performed.\n"

    else:
        # Create None nest list and fill with addition result.
        rows_3 = [[None]*int(my_dimensions_1[1]) for x in range(int(my_dimensions_1[0]))]
        for i in range(len(rows_1)):
            for j in range(len(rows_1[i])):
                rows_3[i][j] = float(rows_1[i][j]) + float(rows_2[i][j])
                if rows_3[i][j] % 1 == 0:
                    rows_3[i][j] = int(rows_3[i][j])
        # ans = " ".join(str(y) for x in rows_3 for y in x)
        ans = ""
        for x in rows_3:
            for y in x:
                ans = f"{ans}{str(y)} "
            ans = f"{ans}\n"
        ans = f"The result is:\n{ans}"

        return ans

def multiplyMatrices():
    # Dimensions of First Matrix as string.
    my_dimensions_1 = input("Enter size of first matrix: ")
    my_dimensions_1 = my_dimensions_1.split()
    rows_1 = []

    # Storing First matrix as string.
    print("Enter first matrix:")
    for _ in range(int(my_dimensions_1[0])):
        my_row = input()
        my_row = my_row.split()
        rows_1.append(my_row)

    # Dimensions of Second Matrix as string.
    my_dimensions_2 = input("Enter size of second matrix: ")
    my_dimensions_2 = my_dimensions_2.split()
    rows_2 = []

    # Storing second matrix as string.
    print("Enter second matrix:")
    for _ in range(int(my_dimensions_2[0])):
        my_row = input()
        my_row = my_row.split()
        rows_2.append(my_row)

    # If dimensions are not equal, print error.
    if my_dimensions_1[1] != my_dimensions_2[0]:
        return "The operation cannot be performed.\n"
    
    else:
        rows_3 = [[None]*int(my_dimensions_2[1]) for x in range(int(my_dimensions_1[0]))]
        for i in range(len(rows_1)):
            for j in range(len(rows_2[0])):
                rows_3[i][j] = 0
                for k in range(len(rows_1[0])):
                    rows_3[i][j] += float(rows_1[i][k]) * float(rows_2[k][j])
                if rows_3[i][j] % 1 == 0:
                    rows_3[i][j] = int(rows_3[i][j])

        # ans = " ".join(str(y) for x in rows_3 for y in x)
        ans = ""
        for x in rows_3:
            for y in x:
                ans = f"{ans}{str(y)} "
            ans = f"{ans}\n"
        ans = f"The result is:\n{ans}"

        return ans

def transpose1():
    # Dimensions of First Matrix as string.
    my_dimensions_1 = input("Enter matrix size: ")
    my_dimensions_1 = my_dimensions_1.split()
    rows_1 = []

    # Storing First matrix as string.
    print("Enter matrix:")
    for _ in range(int(my_dimensions_1[0])):
        my_row = input()
        my_row = my_row.split()
        rows_1.append(my_row)

    rows_3 = [[None]*int(my_dimensions_1[0]) for x in range(int(my_dimensions_1[1]))]
    for i in range(int(my_dimensions_1[1])):
        for j in range(int(my_dimensions_1[0])):
            rows_3[i][j] =float(rows_1[j][i])
            if rows_3[i][j] % 1 == 0:
                rows_3[i][j] = int(rows_3[i][j])
    
    # ans = " ".join(str(y) for x in rows_3 for y in x)
    ans = ""
    for x in rows_3:
        for y in x:
            ans = f"{ans}{str(y)} "
        ans = f"{ans}\n"
    ans = f"The result is:\n{ans}"

    return ans

def transpose2():
    # Dimensions of First Matrix as string.
    my_dimensions_1 = input("Enter matrix size: ")
    my_dimensions_1 = my_dimensions_1.split()
    rows_1 = []

    # Storing First matrix as string.
    print("Enter matrix:")
    for _ in range(int(my_dimensions_1[0])):
        my_row = input()
        my_row = my_row.split()
        rows_1.append(my_row)

    rows_3 = [[None]*int(my_dimensions_1[0]) for x in range(int(my_dimensions_1[1]))]
    for i in range(int(my_dimensions_1[1])):
        for j in range(int(my_dimensions_1[0])):
            rows_3[i][j] =float(rows_1[int(my_dimensions_1[0]) - j - 1][int(my_dimensions_1[1]) - i - 1])
            if rows_3[i][j] % 1 == 0:
                rows_3[i][j] = int(rows_3[i][j])
    
    # ans = " ".join(str(y) for x in rows_3 for y in x)
    ans = ""
    for x in rows_3:
        for y in x:
            ans = f"{ans}{str(y)} "
        ans = f"{ans}\n"
    ans = f"The result is:\n{ans}"

    return ans

def transpose3():
    # Dimensions of First Matrix as string.
    my_dimensions_1 = input("Enter matrix size: ")
    my_dimensions_1 = my_dimensions_1.split()
    rows_1 = []

    # Storing First matrix as string.
    print("Enter matrix:")
    for _ in range(int(my_dimensions_1[0])):
        my_row = input()
        my_row = my_row.split()
        rows_1.append(my_row)

    rows_3 = [[None]*int(my_dimensions_1[1]) for x in range(int(my_dimensions_1[0]))]
    for i in range(int(my_dimensions_1[0])):
        for j in range(int(my_dimensions_1[1])):
            rows_3[i][j] =float(rows_1[i][int(my_dimensions_1[1]) - j - 1])
            if rows_3[i][j] % 1 == 0:
                rows_3[i][j] = int(rows_3[i][j])
    
    # ans = " ".join(str(y) for x in rows_3 for y in x)
    ans = ""
    for x in rows_3:
        for y in x:
            ans = f"{ans}{str(y)} "
        ans = f"{ans}\n"
    ans = f"The result is:\n{ans}"

    return ans
  

def transpose4():
    # Dimensions of First Matrix as string.
    my_dimensions_1 = input("Enter matrix size: ")
    my_dimensions_1 = my_dimensions_1.split()
    rows_1 = []

    # Storing First matrix as string.
    print("Enter matrix:")
    for _ in range(int(my_dimensions_1[0])):
        my_row = input()
        my_row = my_row.split()
        rows_1.append(my_row)

    rows_3 = [[None]*int(my_dimensions_1[1]) for x in range(int(my_dimensions_1[0]))]
    for i in range(int(my_dimensions_1[0])):
        for j in range(int(my_dimensions_1[1])):
            rows_3[i][j] =float(rows_1[int(my_dimensions_1[0]) - i - 1][j])
            if rows_3[i][j] % 1 == 0:
                rows_3[i][j] = int(rows_3[i][j])
    
    # ans = " ".join(str(y) for x in rows_3 for y in x)
    ans = ""
    for x in rows_3:
        for y in x:
            ans = f"{ans}{str(y)} "
        ans = f"{ans}\n"
    ans = f"The result is:\n{ans}"

    return ans

def determinant():
    # Dimensions of First Matrix as string.
    my_dimensions_1 = input("Enter matrix size: ")
    my_dimensions_1 = my_dimensions_1.split()
    rows_1 = []

    if my_dimensions_1[0] != my_dimensions_1[1]:
        return "Determinant can only be found for square matrices"

    # Storing First matrix as floats.
    print("Enter matrix:")
    for _ in range(int(my_dimensions_1[0])):
        my_row = input()
        my_row = my_row.split()
        rows_1.append(list(map(float, my_row)))
    
    # Sends it to our recursive function.
    ans = det(rows_1, int(my_dimensions_1[0]))
    if ans % 1 == 0:
        return int(ans)
    return ans

def det(matrix, n):
    sum = 0
    # Corner case.
    if n == 1:
        return matrix[0][0]
    # Base case.
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Recursion
    for i in range(n):
        new_matrix = copy.deepcopy(matrix)
        new_matrix.pop(0)
        for j in range(n - 1):
            new_matrix[j].pop(i)
        sum += matrix[0][i] * ((-1) ** i) * det(new_matrix, n - 1)
    return sum
        

def main():
    while True:
        options = input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n0. Exit\nYour choice: ")
        if options == "1":
            print(addMatrices())
        elif options == "2":
            print(multiplyMatrixConstant())
        elif options == "3":
            print(multiplyMatrices())
        elif options == "4":
            transpose_options = input("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice: ")
            if transpose_options == "1":
                print(transpose1())
            if transpose_options == "2":
                print(transpose2())
            if transpose_options == "3":
                print(transpose3())
            if transpose_options == "4":
                print(transpose4())
        elif options == "5":
            print(determinant())
        elif options == "0":
            break


main()