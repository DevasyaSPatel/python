x=int(input("enter the no. "))
y=int(input("enter the no. "))
def rect(x,y):
  area=x*y
  perimeter=2*(x+y)
  if(area>perimeter):
    print("area is bigger then perimeter")
  else: 
    print("perimeter is bigger")  
check=rect(x,y)    