class Candless:
    def __init__(self,num_candles,num_candles_makenew):
        self.num_candles = num_candles
        self.num_candles_makenew = num_candles_makenew
        self.burn_candles = 0
        self.hours = 0

    def burn(self):
        while True:
            self.hours+=self.num_candles
            if self.num_candles<self.num_candles_makenew:
                self.burn_candles+=self.num_candles
                if self.burn_candles<self.num_candles_makenew:
                     break
                else:
                    self.num_candles=int(self.burn_candles/self.num_candles_makenew)
                    self.burn_candles = self.burn_candles%self.num_candles_makenew
            else:
                self.burn_candles+= (self.num_candles%self.num_candles_makenew)
                self.num_candles = int(self.num_candles/self.num_candles_makenew)

    def get_hours(self):
        print(self.hours)

c , n = map(int, input().split(' '))
C = Candless(c,n)
C.burn()
C.get_hours()