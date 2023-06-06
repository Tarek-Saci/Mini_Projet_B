import matplotlib.pyplot as plt
import timeit
import numpy as np

# -------fixer les parametres----------------------------------------------------
p1 = 1
p2 = 2
p3 = 3
p4 = 4
n = 200
a = -1
b = 1


# -------une fonction qui determine la solution analytique ----------------------
def integrale_analytique(p1, p2, p3, p4, a, b):
    x = a
    primitive_1 = (p1 * x) + (0.5 * p2 * x ** 2) + ((1 / 3) * p3 * x ** 3) + (0.25 * p4 * x ** 4)
    x = b
    primitive_2 = (p1 * x) + (0.5 * p2 * x ** 2) + ((1 / 3) * p3 * x ** 3) + (0.25 * p4 * x ** 4)
    resultat = primitive_2 - primitive_1
    return resultat


# -------fonction methode des rectangles-----------------------------------------
def integrale_rectangles(n):
    largeur_rectangle = (b - a) / n
    liste_aires_rectangle = []  # on initalise une liste qui va contenir toutes les aires des rectangles qu'on poura ensuite aditionner
    x = a #+ (largeur_rectangle / 2)  # on éssaye de placer x au milieu du rectangle
    while x <= b :#- (largeur_rectangle / 2):  # on fait varier x avec un pas égale a la largeur du rectangle
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
    resultat_rectangle = integrale_rectangles(n)
    resultat_analytique = integrale_analytique(p1, p2, p3, p4, a, b)
    erreur = (abs(resultat_analytique - resultat_rectangle) / resultat_analytique) * 100
    return erreur

# -------fonction de calcul d'integral numpy methode des trapèzes--------------------------------------
# def integrale_numpy(n):
#     x = np.linspace(a, b, n)
#     y = ((p1) + (p2 * x) + (p3 * x ** 2) + (p4 * x ** 3))
#     resultat = np.trapz(y, x)
#     return resultat
def integrale_numpy(n):
    x = np.linspace(a, b, n + 1)  # Points d'échantillonnage
    largeur_segment = (b - a) / n  # Largeur de chaque segment
    hauteurs = p1 + p2 * x[:-1] + p3 * x[:-1] ** 2 + p4 * x[:-1] ** 3  # Hauteurs des rectangles
    resultat = np.sum(hauteurs * largeur_segment)  # Somme des aires des rectangles
    return resultat

# -------fonction calcul d'erreur en fonction de n methode NumPy------------------
def erreur_fonction_n_numpy(n):
    resultat_numpy = integrale_numpy(n)
    resultat_analytique = integrale_analytique(p1, p2, p3, p4, a, b)
    erreur_numpy = (abs(resultat_analytique - resultat_numpy) / resultat_analytique) * 100
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
    plt.title('erreur en fonction du nombre de segments\nmethode NumPy et python de base')
    plt.xlabel('n')
    plt.ylabel('erreur [%]')
    plt.grid(True)
    plt.legend()
    #plt.show()
    return

# -------erreur en fonction du temps d'execution methode des rectangles-----------
def erreur_temps_rectangles(n):
    x = []
    y = []
    for i in range(1,n,1):
        x.append(timeit.timeit(lambda: integrale_rectangles(i), number=100))
        y.append(erreur_fonction_n_rectangles(i))
    # !!!il faut trieer les listes x et y!!!
    liste_combnee = list(zip(x , y)) #on combine les liste en une liste de liste a deux elements
    liste_combnee = sorted(liste_combnee) #on trie la liste obtenu
    x , y = zip(*liste_combnee) #on decoupe les tuples en deux pour mettre chaque element dans des listes differentes
    #on affiche le graphe

    plt.plot(x , y , label = 'methode rectangles')
    plt.xlabel("temps d'execution [s]")
    plt.ylabel("erreur [%]")
    plt.title("erreur numerique en fonction du temps d'execution methode rectangles")
    plt.grid(True)
    plt.legend()
    #plt.show()
# -------erreur en fonction du temps d'execution methode NumPy--------------------
def erreur_temps_numpy(n):
    x = []
    y = []
    for i in range(1, n, 1):
        x.append(timeit.timeit(lambda: integrale_rectangles(i), number=100))
        y.append(erreur_fonction_n_rectangles(i))
    # !!!il faut trieer les listes x et y!!!
    liste_combnee = list(zip(x, y))  # on combine les liste en une liste de liste a deux elements
    liste_combnee = sorted(liste_combnee)  # on trie la liste obtenu
    x, y = zip(*liste_combnee)  # on decoupe les tuples en deux pour mettre chaque element dans des listes differentes
    # on affiche le graphe
    #plt.figure()
    plt.plot(x, y, label='methode NumPy')
    plt.xlabel("temps d'execution [s]")
    plt.ylabel("erreur [%]")
    plt.title("erreur numerique en fonction du temps d'execution\nmethode NumPy et python de base")
    plt.grid(True)
    plt.legend()
    plt.show()
    return