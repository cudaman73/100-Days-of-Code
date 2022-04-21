# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_dict = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
# Iterate over csv in form letter: code to create new dictionary with values
nato_alphabet = {row.letter: row.code for (index, row) in nato_dict.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
# Day 30 - we add KeyError catching for when users enter invalid input. An
# alternative approach would be to use function recursion - if we encased our
# try/except/else functionality in a function, we can call the function again
# during the exception, which will loop until there is no KeyError.

while True:
    try:
        word = input("Give me a word, I will spell it out phonetically:").upper()
        nato_array = [nato_alphabet[letter] for letter in word]
        break
    except KeyError:
        print("Sorry, please only input letters.")

print(nato_array)

