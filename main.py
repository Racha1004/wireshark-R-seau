#coding:utf8
from Utils import * 
from Trace import * 
import sys
from cleanTrame import *

FileTrameTest="./trameOffset.txt"
cleanTrameFile="./cleanTrames.txt"
resultatAnalyseTrame="./outPuts.txt"
PROTOCOLES=["ETHERNET","IPV4","TCP","HTTP"]
#On extrait a partir du fichier d'entrée toutes les trames qui respectent le bon format !
formatOk=False
aucune=False
nameFileErr=False
if len(sys.argv)==2 and sys.argv[1]=="--interface":
	print("Interface")
	formatOk=True

elif "--terminal" in sys.argv:

	if len(sys.argv)>=3 and sys.argv[1]=="--terminal":
		fileName=sys.argv[2]
		trames=[]
		trace=None
		i=0		
		if( len(sys.argv)==4 and len(sys.argv[3].split("=")))==2 and sys.argv[3].split("=")[0]=="--protocol":
			trace=getTrace(fileName,resultatAnalyseTrame)
			if sys.argv[3].split("=")[1] in PROTOCOLES:
				formatOk=True
			if(trace!=None):
				trames=trace.filtre(sys.argv[3].split("=")[1],"","")
				print("nbr de trames : {}".format(len(trames)))
				i=1
				
		elif len(sys.argv)==5 and len(sys.argv[3].split("="))==2 and sys.argv[3].split("=")[0]=="--adr1" and len(sys.argv[4].split("="))==2 and sys.argv[4].split("=")[0]=="--adr2":
			trace=getTrace(fileName,resultatAnalyseTrame)
			if(trace!=None):
				trames=trace.filtre("",sys.argv[3].split("=")[1],sys.argv[4].split("=")[1])
				print("nbr de trames : {}".format(len(trames)))
			formatOk=True
				
		elif  len(sys.argv)==6 and len(sys.argv[3].split("="))==2 and sys.argv[3].split("=")[0]=="--protocol" and len(sys.argv[4].split("="))==2 and sys.argv[4].split("=")[0]=="--adr1"and len(sys.argv[5].split("="))==2 and sys.argv[5].split("=")[0]=="--adr2":
			trace=getTrace(fileName,resultatAnalyseTrame)
			formatOk=True

			if(trace!=None):
				trames=trace.filtre(sys.argv[3].split("=")[1],sys.argv[4].split("=")[1],sys.argv[5].split("=")[1])
				print("nbr de trames : {}".format(len(trames)))
				i=1
				
		elif len(sys.argv)==3:
			#outPut(afficheTrame("08002087b04408001108c06308004500007c3f860000fb0649afc0219f0684e33d05ffad13895c3e066a00000000a00240009c2e0000020405a0010303000101080a009e7bc400000000474554202f7e737061746869732f20485454502f312e310d0a486f73743a207777772d6e70612e6c6970362e66720d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a557067726164652d496e7365637572652d52657175657374733a20310d0a557365722d4167656e743a204d6f7a696c6c612f352e3020284d6163696e746f73683b20496e74656c204d6163204f5320582031305f31345f3634330d0a0d0a"),fileName)
			trace=getTrace(fileName,resultatAnalyseTrame)
			if(trace!=None):
				trames=trace.listeDeTrames
			formatOk=True
		
		if formatOk and len(trames)!=0:
			print("here")
			for trame in trames:
				if i==1:
					message=trame.getMsgTerminal(sys.argv[3].split("=")[1])
				else:
					message=trame.getMsgTerminal("")
				if(len(message)!=0):
					if message[0]=="HTTP" or message[0]=="TCP":
						print("{} ,{} :--------------{}-------------> {}, {}\n".format(colorise(formatIPAdress(message[1]),0),colorise(str(hexToDec(message[2])),1),colorise(message[3],2),colorise(str(hexToDec(message[5])),1),colorise(formatIPAdress(message[4]),0)))
						#a="{} ,{} :--------------{}-------------> {}, {}\n".format(formatIPAdress(message[1]),hexToDec(message[2]),message[3],hexToDec(message[5]),formatIPAdress(message[4]))
						#outPut(a,resultatAnalyseTrame)
					elif message[0]=="IPV4":
						print("{} :--------------{}-------------> {} {}\n".format(colorise(formatIPAdress(message[1]),0),colorise(message[2],2),colorise(formatIPAdress(message[3]),0),colorise(message[4],3)))
					elif message[0]=="ETHERNET":
						print("{} :--------------{}-------------> {} {}\n".format(colorise(formatMACAdress(message[1]),4),colorise(message[2],2),colorise(formatMACAdress(message[3]),4),colorise(message[4],3)))
		
		if formatOk and (trace==None or(trace!=None and len(trames)==0)):
			aucune=True


			

if not formatOk and not aucune:					
	print("Veuillez respecter le format suivant : \nRajouter ces 2 options à la commande d'execution pour selectionner: \n\t 1)La version termianl :"
	"'--terminal' \n\t 2)La version graphique '--interface'")
	
	print("Si vous optez pour une version terminal : \n 3 Options s'offrent à vous mais il faudra imperativement resepcter les formats suivants :")
	print("\n\t 1)Pour une analyse simple:\n\t\t->python3 main.py --temrinal [chemin vers le fichier(txt)]")
	print("\n\t 2)Pour présicer un protocol donné:\n\t\t->python3 main.py --temrinal [chemin vers le fichier(txt)] --protocol=[nom du protocol]")
	print("\n\t\t\t->Les protocoles supportés par le programme : ETHERNET , IPV4 , TCP , HTTP ")
	print("\n\t 3)Pour visualiser un flot particulier en selectionnant les adresses IP les 2 machines imbriquées :"
	"\n\t\tpython3 main.py --temrinal [chemin vers le fichier(txt)] --adr1=[Adresse IP] --adr2=[Adresse IP]\n\t\t\t->'Adresse IP' respecte"
	" le format X.X.X.X ou X est une valeur dans l'intervalle : [0-255]")
	print("\n\t 4)Pour visualiser un flot particulier en selectionnant les adresses IP les 2 machines imbriquées plus le protocole :"
	"\n\t\t->python3 main.py --temrinal [chemin vers le fichier(txt)]  --protocol=[nom du protocol] --adr1=[Adresse IP] --adr2=[Adresse IP]")
elif aucune:
	print("Aucune trame n'a été analysée, Verifiez que votre fichier existe bien et qu'il contient des trames qui respectent le format attendu")
	


"""

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
#ainsi que la vraie structure trame appropiée à chaqu'un des messages capturés (C'est là qu'on delimite tous les champs)

if len(listeDeTrame)!=0:   # On verifie qu'il existe bien des trames respectant le format attendu dans le fichier trace lu
	trace=Trace(listeDeTrame)
	resultat=trace.analyse()  #La fonction analyse permet d'initialiser les champs de la trame(champ ethernet, ipv4,tcp et http)
	outPut(resultat,resultatAnalyseTrame)
	
	liste=trace.filtre("","55.51.4.23","55.51.246.193")
	print(len(liste))

"""