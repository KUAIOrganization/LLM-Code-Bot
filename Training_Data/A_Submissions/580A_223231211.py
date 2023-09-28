n = int(input())
subsegment = list(map(int,input().split()))
if n == len(subsegment):
    lst = []
    for i in range(len(subsegment)-1):
        if subsegment[i] <= subsegment[i+1]:
            lst.append(1)
        else:
            lst.append(0)
    word = "".join(list(map(str,lst)))
    word_lst = word.split("0")
    num = max([len(letter) for letter in word_lst])
    print(num+1)