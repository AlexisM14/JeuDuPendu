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
alphabet_min = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z')
accent_maj_dico = {'A': ('Ã€', 'Ã‚', 'Ã„'),
                   'E': ('Ã‰', 'Ãˆ', 'ÃŠ', 'Ã‹'),
                   'I': ('ÃŽ', 'O', 'Ã”', 'Ã–'),
                   'U': ('Ã™', 'Ã›', 'Ãœ'),
                   'Y': 'Å¸',
                   'C': 'Ã‡',
                   'AE': 'Ã†',
                   'OE': 'Å'}
alphabet_maj = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z')
alphabet = alphabet_maj + alphabet_min


# Définition de la fonction ouvrir_fichier
def lire_fichier(nom):
    """Cette fonction permet d'ouvrir le fichier "nom" et d'en extraire les mots"""
    # Prend le nom du fichier en entrée et renvoie une liste des mots contenus dans le fichier
    # Entrée : chaine de caractère
    # Sortie : liste
    mots_pendu = open(nom)
    liste_mots_pendu = [i[0:-1] for i in mots_pendu.readlines()]
    mots_pendu.close()
    return liste_mots_pendu


# Définition de la fonction passer_liste_vers_mot
def passer_liste_vers_mot(liste):
    """Cette fonction permet de passer d'une liste dont les éléments sont les lettres d'un mot
    à une chaîne de caractère représentant le mot"""
    # Prend une liste de lettres en entrée et renvoie le mot formé de ces lettres en chaîne de caractère
    # Entrée : liste
    # Sortie : chaîne de caractère
    mot = ''
    for i in liste:
        mot += i
    return mot


# Définition de la fonction convertir_special_vers_lettre_min
def convertir_special_vers_lettre_min(mot):
    """Cette fonction permet "d'enlever les accents des lettres minuscules" on relie les lettres accentuées à leur
    homologue non accentué"""
    # Entrée : chaîne de caractère
    # Sortie : chaîne de caractère
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
            # Dans accent_min_dico, seul "à" est codé par 5 caractères dont le dernier est 0 donc
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


# Définition de la fonction convertir_special_vers_lettre_maj
def convertir_special_vers_lettre_maj(mot):
    """Cette fonction permet "d'enlever les accents des lettres majuscule" on relie les lettres accentuées à leur
       homologue non accentué"""
    # Entrée : chaîne de caractère
    # Sortie : chaîne de caractère
    taille_mot = len(mot)
    nouvelle_lettre = ''
    emplacement = 0  # Emplacement de la lettre accentuée
    longueur = 0  # Longueur de la lettre accentuée (combien de caractères il faut échanger avec la lettre sans accent)
    conversion = False  # Si on doit convertir une lettre alors conversion devient True
    duo_caract = ''  # Le couple de caractère qui crypte l'accent

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


# Définition de la fonction convertir_mot_en_min
def convertir_mot_en_min(mot):
    """Cette fonction permet de convertir un mot pour qu'il soit uniquement en minuscule"""
    # Entrée : chaîne de caractère
    # Sortie : chaîne de caractère
    mot_en_liste = [i for i in mot]
    # On parcourt le mot de lettre en lettre
    for i in range(len(mot_en_liste)):
        # Si la lettre est en majuscule, on la convertit en minuscule
        if mot_en_liste[i] in alphabet_maj:
            # On récupère l'index de la lettre majuscule dans l'alphabet
            print(mot_en_liste[i])
            idx = alphabet_maj.index(mot_en_liste[i])
            # La lettre majuscule et minuscule ont le même index dans leur alphabet respectif,
            # on peut directement remplacer la lettre de mot_en_liste
            mot_en_liste[i] = alphabet_min[idx]
    return passer_liste_vers_mot(mot_en_liste)


# Définition de la procédure dessiner_pendu
def dessiner_pendu(n, etat=1):
    """Cette procédure sert à dessiner l'état du pendu en fonction du nombre d'erreurs n, et de l'état du jeu etat"""
    # Entrée : un entier n : le nombre d'erreurs, un entier etat : 0 pour défaite, 1 pour en cours, 2 pour gagné

    # La procédure peut être récursive donc on fait attention à couvrir tous les cas
    if etat == 2:
        dessiner_pendu(n, 1)
        print("  GAGNÉ  ")
    elif etat == 0:
        dessiner_pendu(n, 1)
        print("  PERDU  ")
    else:
        if n <= 0:
            print("")
        elif n == 1:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == 2:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |      |")
            print("   |      |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == 3:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |      |/")
            print("   |      |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == 4:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |     l|/")
            print("   |      |")
            print("   |")
            print("   |")
            print(" __|_______")
        elif n == 5:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |     l|/")
            print("   |      |")
            print("   |     1")
            print("   |")
            print(" __|_______")
        elif n == 6:
            print("   ________")
            print("   |      |")
            print("   |      O")
            print("   |     l|/")
            print("   |      |")
            print("   |     1 1")
            print("   |")
            print(" __|_______")


# Définition de la procédure nettoyer_écran
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


# Définition de la fonction choisir_oui_ou_non
def choisir_oui_ou_non():
    """Cette fonction permet de demander à l'utilisateur de répondre par oui ou non"""
    # Entrée :
    # Sortie : un booléen, True si l'utilisateur répond oui, False pour non
    reponse = input("Entrez o pour oui, n pour non ")
    # On veut s'assurer que l'utilisateur entre 'o' ou 'n'
    while reponse != 'o' and reponse != 'n':
        print("Désolé, la réponse entrée n'est pas correcte")
        reponse = input("Entrez o pour oui, n pour non ")
    if reponse == 'o':
        return True
    else:
        return False


# Définition de la procédure afficher_etat_jeu
def afficher_etat_jeu(nbre_lettres_f, liste_lettres_f, mot):
    """Cette procédure permet d'afficher l'état du pendu, les lettres fausses et le mot découvert"""
    # Entrée : un entier : le nombre de lettres fausses, une liste : les lettres de fausses,
    # une chaîne de caractère : le mot découvert
    dessiner_pendu(nbre_lettres_f)
    print(f"Les lettres fausses déjà données : {passer_liste_vers_mot(liste_lettres_f)}")
    print(f"Le mot découvert : {passer_liste_vers_mot(mot)}")


# Définition de la fonction lisser_mot
def lisser_mot(mot):
    """Cette fonction sert à enlever les accents du mot et le convertir en minuscule"""
    # Entrée : mot une chaîne de caractère
    # Sortie : une chaîne de caractère correspondante au mot en minuscule, sans accent
    mot_bis = convertir_special_vers_lettre_min(mot)
    mot_bis = convertir_special_vers_lettre_maj(mot)
    return convertir_mot_en_min(mot)


# Definition de la procédure main(), il s'agit du jeu, le définir ainsi permet de le relancer par la suite
def main():
    """Cette fonction est le jeu du pendu"""
    # On propose au joueur de jouer avec son propre fichier
    print("Avez vous un fichier personnalisé de mots ?")
    print("Le fichier doit être enregistré dans le même dossier que ce script.")
    print("Si ce n'est pas le cas, cela menera à une erreur et il faudra relancer le script.")
    if choisir_oui_ou_non():
        nom_fichier = input("Entrez le nom du fichier dans lequel sont enregistrés vos mots en y ajoutant '.txt' ")
    else:
        nom_fichier = 'mots_pendu.txt'

    # On cherche le mot à faire deviner dans le fichier
    mot_a_deviner = lisser_mot(r.choice(lire_fichier(nom_fichier)))
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

    # On affiche les règles au joueur
    nettoyer_ecran()
    print(f"Vous aurez 6 essais pour trouver le mot mystère, "
          f"à la septième erreur (lorsque le pendu sera complet) le jeu sera perdu !")

    # On enregistre les lettres du mot découvert dans une liste. Si elles ne sont pas encore découvertes alors,
    # on met "_" par la suite, on remplacera "_" par les lettres découvertes
    mystere = '_'
    mot_decouvert = [lettre_init] + nbre_trous * [mystere] + [lettre_fin]  # Mot sous forme de liste, lettre par lettre
    print(f"Le mot est caché derrière : {lettre_init + nbre_trous * mystere + lettre_fin} ")

    # Avant de rentrer dans la boucle du jeu, on affirme que l'utilisateur dispose d'un indice qu'il
    # pourra utiliser lorsqu'il ne lui restera plus qu'une vie
    indice = True
    # Tant que toutes les lettres n'ont pas été découvertes ou que le joueur a fait moins de 6 erreurs, le jeu continue
    while nbre_lettres_correctes < nbre_trous and nbre_lettres_fausses < 6:
        # S'il ne reste qu'une erreur à l'utilisateur, qu'il lui manque plus d'une lettre à découvrir
        # et qu'il n'a pas encore eu d'indice, on lui propose un indice
        if nbre_lettres_fausses == 6 - 1 and nbre_lettres_correctes < nbre_trous - 1 and indice:
            print("Voulez-vous un indice ? Il se peut qu'il vous fasse gagner la partie. "
                  "Si vous refusez vous n'aurez plus d'autre occasion d'avoir un indice")
            if choisir_oui_ou_non():
                lettre_bonus_idx = r.randint(1, len(mot_a_deviner) - 2)  # On choisit un index aléatoirement
                # Tant que la lettre est déjà découverte
                while mot_decouvert[lettre_bonus_idx] == mot_a_deviner[lettre_bonus_idx]:
                    # On tire un autre index aléatoirement
                    lettre_bonus_idx = r.randint(1, len(mot_a_deviner) - 2)
                lettre_bonus = mot_a_deviner[lettre_bonus_idx]  # On enregistre la lettre bonus
                print(f"Mon petit doigt me dit que la lettre '{lettre_bonus}' appartient au mot...")
            else:
                nettoyer_ecran()
                print("Dommage... Bonne chance pour trouver la dernière lettre !")
                afficher_etat_jeu(nbre_lettres_fausses, liste_lettres_fausses, mot_decouvert)
            indice = False

        # On donne une chance supplémentaire à l'utilisateur
        # Probabilité d'avoir un indice supplémentaire : 5% (5 sur 100)
        nbre_aleatoire = r.randint(1, 100)
        if nbre_aleatoire < 6:
            indice = True

        # On effectue une boucle "infinie" pour demander la lettre, on vérifie qu'elle est bien conforme.
        boucle1 = True
        while boucle1:
            print(" ")
            lettre = input("Veuillez saisir la lettre à découvrir en minuscule, sans accent : ")
            print(" ")
            # Si le caractère entré n'est pas dans l'alphabet ou plus grand que 1
            if (lettre not in alphabet_min) or len(lettre) > 1:
                boucle1 = True
                print("Le caractère entré n'est pas une lettre minuscule sans accent.")
                continue
            # Si la lettre a déjà été découverte
            elif lettre in liste_lettres_correctes:
                boucle1 = True
                nettoyer_ecran()
                print("La lettre entrée est déjà dans le mot.")
                print("")
                dessiner_pendu(nbre_lettres_fausses)
                print(f"Les lettres fausses déjà données : {passer_liste_vers_mot(liste_lettres_fausses)}")
                print(f"Le mot découvert : {passer_liste_vers_mot(mot_decouvert)}")
            # Sinon, y compris si la lettre est fausse et a déjà été donnée
            else:
                nbre_essai += 1
                nettoyer_ecran()
                boucle1 = False
        boucle1 = True

        # Si la lettre est une lettre du mot à deviner
        if lettre in mot_a_deviner[1:-1]:
            liste_lettres_correctes.append(lettre)
            # On veut chercher son emplacement dans le mot, on initialise donc une variable emplacement
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
        afficher_etat_jeu(nbre_lettres_fausses, liste_lettres_fausses, mot_decouvert)

    # Si toutes les lettres ont été découvertes, le joueur a gagné
    if nbre_lettres_correctes == len(mot_a_deviner[1:-1]):
        nettoyer_ecran()
        dessiner_pendu(nbre_lettres_fausses, etat=2)
        print(f"Vous avez gagné en {nbre_essai} essais, le mot à trouver était {mot_a_deviner}")
        # On propose au joueur de rejouer
        print("Voulez vous jouer à nouveau ? ")
        if choisir_oui_ou_non():
            nettoyer_ecran()
            print("C'est reparti !")
            main()
        else:
            print("Dommage... A bientôt !")

    # S'il y a autant de lettres fausses que de nombres d'erreurs maximum, le joueur a perdu
    elif nbre_lettres_fausses == 6:
        nettoyer_ecran()
        dessiner_pendu(6, etat=0)
        print(f"Vous avez perdu, le mot à trouver était : {mot_a_deviner}")
        print("Voulez vous jouer à nouveau ? ")
        # On propose au joueur de rejouer
        if choisir_oui_ou_non():
            nettoyer_ecran()
            print("C'est reparti !")
            main()
        else:
            print("Dommage... A bientôt !")


main()