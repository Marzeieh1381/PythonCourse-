def check_winner(n):
    matjadid = [[0]*len(n)] * len(n)
    for i in range(len(n)):
        for j in range(len(n[0])):
            matjadid[i][j] = n[i][j]
    for i in n :
        if i[0] == i[1]== i[2] == "x":
            return "x"
        elif i[0] == i[1]== i[2]=="o":
            return "o"
    for i in matjadid:
        if i[0] == i[1] == i[2] == "x":
            return "x"
        elif i[0] == i[1] == i[2] == "o":
            return "o"
    if n[0][0] == n[1][1] == n[2][2] == "x":
        return "x" 
    elif n[0][0] == n[1][1] == n[2][2] == "o":
        return "o"     
    if n[0][2] == n[1][1] == n[2][0] == "x":
        return "x"     
    elif n[0][2] == n[1][1] == n[2][0] == "x":
            return "o"   
    return " " 

print(check_winner(n))