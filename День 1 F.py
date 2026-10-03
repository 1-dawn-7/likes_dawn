import random

m = {"A": "MD", "E": "TSM", "I": "TSM", "T": "LN", "M": "LN",
       "N": "AI", "D": "AI", "S": "EID", "L": "EID"}

def f():
    la = "S"
    st = 0
    while True:
        new = random.choice(m[la])
        st += 1
        if la == "M" and new == "L":
            return st
        la = new

random.seed(73)
n = 1000000
ans = 0
for i in range(n):
    ans += f()
print(round(ans / n, 2))
