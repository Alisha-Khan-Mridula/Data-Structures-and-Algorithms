# Time Complexity = O(N^2) As there are two for loops and time complexity of each loop is O(N). So, Total O(N)*O(N) = O(N^2)
# Space Cpmpexity = O(1)

numbers = [4,9,3,6,2]

for i in range(len(numbers)):
    MinIndex = i 
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            MinIndex = j 
    
    #Swapping with the minimum number        
    numbers[i], numbers[MinIndex] = numbers[MinIndex], numbers[i]    
    
print("Sorted List  Usuing Selection Sort:")    

for i in range(len(numbers)):
    print(numbers[i], end=" ")