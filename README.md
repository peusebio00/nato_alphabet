# nato_alphabet
O
Small project made using the Pandas library within Python to analyse a CSV file with the NATO alphabet in it - organised by letter (Standard Roman ALphabet letters) and their respective code within the NATO Alphabet (Alpha, Beta, Charlie, etc)

CSV file read using Pandas, then transformed to DataFrame, then rows iterated to create a new dictionary (phonetic_dict) in which the key == letters and value == NATO code

Finally, using list comprehension, user is asked for an input (string in which each letter will looped through and turned into the NATO alphabet - Pedro will be turned into Papa, Echo, Delta, Romeo, Oscar) - also supports blank spaces if user wants to input a sentence rather than an individual word
