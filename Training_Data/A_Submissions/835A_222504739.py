s, v1, v2, t1, t2 = map(int, input().split())
 
x1 = 2 * t1 + s * v1
x2 = 2 * t2 + s * v2
 
if x1 < x2:
    print("First")
elif x2 < x1:
    print("Second")
else:
    print("Friendship")