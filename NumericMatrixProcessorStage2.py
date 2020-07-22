# Dimensions of First Matrix as string.
my_dimensions_1 = input()
my_dimensions_1 = my_dimensions_1.split()
rows_1 = []

# Storing First matrix as string.
for _ in range(int(my_dimensions_1[0])):
    my_row = input()
    my_row = my_row.split()
    rows_1.append(my_row)

# Storing our constant.
CONSTANT = int(input())

# Working out answer.
ans = [[None]*int(my_dimensions_1[1]) for x in range(int(my_dimensions_1[0]))]
for i in range(int(my_dimensions_1[0])):
    for j in range(int(my_dimensions_1[1])):
        ans[i][j] = int(rows_1[i][j]) * CONSTANT

# Print ans in required format.
final_ans = "" 
for x in ans:
    for y in x:
        final_ans = f"{final_ans}{str(y)} "
    final_ans = f"{final_ans}\n"

print(final_ans)

