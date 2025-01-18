x=int(input("enter the no"))
y=int(input("enter the no"))

def min(x,y):
 if(x>y):
     print("this is the greatest value",x)
     print("this is the smallest value",y)
 else:
     print("this is the greatest value",y)
     print("this is the smallest value",x)     

check=min(x,y)    