from re import *
from functools import reduce
def main():
    s = lambda p, M: sub(p, '.', M).splitlines()
    with open('input.txt') as f:
        D, K, G = s('[^\d\n]', L:=f.read()), s('[\d]', L), s('[^*\n]', L)
    h = ['.'*(w:=len(D[0])+2)]
    p = lambda M: ''.join(h+[f'.{l}.' for l in M]+h)
    d, k, g = p(D), p(K), p(G)
    S = [(m.start(), m.end()) for m in finditer('[^.]+', d)]
    C = lambda m: [i=='1' for i in sub('[^.]', '1', m)]
    K, G = C(k), C(g)
    c = lambda i, T: {i+j: T[i+j] for j in[-w-1,-w,-w+1,-1,1,w-1,w,w+1]}
    print(sum([int(d[slice(*r)]) for r in S if any([any(c(i, K).values()) for i in range(*r)])]))
    L = {i: set() for i in range(len(G))}
    for r in S: [L[j].add(r) for i in range(*r) for j,v in c(i,K).items() if v]
    prod = lambda l: reduce(lambda x, y: x*y, l, 1)
    print(sum([prod([int(d[slice(*r)]) for r in v]) for _, v in L.items() if len(v)==2]))
if __name__ == '__main__':
    main()