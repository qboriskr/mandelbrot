def rpt(f, n, x):
    if n == 0:
        return x
    return rpt(f, n - 1, f(x))


def m(z, c):
    return z *z + c


def m_c(c):
    return lambda z: m(z, c)


def scale_and_rotate(xs, ys, i, j):
    n = 50
    return complex((j - ys) / n, 2 * (i - xs) / n)


xs = 80
ys = 160
di = 0
colors = " .:-=+*#%@"
for i in range(xs):
    for j in range(ys):
        try:
            c = abs(rpt(m_c(scale_and_rotate(xs / 2, ys / 2, i - di, j)), 10, complex(0, 0)))
        except:
            c=2
        s = colors[int(c * 10)] if c < 1.0 else " "
        print(s, end="")
    print()
