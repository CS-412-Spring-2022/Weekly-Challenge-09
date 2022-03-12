import random

from cutrod import *


def test_cutrod():
    n = 20
    p = [None] * (n+1)
    p[0] = 0
    for i in range(1, n+1):
        p[i] = p[i-1] + random.randint(0,5)
        rec, memo, bup = cut_rod(p, i), cut_rod_memoize(p, i), cut_rod_bottom_up(p, i)
        assert rec == memo == bup, f'mismatch at {i=}: {rec=}, {memo=}, {bup=}'
