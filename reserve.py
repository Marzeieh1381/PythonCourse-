def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
lst=[] 
n = int(input("enter a number of element :"))
for i in range (0,n):
    ele = int(input())
    lst +=[ele] 


print(Reverse(lst))
