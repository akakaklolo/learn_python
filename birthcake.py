import numbers

from quicksort import quickSort


qui = quickSort(numbers, 0, len(numbers)-1, 0, 0)

def partition(numbers, start_index, end_index, qui_swap):

    # Select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]
   
    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = start_index
    high = end_index
   
    done = False
    while not done:
        # Increment low while numbers[low] < pivot
        while numbers[low] < pivot:
            low = low + 1
          
      
        # Decrement high while pivot < numbers[high]
        while pivot < numbers[high]:
            high = high - 1
            
      
        # If low and high have crossed each other, the loop
        # is done. If not, the elements are swapped, low is
        # incremented and high is decremented.
        if low >= high:
            done = True
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low += 1
            high -= 1
            qui_swap += 1

   
    # "high" is the last index in the left segment.
    return (high, qui_swap)

def quicksort(numbers, start_index, end_index, qui_swap, qui_comp):
    # Only attempt to sort the list segment if there are
    # at least 2 elements

    
    if end_index <= start_index:  
       
        return   
    # Partition the list segment
    
     #count comparisons here
    qui_comp += 1
         
    high = partition(numbers, start_index, end_index,qui_swap)
    qui_swap = high[1]
    
    # Recursively sort the left segment
    quicksort(numbers, start_index, int(high[0]), qui_swap, qui_comp+1)
    
    # Recursively sort the right segment
    quicksort(numbers, int(high[0]) + 1, end_index, qui_swap, qui_comp+1)
    
    return(qui_swap, qui_comp)
