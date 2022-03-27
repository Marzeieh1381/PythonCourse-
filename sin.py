x=float(input("Enter the valu of degreas :"))
n = int(input("Enter the number of terms:"))
pi=3.14
sine=0
fact = 1
if n >= 1:
   for i in range (1,n+1):
      fact = fact * i
else:
   if n == 0:
      fact=n
for i in range(n) : 
   d=(-1)**i
   x = n*(pi/180)
   z= x**((2*i)+1)
   a =(d*(z))
   sine=sine + (a/fact*(2*i+1))
   print (sine)    
   break 
