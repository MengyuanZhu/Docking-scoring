import sys
print "python enrichment.py decoyfile ligandfile outfile"

num_lines_decoy = sum(1 for line in open(sys.argv[1]))
num_lines_ligand= sum(1 for line in open(sys.argv[2]))

span_decoy = 402
span_ligand= 1


if span_decoy==0:
	span_decoy=1
if span_ligand==0:
	span_ligand=1


file1 = open(sys.argv[1], 'r')
file2 = open(sys.argv[2], 'r')
fileout=open(sys.argv[3], 'w')

file1.readline()
file2.readline()
x = 0
y = 0
line_ligand=file2.readline()

line_ligand=line_ligand.split()

score_ligand=float(line_ligand[1])


while True:
	line_decoy=file1.readline()
	if not line_decoy:
		break
	x+=1
	line_decoy=line_decoy.split()
	score_decoy=float(line_decoy[1])
	
	while True:
		if score_ligand<=score_decoy:
			y=y+1
			
					
			line_ligand=file2.readline()
			if not line_ligand:
				break
			line_ligand=line_ligand.split()
			print line_ligand
			
			score_ligand=float(line_ligand[1])
			
			if x%span_decoy==0:
			
				fileout.write(str(x/span_decoy))
				fileout.write(" ")
				fileout.write(str(y/span_ligand))
				fileout.write("\n")
				
				
		else:
			if x%span_decoy==0:
				fileout.write(str(x))
				fileout.write(" ")
				fileout.write(str(y+1))
				fileout.write("\n")
			break
		if not line_ligand:
			break	
		

file1.close()
file2.close()
