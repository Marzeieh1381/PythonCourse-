
#first way 
Lis = []
for i in range(1,11):
    Lis +=[i]
print(Lis)

#second way 
lis = []
i=0
while i<10:
    i+=1
    lis +=[i] 
print(lis)

#thirdway
lis=[10,9,8,7,6,5,4,3,2,1]
new=[]
for i in lis[ ::-1]:
    new += [i]
print(new)

#forthway
lis=[20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10,0]
new=[]
for i in lis[-11 : -1: 1]:
    new +=[i]
print(new)

#fifthway
lis = [] 
i=11
while i>1:
    i = i -1 
    lis += [i]
for i in lis[ :: -1]:
    x = lis[ ::-1]
print(x)