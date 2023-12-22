"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
def merge_sort(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                k += 1
                j += 1
            else:
                arr[k] = right[j]
                k += 1
                j += 1
                
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1 
        
        
        

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
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
