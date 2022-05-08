def next_number(lst):
    my_max=0
    number =0
    for i in lst:
        if i > my_max:
            my_max = i 
            
            for i in range (1, my_max + 1):
                if i not in lst:
                    return i 
    
    return my_max + 1 



lst=[] 
n = int(input("enter a number of element :"))
for i in range (0,n):
    ele = int(input("enter the number of list:"))
    lst +=[ele] 



print(next_number(lst))
        