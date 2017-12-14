#!/usr/bin/env python3
# coding: utf8 albo # -*- coding: utf-8 -*-
import math
import time

# funkcja wyznaczajaca liczby pierwsze za pomoca list skladanych
def pierwsze_skladane2(n):
    prime = [x for x in range(2, n) if all(x % y != 0 for y in range(2, math.floor(math.sqrt(x)+1)))]
    return prime

# funckja wyznaczajaca liczby pierwsze za pomoca list skladanych inny sposob
def pierwsze_skladane(n):
    compleks = [x*k for x in range(2, n+1) for k in range(2, n+1)]
    prime = [x for x in range(2, n + 1) if x not in compleks]
    return prime

# funckja wyznaczajaca liczby pierwsze za pomoca list funkcyjnych
def pierwsze_funkcyjne(n):
    prime = list(filter(lambda x: all(x % y != 0 for y in range(2, math.floor(math.sqrt(x)+1))), range(2, n)))
    return prime

# funkcja sprawdzajaca czy liczba jest pierwsza
def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# iterator
class Iter(object):
    def __init__(self):
        self.c = 1

    def __next__(self):
        self.c += 1
        while not(is_prime(self.c)):
            self.c += 1
        return self.c


if __name__ == "__main__":

    it = Iter()

    x = time.time()*1000
    pierwsze_funkcyjne(10)
    x1 = time.time()*1000 - x
    x = time.time()*1000
    z = pierwsze_skladane2(10)

    x2 = time.time()*1000 - x
    x = time.time()*1000
    for i in range(10):
        if it.__next__() > 10:
            break
    x3 = time.time()*1000 - x
    print("     | funkcyjna | skladana | iterator")
    print("  10 |", "%1.2f" % x1, "     |", "%1.2f" % x2,  "    |", "%1.2f" % x3, end=" ")

    print("")
    x = time.time()*1000
    pierwsze_funkcyjne(100)
    x1 = time.time()*1000 - x
    x = time.time()*1000
    pierwsze_skladane2(100)
    x2 = time.time()*1000 - x
    x = time.time()*1000
    for i in range(100):
        if it.__next__() > 100:
            break
    x3 = time.time()*1000 - x
    print(" 100 |", "%1.2f" % x1, "     |", "%1.2f" % x2,  "    |", "%1.2f" % x3, end=" ")

    print("")
    x = time.time()*1000
    pierwsze_funkcyjne(1000)
    x1 = time.time()*1000 - x
    x = time.time()*1000
    pierwsze_skladane2(1000)
    x2 = time.time()*1000 - x
    x = time.time()*1000
    for i in range(1000):
        if it.__next__() > 1000:
            break
    x3 = time.time()*1000 - x
    print("1000 |", "%1.2f " % x1, "     |", "%1.2f" % x2, "    |", "%1.2f" % x3, end=" ")

    print()
    #print(pierwsze_skladane2(100))
    #print(pierwsze_funkcyjne(100))
