sum = 0.0
big = None
small = None
count = 0
while True:
            numbers = float(input('Enter a positive number: '))
            sum += numbers
            count += 1
            if big is None or numbers > big:
                        big = numbers
            if small is None or numbers < small:
                        small = numbers
            if count == 20:
                        print('Sum is:', sum)
                        print('Average is:',sum / 20)
                        print('Maximum is:',big)
                        print('Minimum is:',small)   
                        break
                            
           
   