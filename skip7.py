#!/usr/bin/env python3
a=1
while a < 101:
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7 :
        pass
    else:
        print(a, end=' ')
    a+=1
