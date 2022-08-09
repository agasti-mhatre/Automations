import os
from pathlib import Path
import PyPDF2

#password = abc
password = str(input("Enter a password for all of the PDFs: "))

#Go through each pdf file and decrypt it

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

        #if the extension is a pdf, decrypt it
        if(extension == "pdf"):

            fileObj = open(dir + '\\' + file, 'rb')
            temp_reader = PyPDF2.PdfFileReader(fileObj)


            #if file is encrypted, attempt to decrypt it
            if(temp_reader.isEncrypted):
                if(temp_reader.decrypt(password)):
                    #change the name of the file so that it is no longer labeled as a decrypted PDF
                    old_name = []
                    old_name = file.split("_")
                    new_name = ""

                    for word in range(0, len(old_name)): 
                        if old_name[word] != "encrypted.pdf":
                            if word > 0:
                                new_name += "_" + old_name[word]
                                continue
                            new_name += old_name[word]
                    
                    new_name += ".pdf"

                    #create writer object and make a new PDF that is not encrypted
                    file_writer = PyPDF2.PdfFileWriter()

                    for pageNum in range(temp_reader.numPages):
                        file_writer.addPage(temp_reader.getPage(pageNum))

                    writer_obj = open(dir + '\\' + new_name, 'wb')
                    file_writer.write(writer_obj)

                    writer_obj.close()
                    fileObj.close()

                else:
                    print("PDF could not be decrypted because the password is incorrect.")
                    fileObj.close()
                    continue





            