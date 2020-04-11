#!/usr/bin/env python
# coding: utf-8

# В этом задании создайте класс банковского счета, который имеет два атрибута 
 		# owner - владелец
 		# balance - баланс 
# и два метода
		# deposit - внести средства
		# withdraw - снять средства
# Дополнительные условия - сумма снятия не должна превышать доступный баланс. 

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, cash):
        self.balance+=cash
        print('Внесение выполнено')
    
    def withdraw(self, cash):
        if self.balance>=cash:
            self.balance-=cash
            print('Снятие выполнено')
        else:
            print('Недостаточно средств')
        
    def __str__(self):
        return f"Владелец счета: {self.owner}\nБаланс счета: ${self.balance}"
    
acc1 = Account('Влад', 100)
acc1.balance
acc1.owner
print(acc1)
acc1.deposit(100)
acc1.balance
acc1.withdraw(75)
acc1.balance
acc1.withdraw(300)