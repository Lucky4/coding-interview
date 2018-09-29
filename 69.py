import math


def func(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


# 从2到n的开方之间的任何数只要有一个数被n整除，那么n就不是素数，否则n是素数。