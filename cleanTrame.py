def enHexa(test):
	try:
		int("0x"+test,base=16)
		return True
	except:
		return False

def nouvelleTrame(byte):
	try:
		x=int("0x"+byte,base=16)
	except:
		return False
	return x==0


def offsetValide(byte,ancienOffset,byteLu):
	try:
		dec=int("0X"+byte,base=16)
	except:
		return False
	return dec== ancienOffset+byteLu

def tramesValides(nameFile):
	trames=""
	trame=""
	numLigne=0
	byteLu=0
	ancienOffset=0
	with open(nameFile,"r") as fichier:
		
		lignes=fichier.readlines()

		for ligne in lignes:
			pos=0

			ligne=ligne.rstrip()
			if(len(ligne)!=0):

				numLigne+=1
				isOffset=True
				erreurDetectee=False#Pour sauter toutes les lignes de trame comportant une erreur!

				splitted=ligne.split(" ")

				print(splitted)


				for byte in range(len(splitted)):

					if isOffset:
						isOffset=False
						pos=1
						if(nouvelleTrame(splitted[byte])):
							if(len(trame)>=10 and not erreurDetectee):#Si la trame a au la taille min requise
								if trames!="":
									trames+="\n"
								trames+=trame
							byteLu=0
							ancienOffset=0
							erreurDetectee=False
							trame=""
						elif erreurDetectee:
							break
						elif offsetValide(splitted[byte],ancienOffset,byteLu) :
							ancienOffset+=byteLu
							byteLu=0
						else:
							erreurDetectee=True
							trame=""
							print("Offset incorrect ligne : {}, {}, {} ,{}".format(numLigne,splitted[byte],ancienOffset,byteLu))
							break

					elif byte==1 or byte==2 :#pour les 3 espaces de l'offset
						if splitted[byte]!="":
							erreurDetectee=True
							print("Offset de la ligne : {} n'est pas separé de 3 espaces des octets".format(numLigne))
							break
						else:
							continue
					elif not erreurDetectee :
						if(len(splitted[byte])==2 and enHexa(splitted[byte])):
							byteLu+=1
							trame+=splitted[byte]
						else:
							erreurDetectee=True
							trame=""
							print("La ligne {} contient un octet : _{}_ qui ne respecte pas le format attendu".format(numLigne,splitted[byte]))
					else:
						break

	if(len(trame)>=10 and not erreurDetectee):#Si la trame a au la taille min requise
		if trames!="":
			trames+="\n"
		trames+=trame


	fichier.close()
	return trames


trame=tramesValides("trameOffset.txt")
print(trame)




		