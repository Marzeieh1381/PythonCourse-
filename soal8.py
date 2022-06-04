def product(touple):
	
	if len(touple)==0:
		
		return 1 
	else:
		result =1
	for i in touple :
		result *= i 
	    
	    
	return result 
	
def convert(list):
	return tuple (list)
	    
list = []
n= int(input("enter a number of element in tople  :"))
for i in range (0,n ):
	ele =float(input( ))
	list +=[ele]
	    
	    
	    
touple=convert(list)
	
	
print("the touple is :" , touple)
print ("Multiplication between Tupel members:",product(touple))