from sys import stdin, stdout

n = stdin.readline()
inputs = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
keys = map(int, stdin.readline().split())

 

outputs = []

 
for key in keys:
  low = 0;
  high = len(inputs) - 1
  mid = 0;

  endWithoutFoundFlag = True
  while(low <= high):
    mid = (low + high) // 2

    if (inputs[mid] == key):
      outputs.append(1)
      endWithoutFoundFlag = False
      break
    elif (inputs[mid] > key):
      high = mid - 1
    else:
      low = mid + 1

  if endWithoutFoundFlag == True:
    outputs.append(0)
  
  
for o in outputs:
  print(o)