"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,contract, commission =  None):
        self.name = name
        self.contract  =  contract
        self.commission = commission

    def set_hourly_contract(self,hourly_wage, hours):
        self.hourly_wage = hourly_wage
        self.hours = hours

    def  set_monthly_contract(self,salary):
        self.salary = salary

    def set_bonus_commission(self, bonus_value ):
        self.bonus_value  = bonus_value

    def set_contract_commission(self, contracts , contract_price ):
        self.contracts = contracts
        self.contract_price = contract_price

    def get_pay(self):
        if self.contract == "monthly":
            if not self.commission:
                return self.salary
            elif self.commission == 'contract':
                return self.salary + (self.contracts * self.contract_price)
            else:
                return self.salary + self.bonus_value
        else:
            if not self.commission:
                return self.hourly_wage * self.hours
            elif self.commission == 'bonus':
                return self.hourly_wage * self.hours +  self.bonus_value
            else:
                return  self.hourly_wage * self.hours  + (self.contracts *  self.contract_price)



    def __str__(self):
        if self.contract == 'monthly':
            if not self.commission:
                return (f'{self.name} works on a {self.contract} salary of {self.salary}.  Their total pay is {self.get_pay()}.')
            elif self.commission == 'contract':
                 return (f'{self.name} works on a {self.contract} salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.contract_price}/contract.  Their total pay is {self.get_pay()}.')
            else:
                return (f'{self.name} works on a {self.contract} salary of {self.salary} and receives a bonus commission of {self.bonus_value}.  Their total pay is {self.get_pay()}.')
        else:
            if not self.commission:
                return (f'{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour.  Their total pay is {self.get_pay()}.')
            elif self.commission == 'contract':
                return (f'{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour and receives a commission for {self.contracts} contract(s) at {self.contract_price}/contract.  Their total pay is {self.get_pay()}.')
            else:
                return (f'{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus_value}.  Their total pay is {self.get_pay()}.')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly')
billie.set_monthly_contract(4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie','hourly')
charlie.set_hourly_contract(25,100)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly','contract')
renee.set_monthly_contract(3000)
renee.set_contract_commission(4,200)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly','contract')
jan.set_hourly_contract(25,150)
jan.set_contract_commission(3,220)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 'bonus')
robbie.set_monthly_contract(2000)
robbie.set_bonus_commission(1500)
print(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','hourly','bonus')
ariel.set_hourly_contract(30,120)
ariel.set_bonus_commission(600)
print(ariel)
