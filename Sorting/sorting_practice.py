"""   BUBBLE SORT  """  

def bubblesort(arr):
    size = len(arr)
    for i in range(size-1):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                
arr= [ 3,4,6,7,3,8,98,98,0]
bubblesort(arr)
print(arr)

print('!!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!')
"""  SELECTION SORT  """

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] 
                
arr= [ 3,4,6,7,3,8,98,98,0]
bubblesort(arr)
print(arr)

print('!!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!')

"""  INSERTION SORT  """

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j >=0 and key < arr[j]:
            arr[j+1]= arr[j]
            j -= 1
            
        arr[j+1] = key
            
        
                
arr= [ 3,4,6,7,3,8,98,98,0]
insertion_sort(arr)
print(arr)
print('!!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!')

def quicksort(arr, left, right):
    if left < right:
        index = partition(arr, left, right)
        quicksort(arr, index+1 , right)
        quicksort(arr, left, index-1)

def partition(arr, left, right):
    
    i = left 
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
            
    
    if arr[i] > pivot:
        arr[right], arr[i] = arr[i], arr[right]
        
    return i 
    
        
                
arr= [ 3,4,6,7,3,8,98,98,0]
quicksort(arr, 0, len(arr)-1)
print(arr)
print('!!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!')


print('!!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!')
"""  MERGE SORT  """

def merge_sort(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        merge_sort(left)
        merge_sort(right)
        
        i=j=k=0
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
            k += 1
            j += 1
                    
arr = [ 3,4,6,7,3,8,98,98,0]
merge_sort(arr)
print(arr)

print('!!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!')