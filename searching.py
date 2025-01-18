def binary_search(array, target):
 
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

def linear_search(array, target):

    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1  # Target not found



if __name__ == "__main__":
    # Test Binary Search
    binary_array = [10, 20, 30, 40, 50]
    binary_target = 30
    binary_result = binary_search(binary_array, binary_target)
    print(f"Binary Search Result: {binary_result}")

    # Test Linear Search
    linear_array = [60, 70, 80, 90, 100]
    linear_target = 90
    linear_result = linear_search(linear_array, linear_target)
    print(f"Linear Search Result: {linear_result}")
