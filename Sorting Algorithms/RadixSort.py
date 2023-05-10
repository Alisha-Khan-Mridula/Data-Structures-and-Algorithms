### Time Complexity: O(d*(n+k))

numbers = [27,146,259,348,152,163,235,48,36,62]
comply = []

for i in range(10):
    comply.append([])
      
    
num = max(numbers)


num = str(num)
num = len(num)
l = 0
k = 0 
m = 0
for i in range(num):
    #print(numbers)
    for j in range(len(numbers)):
        #print(numbers[j])
        digit = (numbers[j]//(10**i))%10
        #print(digit)
        comply[digit].append(numbers[j])
            
    #print(comply[3][0])
    k = 0
    m = 0
    while k < len(numbers):
          count = len(comply[k])
         # print(count)
          while count > l:
                numbers[m] = comply[k][l]
                #print(numbers)
                l = l+1
                m = m+1
          k = k+1
          #print(k)
          l = 0  
    comply = []

    for p in range(10):
       comply.append([])


    
        
    
print(numbers)
        
     
