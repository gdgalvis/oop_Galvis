from random import randint


class Budget():
    def __init__(self, category :str, innitBal: float) -> None:
        self.category=category
        self.innitBal=innitBal
        self.runningBal= innitBal
    
    def get_running_balance(self) -> float:
        return self.runningBal
    
    def withdraw(self,amount: float) -> None:
        self.runningBal=self.runningBal-amount
    
    def deposit(self,amount: float) -> None:
        self.runningBal=self.runningBal+amount
        
class User():
    def __init__(self, name: str, total_budget: float) -> None:
        self.name=name
        self.total_budget=total_budget
        self.id=randint(1,1000)
        budgets={}
        
    def addBudget(self, category: str, innitBal: float ):
        budget= Budget(category=category,innitBal=innitBal)
        #self.budgets.update(category:budget)