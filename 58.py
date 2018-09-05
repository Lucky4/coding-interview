# -*- coding: utf-8 -*-


def func(s):
    if len(s) == 1:
        return 1
    
    if len(s) == 2:
        if int(s) <= 26:
            return 2
        return 1

    return func(s[1:]) + (func(s[0:2])-1) * func(s[2:])


# print func('12258')