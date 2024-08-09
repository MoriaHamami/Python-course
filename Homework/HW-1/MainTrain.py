from datetime import date
from solution1 import *

d1 = (2024,4,2)
d2 = (2022,11,9)
dd1 = date(d1[0],d1[1],d1[2])
dd2 = date(d2[0],d2[1],d2[2])
delta = dd1 - dd2

if calcDays(d1,d2) != abs(delta.days):
    print(f"you got a wrong result for {d1} , {d2} (-50)")

if calcDays(d2,d1) != abs(delta.days):
    print(f"you got a wrong result for {d2} , {d1} (-50)")


print("done")
