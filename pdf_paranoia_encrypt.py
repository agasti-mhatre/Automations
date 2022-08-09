import os
from pathlib import Path
import PyPDF2

#password = abc
password = str(input("Enter a password for all of the PDFs: "))

#Go through each pdf file and encrypt it

for dir, sub_dir, files in os.walk(Path.cwd()):    
    #print(dir)
    #print(sub_dir)
    #print(files)
    
    #make name list to ensure that if the core name of the file is separated by dots, that these components will not be lost
    name = []
    for file in files:
        #extract extension from file name
        name = file.split(".")
        extension = name[-1]
        #print("{} {}".format(name, extension))

        #if the extension is a pdf, encrypt it
        if(extension == "pdf"):
            fileObj = open(dir + '\\' + file, 'rb')
            temp_reader = PyPDF2.PdfFileReader(fileObj)

            #if the pdf is encrypted, skip the file
            if(temp_reader.isEncrypted):
                fileObj.close()
                continue


            temp_writer = PyPDF2.PdfFileWriter()
            for pageNum in range(temp_reader.numPages):
                temp_writer.addPage(temp_reader.getPage(pageNum))

            #create new file that is encrypted with "_encrypted" added to file name
            new_name = ""
            for word in range(0, len(name) - 1):
                if word > 0:
                    new_name += "." + name[word]
                    continue
                new_name += name[word] 

            new_name += "_encrypted" + ".pdf"

            #encrypt and save file
            temp_writer.encrypt(password)
            pdf_writer = open(dir + '\\' + new_name, 'wb')
            temp_writer.write(pdf_writer)

            #close all open files
            pdf_writer.close()
            fileObj.close()

            #attempt to read and decrypt the new file before deleting old file
            original_name = ""
            for word in range(0, len(name) - 1):
                if word > 0:
                    original_name += "." + name[word]
                    continue
                original_name += name[word]

            original_name += ".pdf"

            file_encrypted_obj = open(dir + '\\' + new_name, 'rb')
            file_encrypted = PyPDF2.PdfFileReader(file_encrypted_obj)

            if(file_encrypted.decrypt(password)):
                os.remove(dir + '\\' + original_name)

            file_encrypted_obj.close()


  