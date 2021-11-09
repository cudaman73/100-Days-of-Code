#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("Input/Names/invited_names.txt")
name_list = f.readlines()
f.close()

f = open("Input/Letters/starting_letter.txt")
start_letter = f.readlines()
f.close()
old_name = "[name]"

for name in name_list:
    letter = start_letter
    name = name.strip()
    letter[0] = start_letter[0].replace(old_name, name)
    filename = f"Output/ReadyToSend/letter_for_{name}.txt"
    f = open(filename, "w")
    f.writelines(letter)
    f.close()
    old_name = name
