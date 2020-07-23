# Not complete, deal with floats and integer inputs in transpose and other functions.
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
            rows_3[i][j] =int(rows_1[j][i])
    
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
            rows_3[i][j] =int(rows_1[int(my_dimensions_1[0]) - j - 1][int(my_dimensions_1[1]) - i - 1])
    
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
            rows_3[i][j] =int(rows_1[i][int(my_dimensions_1[1]) - j - 1])
    
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
            rows_3[i][j] =int(rows_1[int(my_dimensions_1[0]) - i - 1][j])
    
    # ans = " ".join(str(y) for x in rows_3 for y in x)
    ans = ""
    for x in rows_3:
        for y in x:
            ans = f"{ans}{str(y)} "
        ans = f"{ans}\n"
    ans = f"The result is:\n{ans}"

    return ans

def main():
    while True:
        options = input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit\nYour choice: ")
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
        elif options == "0":
            break


main()