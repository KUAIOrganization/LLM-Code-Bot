from TokenGenerator import TokenGenerator
import os

def main():
    gen = TokenGenerator("C:\\AIClub\\Code\\IsPrime", 52, 5, allowWhitespace=False, allowTextAndSpceial=False)
    gen.initTokens()
    try:
        gen.genTokens()
    except RuntimeError:
        print("Max legal tokens achieved!")
    print(gen.getCanonList())
    
if __name__ == "__main__":
    main()