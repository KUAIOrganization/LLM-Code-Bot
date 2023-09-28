n, x = [int(i) for i in input().split()]

records = []

for _ in range(n):
    records.append(input().split(" "))

def main(x, records):
    distress = 0
    for i in records:
        if i[0] == "+":
            x += int(i[1])
            continue
        if i[0] == "-" and int(i[1]) <= x:
            x -= int(i[1])
        else:
            distress += 1

    return x, distress

print(*main(x, records))