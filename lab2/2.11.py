x1=int(input("enter the no."))
y1=int(input("enter the no."))
x2=int(input("enter the no."))
y2=int(input("enter the no."))
x3=int(input("enter the no."))
y3=int(input("enter the no."))
def col(x1,y1,x2,y2,x3,y3):
    s1=(y2-y1)/(x2-x1)
    s2=(y3-y2)/(x3-x2)
    s3=(y3-y1)/(x3-x1)
    if(s1==s2==s3):
        print("collinear")
    else:
        print("not collinear")    

check=col(x1,y1,x2,y2,x3,y3)