File1 = open("InputFile1", "r")
File2 = open("InputFile2.txt", "r")
File3 = open("Differences.txt", "w")

for File1Rows in File1:
        File2Rows = File2.readline()
        if(File1Rows != File2Rows):
                File3.write(File1Rows)
			
File1.close()
File2.close()
File3.close()
