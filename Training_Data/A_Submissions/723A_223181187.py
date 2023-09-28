hl = list(map(int,input().split()))
def dis(startpoint, i):
    return abs(startpoint - i)
disl = set()
# for j in range(3):
#     temp = 0
#     for i in range(3):
#         if j !=2:
#             temp += dis(hl[i] , hl[j] , hl[j+1])
#         else:
#             temp += dis(hl[i], hl[2], hl[0])
#     disl.add(temp)
# print(min(disl))        
for i in range(min(hl),max(hl)):
    disl.add(dis(hl[0],i)+dis(hl[1],i)+dis(hl[2],i))
print(min(disl))