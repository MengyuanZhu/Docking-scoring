import sys
print "python enrichment.py ligandfileX5 outfile"

fileout=open(sys.argv[14], 'w')
dic={}

weight=1 #weight of pocket
for fileindex in range(1,13):
	fileread = open(sys.argv[fileindex], 'r')
	fileread.readline() #escape the first line
	if fileindex==13:
		weight=2
	while True:
		line=fileread.readline()
		if not line:
			break
		info=line.split()
		
		if dic.has_key(info[0]):
			dic[info[0]]=float(dic[info[0]])+float(info[1])*weight
		else:
			dic[info[0]]=info[1]*weight
		
	

dic_sorted=sorted(dic.iteritems(),key=lambda d:d[1],reverse=False)
for value,test in dic_sorted:
	
	fileout.write(value)
	fileout.write(" ")
	fileout.write(str(test))
	fileout.write("\n")		

fileread.close()
fileout.close()
