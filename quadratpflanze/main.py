def umfang(n, m):
    if n == 0:
        return 4 * m
    else:
        return umfang(n - 1, m) + 3**n * 4 * (m / 3**n)

def flaecheninhalt(n, m):
    if n == 0:
        return m ** 2
    else:

        return flaecheninhalt(n - 1, m) + 3**n * (m / 3**n) ** 2

m = 10
for n in range(9):
    print(f"Jahr {n}: Umfang = {umfang(n, m)}, Flaeche = {flaecheninhalt(n, m)}")