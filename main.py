

with open("./Input/Letters/starting_letter.txt", 'r') as f:
    line_list = f.readlines()

with open("./Input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()


for name in name_list:
    correct_name = line_list[0].replace("[name]", name_list[name_list.index(name)])
    corrected_letter = line_list[0].replace("Dear [name]", correct_name)

    with open("/Users/admin/Pictures/Mail Merge Project Start/Output/ReadyToSend/invitation_letter.txt", '') as f:
        final_letter = f.write(corrected_letter + line_list[1] + line_list[2] + line_list[3])
''' with open("/Users/admin/Pictures/Mail Merge Project Start/Output/ReadyToSend/invitation_letter.txt", 'a') as f:
        for line in line_list:
            f.write(line_list[1] + line_list[2] + line_list[3])
'''









#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp