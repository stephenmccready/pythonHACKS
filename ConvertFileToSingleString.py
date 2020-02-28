import sys
infilename=sys.argv[1]
outfilename = infilename.rstrip('.txt') + '.270'

i = open(infilename)
o = open(outfilename, "w")
outputString = ''

for x in i:
	outputString+=x.rstrip('\r\n')

o.write(outputString)
