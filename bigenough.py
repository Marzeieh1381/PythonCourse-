def bigenough(lst):
 L = []
 x=int(input("enter a number"))
 for item in lst :
  if item>=x :
   L += [item]
   
 return L


lst=[] 
n = int(input("enter a number of element :"))
for i in range (0,n):
        ele = int(input("enter the number of list:"))
        lst +=[ele] 

print(bigenough(lst) , " " ) 