import sys
print('#Color' if set('CMY')&set(sys.stdin.read())else '#Black&White')