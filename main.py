import sylls
if __name__ == "__main__":
    sb = sylls.Syll_Builder().return_all_sylls()
    count = 0
    for syll in sb:
        if syll.valid():
            count +=1
    print(count)
    '''s = sylls.Syll("a","i","o",1)
    for i in range(4):
        print(s.check_rule(i+1))'''