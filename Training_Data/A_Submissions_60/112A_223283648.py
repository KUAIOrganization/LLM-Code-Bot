#n=input().lower()
#m=input().lower()#注意注意！！！！这里先让所有都小写，目的就是为了让后文的sort比较的时候能够不受大写的影响！！
#num=0
#for i in range(len(n)):
#    l = [n[i], m[i]]#注意第几个，这里要十分熟练！！！
#    if n[i]==m[i]:#等价！！！
#        num+=0
#    elif sorted(l)==[n[i],m[i]]:
#        num+=-1
#    else:
#        num+=1
#print(num)
#以上内容是我所想象的代码，就是认为字符串中每一个都需要比较，但是他根本就不需要比较！！！只要找到第一个不一样的就可以了！！！
#另外看ceshi.py你会学到更多！
n=input().lower()
m=input().lower()
list_n=list(n)
list_m=list(m)
if list_n>list_m:
    print(1)
elif list_n==list_m:
    print(0)
else:
    print(-1)