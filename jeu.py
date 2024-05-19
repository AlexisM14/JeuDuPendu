# Ce code permet de jouer au jeu du pendu

# Importation de la bibliothèque qui permettra de choisir un mot au hasard
import random as r

# On crée un dictionnaire qui associe les accents à leur lettre, et un tuple qui correspond à l'alphabet.
# En minuscule et majuscule
accent_min_dico = {'a': ('Ã\xa0', 'Ã¢', 'Ã¤'),
                   'e': ('Ã©', 'Ã¨', 'Ãª', 'Ã«'),
                   'i': ('Ã®', 'Ã¯'),
                   'o': ('Ã´', 'Ã¶'),
                   'u': ('Ã¹', 'Ã»', 'Ã¼'),
                   'y': 'Ã¿',
                   'c': 'Ã§',
                   'ae': 'Ã¦',
                   'oe': 'Å“'}
alphabet_min = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
accent_maj_dico = {'A': ('Ã€', 'Ã‚', 'Ã„'),
                   'E': ('Ã‰', 'Ãˆ', 'ÃŠ', 'Ã‹'),
                   'I': ('ÃŽ', 'O', 'Ã”', 'Ã–'),
                   'U': ('Ã™', 'Ã›', 'Ãœ'),
                   'Y': 'Å¸',
                   'C': 'Ã‡',
                   'AE': 'Ã†',
                   'OE': 'Å'}
alphabet_maj = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
alphabet = alphabet_maj + alphabet_min


# Définition de la fonction ouvrir_fichier
def ouvrir_fichier(nom):
    """Cette fonction permet d'ouvrir le fichier "nom" et d'en extraire les mots"""
    # Prend le nom du fichier en entrée et renvoie une liste des mots contenus dans le fichier
    mots_pendu = open(nom)
    liste_mots_pendu = [i[0:-1] for i in mots_pendu.readlines()]
    mots_pendu.close()
    return liste_mots_pendu


# Définition de la fonction passer_liste_vers_mot
def passer_liste_vers_mot(L):
    """Cette fonction permet de passer d'une liste dont les éléments sont les lettres d'un mot
    à une chaîne de caractère représentant le mot"""
    # Prend une liste de lettres en entrée et renvoie le mot formé de ces lettres en chaîne de caractère
    mot = ''
    for i in L:
        if type(i) != str:
            return None
        else:
            mot += i
    return mot


def convertir_special_vers_lettre_min(mot):
    """Cette fonction permet "d'enlever les accents des lettres" on relie les lettres accentuées à leur
    homologue non accentué"""
    taille_mot = len(mot)
    nouvelle_lettre = ''
    emplacement = 0  # Emplacement de la lettre accentuée
    longueur = 0  # Longueur de la lettre accentuée (combien de caractères il faut échanger avec la lettre sans accent)
    conversion = False  # Si on doit convertir une lettre alors conversion devient True
    duo_caract = ''  # Le couple de caractère qui crypte l'accent

    # On parcourt le mot lettre par lettre
    for i in range(taille_mot):
        # Toutes les lettres accentuées commencent par "Ã", donc dès qu'on croise "Ã", c'est un accent
        if mot[i] == 'Ã':
            # Dans accent_dico, seul "à" est codé par 5 caractères dont le dernier est 0 donc
            # on regarde donc si le quatrième caractère apres est 0
            if i + 4 < taille_mot and mot[i + 4] == '0':
                conversion = True
                nouvelle_lettre = 'a'
                emplacement = i
                longueur = 5
            # Sinon, on regarde alors le duo de 2 lettres et si la combinaison n'existe par ainsi, il s'agit de "à"
            else:
                duo_caract = mot[i] + mot[i + 1]
                emplacement = i
                longueur = 2
                # On cherche à quelle clé le duo de lettre appartient
                for j in accent_min_dico:
                    if duo_caract in accent_min_dico[j]:
                        conversion = True
                        nouvelle_lettre = j
    mot_en_liste = [i for i in mot]
    if conversion:
        mot_en_liste[emplacement] = nouvelle_lettre
        for k in range(1, longueur):
            del (mot_en_liste[emplacement + k])
        return passer_liste_vers_mot(mot_en_liste)
    else:
        return passer_liste_vers_mot(mot_en_liste)


def convertir_special_vers_lettre_maj(mot):
    taille_mot = len(mot)
    nouvelle_lettre = ''
    emplacement = 0
    longueur = 0
    conversion = False
    duo_caract = ''
    # On parcourt le mot lettre par lettre
    for i in range(taille_mot):
        # Toutes les lettres accentuées commencent par "Ã", donc dès qu'on croise "Ã"
        # on a affaire à une lettre accentuée
        if mot[i] == 'Ã':
            duo_caract = mot[i] + mot[i + 1]
            emplacement = i
            longueur = 2
            # On cherche à quelle clé le duo de lettre appartient
            for j in accent_maj_dico:
                if duo_caract in accent_maj_dico[j]:
                    conversion = True
                    nouvelle_lettre = j
    mot_en_liste = [i for i in mot]
    if conversion:
        mot_en_liste[emplacement] = nouvelle_lettre
        for k in range(1, longueur):
            del (mot_en_liste[emplacement + k])
        return passer_liste_vers_mot(mot_en_liste)
    else:
        return passer_liste_vers_mot(mot_en_liste)


def convertir_mot_en_min(mot):
    mot_en_liste = [i for i in mot]
    # On parcourt le mot
    for i in range(len(mot_en_liste)):
        # On vérifie que la lettre est en majuscule, si c'est le cas on la convertit en minuscule
        if mot_en_liste[i] in alphabet_maj:
            # On récupère l'index de la lettre majuscule dans l'alphabet
            print(mot_en_liste[i])
            idx = alphabet_maj.index(mot_en_liste[i])
            # La lettre majuscule et minuscule ont le même index dans leur alphabet respectif,
            # on peut directement remplacer la lettre de mot_en_liste
            mot_en_liste[i] = alphabet_min[idx]
    return passer_liste_vers_mot(mot_en_liste)


def dessiner_pendu(n, etat=1, nbre_max=7):
    """Cette procédure sert à dessiner l'état du pendu en fonction du nombre d'erreurs n, et de l'état du jeu etat"""
    # n est le nombre d'erreurs
    # etat est l'état du jeu : 2 pour victoire, 1 pour en cours de jeu et 0 pour défaite
    if etat == 2:
        dessiner_pendu(n, 1, nbre_max)
        print("  GAGNÉ  ")
    elif etat == 0:
        dessiner_pendu(n, 1, n)
        print("  PERDU  ")
    else:
        if n <= 0:
            print("")
        elif n == nbre_max - 6:
            print("   ________")
            print("   |      |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == nbre_max - 5:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == nbre_max - 4:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |      |")
            print("   |      |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == nbre_max - 3:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |      |/")
            print("   |      |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == nbre_max - 2:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |     l|/")
            print("   |      |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == nbre_max - 1:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |     l|/")
            print("   |      |")
            print("   |     1")
            print("   |")
            print(" __|_______")
        elif n == nbre_max:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |     l|/")
            print("   |      |")
            print("   |     1 1")
            print("   |")
            print(" __|_______")


def nettoyer_ecran():
    """Cette procédure permet de nettoyer la console, afin que rien n'y soit plus affiché"""
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")


def choisir_oui_ou_non():
    reponse = input("Entrez o pour oui, n pour non ")
    while reponse != 'o' and reponse != 'n':
        print("Désolé, la réponse entrée n'est pas correcte")
        reponse = input("Entrez o pour oui, n pour non ")
    if reponse == 'o':
        return True
    else:
        return False


def afficher_etat_jeu(nbre_lettres_f, nbre_erreurs_max, liste_lettres_f, mot):
    dessiner_pendu(nbre_lettres_f, nbre_max=nbre_erreurs_max)
    print(f"Les lettres fausses déjà données : {passer_liste_vers_mot(liste_lettres_f)}")
    print(f"Le mot découvert : {passer_liste_vers_mot(mot)}")


# On écrit le jeu sous la procédure main afin de pouvoir run le script sans le jeu par la suite,
# on ajoute main() à la fin pour lancer le pendu
def main():
    nom_fichier = input("Entrez le nom du fichier dans lequel sont enregistrés les mots en y ajoutant '.txt' ")
    nom_fichier = 'mots_pendu.txt'
    # Cette boucle sert à demander le mot à faire deviner et vérifier sa conformité
    # On affiche les règles au joueur
    nbre_essais_max = 6
    nettoyer_ecran()
    print(f"Vous aurez {nbre_essais_max} essais pour trouver le mot mystère, "
          f"à la septième erreur (lorsque le pendu sera complet) le jeu sera perdu !")
    # On cherche le mot à faire deviner dans le fichier
    mot_a_deviner = r.choice(ouvrir_fichier(nom_fichier))
    # On convertit pour remplacer les accents et les lettres majuscules
    mot_a_deviner = convertir_special_vers_lettre_min(mot_a_deviner)
    mot_a_deviner = convertir_special_vers_lettre_maj(mot_a_deviner)
    mot_a_deviner = convertir_mot_en_min(mot_a_deviner)
    print("Voulez-vous tricher ?")
    triche = choisir_oui_ou_non()
    # La triche permet au développeur de vérifier que le jeu fonctionne bien
    if triche:
        print(f"Je suis choqué, le mot secret est : {mot_a_deviner}")
    else:
        print("Voila quelqu'un d'honnête !")
    # On stocke la lettre initiale et finale du mot, elles seront affichées au joueur
    lettre_init = mot_a_deviner[0]
    lettre_fin = mot_a_deviner[-1]
    # Il faut deviner toutes les lettres du mot sauf 2 : la première et la dernière
    nbre_trous = len(mot_a_deviner) - 2

    # On initialise les compteurs de lettres correctes, fausses et la liste des mauvaises lettres,
    # qui servira à afficher les lettres déja données et fausses.
    # La liste des lettres correctes sert à vérifier que la lettre n'a pas déjà été donnée
    nbre_lettres_correctes = 0
    liste_lettres_correctes = []
    nbre_lettres_fausses = 0
    liste_lettres_fausses = []
    # Initialisation du compteur d'essai
    nbre_essai = 0
    # On enregistre les lettres du mot découvert dans une liste. Si elles ne sont pas encore découvertes alors,
    # on met "_" par la suite, on remplacera "_" par les lettres découvertes, ce qui n'est pas possible
    # avec une chaîne de caractère.
    # Les lettres manquantes seront affichées par des tirets bas "_"
    mystere = '_'
    mot_decouvert = [lettre_init] + nbre_trous * [mystere] + [lettre_fin]
    print(f"Le mot est : {lettre_init + nbre_trous * mystere + lettre_fin} ")

    # Avant de rentrer dans la boucle du jeu, on affirme que l'utilisateur dispose encore d'un indice qu'il
    # pourra utiliser lorsqu'il ne lui restera plus qu'une vie
    indice = True
    # Tant que toutes les lettres n'ont pas été découvertes ou que le joueur a fait moins de 7 erreurs, le jeu continue
    while nbre_lettres_correctes < nbre_trous and nbre_lettres_fausses < nbre_essais_max:
        # On effectue la boucle 1, mais pour la lettre, on vérifie qu'elle est bien conforme. Mais avant, on vérifie
        boucle2 = True
        # S'il ne reste qu'une erreur à l'utilisateur, qu'il lui manque
        # plus d'une lettre à découvrir et qu'il n'a pas encore refusé l'indice, on lui propose un indice

        # Il y a un probleme lorsqu'il reste n lettre à découvrir et qu'elles sont identiques, il faut soit proposer l'indice et dans ce cas ne pas ajouter la lettre à la liste des lettres découvertes sinon on ne peut plus jouer, soit ne pas proposer l'indice mais dans ce cas ca donne une info sur les lettres restantes

        if nbre_lettres_fausses == nbre_essais_max - 1 and nbre_lettres_correctes < nbre_trous - 1 and indice:
            print("Voulez-vous un indice ? Il se peut que celui vous fasse gagner la partie. "
                  "Si vous refusez vous n'aurez plus d'autre occasion d'avoir un indice")
            reponse = choisir_oui_ou_non()
            if reponse:
                indice = False
                lettre_bonus_idx = r.randint(1, len(mot_a_deviner) - 2)
                while mot_decouvert[lettre_bonus_idx] == mot_a_deviner[lettre_bonus_idx]:
                    lettre_bonus_idx = r.randint(1, len(mot_a_deviner) - 2)
                lettre_bonus = mot_a_deviner[lettre_bonus_idx]
                print(f"Mon petit doigt me dit que la lettre '{lettre_bonus}' appartient au mot...")
            else:
                nettoyer_ecran()
                print("Dommage... Bonne chance pour trouver la dernière lettre !")
                afficher_etat_jeu(nbre_lettres_fausses, nbre_essais_max, liste_lettres_fausses, mot_decouvert)
            indice = False

        # Probabilité d'avoir un indice supplémentaire : 25% (25 sur 100)
        nbre_aleatoire = r.randint(1, 100)
        if nbre_aleatoire < 26:
            indice = True

        while boucle2:
            print(" ")
            lettre = input("Veuillez saisir la lettre à découvrir en minuscule, sans accent : ")
            print(" ")
            if (lettre not in alphabet_min) or len(lettre) > 1:
                boucle2 = True
                print("Le caractère entré n'est pas une lettre minuscule sans accent.")
                continue
            elif lettre in liste_lettres_correctes:
                boucle2 = True
                nettoyer_ecran()
                print("La lettre entrée est déjà dans le mot.")
                print("")
                dessiner_pendu(nbre_lettres_fausses, nbre_max=nbre_essais_max)
                print(f"Les lettres fausses déjà données : {passer_liste_vers_mot(liste_lettres_fausses)}")
                print(f"Le mot découvert : {passer_liste_vers_mot(mot_decouvert)}")
                continue
            else:
                nbre_essai += 1
                nettoyer_ecran()
                boucle2 = False
        boucle2 = True
        # Si la lettre est une lettre du mot à deviner
        if lettre in mot_a_deviner[1:-1]:
            liste_lettres_correctes.append(lettre)
            # On va chercher son emplacement dans le mot, on initialise donc une variable emplacement
            emplacement = 0
            for i in mot_a_deviner[1:-1]:
                # On commence à partir de la deuxième lettre du mot, soit l'index 1
                emplacement += 1
                # Si la lettre est à cet emplacement dans le mot
                if lettre == i:
                    # On ajoute 1 au compteur de lettres correctes à chaque lettre du mot identique à la lettre entrée
                    # Cela permet d'afficher et de compter les lettres qui apparaissent plusieurs fois dans le mot
                    nbre_lettres_correctes += 1
                    # On ajoute la lettre à l'emplacement dans la liste du mot découvert
                    mot_decouvert[emplacement] = i
        elif lettre in alphabet_min and lettre not in mot_a_deviner[1:-1]:
            # Si la lettre n'est pas une des lettres à découvrir, on ajoute 1 au compteur des lettres fausses et
            # la lettre est ajoutée à la liste des lettres déja données
            nbre_lettres_fausses += 1
            # Si la lettre est déjà dans la liste des fausses lettres, on ne la rajoute pas
            if lettre not in liste_lettres_fausses:
                liste_lettres_fausses.append(lettre)
        afficher_etat_jeu(nbre_lettres_fausses, nbre_essais_max, liste_lettres_fausses, mot_decouvert)

    if nbre_lettres_correctes == len(mot_a_deviner[1:-1]):
        nettoyer_ecran()
        dessiner_pendu(nbre_lettres_fausses, etat=2, nbre_max=nbre_essais_max)
        print(f"Vous avez gagné en {nbre_essai} essais, le mot à trouver était {mot_a_deviner}")
        print("Voulez vous jouer à nouveau ? ")
        rejouer = choisir_oui_ou_non()
        if rejouer:
            nettoyer_ecran()
            print("C'est reparti !")
            main()
        else:
            print("Dommage... A bientôt !")


    elif nbre_lettres_fausses == nbre_essais_max:
        nettoyer_ecran()
        dessiner_pendu(nbre_essais_max, etat=0, nbre_max=nbre_essais_max)
        print(f"Vous avez perdu, le mot à trouver était : {mot_a_deviner}")
        print("Voulez vous jouer à nouveau ? ")
        rejouer = choisir_oui_ou_non()
        if rejouer:
            nettoyer_ecran()
            print("C'est reparti !")
            main()
        else:
            print("Dommage... A bientôt !")


main()
