
s = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            i = c 
            s = s + i
    print(s)
        