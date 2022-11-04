num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
while True:
    print("select operation")
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("5 exit")
    choice=int(input("enter your choice"))
    if choice==1:
        a=num1+num2
        print("the sum of num1 and num2 is" ,a)
    elif choice==2:
        b=num1-num2
        print("the difference of num1 and num2 is" ,b)
    elif choice==3:
        c=num1*num2
        print("the product of num1 and num2 is" ,c)
    elif choice==4:
        d=num1/num2
        print("the division od num1 and num2 is" ,d)
    elif choice==5:
        break
    else:
        print("invalid choice")
