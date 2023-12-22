"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

def bubblesort(arr):
    size = len(arr)
    
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

arr = [5,7,3,6,34,6,45,64, 4, 2,1,0,-3]
result = bubblesort(arr)
print(result)


"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CODE   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""




"""  ADVANTAGES AND DISADVANTAGES OF BUBBLE SORT """

"""
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements, and swaps them if they are in the wrong order. While
Bubble Sort is easy to understand and implement, it is not the most efficient sorting
algorithm for large datasets. Here are the advantages and disadvantages of Bubble Sort:

Advantages:

Simplicity:

    Bubble Sort is easy to understand and implement
    . It's a straightforward algorithm that is often used for
    educational purposes to introduce the concept of sorting.

Space Complexity:

    Bubble Sort has a space complexity of O(1), which means it uses a
    constant amount of extra memory. It doesn't require additional
    storage proportional to the size of the input.

Adaptability
    It performs well when the list is already partially sorted.
    In a partially sorted list, Bubble Sort can have better performance
    compared to other sorting algorithms.




Disadvantages:

Time Complexity:
    The main disadvantage of Bubble Sort is its time complexity
    . In the worst-case scenario, where the input list is in reverse order, 
    Bubble Sort has a time complexity of O(n^2), making it inefficient for large datasets.

Performance:
    Bubble Sort is generally less efficient than many other sorting algorithms,
    especially for large datasets. More advanced algorithms like Merge Sort, QuickSort,
    or HeapSort often outperform Bubble Sort in terms of speed.

Stability: 
    While Bubble Sort is a stable sorting algorithm (it maintains the relative order of equal elements),
    its stability comes at the cost of performance. Some more efficient algorithms sacrifice stability for speed.

Not suitable for large datasets: 
    Bubble Sort is not recommended for sorting large datasets because
    its time complexity grows significantly as the size of the dataset increases.
    More efficient algorithms become more practical for larger lists.
"""