from mod2 import *
# -------timeit methode des rectangles--------------------------------------------
temps_execution_rectangles = timeit.timeit(lambda: integrale_rectangles(n), number=100)
temps_exectution_numpy = timeit.timeit(lambda: integrale_numpy(n), number=100)
# --------------------------------------------------------------------------------
resultat_analytique = integrale_analytique(p1, p2, p3, p4, a, b)
resultat_rectangle = integrale_rectangles(n)
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

erreur_temps_rectangles(n)

erreur_temps_numpy(n)