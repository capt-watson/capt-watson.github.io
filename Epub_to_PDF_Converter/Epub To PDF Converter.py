
## import aspose.pdf as pdf

# Set the source directory path
filePath = "C://Words//"

# Load the license in your application to convert EPUB to PDF
pdfToPngLicense = pdf.License()
pdfToPngLicense.set_license(filePath + "Conholdate.Total.Product.Family.lic")

#Declare EpubLoadOptions object
epubLoadOptions = pdf.EpubLoadOptions()

marginInfo =pdf.MarginInfo() 
marginInfo.top=200

#Set margin info
epubLoadOptions.margin=marginInfo

#Load the EPUB into a Document class object
document = pdf.Document(filePath + "EPUBToPDF.epub", epubLoadOptions)

#save the document as PDF
document.save(filePath + "output.pdf")