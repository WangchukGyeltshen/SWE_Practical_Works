def in_place_quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        in_place_quick_sort(arr, low, pivot_index - 1)
        in_place_quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

test_arr = [64, 34, 25, 12, 22, 11, 90]
in_place_quick_sort(test_arr, 0, len(test_arr) - 1)
print("In-Place Quick Sort Result:", test_arr)

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  
    return arr

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = optimized_bubble_sort(test_arr.copy())
print("Optimized Bubble Sort Result:", sorted_arr)

def hybrid_merge_sort(arr, threshold=10):
    if len(arr) <= threshold:
        return insertion_sort(arr)
    
    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)
    
    return merge(left, right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = hybrid_merge_sort(test_arr)
print("Hybrid Merge Sort Result:", sorted_arr)

import matplotlib.pyplot as plt
import time

def visualize_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        plt.bar(range(len(arr)), arr, color='skyblue')
        plt.pause(0.1)
        plt.clf()
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        plt.bar(range(len(arr)), arr, color='lightcoral')
        plt.pause(0.1)
        plt.clf()

test_arr = [64, 34, 25, 12, 22, 11, 90]
plt.ion()
visualize_bubble_sort(test_arr.copy())
plt.ioff()
plt.show()
