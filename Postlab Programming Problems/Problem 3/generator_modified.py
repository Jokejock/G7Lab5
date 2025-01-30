"""
Program: generator_modified.py
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random
def getWords(filename):
    """Reads a file and returns a tuple of words."""
    word_list = []
    try:
        with open(filename, 'r') as file:
            # Read each line and strip newline characters
            for line in file:
                word_list.append(line.strip())
        # Convert list to tuple before returning
        return tuple(word_list)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return tuple()

# Load vocabulary from files
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
articles = getWords("articles.txt")
prepositions = getWords("prepositions.txt")

# Ensure all files were loaded successfully
if not all([nouns, verbs, articles, prepositions]):
    print("Error: One or more vocabulary files are missing or empty.")
    exit()

# Function to generate a random sentence
def generate_sentence():
    article = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    preposition = random.choice(prepositions)
    object_noun = random.choice(nouns)

    # Form the sentence
    sentence = f"{article} {noun} {verb} {preposition} {object_noun}."
    return sentence

# Main loop to generate sentences
if __name__ == "__main__":
    print("Sentence Generator!")
    while True:
        print(generate_sentence())
        continue_choice = input("Generate another sentence? (y/n): ").strip().lower()
        if continue_choice != 'y':
            break