from math import floor

import math
from math import *
from math import factorial, fabs
from decimal import *
eps = 0.0000001


class FunctionUndefinedException(Exception):
    pass


def check(fun1, fun2, point):
    print(fun1(point), fun2(point), sep='\t~\t')


def my_cos(x):
    my_sum = 0
    old = 0
    new = 1  # for n == 0
    n = 0
    while math.fabs(new - old) >= eps:

        my_sum += new

        old = new
        new = new * ((-1) * (x ** 2)) / ((2 * n + 1) * (2 * n + 2))
        n += 1
    return my_sum


def my_sin(x):
    my_sum = 0
    old = 0
    new = x  # for n == 0
    n = 0
    while math.fabs(new - old) >= eps:

        my_sum += new

        old = new
        new = new * ((-1) * (x ** 2)) / ((2 * n + 2) * (2 * n + 3))
        n += 1
    return my_sum


def my_tg(x):
    return my_sin(x) / my_cos(x)


def my_asin(x):
    if fabs(x) > 1:
        raise Exception('Function is undefined at this point.')

    my_sum = 0
    old = 0
    new = x
    n = 0
    while math.fabs(new - old) >= eps:

        my_sum += new / (2*n + 1)

        old = new
        new = new * ((2*n + 1) * (2*n + 2) * (x**2)) / (4 * ((n + 1) ** 2))
        n += 1
    return my_sum


def my_acos(x):  # pi/2 - asinx
    return math.pi/2 - my_asin(x)


def my_atg(x):
    if fabs(x) > 1:
        raise Exception('Function is undefined at this point.')
    my_sum = 0
    old = 0
    new = x  # for n == 0
    n = 1
    while math.fabs(new - old) >= eps:
        my_sum += new / (2*n-1)

        old = new
        new = new * (-1) * (x ** 2)
        n += 1
    return my_sum


def my_cosh(x):
    my_sum = 0
    old = 0
    new = 1
    n = 0
    while math.fabs(new - old) >= eps:
        my_sum += new
        old = new
        new = new * (x**2 / ((2*n + 1) * (2*n + 2)))
        n += 1
    return my_sum


def my_sinh(x):
    my_sum = 0
    old = 0
    new = x
    n = 0
    while math.fabs(new - old) >= eps:
        my_sum += new
        old = new
        new = new * (x**2 / ((2*n + 2) * (2*n + 3)))
        n += 1
    return my_sum


def my_tgh(x):
    return my_sinh(x) / my_cosh(x)


def my_acosh(x):
    if x <= 1:
        raise Exception('Function is undefined at this point.')
    my_sum = 0
    old = 0
    new = 1/(4 * (x**2))
    n = 1
    while math.fabs(new - old) >= eps:
        my_sum += new / (2 * n)
        old = new
        new = new * ((2*n + 1)*(2*n + 2)) / (4 * ((n + 1) ** 2) * (x**2))
        n += 1
    res = math.log(2*x) - my_sum
    return res


def my_asinh(x):
    if math.fabs(x) >= 1:
        raise Exception('Function is undefined at this point.')
    my_sum = 0
    old = 0
    new = x
    n = 0
    while math.fabs(new - old) >= eps:
        my_sum += new / (2 * n + 1)
        old = new
        new = new * (-(2*n + 1)*(2*n + 2)*(x**2)) / (4 * ((n + 1) ** 2))
        n += 1
    return my_sum


def my_atgh(x):
    if math.fabs(x) >= 1:
        raise Exception('Function is undefined at this point.')
    my_sum = 0
    old = 0
    new = x
    n = 0
    while math.fabs(new - old) >= eps:
        my_sum += new / (2*n+1)
        old = new
        new = new * (x ** 2)
        n += 1
    return my_sum


check(my_cos, cos, -math.pi)
check(my_sin, sin, 34)
check(my_tg, tan, 25)

check(my_acos, acos, 0.3)
check(my_asin, asin, -0.4)
check(my_atg, atan, 0.9)

check(my_cosh, cosh, -math.pi)
check(my_sinh, sinh, 34)
check(my_tgh, tanh, 25)

check(my_acosh, acosh, 33)
check(my_asinh, asinh, -0.5)
check(my_atgh, atanh, 0.5)

