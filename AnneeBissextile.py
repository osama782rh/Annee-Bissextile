"""En Italique, calcul du jour de la semaine de l'exemple 1er août 1947."""

#Je déclare mon dictionnaire des mois

dictio_mois = {
    "Janvier" : "0",
    "Février" : "3",
    "Mars" : "3",
    "Avril" : "6",
    "Mai" : "1" ,
    "Juin" : "4",
    "Juillet" : "6",
    "Août" : "2",
    "Septembre" : "5",
    "Octobre" : "0",
    "Novembre" : "3",
    "Décembre" : "5"
}
#Je déclare mon dictionnaire de siècles

dictio_siecle = {
    "16" : "6",
    "17" : "4",
    "18" : "2",
    "19" : "0",
    "20" : "6",
    "21" : "4"
}
#Je déclare mon dictionnaire de semaine

dictio_semaine = {
    "0" : "Dimanche",
    "1" : "Lundi",
    "2" : "Mardi",
    "3" : "Mercredi",
    "4" : "Jeudi",
    "5" : "Vendredi",
    "6" : "Samedi"
}
somme = 0


# Je crée une méthode qui me permet de récupérer la date et de verifier si elle est au bon format
def recup_date():
    date_saisie = 0
    while date_saisie == 0:     #tant que l'utilisateur n'a pas saisie la date au bon format je lui redemande de resaisir
        date_saisie = input(f"Veuillez saisir la date au format 00/00/0000 :  ")
        try:
            date_saisie = str(date_saisie)
        except:
            print("ERREUR: Réessayez :  Veuillez saisir la date au format 00/00/0000 : ")
            date_saisie == 0
    return date_saisie

def affiche():
    print(f'Le jour {date_str} était un {jour} !')  # J'affiche le résultat
    if annee_i % 4 == 0:
        print(f'L\'année {annee_i} est une année bissextile')
    else:
        print(f'l\'année {annee_i} n\'est pas une année bissextile')


date_str = recup_date()                 #Je stocke la date dans une variable pour pouvoir l'appeler à la fin et j'appelle la méthode
d = date_str.split("/")             #Je sépare le jour, le mois et l'année
jour = d[0]                             #Je récupére le jour
mois = d[1]                             #Je récupére le mois
annee = d[2]                            #Je récupére l'année



"""def deux_derniers_chiffres_annee ():"""
#Je récupére les deux derniers chiffres de l'année et je les stocke dans une variable
deux_derniers_chiffres = annee[-2:]
somme = int(deux_derniers_chiffres)
somme += (somme // 4 + 1)                                           # On garde la division écludienne et on ajoute 1


"""def convertir_le_mois_en_str():"""
"""def convertir_le_mois_en_str():"""
#on stocke le dictionnaire dans une liste afin de pouvoir retrouver des clés numériques correspondant au mois saisi
liste = list(dictio_mois.keys())
mois_i = int(mois)                                     #Je convertis la saisie en int et je la stocke dans une variable
mois_string = liste[mois_i - 1]              # on stocke le mois saisi en format string
somme_s = dictio_mois[mois_string]                      #Je récupère en format string la valeure lié
somme = somme + int(somme_s)                         #Je fais la somme et je la stocke dans la variable principale
annee_i = int(annee)                                        #Je converti l'année en int pour pouvoir diviser

bissextile = 0
#Si l'année est bissextile et le mois est janvier ou février, on ôte 1
if annee_i % 4 == 0 and mois_string == "Janvier" or mois_string == "Fevrier":
    somme = somme - 1                 #somme = somme + 1 'Exemple 1947 année non bisextile' || 'Exemple : 2022 on ôte 1'


siecle = annee[0:2]                                             #On récupére le siecle exemple '19' pour '1947'
valeur_siecle = dictio_siecle[siecle]                        #Selon le siècle, on ajoute une valuer liée au dictionnaire
somme = somme + int(valeur_siecle)                                   #On ajoute la valeur à la somme

reste = somme % 7                                                    #On récupère le reste de la division


reste = str(reste)              #On converti le reste de la division en str pour comparer aux clés dans le dictionnaire
jour = dictio_semaine[reste]                                #On récupère le jour lié au reste en le comparant aux clés


affiche()










