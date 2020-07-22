# Dimensions of First Matrix as string.
my_dimensions_1 = input()
my_dimensions_1 = my_dimensions_1.split()
rows_1 = []

# Storing First matrix as string.
for _ in range(int(my_dimensions_1[0])):
    my_row = input()
    my_row = my_row.split()
    rows_1.append(my_row)

# Dimensions of Second Matrix as string.
my_dimensions_2 = input()
my_dimensions_2 = my_dimensions_2.split()
rows_2 = []

# Storing second matrix as string.
for _ in range(int(my_dimensions_2[0])):
    my_row = input()
    my_row = my_row.split()
    rows_2.append(my_row)

# If dimensions are not equal, print error.
if my_dimensions_1 != my_dimensions_2:
    print("ERROR")

else:
    # Create None nest list and fill with addition result.
    rows_3 = [[None]*int(my_dimensions_1[1]) for x in range(int(my_dimensions_1[0]))]
    for i in range(len(rows_1)):
        for j in range(len(rows_1[i])):
            rows_3[i][j] = int(rows_1[i][j]) + int(rows_2[i][j])
    # ans = " ".join(str(y) for x in rows_3 for y in x)
    ans = ""
    for x in rows_3:
        for y in x:
            ans = f"{ans}{str(y)} "
        ans = f"{ans}\n"

    print(ans)

