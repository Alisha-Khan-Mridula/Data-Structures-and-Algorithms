

def partition(numbers, low, high):
        pivot = numbers[low]
        i = low+1
        j = high
        while i<j:
         if  numbers[i] > pivot and numbers[j] < pivot:
            numbers[i] , numbers[j] = numbers[j] , numbers[i]
            i = i+1
            j = j-1
        
            
         elif numbers[i] > pivot and numbers[j] > pivot:
            j = j-1

         elif numbers[i] < pivot and numbers[j] > pivot:
            i = i+1
            j = j-1

         elif numbers[i] < pivot and numbers[j] < pivot:
            numbers[low] = numbers[j]
            numbers[j] = pivot
            #print(numbers)
            return j
    


        if numbers[low] > numbers[j]: 
          numbers[low] = numbers[j]
          numbers[j] = pivot

        #print(numbers)
        return j


def QuickSort(numbers, low, high):
        if low < high: 
                a = partition(numbers, low , high)
                QuickSort(numbers, low, a-1)
                QuickSort(numbers, a+1, high)
                
                
numbers = [10,6,5,8,9,3,15,12,1]

low = 0
high = len(numbers) - 1

QuickSort(numbers, low, high)
print(numbers)
        
        




    
        


        








