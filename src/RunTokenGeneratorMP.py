from Tokenization.TokenGeneratorMPContinuous import TokenGeneratorDriverMP

# Normally I would do 5 tokens per round, but the dataset is so small that if we do more than one, we might end up missing some because
# of the protections to prevent selecting overlapping tokens.
gen = TokenGeneratorDriverMP("C:\\AIClub\\Code\\ModelTesting", 100, 1, threads=3, allowWhitespace=False, removesBeforeClean=20, allowTextAndSpecial=False)

if __name__ == "__main__":
    gen.initTokens()
    try:
        gen.run()
    except RuntimeError:
        print("Max legal tokens achieved!")
    print(gen.getCanonList())