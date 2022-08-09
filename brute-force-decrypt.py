import PyPDF2


#encrypt for testing purposes
'''pdf_file_obj = open("finance-sample.pdf", "rb")
pdf_file_reader = PyPDF2.PdfFileReader(pdf_file_obj)
pdf_file_writer = PyPDF2.PdfFileWriter()


for page in range(0, pdf_file_reader.numPages):
    pdf_file_writer.addPage(pdf_file_reader.getPage(page))


pdf_file_writer.encrypt("CASUALS")
result_pdf = open("finance-sample_encrypted.pdf", "wb")
pdf_file_writer.write(result_pdf)
result_pdf.close()
pdf_file_obj.close()'''



#open PDF for decryption
pdf_file_obj = open("finance-sample_encrypted.pdf", "rb")
pdf_file_reader = PyPDF2.PdfFileReader(pdf_file_obj) 


#read text file and test which password works (default uppercase or lowercase)
decrypted = False
text_file = open("dictionary.txt", "r")
password = text_file.readline()
password = password.strip("\n")
while password != "":
        #print(password)
        if(pdf_file_reader.decrypt(password)):
            print("PDF was decrypted by the following password: {}".format(password))
            print("Evidence: ")
            print(pdf_file_reader.getPage(0))
            decrypted = True
            break
            
        if(pdf_file_reader.decrypt(password.lower())):
            print("PDF was decrypted by the following password: {}".format(password.lower()))
            print("Evidence: ")
            print(pdf_file_reader.getPage(0))
            decrypted = True
            break

        password = text_file.readline()
        password = password.strip("\n")

text_file.close()
pdf_file_obj.close()

if not decrypted:
    print("File could not be decrypted.")