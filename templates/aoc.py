from collections import *
from heapq import *
from bisect import *
from math import *
from sys import stdin
from functools import *
def rl(f=int):
    return list(map(f, input().split()))
def rn(f=int):
    return f(input())
def rls():
    return [line.strip() for line in stdin.readlines()]
def pj(line):
    ''.join(map(str,line))

mx=my=-inf
Mx=My=inf
lines = rls()
for line in lines:
    
