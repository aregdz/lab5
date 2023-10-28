#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = float(input("Введите координату по оси x "))
    b = float(input("Введите координату по оси y "))
    distance = a**2 + b**2
    if 0.25 <= distance <= 1:
        print("Точка принадлежит кольцу")
    else:
        print("Точка не принадлежит кольцу")
