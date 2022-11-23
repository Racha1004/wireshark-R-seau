def hexToBin(test):
	entier=int("0x"+test,base=16)
	binaire=bin(entier)
	return binaire[2:]

def hexToDec(test):
	return int("0x"+test,base=16)

def binToDec(test):
	return int("0b"+test,base=2)

def parseTrame(liste):
	stringValeurs=""
	stringValeurs+=''.join(liste)
	stringValeurs=stringValeurs.replace('\n','')
	return stringValeurs

def formatMACAdress(adressMAC):
	res = adressMAC[0:2] + ":" + adressMAC[2:4] + ":" + adressMAC[4:6] + \
		":" + adressMAC[6:8] + ":" + adressMAC[8:10] + ":" + adressMAC[10:12]
	return res

def formatIPAdress(adressIP):
	return "{}.{}.{}.{}".format(hexToDec(adressIP[0:2]),
								hexToDec(adressIP[2:4]),
								hexToDec(adressIP[4:6]),
								hexToDec(adressIP[6:8]))
