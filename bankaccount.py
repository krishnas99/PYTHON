class BankAccount:
    def __init__(self,accno,name,types,bal):
        self.AccountNumber=accno
        self.Name=name
        self.AccountType=types
        self.Balance=bal
    def deposits(self,amt):
        self.Balance=self.Balance+amt 
        print("the deposited amount is:",self.Balance)
    def withdraw(self,amt):
        if self.Balance==0:
            print("balance is zero")
        else:
            self.Balance=self.Balance-amt
            print(self.Balance)
al=BankAccount(100000,"ansar","saving",5000)
while(True):
    print("\n 1:deposit \n 2:withdraw \n 3:exit")
    op=int(input("enter your choice:"))
    if(op==1):
        al.deposits(1000)
    elif(op==2):
        al.withdraw(200)
    else:
        exit(0)
            