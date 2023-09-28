def rook_moves():
    if(r1 == r2 or c1 == c2):
        return 1
    return 2

def bishop_moves():
  if ((r1+c1) % 2 != (r2+c2) % 2): # Starting and ending cells are different color.
    return 0
  if (abs(r1-r2)==abs(c1-c2)):
    return 1
  return 2

def king_moves():
    return max(abs(r2-r1), abs(c2-c1))
    
r1, c1, r2, c2 = map(int, input().split(" "))
print(rook_moves(), bishop_moves(), king_moves())