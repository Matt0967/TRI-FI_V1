def trier_liste_noms(liste_noms):
    return sorted(liste_noms)

if __name__ == "__main__":
    noms = ["Alice", "Bob", "Charlie", "David", "Eve"]
    noms_tries = trier_liste_noms(noms)
    print("Noms non triés:", noms)
    print("Noms triés:", noms_tries)
