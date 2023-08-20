
def partition(array, low, high):    
    pivot = array[high]    
    i = low - 1    
    for j in range(low, high):
        if array[j] <= pivot:            
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)        
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
n = int(input())
data = list(map(int, input().split()))
size = len(data)
quickSort(data, 0, size - 1)
max_value = max(data)
count = 0
for x in data:
  if x == max_value:
    count += 1
print( count)
