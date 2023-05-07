##### Time Complexity: O(N+K)
##### Space Complexity: O(N+K)
####                   N = Number of elements
####                   K = Number of Range                       


numbers = [1,2,4,3,0,2,1,7,1,4,3,0]


maximun = max(numbers)
minimum = min(numbers)

count = []
for i in range(maximun+1):
    count.append(0)
    
output = []
for i in range(len(numbers)):
    output.append(0)

for i in range(len(numbers)):
    count[numbers[i]] = count[numbers[i]] + 1
   
    
for i in range(minimum+1, maximun+1):
    count[i] = count[i] + count[i-1]
    
for i in range(len(numbers)-1, -1, -1):
    count[numbers[i]] = count[numbers[i]] - 1 
    output[count[numbers[i]]] = numbers[i]

print(output)        
    
    