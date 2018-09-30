#Voici le programme qui permet d'obtenir le jour de la semaine pour une date donnée (dans le calendrier grégorien)


# J'ai créé les trois tableaux ci-dessous afin de répertorier les différents cas de figures (en fonction du mois, de l'année, etc..) et ainsi de faciliter le calcul final
JOURS = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'] # J'ai créé le tableau JOURS sur le modèle de celui donné au point 8 du sujet
MOIS = [0,3,3,6,1,4,6,2,5,0,3,5] #Pour ce tableau MOIS, j'ai entré les valeurs dans l'ordre des mois associés (voir le point 4 du sujet); elles sont accessibles via MOIS[mois-1]
ANNEES = [6,4,2,0] # Le tableau ANNEES correspond aux valeurs qu'il faut ajouté au calcul final en fonction du siècle de la date donnée (voir le point 6 du sujet); elles sont accessibles via ANNEES[a_deb%4]


date = input("Entrez une date (JJ/MM/AAAA) : ") # est la variable à partir de laquelle on va isoler les informations nécessaires au calcul final (voir lignes 13 à 17)

if len(date)==10 and date[2]=='/' and date[5]=='/':
    jour = int(date[0:2]) # sera un entier compris entre 1 et 31 (correspondant au jour dans le mois)
    mois = int(date[3:5]) # sera un entier compris entre 1 et 12 (correspondant au mois dans l'année)
    annee = int(date[6:]) # sera un entier correspondant à une année
    a_deb = int(date[6:8]) # correspond au nombre formé par les deux premiers chiffres de l'année
    a_fin = int(date[8:]) # correspond au nombre formé par les deux derniers chiffres de l'année
else:
    print('Erreur date')



# La fonction init() sert à déterminer si la date entrée est après le 1er novembre ou non
def init():
    if annee > 1582:
        return True
    elif annee == 1582 and mois >= 11 :
        return True
    else :
        return False

# La fonction bissextile, qui prend en arg1 l'année et en arg2 le mois, permet de déterminer s'il faut oui ou non prendre en compte le point 5 du sujet
def bissextile(arg1, arg2):
    if arg1%4 == 0 and arg2 <= 2:
        return True # NB : pour cette fonction, j'aurais pu renvoyer 1 ou -1 à la place de True (et 0 à la place de False) et insérer l'appel de la fonction dans le calcul final directement
    else:
        return False

#La fonction calcul effectue le calcul final en fonction du résultat de la fonction bissextile() et renvoie ce qui correspond à l'indice d'un des éléments du tableau JOURS
def calcul():
    if bissextile(annee, mois):
        somme = a_fin + a_fin // 4 + jour + MOIS[mois - 1] -1 + ANNEES[a_deb % 4]
    else:
        somme = a_fin + a_fin // 4 + jour + MOIS[mois - 1] + ANNEES[a_deb % 4]

    res = somme % 7

    return res


if init(): # 'Si on se place après le 1er novembre 1582'
    print('Le', date, 'était ou sera un ', JOURS[calcul()])

else :
    print("Les calculs demandés ne sont valables que pour les dates d'à partir du 1er Novembre 1582!")