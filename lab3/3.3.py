x=input("enter the string 1 ")
y=input("enter the string 2 ")
def check(x,y):
    for i in x:
        if i==y[0]:
            for j in y :
                if i == j:
                    print("yes")
                else:
                    break
check(x,y)


