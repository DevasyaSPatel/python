x=input("enter the string")
count=0
def vow(x):
    count=0
    v=["a","e","i","o","u"]
    for i in x:
        for j in v:
            if i==j:
                count=count+1
    print(count)
vow(x)               
