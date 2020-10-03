def unique_paths(n, m):
    m, n = min(m, n), max(m, n)
    lvl = m + n - 2
    pos = m - 1
    comb = 1

    # combinations formula C(N, R) = N! / R! * (N - R)!
    for i in range(1, pos + 1):
        comb *= lvl
        comb /= i
        lvl -= 1

    return int(comb + 0.001)
