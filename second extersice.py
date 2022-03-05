a = int(input("Enter a number as side of the triangle :"))              # a , b , c are three numbers for sides of triangle 
b = int(input("Enter secend number as side of the triangle :"))
c = int(input("Enter thired number as hypotenuse :"))
        
if a**2 + b**2 == c**2 :                 #use a formol  fisagores for know is it a Right triangle or not 
    print("Right")
else:
    print("Not Right")
    
