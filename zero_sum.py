def zero_sum(touple):

    if len(touple)==0:

        return True
    sum =0
    for i in touple :
        sum += i 
    if sum == 0:
        return True
    
    else:
        
        return False


def convert(list):
    return tuple (list)

list = []
n= int(input("enter a number of element in tople  :"))
for i in range (0,n ):
    ele =int(input( ))
    list +=[ele]



touple=convert(list)


print("the tuple is :",touple)
print (zero_sum(touple))