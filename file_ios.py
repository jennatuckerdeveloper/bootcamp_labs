#with open("test_file.txt", "r+") as this:
    #this.write("This should overwrite some portion of the file.")
    #and it should close automatically
    #print(this.read())
    #so it doesn't overwrite the entire file.  It kept the last portion.  Weird af.
#this overwrote a portion of the file as long as the string
#then it printed from there onwards
with open("test_file.txt", "r+") as this:
    print(this.read())
    this.seek(0)
    this.write("Where does this end up.")
    #this order added the line to the end of the file!
this = open("test_file.txt", "r+")
print(this.read())
this.close()
#it ends up at the beginning
