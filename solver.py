from typing import List

wordfile = open("words.txt", "r")
wordlist = wordfile.read()

WORDS = []
possible_words = []


def filter(color: str, letter: str, index: int, words: List) -> List:
    filtered_words = []

    if color == "Y":
        for word in words:
            for i in range (0,5):
                if (word[i] == letter) and (i != (index - 1)):
                    filtered_words.append(word)

    elif color == "G":
        for word in words:
            if word[index - 1] == letter:
                filtered_words.append(word)

    else:
        for word in words:
            in_word = False
            for i in range (0,5):
                if word[i] == letter:
                    in_word = True

            if(not in_word):
                filtered_words.append(word)

    filtered_words = list(set(filtered_words))
    return filtered_words


def main():
    for line in wordlist.split("\n"):
        if len(line) == 5:
            WORDS.append(line.upper())

    possible_words = WORDS

    while len(possible_words) > 1:
        color = input("Color of square - G for green, Y for yellow, or B for black: ").upper()
        letter = input("Letter: ").upper()
        index = int(input("Position of letter (1-5): "))
        print("\n")

        possible_words = filter(color, letter, index, possible_words)

        if len(possible_words) > 1:
            print("Possible words: " + ", ".join(possible_words))

        elif len(possible_words) == 0:
            print("Error! No words match your criteria.")

        else:
            print("The word is: " + possible_words[0])
            print("Nice job!")


if __name__ == "__main__":
    main()
