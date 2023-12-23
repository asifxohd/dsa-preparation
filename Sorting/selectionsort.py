"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
def selection_sort(arr):
    for i in range(len(arr)-1):
        minpos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minpos]:
                minpos = j
        arr[j], arr[i] = arr[i], arr[j]
    
    return arr



arr = [5,7,3,6,34,6,45,64, 4, 2,1,0,-3]
result = selection_sort(arr)
print(result)


"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

""" ADVANTAGES AND DISADVANTAGES OF SELECTION SORT """
'''
Selection sort is a simple and efficient sorting algorithm that works by
repeatedly selecting the smallest (or largest) element from the unsorted portion 
of the list and moving it to the sorted portion of the list. 


Advantages of Selection Sort Algorithm:
    Simple and easy to understand.
    Works well with small datasets.
    
Disadvantages of the Selection Sort Algorithm:
    Selection sort has a time complexity of O(n^2) in the worst and average case.
    Does not work well on large datasets.
    Does not preserve the relative order of items with equal keys which means it is not stable
'''