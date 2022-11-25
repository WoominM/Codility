import string

def solution(N):
    # write your code in Python 3.8.10
    binum = convert(N, 2)
    idx = []
    for i in range(len(binum)):
        if binum[i] == '1':
            idx.append(i)
            
    if len(idx) < 2:
        return 0
    else:
        out = 0
        for i in range(1, len(idx)):
            out = max(out, idx[i] - idx[i-1] - 1)
        return out


def convert(N, mod):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(N, mod)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, mod) + tmp[r]