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

if __name__ == "__main__":
    nom_fichier = "noms_fichiers.txt"  # Nom du fichier contenant les noms des fichiers
    noms = lire_noms_de_fichier(nom_fichier)
    noms_tries = trier_liste_noms(noms)
    
    if noms:
        print("Noms non triés:", noms)
        print("Noms triés:", noms_tries)
