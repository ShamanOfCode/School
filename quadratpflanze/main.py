# Aufgabe 3: Die seltsame Quadratpflanze

def umfang(n, m):
    if n == 0:
        return 4 * m
    else:
        return umfang(n - 1, m) + (3 ** n) * 4 * (m / (2 ** n))

def flaecheninhalt(n, m):
    if n == 0:
        return m * m
    else:
        return flaecheninhalt(n - 1, m) + (3 ** n) * (m / (2 ** n)) ** 2

n = 5 # Jahre
m = 10 # Seitenlaenge
print(f"Umfang: {umfang(n, m)}")
print(f"Flaecheninhalt {flaecheninhalt(n, m)}")
print("\nBeobachtung:")
print("Für große n wächst der Umfang exponentiell")
