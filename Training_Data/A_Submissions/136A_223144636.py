from sys import stdin
input = stdin.readline


if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    res = [0]*n
    for i, v in enumerate(data):
        res[v-1] = i+1
    print(*res)
	   	  	    		   			  		  		  	