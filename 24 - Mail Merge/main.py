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
