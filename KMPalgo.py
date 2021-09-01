# find occurance of pat in txt
# tut - https://www.youtube.com/watch?v=4jY57Ehc14Y

# Longest prefix that is also a suffix
def computeLPSArray(pat,m,lps):
    len = 0
    i = 1
    lps[0] = 0
    while i < m:
        if pat[i] == pat[len]:
            lps[i] = len + 1
            len += 1
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

def KMPSearch(pat,txt):
    N = len(txt)
    M = len(pat)
    lps = [0]*M
    computeLPSArray(pat,M,lps)
    i,j = 0,0
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if i == M:
            print(i-j)
            j = lps[j-1]