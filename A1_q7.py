from os import listdir,rename

def list_dir(directory_name):
	directory_name = input("Enter the directory: ")
	list(listdir(directory_name))

def rename_file(directory_name,old_filename,new_filename):
	src = directory_name + '/' + old_filename
	des = directory_name + '/' + new_filename
	try:
	    rename(src,des)
	except:
	    print("ERROR! Couldn't find the source file name")
	else:
	    print("File rename executed succesfully")


directory_name = input("Enter the directory name: ")
old_filename = input("Enter old filename: ")
new_filename = input("Enter new filename: ")

listdir(directory_name)
rename_file(directory_name,old_filename,new_filename)