k_dragon = int(input())
l_dragon = int(input())
m_dragon = int(input())
n_dragon = int(input())
b_dragon = int(input())
massive = []
count_suffered_dragons = 0
for i in range(1, b_dragon+1):
    massive.append(i)
for i in range(b_dragon):
    if massive[i] % k_dragon == 0:
        count_suffered_dragons += 1
    elif massive[i] % l_dragon == 0:
        count_suffered_dragons += 1
    elif massive[i] % m_dragon == 0:
        count_suffered_dragons += 1
    elif massive[i] % n_dragon == 0:
        count_suffered_dragons += 1
print(count_suffered_dragons)
    
        
        
