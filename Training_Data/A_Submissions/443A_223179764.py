a = [i for i in input()[1:-1].split(", ")]
 
 
def main(a):
    if len(a) == 1 and not a[0]:
        return 0
    return len(set(a))
 
print(main(a))