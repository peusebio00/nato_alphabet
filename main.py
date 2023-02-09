import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
phonetic_dict[" "] = " "

game_is_on = True
while game_is_on:
    word = input("Enter a word: ").upper()
    output = [phonetic_dict[letter] for letter in word]
    print(output)
    question = input("Would you like to convert a different name? Type 'y' or 'n': ")
    if question == "n":
        game_is_on = False
