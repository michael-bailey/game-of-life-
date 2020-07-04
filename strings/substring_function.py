def subStrings(S):
    print(S)
    letters = []
    
    for i in range(len(S)):
        if len(S) == 1:
            return 1
            
        elif S[i] in letters:
            return subStrings(S[i:])+1
            
        else:
            letters.append(S[i])
        
    return 1

subStrings("dddd")
