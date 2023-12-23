"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


array1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
array4 = [5, 2, 7, 5, 8, 4, 1, 2, 5, 3]

insertion_sort(array1)
insertion_sort(array2)
insertion_sort(array3)
insertion_sort(array4)

print("Sorted array1:", array1)
print("Sorted array2:", array2)
print("Sorted array3:", array3)
print("Sorted array4:", array4)



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