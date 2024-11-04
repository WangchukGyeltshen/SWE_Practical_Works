def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  

test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

import time

def compare_search_algorithms(arr, target):
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

def main():
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  
    print(f"\nSearching for: {target}")
    
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()


#Exercise
def linear_search_all_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  
    return indices if indices else -1  

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search_all_indices(test_list, 5)
print(f"Linear for All Indices: Indices of 5 are {result}")


def find_insertion_point(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left  

sorted_list = [1, 3, 4, 6, 8, 9]
target = 5
insertion_point = find_insertion_point(sorted_list, target)
print(f"Insertion Point for {target} is at index {insertion_point}")
print("Updated list:", sorted_list)


def linear_search_with_count(arr, target):
    comparisons = 0
    for i, num in enumerate(arr):
        comparisons += 1
        if num == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    left, right, comparisons = 0, len(arr) - 1, 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons
    mid = (left + right) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons + 1)
    return binary_search_recursive(arr, target, left, mid - 1, comparisons + 1)

def main():
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list) 
    print(f"\nSearching for: {target}")
    
    result, comparisons = linear_search_with_count(test_list, target)
    print(f"Linear Search: Found at index {result} with {comparisons} comparisons")
    
    sorted_list = sorted(test_list)
    result, comparisons = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result} with {comparisons} comparisons")
    
    result, comparisons = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result} with {comparisons} comparisons")

if __name__ == "_main_":
    main()