#coding:utf8

with open("trameTest.txt","r") as fichier:
	contenu=fichier.readlines()
	lineBis=[]
	for line in contenu:
		lineBis.append(line.split(" "))
		

#print(lineBis)
trames=[]
ligneI=[]
i=0

for line in lineBis:
	d=int(line[0],base=16)
	print(len(trames))
	if d==0 and i!=0:
		if len(trames)==0:
			trames=[ligneI] 
		else:
			trames.append(ligneI)
		ligneI=[]

	lineSansOffset=line[1:]
	ligneI.extend(lineSansOffset)
	i+=1

trames.append(ligneI)
print(trames)


