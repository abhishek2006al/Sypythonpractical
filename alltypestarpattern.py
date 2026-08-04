print("=================Star pattern=================")

rows=7
col=30

for i in range(rows):
      for j in range(col):
            if i==0 or i==rows-1 or j==0 or j==col-1:
                  print("*",end=" ")
            else:
                  print(" ",end=" ") 
      print()    

rows=8
for i in range(rows):
      for j in range(20):
            print("*",end=" ")
      print()

rows=5

for i in range(1,rows+1):
      for j in range(1,6):
            print(j,end=" ")
      print()  
rows=5

for i in range(1,rows+1):
      for j in range(1,i+1):
            print(j,end=" ")
      print()  

rows=5
for i in range(1,rows+1):
      for j in range(i):
            print("*",end=" ")
      print()  
rows=5

for i in range(rows,0,-1):
      for j in range(i):
            print("*",end=" ")
      print()  




