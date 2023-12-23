"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
'''  MORE EFFICIANT APPROACH  '''
def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr,left,right)
        quicksort(arr, left, partition_pos-1)
        quicksort(arr, partition_pos+1, right)
     
    
     
def partition(arr,left,right):
    i = left
    j = right
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        
        while j > left and arr[j] >= pivot:
            j -= 1
            
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
            
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i    
            
    



arr = [5,7,3,6,34,6,45,64, 4, 2,1,0,-3]
quicksort(arr, 0, len(arr)-1)
print(arr)

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""



"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
'''  STRIGHT FORWARD APPROACH NOT EFFICIANT ENGOUGH  '''

# def quicksort(arr):
#     length = len(arr)
#     if length <= 1:
#         return arr
#     else:
#         pivot = arr.pop()
        
#     items_greater = []
#     items_lower = []
    
#     for item in arr:
#         if item > pivot:
#             items_greater.append(item)
#         else:
#             items_lower.append(item)
    
#     return quicksort(items_lower) + [pivot] + quicksort(items_greater)     




# arr = [5,7,3,6,34,6,45,64, 4, 2,1,0,-3]
# result = quicksort(arr)
# print(result)


"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""