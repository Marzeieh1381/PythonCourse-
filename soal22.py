def dobodi(n):
    matjadid = [[0]*len(n)] * len(n)
    for i in range(len(n)):
        for j in range(len(n[0])):
            matjadid[i][j] = n[i][j]
    flag = 0
    
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] == matjadid[j]:
                flag = 1
                
                
    if flag :
        return True
    else:
        return False

print (dobodi(n))
    