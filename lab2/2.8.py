def tri(x,y,z):
    if (x+y+z==180):
        print("its corect triangle")
    else:
        print("not correct triangle")    

x=int(input("enter the angle"))
y=int(input("enter the angle"))
z=int(input("enter the angle"))        
check=tri(x,y,z)