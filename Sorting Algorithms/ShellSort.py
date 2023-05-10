### Time Complexity: Best Case: O(nlog(n))
###                  Worst Case: O(n^2)

array = [77, 62, 14, 9, -30, 21, 80, 25,70, 20]
length = len(array)

count = 0
while True:
  if length != 0:
    count = count+1
    length = length//2

  else:
    break

gap = len(array)
for k in range(count+1):
  gap = gap//2
  if gap == 0: 
    i = 0
    b = len(array) - 1
    while True:
         if i == b:
            break
         if array[i] > array[i+1]:

             array[i], array[i+1] = array[i+1], array[i] 
             i=i+1
         else:
            i=i+1
             

  else: 
        i = 0
        b = len(array) - gap
        while True:
          if i == b:
            break


          if array[i] > array[i+gap]:

              array[i], array[i+gap] = array[i+gap], array[i] 
              i = i+1

          else: 
              i = i+1
print(array)