"""bubble sort"""
"""def bubblesort(arr):
    for i in range(len(arr) -1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j],
                
                
                
arr = [4,6,7,3,4,63,3,56,76,33,56,66,55]
bubblesort(arr)
print(arr)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")"""

"""quicksort"""

"""def quicksort(arr,left,right):
    if left < right:
        partision_pos = partision(arr,left, right)
        quicksort(arr, partision_pos+1, right)
        quicksort(arr,left, partision_pos-1)


def partision(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        
        while i < right and arr[i] < pivot:
            i += 1
            
        while j > left and arr[j] >= pivot:
            j -= 1
            
        if i < j :
            arr[i],arr[j] = arr[j],arr[i]  
        
        
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i


arr = [4,6,7,3,4,63,3,56,76,33,56,66,55]
quicksort(arr, 0 , len(arr) - 1)
print(arr)"""
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


"""def merge_sort(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j] 
            j += 1
            k += 1
        
array1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
array4 = [5, 2, 7, 5, 8, 4, 1, 2, 5, 3]

merge_sort(array1)
merge_sort(array2)
merge_sort(array3)
merge_sort(array4)

print("Sorted array1:", array1)
print("Sorted array2:", array2)
print("Sorted array3:", array3)
print("Sorted array4:", array4)
"""


"""def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    


array1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
array4 = [5, 2, 7, 5, 8, 4, 1, 2, 5, 3]

selection_sort(array1)
selection_sort(array2)
selection_sort(array3)
selection_sort(array4)

print("Sorted array1:", array1)
print("Sorted array2:", array2)
print("Sorted array3:", array3)
print("Sorted array4:", array4)"""


