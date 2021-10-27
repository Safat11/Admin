'''
Mode : "a" - {append}
\n- new line
Function : .write
#
-> Variable = open("File Name", "a")
Variable.write("\nTEXT")

->Variable.close()
.....................................
#Use Mode "w" all text overwrite :
#-> Variable = open("File Name", "w")

#New Text File Open :
#-> Variable = open("New File Name", "w")

'''

#
file = open("41.2. student.txt", "a")

file.write("\nSafat - Lecturer Of Physics")
file.close()

##New Text File Create :

file = open("42.2. Student.txt", "w")

file.write("Safat is learning in Python.")
file.write("\nSafat passed in HSC exam.")
file.write("\nSafat is a student of East West University.")

file.close()

## HTML File Create :

File = open("Hello.html", "w")
File.write("<h1>This is text </h1>")

File.close()