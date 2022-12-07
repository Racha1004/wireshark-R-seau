def hexToBin(test):
	entier=int("0x"+test,base=16)
	binaire=bin(entier)
	return binaire[2:]

def hexToDec(test):
	return int("0x"+test,base=16)

def binToDec(test):
	return int("0b"+test,base=2)

def decToHex(test):
	hexa=hex(test)
	return hexa[2:]

def binToHex(test):
	hexa=hex(int("0b"+test,base=2))
	return hexa[2:]

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

"""
def outPut (data,fileName):
	with open(fileName,"w") as output: 
		output.write(data)
	output.close()
"""

def afficheTrame (trameParsée):
	trame=""
	hex=0
	for i in range(0,len(trameParsée),2):
		if i%32==0:
			if i!=0:
				trame=trame[:-1]
				trame+="\n"

			hex=decToHex(i//2)
			hex=hex.zfill(4)
			trame+=hex+"   "
		
		trame+=trameParsée[i:i+2]+" "

	trame=trame[:-1]
	return trame

def infoOption(liste,k):
	for d in liste:
		if d.get("Kind")==str(k):
			return d
	return None 


def asciiToString(ascii):
	i=0
	string=""
	while(i+1<=len(ascii)-1):
		string+=chr(hexToDec(ascii[i:i+2]))
		i+=2
	if len(ascii[i:])!=0:
		string+=chr(hexToDec(ascii[i:]))
	return string

class color:
	b = '\033[94m' #bleu
	g = '\033[92m' # vert
	y = '\033[93m' # jaune
	r = '\033[91m' # rouge
	n = '\033[0m' #gris, couleur normale
	m = '\033[95m'

lipsum = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, felis. Curabitur dictum gravida mauris. Nam arcu libero, nonummy eget, consectetuer id, vulputate a, magna. Donec vehicula augue eu neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris ut leo. Cras viverra metus rhoncus sem. Nulla et lectus vestibulum urna fringilla ultrices. Phasellus eu tellus sit amet tortor gravida placerat. Integer sapien est, iaculis in, pretium quis, viverra ac, nunc. Praesent eget sem vel leo ultrices bibendum. Aenean faucibus. Morbi dolor nulla, malesuada eu, pulvinar at, mollis ac, nulla. Curabitur auctor semper nulla. Donec varius orci eget risus. Duis nibh mi, congue eu, accumsan eleifend, sagittis quis, diam. Duis eget orci sit amet orci dignissim rutrum.'
couleurs =[color.g,color.y,color.b,color.r,color.m]

def colorise(text,i):
	r=''
	for c in text:
		r+=couleurs[i] + c + color.n 
	return r

def adIPDistinctes(listeDeTrames):
	listeIp=[]
	for trame in listeDeTrames:
		if not trame.erronee and (trame.tcp!=None or trame.http!=None):
			if formatIPAdress(trame.ipv4.sourceAdress) not in listeIp:
				listeIp.append(formatIPAdress(trame.ipv4.sourceAdress))
			if formatIPAdress(trame.ipv4.destinationAdress) not in listeIp:
				listeIp.append(formatIPAdress(trame.ipv4.destinationAdress))
	return listeIp
		
#afficheTrame("0812002087b008001108c063080045004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029e5fc815890700812002087b008001108c063080045004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029e5fc815890700812002087b008001108c063080045004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029e5fc815890700812002087b008001108c063080045004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029e5fc81589070")
#print("_{}_".format(asciiToString("475a54")))