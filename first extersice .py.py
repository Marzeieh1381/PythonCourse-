income = float(input("Enter your incom and see your net income : "))       #income is a float number 
if income < 1000 :
    print(" " , income)                                                
else:
    if 1000 < income <= 2500 :                             #calculate net income and print it 
        netincome =  income - (income * 0.1)                  
        print (" " , netincome )
    else:
        if 2500< income <= 4000 :
            netincome = income - ( income * 0.15 )
            print(" " , netincome )
        else:
            if 4000 < income <= 6000:
                netincome= income - ( income * 0.2 )
                print ( " " , netincome )
            else:
                if income >= 8000 :
                    netincome = income - (income * 0.3 )
                    print (" " , netincome )
        