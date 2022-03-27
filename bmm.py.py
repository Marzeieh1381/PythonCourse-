while True:
    x = int(input("Enter the first number :"))
    y = int(input("Enter the second number :"))
    break 
if  x<y :
        temp = x
        x = y
        y = temp
while (y != 0):
    t = x % y
    x = y 
    y = t
    r = x
print("bmm (x ,y ):" , r)