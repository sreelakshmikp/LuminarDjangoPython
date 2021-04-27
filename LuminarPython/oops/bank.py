class Bank:
    def create_account(self,acno,pname,minbalance):
        self.accountnumber=acno
        self.personname=pname
        self.balance=minbalance
    def deposit(self,amount):
        self.balance+=amount
        print("amount credited with amount",amount,"ava balance is",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("account debited with amount",amount,"ava balance is",self.balance)
obj1=Bank()
obj1.create_account(100,"amal",1000)
obj1.deposit(2000)
obj2=Bank()
obj2.create_account(101,"vijay",2000)
obj2.withdraw(3000)
obj3=Bank()
obj3.create_account(102,"ravi",5000)
obj3.withdraw(3000)

