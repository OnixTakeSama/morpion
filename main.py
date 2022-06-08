plateau = [" " for _ in range(9)]

def afficherPlateau(p,gagnant=None):
    print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
    print("---+---+---")
    print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
    print("---+---+---")
    print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")

    if gagnant:
        print("Partie terminée : le joueur " + gagnant + " a gagné!")

def choisirCase():
    case = int(input("Choissiez une case entre 1 et 9 ! : "))
    while  case < 1 or case > 9:
        case = int(input("Choissiez une case entre 1 et 9 ! : "))
    return case

def viderPlateau():
    for i in range(9):
        plateau[i] = " "

def morpion():
    joueur = "X"
    tour = 0

    while True:
        afficherPlateau(plateau)
        print("Tour du joueur " + joueur + ". Jouez en choisissant un nombre de 1 à 9 !")
        res = choisirCase()

        if plateau[res-1] != " ":
            print("Case déjà occupée ! Veuillez entrer une case valide!")
            continue
        else:
            plateau[res-1] = joueur
            tour += 1

        if plateau[0] == plateau[1] == plateau[2] != " "\
        or plateau[3] == plateau[4] == plateau[5] != " "\
        or plateau[6] == plateau[7] == plateau[8] != " "\
        or plateau[0] == plateau[3] == plateau[6] != " "\
        or plateau[1] == plateau[4] == plateau[7] != " "\
        or plateau[2] == plateau[5] == plateau[8] != " "\
        or plateau[0] == plateau[4] == plateau[8] != " "\
        or plateau[6] == plateau[4] == plateau[2] != " ":
            afficherPlateau(plateau,joueur)
            rejouer = input("Voulez-vous rejouer ? : Y pour Oui | N pour Non")
            if rejouer == 'Y':
                viderPlateau()
                tour = 0
            else:
                break

        if tour == 9:
            print("Egalité !")
            rejouer = input("Voulez-vous rejouer ? : Y pour Oui | N pour Non")
            if rejouer == 'Y':
                viderPlateau()
                tour = 0
            else:
                break

        joueur = "O" if joueur == "X" else "X"

if __name__ == "__main__":
    morpion()