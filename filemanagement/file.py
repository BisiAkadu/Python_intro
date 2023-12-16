definition1 = """
A computer file is a computer resource for recording data discretely in a
computer storage device. Just as words can be written 
to paper, so can information be written to a computer
file. Files can be edited and transferred through the 
internet on that particular computer system."""

# we will write this a file called definition.txt
open("file_definition.txt", "w").write(definition1)

#read the content of the file_definition.txt into another file
new_txt=open("file_definition.txt").read()
print(new_txt)


#create another text file
open("bisi.txt", "w").write(new_txt)
with open("bisi.txt","r") as fh:
    for line in fh:
        print(line.strip())
#if you do not want to use with, alternatively use 
#the code below making sure to exclusively close the loop
sh=open("bisi.txt")
for line in sh:
    print(line.strip())
sh.close()
     


