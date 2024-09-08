#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Account:
    rub_dollar_rate = 80
    rub_eur_rate = 90

    def __init__(self, owner, account_number, interest_rate, balance):
        self.__owner = owner
        self.__account_number = account_number
        self.__interest_rate = interest_rate
        self.__balance = balance

    def change_owner(self, new_owner):
        self.__owner = new_owner

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостаточно средств на счете.")
        else:
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def add_interest(self):
        self.__balance += self.__balance * self.__interest_rate

    def convert_to_usd(self):
        return self.__balance * self.rub_dollar_rate

    def convert_to_eur(self):
        return self.__balance * self.rub_eur_rate

    def amount_in_words(self):
        # Реализация преобразования суммы в числительное
        pass

    def display(self):
        print(f"Владелец счета: {self.__owner}")
        print(f"Номер счета: {self.__account_number}")
        print(f"Баланс: {self.__balance} руб")


# Демонстрация возможностей класса
if __name__ == "__main__":
    my_account = Account("Иванов", "10032", 0.05, 1000)
    my_account.display()
    my_account.change_owner("Петров")
    my_account.deposit(500)
    my_account.withdraw(300)
    my_account.add_interest()
    print("\nИзменённый счет:\n")
    my_account.display()
    usd_amount = my_account.convert_to_usd()
    print(f"Баланс в USD: ${usd_amount}")
    eur_amount = my_account.convert_to_eur()
    print(f"Баланс в EUR: €{eur_amount}")
