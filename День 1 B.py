t1 = [60, 40, 100]
t2 = [200, 50, 80]
ans = []
for i in range(3):
    val = 3 * t1[i] - 1 * t2[i]
    val = max(0, min(255, val))
    ans.append(val)
print(ans)
