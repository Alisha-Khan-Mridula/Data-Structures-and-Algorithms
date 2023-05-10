##### Time Complexity: Best case: O(nlog(n)) => log(n) for the levels and n is the n number od elements 
#####                  Worst case: O(n^2) => O(n) for in no of levels and O(n) for n no of elements sorting




###### Represnting a node as a class #########
class Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


#### Calling for inserting and in order traversing
def TreeSort(array):
  root = None

  for i in array:
    root = insert(root,i)
  

  result = []
  InOrderTraverse(root, result)
  return result



####### Inserting Data into a tree ##########
def insert(root, data):
  if root is None:
    return Node(data)

  if data < root.data :
    root.left = insert(root.left, data)

  else:
    root.right = insert(root.right, data)

  return root

###### In order traversal ###############
def InOrderTraverse(root, result):
  if root is not None:
    InOrderTraverse(root.left, result)
    result.append(root.data)
    InOrderTraverse(root.right, result)



array = [237,146,259,348,168]
output = TreeSort(array)
print(output)