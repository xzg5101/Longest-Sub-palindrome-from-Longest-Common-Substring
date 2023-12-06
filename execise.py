import math


def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for i in range(m+1)]
    C = [[""]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
                C[i][j] = ""
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                C[i][j] = C[i-1][j-1]+X[i-1]
            else:
                if L[i-1][j] > L[i][j-1]:
                    L[i][j] = L[i-1][j]
                    C[i][j] = C[i-1][j]
                else:
                    L[i][j] = L[i][j-1]
                    C[i][j] = C[i][j-1]
    return L[m][n], C[m][n]


def lps_w(s):
    r = s[::-1]
    l = lcs(s, r)
    return l[0:math.ceil(len(l)/2)] + (l[math.ceil(len(l)/2):])[::-1]


def lps(s):
    R = s[::-1]

    dp = [[0] * (len(R) + 1) for _ in range(len(s) + 1)]
    c = [[""] * (len(R) + 1) for _ in range(len(s) + 1)]
    ts = [[(-1, -1, -1)] * (len(R) + 1) for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(R) + 1):
            if s[i - 1] == R[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                c[i][j] = c[i-1][j-1] + s[i-1]
                ts[i][j] = (i-1, j-1, i-1)
            else:
                if dp[i][j - 1] > dp[i - 1][j]:
                    dp[i][j] = dp[i][j - 1]
                    c[i][j] = c[i][j-1]
                    ts[i][j] = (i, j-1, -1)
                else:
                    dp[i][j] = dp[i - 1][j]
                    c[i][j] = c[i-1][j]
                    ts[i][j] = (i-1, j, -1)
    ss = ""
    t = ts[len(s)][len(R)]
    while t[0] >= 0:
        if t[2] >= 0:
            ss = ss + s[t[2]]
        t = ts[t[0]][t[1]]

    return dp[len(s)][len(R)], ss


X = "AGGTAB"
Y = "GXTXAYB"
Z = "SYUITGBVFSJKTG"
W = "JSGNIRUTAGHNERJFHNAMEDFYHGJVKBLNKJUYTRDCHVUBYTVHGYJHLKNIUHUTRFXCFVRUCYITMLTRKLFGJMAFR"

# JSGNIRUTAGHNERJFHNAMEDFYHGJVKBLNKJUYTRDCHVUBYTVHGYJHLKNIUHUTRFXCFVRUCYITMLTRKLFGJMAFR
# |||-|-|------|-|||----------|-|--|-|----|||---||-||-|||--|---|----||--|--------||----
# -----|---------|--||------|-|--------|-------|------|--||---||-||-||--|---||||--|||||

#l, c = lcs(X, Y)
#print("The Len of LCS is", l, "  lcs is", c)

print("lsp of X is", lps(W))
print("lsp_w of X is", lps_w(W))
