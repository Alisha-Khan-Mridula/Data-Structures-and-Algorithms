### Time Complexity: Best Case: O(n+K) = n is the total number of element and K is the total bucket numbers = More Buckets less time complexity because individual buckets will take less time to sort itself.and
###                  Worst case: O(n^2) = All elements in one bucket so take time to do insertion sort/ build in sort/ Bubble sort or any other sort    
### space Complexity: O(n)           
def bucketSort(x):
    array = []
    slotNumber = 10 
    for i in range(slotNumber):
        array.append([])
          
  
    for j in x:
        if j//2 == 0: 
            array[0].append(j)
            print(array)
        else: 
            if j >=100:
                array[9].append(j)
                print(array)
            else:
                index = int(j/10)
                array[index].append(j)
                print(array)
      

    for i in range(slotNumber):
        array[i].sort()
          

    k = 0
    for i in range(slotNumber):
        for j in range(len(array[i])):
            x[k] = array[i][j]
            k += 1
    return x
  
# Driver Code
x = [.42, .32, .33, .52, .37, .47, .51,10,4,2,1,-8,0,10,2,11,23,43.2,11,24,25,23,230] 
print("Sorted Array is")
print(bucketSort(x))