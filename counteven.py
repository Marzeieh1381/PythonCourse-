def evencount(lst):
    count=0
    for item in lst :
        if item %2 == 0 :
            count=count+ 1

    return count


lst=[] 
n = int(input("enter a number of element :"))
if n == 0:
    print ("this list is empty")
else :
    if n >0:
        for i in range (0,n):
            ele = int(input())
            lst +=[ele] 
    print (evencount(lst),"the number of  even  numbers ")
