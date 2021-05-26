# txt = AAAABAABABA
# pat = AAAA


def KMPSearch(pat, txt):
    m = len(pat)
    n = len(txt)

    lps = [0] * m
    j = 0  # index for pat[]
    i = 0  # index for txt[]

    while i < n:  # checking first index of pat and length as both starting from 0
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:  # if length of pattern and j is the same, pattern found
            print(pat + " is found at index " + str(i - j)) #j=4
            j = lps[j - 1] #untuk index next "search"

        elif i < n and pat[j] != txt[i]:  # if match not found
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


text = "algorithmisfun"
pattern = "fun"
KMPSearch(pattern, text)
