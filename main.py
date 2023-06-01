# -------fixer les parametres----------------------------------------------------
p1 = 1
p2 = 2
p3 = 3
p4 = 4
n = 10
a = -10
b = 15


# -------une fonction qui determine la solution analytique ----------------------
def integrale_analytique(p1, p2, p3, p4, a, b):
    x = a
    primitive_1 = (p1 * x) + (0.5 * p2 * x ** 2) + ((1 / 3) * p3 * x ** 3) + (0.25 * p4 * x ** 4)
    x = b
    primitive_2 = (p1 * x) + (0.5 * p2 * x ** 2) + ((1 / 3) * p3 * x ** 3) + (0.25 * p4 * x ** 4)
    resultat = primitive_2 - primitive_1
    return resultat


# -------fonction methode des rectangles-----------------------------------------
def integrale_rectangles(p1, p2, p3, p4, a, b, n):
    largeur_rectangle = (b - a) / n
    x = a
    while x <= b:
        print(x)
        x += largeur_rectangle
    return


# --------------------------------------------------------------------------------
print(integrale_analytique(p1, p2, p3, p4, a, b))
print(integrale_rectangles(p1, p2, p3, p4, a, b, n))
