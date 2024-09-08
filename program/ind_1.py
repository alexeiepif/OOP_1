#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Time:
    def __init__(self, first=0, second=0):
        self.__first = first
        self.__second = second

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(":")))
        if len(parts) != 2:
            raise ValueError("Неправильный формат времени")
        self.__first, self.__second = parts

    def display(self):
        print(f"{self.__first}:{self.__second:02}")

    def minutes(self):
        return self.__first * 60 + self.__second


def make_time(hours=0, minutes=0):
    if not (0 <= hours < 24 and isinstance(hours, int)):
        raise ValueError("Неправильное количество часов")
    if not (0 <= minutes < 60 and isinstance(minutes, int)):
        raise ValueError("Неправильное количество минут")
    return Time(hours, minutes)


if __name__ == "__main__":
    t1 = make_time(20, 30)
    t1.display()
    print(t1.minutes())
    t2 = make_time()
    t2.read("Введите время: ")
    t2.display()
    print(t2.minutes())
