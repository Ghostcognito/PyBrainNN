"Preporceseor for NN"

file = open("SourceIP.txt", "r")


index = []
ind = []
index2 = []

temp = ''
for i in file:
    temp = str(i)
    #temp = temp.rstrip()
    index.append(temp.replace('.','',3))

file1 = open("SourceIPSpacePort.txt", "a")
for i in index:
    temp2 = str(i)
    file1.write(temp2)
file1.close()

file2 = open("SourceIPSpacePort.txt", "r")
for i in file2:
    temp3 = str(i)
    index2.append(temp3.replace('.',' ',))

file3 = open("SourceFormated.txt", "a")
for i in index2:
    temp4 = str(i)
    file3.write(temp4)
file3.close()
    
