# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    #With the built in range function we dont need to explicitly write 0.
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
                
            if arr[j] < arr[smallest_index]:
                smallest_index = j 


        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    init = range(len(arr) - 1)

    for i in init: 
        #Starts at 0
        for j in init: 
            #Compare values
            if arr[i] > arr[j + 1]:
                #Perform the swap
                arr[i], arr[j] = arr[j] arr[i]
            


    """
    made_a_swap = True
    # We say  it's true so we can initiate the while loop
    while made_a_swap:
        made_a_swap = False 

        #Create counters 
        for i in range(0, len(arr) - 1):
            j = i + 1

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                made_a_swap = Trued
    """
# i  j
#[1, 5, 2, 7]
    return arr



'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 
 
What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
