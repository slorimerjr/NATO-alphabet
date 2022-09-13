import pandas


# My solutions

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# # TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the word you'd like to get the phonetic code for: ").upper()
word_list = [letters for letters in word]

nato_word = []
for letter in word_list:
    nato_word.append(nato_dict[letter])
print(nato_word)


# Teacher's solution

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

# All List Comprehension 'templates':

# Pandas DataFrame:
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Lists:
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]

# Dictionaries:
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dictionary.items() if test}
