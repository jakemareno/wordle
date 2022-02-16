wordfile = open("words.txt", "r")
wordlist = wordfile.read()

WORDS = []
possible_words = []


"""
ALPHABET = []
letter = 'A'
while ord(letter) <= ord('Z'):
    ALPHABET.append(letter)
    letter = chr(ord(letter) + 1)
"""

def filter(index: int, letter: str, words):
    temp = []

    if color == "Y":
        for word in words:
            for i in range (0,5):
                if (word[i] == letter) and (i != (index - 1)):
                    temp.append(word)

    elif index == "G":
        for word in words:
            if word[index - 1] == letter:
                temp.append(word)


    else:
        for word in words:
            in_word = False
            for i in range (0,5):
                if word[i] == letter:
                    in_word = True

            if(not in_word):
                temp.append(word)

    return temp

def main():
    for line in wordlist.split("\n"):
        if len(line) == 5:
            WORDS.append(line.upper())

    possible_words = WORDS

    while len(possible_words) > 1:
        color = input("Color of square (G, Y, or B): ").upper()
        index = int(input("Position of letter: "))
        letter = input("Letter: ").upper()
        print("\n")

        possible_words = filter(color, index, letter, possible_words)

        if len(possible_words) > 1:
            print("Possible words: " + ", ".join(possible_words))
            print("\n")

        else:
            print("The word is: " + possible_words[0])
            print("Nice job!")


if __name__ == "__main__":
    main()
