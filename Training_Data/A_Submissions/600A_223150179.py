import sys
import re
s = ""
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    s = line
s = s.strip()
v = re.split(';|,', s)
nums = ""
other = ""
for c in v:
    try:
        for n in c:
            if(n < '0' or n >'9'):
                raise Exception
        if((c[0] == '0' and len(c) > 1 )):
            raise Exception
        nums += c + ","
    except:
        other += c + ","
if(nums == ""):
    print("-")
else:
    print("\""+nums[:-1]+"\"")
if(other == ""):
    print("-")
else:
    print("\""+other[:-1]+"\"")
		  	    	   			 	 			 					  	