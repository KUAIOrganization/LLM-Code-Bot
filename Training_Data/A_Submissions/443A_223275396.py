x = input()
lis = []
for i in range(len(x)):
    if x[i] != " " and x[i] != "," and x[i] != "{" and x[i] !="}":
        lis.append(x[i])
lis = list(set(lis))
print(len(lis))