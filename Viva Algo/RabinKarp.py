def Rabinkarp(text, pattern):
    textlen = len(text)
    patternlen = len(pattern)
    hp = 10**(patternlen-1)
    p = 0  # hash value for pattern
    t = 0  # hash value for text

    for i in range(patternlen):
        p += ord(pattern[i])*(10**(patternlen-i-1))  # hash value for pattern
        t += ord(text[i])*(10**(patternlen-i-1))  # first pattern in text

    for j in range(textlen-patternlen+1):
        if(t == p):
            if(pattern == text[j:j+patternlen]):
                print("fun is found after shifting", j, "times")
        else:  # shifting
            t = ((t - ord(text[j])*hp) * 10) + ord(text[j+patternlen])


text = "algorithmfun"
Rabinkarp(text, "fun")
