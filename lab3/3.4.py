x=input("enter the string 1 ")
y=input("enter the string 2 ")
def remove(x,y):
    if x in y:
        print(y.replace(x,""))
    elif y in x:
        print(x.replace(y,""))
    else:
        print("no string present inside any of them")
check=remove(x,y)        


