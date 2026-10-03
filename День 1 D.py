pt = [(0, 8), (0, 7), (0, 2), (0, 0), (4, 7), (4, 4), (6, 5),
          (6, 1), (9, 7), (9, 4), (9, 1), (9, 0), (11, 6), (11, 2)]
ans = -1
for i in range(len(pt)):
    for j in range(i + 1, len(pt)):
        x1, y1 = pt[i]
        x2, y2 = pt[j]
        if x1 == x2:
            continue
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        tot = sum(abs(a * x + b - y) for x, y in pt)
        if ans == -1 or tot < ans:
            ans = tot

print(round(ans / len(pt), 6))
