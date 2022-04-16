
def TowerOfHanoi(n , s_pole, d_pole, i_pole):   
  if n == 1:
    print("move disc 1 from pole",s_pole,"to pole",d_pole)
  else:
        TowerOfHanoi(n-1, s_pole, i_pole, d_pole)
        movedisc(n,s_pole, d_pole)
        TowerOfHanoi(n-1, i_pole, d_pole, s_pole)
def movedisc(n,s_pole,d_pole):
    print("move disc " ,n,"from ",s_pole ,"to pole",d_pole)
    
n=int(input("enter a number :"))


TowerOfHanoi(n, "A", "B", "C")