import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # print(key, value)
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index, row)
    # print(row.student, row.score)
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict.items()) => dict_items([('A', 'Alfa'), ('B', 'Bravo'), ('C', 'Charlie'), ('D', 'Delta')]

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter the word you'd like to get the phonetic code for: ").upper()
word_list = [letters for letters in word]


# print(nato_dict[word_list[0]]) -> for "Sam" will print "Sierra"
# provides answer:
nato_word = []
for letter in word_list:
    nato_word.append(nato_dict[letter])
print(nato_word)







# nato_dict = {new_key:new_value for (index, row) in DataFrame.iterrows()}


# nato_dict = {new_key:new_value for item in nato_data}


# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dictionary.items() if test}

# new_dict = {new_key:new_value for (index, row) in dataframe.iterrows()}
