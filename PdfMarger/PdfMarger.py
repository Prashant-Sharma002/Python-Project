import PyPDF2
Pdf_1=input("Enter the name of pdf 1: ")
Pdf_2=input("Enter the  name of pdf 2: ")

Pdfile= [f"{Pdf_1}",f"{Pdf_2}"]
Marging=PyPDF2.PdfMerger()

for FileName in Pdfile:
    Pdfile=open(FileName,'rb')
    PdfReader=PyPDF2.PdfReader(Pdfile)
    Marging.append(PdfReader)


Pdfile.close()
Marging.write('Marged.pdf')