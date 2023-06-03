import matplotlib.pyplot as plt
import timeit
import numpy as np

# -------fixer les parametres----------------------------------------------------
p1 = 5
p2 = 5
p3 = 7
p4 = 1
n = 100
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
    liste_aires_rectangle = []  # on initalise une liste qui va contenir toutes les aires des rectangles qu'on poura ensuite aditionner
    x = a + (largeur_rectangle / 2)  # on éssaye de placer x au milieu du rectangle
    while x <= b - (largeur_rectangle / 2):  # on fait varier x avec un pas égale a la largeur du rectangle
        hauteur_rectagle = (p1) + (p2 * x) + (p3 * x ** 2) + (p4 * x ** 3)
        aire = hauteur_rectagle * largeur_rectangle
        liste_aires_rectangle.append(aire)
        x += largeur_rectangle
    resultat = sum(liste_aires_rectangle)
    return resultat


# -------fonction calcule d'erreur -----------------------------------------------
def erreur(resultat_analytique, resultat_rectangle):
    # [(valeur réelle - valeur théorique)/valeur réelle] x 100
    erreur = ((resultat_analytique - resultat_rectangle) / resultat_analytique) * 100
    return erreur

# -------fonction calcul d'erreur en fonction de n methode des rectangles---------
def erreur_fonction_n_rectangles(n):
    resultat_rectangle = integrale_rectangles(p1, p2, p3, p4, a, b, n)
    resultat_analytique = integrale_analytique(p1, p2, p3, p4, a, b)
    erreur = ((resultat_analytique - resultat_rectangle) / resultat_analytique) * 100
    return erreur

# -------fonction de calcul d'integral numpy methode des trapèzes--------------------------------------
def integrale_numpy(n):
    x = [np.linspace(a, b, n)]
    y = []
    for i in x:
        y.append((p1) + (p2 * i) + (p3 * i ** 2) + (p4 * i ** 3))
    resultat = np.trapz(y, x)
    return resultat

# -------fonction calcul d'erreur en fonction de n methode NumPy------------------
def erreur_fonction_n_numpy(n):
    resultat_numpy = integrale_numpy(n)
    resultat_analytique = integrale_analytique(p1, p2, p3, p4, a, b)
    erreur_numpy = ((resultat_analytique - resultat_numpy) / resultat_analytique) * 100
    return erreur_numpy

# -------fonction de verification de convergence par la methode des rectangles----
def convergence_rectangles(n):  # consigne 5 eventuelement
    liste_erreur = []  # initialiser une liste qui nous permetera de recuperer la valeur de l'integrale en fonction de n
    liste_n = []  # initialiser une liste qui nous permetera de recuperer la valeur de n a chaque iteration
    for i in range(1, n, 1):
        liste_erreur.append(erreur_fonction_n_rectangles(i))
        liste_n.append(i)
    #plt.figure()
    plt.plot(liste_n, liste_erreur,label = 'erreur rectangles')
    plt.title('erreur en fonction du nombre de segments méthode des rectangles')
    plt.xlabel('n')
    plt.ylabel('erreur [%]')
    plt.grid(True)
    plt.legend()
    #plt.show()
    return

# -------fonction de verification de convergence par la methode NumPy----
def convergence_numpy(n):  # consigne 5 eventuelement
    liste_erreur = []  # initialiser une liste qui nous permetera de recuperer la valeur de l'integrale en fonction de n
    liste_n = []  # initialiser une liste qui nous permetera de recuperer la valeur de n a chaque iteration
    for i in range(1, n, 1):
        liste_erreur.append(erreur_fonction_n_numpy(i))
        liste_n.append(i)
    #plt.figure()
    plt.plot(liste_n, liste_erreur,label = 'erreur NumPy')
    plt.title('erreur en fonction du nombre de segments methode NumPy')
    plt.xlabel('n')
    plt.ylabel('erreur [%]')
    plt.grid(True)
    plt.legend()
    #plt.show()
    return
# -------timeit methode des rectangles--------------------------------------------
temps_execution_rectangles = timeit.timeit(lambda: integrale_rectangles(p1, p2, p3, p4, a, b, n), number=100)
temps_exectution_numpy = timeit.timeit(lambda: integrale_numpy(n), number=100)

# --------------------------------------------------------------------------------

resultat_analytique = integrale_analytique(p1, p2, p3, p4, a, b)
resultat_rectangle = integrale_rectangles(p1, p2, p3, p4, a, b, n)
resultat_numpy = float(integrale_numpy(n))
erreur_n_rectangles = erreur_fonction_n_rectangles(n)
erreur_n_numpy = erreur_fonction_n_numpy(n)

print(f'resultat analytique : {resultat_analytique}')

print(f'resultat rectangles : {resultat_rectangle}')

print(f'resultat numpy :{resultat_numpy}')

print(f'erreur methode rectangles: {erreur_n_rectangles} %')

print(f'erreur methode NumPy: {erreur_n_numpy} %')

print(f"Temps d'exécution avec la methode des rectangles : {temps_execution_rectangles} secondes")

print(f"Temps d'exécution avec la méthode NumPy : {temps_exectution_numpy} secondes")

convergence_rectangles(n)

convergence_numpy(n)

plt.show()