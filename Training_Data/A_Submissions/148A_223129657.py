k_dragon = int(input())
l_dragon = int(input())
m_dragon = int(input())
n_dragon = int(input())
col_dragons = int(input())
dragons = [_ for _ in range(1, col_dragons + 1)]
victims_dragons = 0

for dragon in dragons:
    if dragon % k_dragon == 0:
        victims_dragons += 1
        continue
    elif dragon % l_dragon == 0:
        victims_dragons += 1
        continue
    elif dragon % m_dragon == 0:
        victims_dragons += 1
        continue
    elif dragon % n_dragon == 0:
        victims_dragons += 1
        continue
print(victims_dragons)


