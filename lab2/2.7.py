def leap(x):
    if(x%4==0):
        if(x%100!=0 or x%400==0 ):
         print("leap year")
        else :
         print("not a leap year")
x=int(input("enter the year"))
check=leap(x)