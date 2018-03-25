def rpt(f, n, x):
    if n == 0:
        return x
    return rpt(f, n - 1, f(x))


def mandel(z, c):
    return z * z + c


def mandel_fix_c(c):
    return lambda z: mandel(z, c)


def scale_and_rotate(xs, ys, i, j):
    n = 50
    return complex((j - ys) / n, 2 * (i - xs) / n)


xs = 80
ys = 160
palette = " .:-=+*#%@"
palette_size = len(palette)
zero = complex(0, 0)
for i in range(xs):
    for j in range(ys):
        try:
            c = scale_and_rotate(xs / 2, ys / 2, i, j)
            r = abs(rpt(mandel_fix_c(c), 10, zero))
        except:
            r = 2
        color = palette[int(r * palette_size)] if r < 1.0 else " "
        print(color, end="")
    print()
