import json

new_list = []
choice = True

try:
	while choice:
		new_dict={}
		new_dict['roll_no'] = input("Enter roll no: ")
		new_dict['name'] = input('Enter name: ')
		new_dict['age'] = input('Enter branch: ')
		new_list.append(new_dict)
		with open('file.json','w') as f:
	   		f.write(json.dumps(new_list, indent =4))
		choice = int(input("Do you want to add another student (0 for no, 1 for yes)? "))
except:
	print("ERROR! couldn't create json file")
else:
	print("\nJson file created succesfully with following format: ")

print(json.dumps(new_list,indent=2))
