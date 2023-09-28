for r in[*open(0)][1:]:
    print(1440-eval(r.replace(' ','*60+')))