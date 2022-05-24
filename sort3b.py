#sort3a.py

def sort(fileName):
	i=0
	homochr = 0
	heterochr(i) = 0
	for line in fileName:
		A, B, C, D, E, F = line.split()
		if int(A)==i:
			if E==F:
				homochr+=1
			else:
				heterochr+=1
		else:
			if E==F:
				#initialize new variables
				i+=1
				homochr(i)+=1
			else:
				heterochr(i)+=1
			i+=1

	print('Homozygous= '+str(homo), 'Heterozygous= '+str(hetero))
	print(i)

sort(fileName=open(raw_input("What's the name of the file? "), "r"))