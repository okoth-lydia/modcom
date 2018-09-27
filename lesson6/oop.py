#  in oop we use classes - a class is a template

#  where code is written

class Account:
    '''docstring - a bank account class'''

    # account states
    def __init__(self, name, balance, branch, type, year, acno):
        self.balance = balance
        self.name = name
        self.branch = branch
        self.type = type
        self.year = year
        self.acno = acno



    # behaviour
    #dep_amount is a parameter
    def deposit(self, dep_ammount):
        if dep_ammount < 100:
            print("you must deposit more than 100")

        else:

            self.balance = dep_ammount + self.balance

            print("you deposited", dep_ammount)

            print("your balance is", self.balance)

#  you can withdraw if withdrw amount is < balance
    def withdraw(self, amount):
        if amount > self.balance:
            print("account balance too low")

        else:
            print("withdrawal successful")

        self.balance = self.balance - amount

        print("the balance is", self.balance)

    def checkbal(self):
        print("account balance is", self.balance)

    def checkdetails(self):
        print(self.name, self.balance, self.branch, self.type, self.year, self.acno)

#  we create the account object and provide the states

    def changebranch(self, newbranch):
        self.branch = newbranch

class LoanAccount(Account):
    def __init__(self, occupation, salary, accno):
        self.occupation = occupation
        self.salary = salary
        self.accno = accno

    def getLoan(self):

        object = LoanAccount(name="miss lee",
                 balance=200,
                 branch="Rongai",
                 type= "personal",
                 year=2015,
                 acno=10002788947)
#object.checkbal()
object.deposit(dep_ammount=2000)
object.withdraw(amount=800)
#object.checkbal()
object.changebranch("Nairobi")`
object.checkdetails()































