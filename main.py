"""
Challenge 1:
    Make a function that receive as parameter a list, and return the same list ordered ascendat
"""
def order_number_list(number_list:int):
    for i in range(len(number_list)):
        for index in range(0, len(number_list) -i -1):
            if number_list[index] > number_list[index+1]:
                prev_number = number_list[index]
                number_list[index] = number_list[index+1]
                number_list[index+1] = prev_number
    return number_list

"""
Challenge 2:
    Make a function that receive as parameter a list, and return all duplicated elements
"""
def duplicate_list(array):
    result = []
    for index,original in enumerate(array):
        for i in range(1,len(array)-index):
            if original == array[index+i] and result.count(original) < 1:
                result.append(original)
    return result

"""
Challenge 3:
    Make a function that receive as parameter a list, and return thes same list but 1level lower,
    like this
    [1,2,3,4,[5,6],7,[8,9]] => [1,2,3,4,5,6,7,8,9]
"""
def remove_nest(array):
    result = []
    for element in array:
        if type(element) == list:
            for i in element:
                result.append(i)
        else:
            result.append(element)
    return result

"""
Challenge 4:
    Make a function that receive as parameter the number of colums of Pascal triangle, and return the triangle in nested arrays,
    like this,
    parameter = 3 => [[1], [1, 1], [1, 2, 1]]
"""
def pascal_triangle(number:int):
    first_array = []
    for i in range(number):
        second_array = []
        for j in range(i+1):
            if j == i or j == 0:
                second_array.append(1)
            else:
                result = first_array[i-1][j-1] + first_array[i-1][j]
                second_array.append(result)
        first_array.append(second_array)
    return first_array

# print(pascal_triangle(7))

# print(remove_nest([0,10,3,55,[5,[8,7],3], 4, 2, [1,3,4]]))

# print(duplicate_list(["ana", "paco", "javier", "paco"]))

# print(order_number_list([1,10,4,5,33,41,3,12,2]))