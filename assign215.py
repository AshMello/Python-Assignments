#Assignment 1
names = ["Alex","John","Mary","Steve","John", "Steve"]
def remove_dupe(a):
    name_list = []
    for name in names:
        if name not in name_list:
            name_list.append(name)
    return name_list
print(remove_dupe(names))

#Assignment 2
numbers = [0, 1, 27, -18, 5]
def maximum(num):
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num
print(maximum(numbers))
    
#Assignment 3
numbers = [5, 3,  6, 81, -19, 0]
def minimum(num):
    min_num = numbers[0]
    for i in numbers:
        if i < min_num:
            min_num = i
    return min_num
print(minimum(numbers))


#Assignment 4
numbers = [0, 1, 2, 3, 4, 6, 7, 8, 9]
def missing_number(a):
    for i in a:
        x = i * (i + 1)/2
        sum_nums = sum(numbers)
    return x - sum_nums

print(missing_number(numbers))


#Assignment 5
array = [1, 2, 3, 4, 5]

def duplicate(array):
    new_array = []
    for i in array:
        new_array.append(i)
    for i in new_array:
        array.append(i)
    return array
print(duplicate(array))
        
      
