arr = [i for i in input()[1:-1].split(", ")]


def main(arr):
    if len(arr) == 1 and not arr[0]:
        return 0
    return len(set(arr))

print(main(arr))