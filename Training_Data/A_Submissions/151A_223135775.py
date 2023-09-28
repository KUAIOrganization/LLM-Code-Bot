
line = [int(i) for i in input().split()]

n, k, l, c, d, p, nl, np = tuple(line)

drink = k*l
limonSlices = c*d
tostdrink = drink//nl
tostlimon = limonSlices
tostsalt = p//np
print((min(tostsalt, tostdrink, tostlimon))//n)