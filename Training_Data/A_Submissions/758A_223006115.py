import os
import sys
import collections
from io import BytesIO, IOBase
from math import ceil,floor,sqrt,sin,cos,tan,factorial,inf,gcd

BUFSIZE=8192
class FastIO(IOBase):
    newlines=0
    def __init__(self, file):
        self._file=file
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="x" in file.mode or "r" not in file.mode
        self.write=self.buffer.write if self.writable else None
    def read(self):
        while True:
            b=os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:break
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()
    def readline(self):
        while self.newlines==0:
            b=os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines=b.count(b"\n")+(not b)
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda s:self.buffer.write(s.encode("ascii"))
        self.read=lambda:self.buffer.read().decode("ascii")
        self.readline=lambda:self.buffer.readline().decode("ascii")
sys.stdin=IOWrapper(sys.stdin)
sys.stdout=IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
cout = sys.stdout.write
data = collections.Counter
queue= collections.deque
endl = lambda:sys.stdout.write("\n")
ii = lambda: int(input())
fi = lambda: float(input())
si = lambda: input().rstrip()
mi = lambda: map(int,input().split())
mf = lambda: map(float,input().split())
msi= lambda: map(str,input().strip().split(" "))
li = lambda: list(mi())
lf = lambda: list(mf())
ls = lambda: list(msi())
set_ii=lambda: set(li())
set_fi=lambda: set(lf())
set_si=lambda: set(input())
def ipow(x,y):return int(pow(x,y))
def maps(arr):return map(str,arr)
def YES(): sys.stdout.write("YES\n")
def Yes(): sys.stdout.write("Yes\n")
def yes(): sys.stdout.write("yes\n")
def NO(): sys.stdout.write("NO\n")
def No(): sys.stdout.write("No\n")
def no(): sys.stdout.write("no\n")
def NOT():sys.stdout.write("NOT\n")
class Solution:
    def __init__(self):
        return
    def solve(self):
        n=ii()
        arr=li()[:n]
        ans=0
        for i in arr:
            ans+=max(arr)-i
        sys.stdout.write(f"{ans}\n")
            




            
        

                




if __name__ == "__main__":
    Solution().solve()