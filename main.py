#coding:utf8
from Utils import * 
from Trace import * 
from cleanTrame import tramesValides

FileTrameTest="./trameOffset.txt"
cleanTrameFile="./cleanTrames.txt"
resultatAnalyseTrame="./outPuts.txt"

#On extrait a partir du fichier d'entrée toutes les trames qui respectent le bon format !

try:
	trameValide=tramesValides(FileTrameTest)
	outPut(trameValide,cleanTrameFile) #On ecrit enregistre l'ensemble de nos bonnes trames dans un fichiers cleanTrames
except:
	print("Veuillez selectionner un fichier existant !")


#Aprés avoir enregistrées les trames à traiter, on les récupére du bon fichier(cleanTrames), et on commence :

#Premiere chose separer les trames en les recuperant sous forme de liste!
listeDeTrame=[]
erreur=False
try:
	with open(cleanTrameFile,"r") as fichier:
		contenu=fichier.readlines()

		for line in contenu:
			listeDeTrame.append(line)
	fichier.close()
except:
	print("Etes vous sur d avoir tout creer pour le lancement du programme(fichier cleanTrames.txt manquant :(")
	exit

#Deuxieme chose on crée notre trace qui contiendra toutes les trames parsées (sous forme de chaines de caracteres)
#	ainsi que la vraie structure trame appropiée à chaqu'un des message capturés (C'est là qu'on delimite tous les champs)

if len(listeDeTrame)!=0:   # On verifie qu'il existe bien des trames respectant le format attendu dans le fichier trace lu
	trace=Trace(listeDeTrame)
	resultat=trace.analyse()  #La fonction analyse permet d'initialiser les champs de la trame
	for trame in trace.listeDeTrames:
		if trame.ipv4!=None and hexToDec(trame.ipv4.protocol)==6:
			outPut(trame.toString(),resultatAnalyseTrame)
	
