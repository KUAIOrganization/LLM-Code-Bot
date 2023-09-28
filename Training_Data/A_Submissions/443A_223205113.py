Set =  set(input())
if "," in Set and "{" in Set : 
    Set.remove(",")
    Set.remove(" ")
    Set.remove("{")
    Set.remove("}")    
else :
    Set.remove("{")
    Set.remove("}")
    
print(len(Set))
