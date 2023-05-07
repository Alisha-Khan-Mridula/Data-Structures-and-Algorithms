### Merge Sort follow divide and conqure procedure
### Time Complexity = O(nlog(n))

def MergeSort(array):
    length = len(array)
    if length > 1:
        mid = len(array)//2  ### Diving with 2 to find mid point 
        
        Left = array[:mid]
        Right = array[mid:]

        #### Left side sorting ####
        MergeSort(Left)
        
        ### right Side sorting
        MergeSort(Right)
        
        i = 0
        j = 0
        k = 0
        
        
        ### Merging ###
        while i<len(Left) and j<len(Right):
            if Left[i] >= Right[j]:
                array[k] = Right[j]
                k = k+1
                j = j+1
                
            else: 
                array[k] = Left[i]
                k = k+1
                i = i+1    
                
        while i < len(Left):
            array[k] = Left[i]
            k = k+1
            i = i+1
            
        while j < len(Right):
            array[k] = Right[j]
            k = k+1
            j = j+1
            




### Calling function
array = [2,6,5,1,7,4,3]
MergeSort(array)
print(array)