len_initial = int(input())
Sequence = input()
def my_func(my_str):
    up_counter = 0
    right_counter = 0
    for i in range(len(my_str)):
        if my_str[i] == "U":
            up_counter += 1
        elif my_str[i] == "D":
            up_counter -= 1
        elif my_str[i] == "R":
            right_counter += 1
        else:
            right_counter -= 1
    if up_counter == 0 and right_counter == 0:
        return 1
    else:
        return 0
counter = 0
for i in range(len_initial):
    for j in range(i + 2, len_initial + 1, 2):
        counter += my_func(Sequence[i:j])
print(counter)