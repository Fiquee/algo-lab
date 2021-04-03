def computeLPSArray(pat, M, lps):
    len = 0

    lps[0]
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # to search step.
            if len != 0:
                len = lps[len-1]

            else:
                lps[i] = 0
                i += 1


def KMP(pat, txt):
    patlen = len(pat)
    txtlen = len(txt)

    lps = [0]*patlen
    j = 0

    computeLPSArray(pat, patlen, lps)

    i = 0  # index for txt[]
    while i < txtlen:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == patlen:
            print("Found pattern at index " + str(i-patlen))
            j = lps[j-1]

        elif i < txtlen and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    print("done iterate")


txt = "ffff"
pat = "fff"
KMP(pat, txt)
