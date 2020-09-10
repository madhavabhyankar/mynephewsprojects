import math
def binary_search(sorted_array, looking_value):
    print("Using binary search")
    
    mid_point = len(sorted_array)

    while(True):
        array_length = len(sorted_array)
        mid_point = array_length // 2
        
        mid_point_value = sorted_array[mid_point]
        if(mid_point_value == looking_value):
            print("Found " + str(looking_value) + " at " + str(mid_point))
            break

        if(mid_point_value > looking_value):
            sorted_array = sorted_array[0:mid_point]

        if(mid_point_value < looking_value):
            sorted_array = sorted_array[mid_point: array_length]

        if(mid_point == 0):
            print("Did not find " + str(looking_value) + " in the array")
            break


def linear_search(sorted_array, looking_value):
    print("Using linear search")
    for index, value in enumerate(sorted_array):
        if(value == looking_value):
            print("Found " + str(looking_value) + " at " + str(index))
            return
    print("Did not find " + str(looking_value))
    return
            

if __name__ == '__main__':
    sorted_array = input('Please enter a sorted array. Ex: 1,2,3,4,5:\n')
    
    sorted_int_array = [int(num) for num in sorted_array.split(',')]

    value_to_look_for = input('Please enter a value to look for:\n')
    function_to_use = input('Please enter l for linear search and b for binary search:\n')

    if(function_to_use == 'l'):
        linear_search(sorted_int_array, int(value_to_look_for))
    if(function_to_use == 'b'):
        binary_search(sorted_int_array, int(value_to_look_for))
    
