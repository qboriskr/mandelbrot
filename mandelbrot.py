def rpt(f, n, x):
    if n == 0:
        return x
    return rpt(f, n - 1, f(x))


def mult(a, b, c, d):
    return a * c - b * d, a * d + b * c


def sum(a, b):
    return a[0] + b[0], a[1] + b[1]


def m(z, c):
    return sum(mult(*z, *z), c)


def m_c(c):
    return lambda z: m(z, c)


def scale(xs, ys, i, j):
    n = 50
    return (j - ys) / n, 2 * (i - xs) / n,


def sqrad(c):
    return c[0] * c[0] + c[1] * c[1]


xs = 80
ys = 160
di = 0
colors = " .:-=+*#%@"
for i in range(xs):
    for j in range(ys):
        c = sqrad(rpt(m_c(scale(xs / 2, ys / 2, i - di, j)), 10, (0, 0)))
        s = colors[int(c * 10)] if c < 1.0 else " "
        print(s, end="")
    print()
