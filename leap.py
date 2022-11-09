s=int(input("enter the start year"))
e=int(input("enter the end year"))
if(s<e):
    print("leap years are")
    for i in range(s,e):
        if(i%4==0 and i%100!=0):
            print(i,end=" ")
else:
    print("invalid")
