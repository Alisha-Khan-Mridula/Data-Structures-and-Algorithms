## Time Complexity: 
#        Best: Iteration O(n) + Shift items O(1) = O(n)
#        Worst: Iteration O(n) + Shift items O(n) = O(n^2)
## Space complexity: O(1) 

numbers = [4,6,2,9]
for i in range(len(numbers)-1):
    stored = 0
    if i == 0:
        if numbers[i] > numbers[i+1]:
            stored = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = stored 
            
        else: 
            pass
        
    else: 
        if numbers[i] > numbers[i+1]: 
            stored = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = stored
            
            for j in range(i, 0, -1):
            
                if numbers[j] < numbers[j-1]:
                    stored = numbers[j-1]
                    numbers[j-1] = numbers[j]
                    numbers[j] = stored 
                    

                                   
print(numbers)  
            