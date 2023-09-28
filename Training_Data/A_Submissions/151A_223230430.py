import math

n, k, l, c, d, p, nl, np = map(int, input().split())

ml_of_drink = k * l               #1
no_of_toasts = ml_of_drink // nl  #2
limes_for_toasts = c * d          #3
salt_for_toasts = p // np         #4

Toasts = min(no_of_toasts, limes_for_toasts, salt_for_toasts) / n

Toasts = math.floor(Toasts)

print(Toasts)