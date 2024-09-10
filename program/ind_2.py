#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу с использованием классов и объектов
# для решения задачи. Во всех заданиях, помимо указанных
# в задании операций, обязательно должны быть реализованы следующие методы:
# метод инициализации __init__ ;
# ввод с клавиатуры read ;
# вывод на экран display .
# Реализовать класс Account, представляющий собой банковский счет.
# В классе должны быть четыре поля: фамилия владельца, номер счета,
# процент начисления и сумма в рублях.
# Открытие нового счета выполняется операцией инициализации.
# Необходимо выполнять следующие операции: сменить владельца счета,
# снять некоторую сумму денег со счета,
# положить деньги на счет, начислить проценты,
# перевести сумму в доллары, перевести сумму
# в евро, получить сумму прописью (преобразовать в числительное).


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
        sl_n = [
            {
                0: "ноль",
                1: "один",
                2: "два",
                3: "три",
                4: "четыре",
                5: "пять",
                6: "шесть",
                7: "семь",
                8: "восемь",
                9: "девять",
            },
            {
                1: "десять",
                2: "двадцать",
                3: "тридцать",
                4: "сорок",
                5: "пятьдесят",
                6: "шестьдесят",
                7: "семьдесят",
                8: "восемьдесят",
                9: "девяносто",
            },
            {
                1: "сто",
                2: "двести",
                3: "триста",
                4: "четыреста",
                5: "пятьсот",
                6: "шестьсот",
                7: "семьсот",
                8: "восемьсот",
                9: "девятьсот",
            },
            {
                1: "тысяча",
                2: "две тысячи",
                3: "три тысячи",
                4: "четыре тысячи",
                5: "пять тысяч",
                6: "шесть тысяч",
                7: "семь тысяч",
                8: "восемь тысяч",
                9: "девять тысяч",
            },
            {
                1: "одиннадцать",
                2: "двенадцать",
                3: "тринадцать",
                4: "четырнадцать",
                5: "пятнадцать",
                6: "шестнадцать",
                7: "семнадцать",
                8: "восемнадцать",
                9: "девятнадцать",
            },
        ]

        bal = list(map(int, str(self.__balance)))
        bal.reverse()
        list_bal = []
        if len(bal) == 1:
            str_bal = sl_n[bal[0]]
        elif len(bal) < 5:
            prew = 0
            for count, i in enumerate(bal):
                if (count == 1) and (i == 1) and (prew != 0):
                    list_bal[0] = sl_n[-1][prew]
                else:
                    val = sl_n[count].get(i, None)
                    if val:
                        list_bal.append(val)
                prew = i
            list_bal.reverse()
            str_bal = " ".join(list_bal)
        else:
            print("Сумма больше 99999")
            return None

        return str_bal

    def display(self):
        print(f"Владелец счета: {self.__owner}")
        print(f"Номер счета: {self.__account_number}")
        print(f"Баланс: {self.__balance} руб")


# Демонстрация возможностей класса
if __name__ == "__main__":
    my_account = Account("Иванов", "10032", 0.05, 9045)
    my_account.display()
    # my_account.change_owner("Петров")
    # my_account.deposit(500)
    # my_account.withdraw(300)
    # my_account.add_interest()
    # print("\nИзменённый счет:\n")
    # my_account.display()
    # usd_amount = my_account.convert_to_usd()
    # print(f"Баланс в USD: ${usd_amount}")
    # eur_amount = my_account.convert_to_eur()
    # print(f"Баланс в EUR: €{eur_amount}")
    word = my_account.amount_in_words()
    print(f"Сумма в рублях: {word}")
