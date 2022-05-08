def mysum(lst):
    result = 0
    for item in lst :
        if len(lst) == 0:
            return 0        
        if item > 0 :
            result=result + item

    return result

lst=[] 
n = int(input("enter a number of element :"))




for i in range (0,n):
            ele = int(input("enter a number of list :"))
            lst +=[ele] 


print (mysum(lst),"the sum of positive numbers ")
