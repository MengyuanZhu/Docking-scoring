import sys
print "python enrichment.py ligandfileX5 outfile"

num_lines_ligand= sum(1 for line in open(sys.argv[1]))

span_decoy = 402
span_ligand= 1

if span_decoy==0:
	span_decoy=1
if span_ligand==0:
	span_ligand=1

file1 = open(sys.argv[1], 'r')

fileout=open(sys.argv[6], 'w')

file1.readline()

x = 0
y = 0

dic={}

while True:
	line_decoy=file1.readline()
	if not line_decoy:
		break
	x+=1
	line_decoy=line_decoy.split()
	score_decoy=float(line_decoy[1])
	compound_name=str(line_decoy[0])

	file2 = open(sys.argv[2], 'r')
	while True:
		line_file2=file2.readline()
		if not line_file2:
			break
		line_file2_split=line_file2.split()
		if compound_name==line_file2_split[0]:
			score_decoy=score_decoy+float(line_file2_split[1])
			break
	file2.close()

	file3 = open(sys.argv[3], 'r')
	while True:
		line_file3=file3.readline()
		if not line_file3:
			break
		line_file3_split=line_file3.split()
		if compound_name==line_file3_split[0]:
			score_decoy=score_decoy+float(line_file3_split[1])
			break
	file3.close()

	file4 = open(sys.argv[4], 'r')
	while True:
		line_file4=file4.readline()
		if not line_file4:
			break
		line_file4_split=line_file4.split()
		if compound_name==line_file4_split[0]:
			score_decoy=score_decoy+float(line_file4_split[1])
			break
	file4.close()

	file5 = open(sys.argv[5], 'r')
	while True:
		line_file5=file5.readline()
		if not line_file5:
			break
		line_file5_split=line_file5.split()
		if compound_name==line_file5_split[0]:
			score_decoy=score_decoy+float(line_file5_split[1])
			break
	file5.close()
	dic[compound_name]=score_decoy

dic_sorted=sorted(dic.iteritems(),key=lambda d:d[1],reverse=False)
for value,test in dic_sorted:
	
	fileout.write(value)
	fileout.write(" ")
	fileout.write(str(test))
	fileout.write("\n")		

file1.close()
fileout.close()
