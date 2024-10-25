
#1 BUBBLE SORTING ALGORITHM WITH RANDOM LIST MAKER FUNCTION
import random as r
def bubblesort(lst) :
    sorted = False 

    while sorted == False :                      #executes when list is not sorted at any time.
        sorted = True 

        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:                  #when list is unsorted 

                sorted =  False                  #set condition as false so loop is ran again to check if sorted 
                lst[i],lst[i+1]=lst[i+1],lst[i]  # swap unsorted operand with its next operand 
    return lst 
#justa random list maker 
def randomlistmaker(L) :
    n=int(input("enter the length of the list you want"))
    for i in range(n) :
        L.append(r.randint(0,100))
    return L
K=[]
print(bubblesort(randomlistmaker(K)))
     

#2 INSERTION SORT  
def insertionsort(arr):
    for i in range(1, len(arr)):
        # first element is considered already started, start from the second element 
        
        j = i
        while arr[j-1] > arr[j] and j > 0:
            # Keep swapping until the current element is in the correct position
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    
    print(arr, "after sorting")

L = eval(input("enter a list of integers"))
insertionsort(L)

     

#3 SELECTION SORT IN PYTHON
def selectionsort(arr):    
    for i in range(0, len(arr) - 1):
        # Iterate through the array, considering each element as a potential minimum
    
        mindex = i
        # Assume the current index has the smallest value
        
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mindex]:
                # Find the smallest element in the unsorted part of the array
                mindex = j
        
        # Swap the smallest element found with the current element
        arr[mindex], arr[i] = arr[i], arr[mindex]
    
    print(arr)
selectionsort([3, 6, 3, 6, 8, 3, 3, 7])
