#!/usr/bin/env python3

import numpy as np

s=np.lib.index_tricks.RClass()
print(s)
print(s[0])
print(s[1])
print(s[1:20])
print(s[1:20:2])
print(s[1:20:2j])
print(s[1:20:20j])
print(s[1:20:100j])

