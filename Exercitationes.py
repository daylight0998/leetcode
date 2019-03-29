#!/usr/bin/python3
# encoding: utf-8
import random
from datetime import timedelta, date

# compute 函数计算输出题目 i 为距今天的天数；f 为算式第一个值；s 为算式第二个值


def compute(i, f, s):
    print('%s:' % (date.today() + timedelta(i)), end="\n")
    for j in range(15):
        symbol = random.choice(['+', '-'])
        first = random.randint(1, f)
        second = random.randint(1, s)
        if (first > second) or (symbol != '-'):
            print('%d %s %d =' % (first, symbol, second))


# go 函数定义不同天数阶段做不同难度题, 调用 compute 函数输出算式。


def go():
    for i in range(30):
        if i <= 10:
            compute(i, 10, 10)
        elif 10 < i < 20:
            compute(i, 20, 10)
        else:
            compute(i, 20, 20)
        print("\n", end="")


go()

