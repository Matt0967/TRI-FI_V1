def trier_liste_noms(liste_noms):
    return sorted(liste_noms)

def lire_noms_de_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            noms = fichier.readlines()
            # Supprimer les sauts de ligne et espaces en trop
            noms_propres = [nom.strip() for nom in noms]
            return noms_propres
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
        return []

def ajouter_fichiers():
    nouveaux_noms = []
    while True:
        nom_fichier = input("Entrez le nom du fichier à ajouter (ou 'fin' pour terminer) : ")
        if nom_fichier.lower() == 'fin':
            break
        nouveaux_noms.append(nom_fichier)
    return nouveaux_noms

if __name__ == "__main__":
    nom_fichier = "noms_fichiers.txt"  # Nom du fichier contenant les noms des fichiers
    noms = lire_noms_de_fichier(nom_fichier)
    
    if noms:
        print("Noms actuels:", noms)
        fichiers_a_ajouter = ajouter_fichiers()
        noms.extend(fichiers_a_ajouter)
        noms_tries = trier_liste_noms(noms)
        
        print("\nNoms triés:", noms_tries)
