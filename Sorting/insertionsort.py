"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        
        j = i-1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
    return arr




arr = [5,7,3,6,34,6,45,64, 4, 2,1,0,-3]
result = insertionsort(arr)
print(result)


"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

""" ADVANTAGES AND DISADVANTAGES OF INSERTION SORT """

'''
Insertion Sort is a simple sorting algorithm that builds 
the final sorted array one item at a time. It is much less efficient 
on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
Here are the advantages and disadvantages of Insertion Sort

'''

'''Advantages:

Simple Implementation:

    Insertion Sort is easy to understand and implement. 
    It involves repeatedly taking elements from the unsorted part
    of the array and inserting them into their correct positions in the sorted part.

Efficient for Small Datasets: 

    Insertion Sort is more efficient than some other algorithms,
    particularly for small datasets or partially sorted datasets.
    Its time complexity is O(n^2) in the worst case, but it has a relatively low constant factor.

Adaptive:
    It is an adaptive algorithm, meaning its performance is better 
    when dealing with partially sorted datasets. If the array is nearly sorted, 
    Insertion Sort can be quite efficient.

Stable:
    Insertion Sort is a stable sorting algorithm, 
    meaning that it maintains the relative order of equal elements in the sorted output.



Disadvantages:

Inefficient for Large Datasets: 
    The main disadvantage of Insertion Sort is its inefficiency for large datasets. 
    Its time complexity is O(n^2), making it less suitable for sorting large lists compared
    to more efficient algorithms like merge sort or quicksort.

Performance: 
    The performance degrades significantly as the size of the dataset increases.
    More advanced algorithms like merge sort, quicksort, or heapsort generally offer better
    average and worst-case time complexities for larger datasets.

'''