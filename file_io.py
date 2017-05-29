#f = open("test_file.txt", "w")
#r+ means read and write file

#f.write("This is a new line.")

#f.close()

#This overwrote all three lines of a file I made with this one new line.
#my_list = ["This is line one", "This is line two", "This is line three"]

#f = open("test_file.txt", "r+")
#for item in my_list:
    #f.write(item + "\n")
#f.close()
#This overwrote that first line with each of these list items on a new line.

f = open("test_file.txt", "r")
print(f.read())
f.close()
#This prined all three lines of the file.

this = open("test_file.txt", "r")
print(this.readline())
f.close()
#this printed line one

this = open("test_file.txt", "r")
print(this.readline())
print(this.readline())
print(this.readline())
this.close()
#this prints each of the lines in sequence
