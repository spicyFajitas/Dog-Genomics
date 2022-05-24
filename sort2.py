#sort2.py
#if confused about functionality about code, check dogSorting.py script and refer to comments

def sort(fileName):
	homo = 0
	hetero = 0
	i=0
	r=raw_input("what is the chromosome you want the data for? ")					#reference variable
	for line in fileName:
		A, B, C, D, E, F = line.split()
		while A==r:
			if E==F:
				homo+=1
			else:
				hetero+=1
			break
			# removed printing each line
			#	in order to tidy up code
			
	print('Homozygous= '+str(homo), 'Heterozygous= '+str(hetero))
	print(i)

sort(fileName=open(input("What's the name of the file? "), "r"))