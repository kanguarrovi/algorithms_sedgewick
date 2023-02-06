# 01 - Find the maximum of the list values

def maximum_of_list(a:list):
    max_item = a[0]
    for element in a:
        if element > max_item:
            max_item = element
    return max_item

# 02 - Compute the average of the list values

def average_list_values(a: list):
    a_length = len(a)
    sum = 0
    for element in a:
        sum += element
    average = sum / a_length
    return average

# 03 - Copy to another list (copy )

def copy_list(a:list):
    # Copy constructor
    # copy_of_a = a
    # return copy_of_a
    copy_of_a = list()
    for element in a:
        copy_of_a.append(element)
    return copy_of_a

# 04 - Reverse a list

def reverse(a:list):
    # return a[::-1]
    a_length = len(a)
    index = 0
    while index < a_length/2:
        temp = a[index]
        a[index] = a[a_length-1-index]
        a[a_length-1-index] = temp
        index += 1

# 05 - matrix-matrix multiplication

def multiply_matrices(a, b):

    rows_a = len(a)
    cols_b = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError

    result = [[0 for row in range(cols_b)] for col in range(rows_a)]

    for i in range(cols_a):
        for j in range(cols_b):
            for k in range(rows_b):
                result[i][j] += a[i][k] * b[k][j]

    return result







