from PyPDF2 import PdfFileWriter, PdfFileReader

inputFile = PdfFileReader(open("fileToBeSplit.pdf", "rb"))
for i in range(inputFile.numPages // 2):
  output = PdfFileWriter()
  output.addPage(inputFile.getPage(i * 2))
  if i * 2 + 1 <  inputFile.numPages:
    output.addPage(inputFile.getPage(i * 2 + 1))
    newname = "Output-" + str(i) + ".pdf"
    outputStream = open(newname, "wb")
    output.write(outputStream)
    outputStream.close()
