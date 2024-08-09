import random
import datetime
import solution2

ar = [random.randint(-100, 100) for _ in range(4096)]

def naiveRangeSum(ar,L,R):
    sum=0
    for i in range(L,R+1):
        sum += ar[i]
    return sum


qrs = []
for i in range(50):
    l = random.randint(0,len(ar)/2)
    r = l + random.randint(0,len(ar)-l-1)
    qrs.append((l,r))

t0 = datetime.datetime.now()
ns=0
for i in range(50):
    l = qrs[i][0]
    r = qrs[i][1]
    ns+= naiveRangeSum(ar,l,r)
t1 = datetime.datetime.now()
naive_dt = t1 -t0

solution2.setArray(ar)

t0 = datetime.datetime.now()
s=0
for i in range(50):
    l = qrs[i][0]
    r = qrs[i][1]
    s+= solution2.rangeSum(l,r)
t1 = datetime.datetime.now()
dt = t1 -t0

print(f"naive time: {naive_dt.microseconds} ms")
print(f"your time: {dt.microseconds} ms")

if s!=ns: 
    print("you didn't get the same sum (-100)")
elif naive_dt.microseconds <= dt.microseconds * 2:
    print("you didn't improve the time (-100)")




print('done')
