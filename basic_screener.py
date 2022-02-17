wordfile = open("english_words.txt", "r") # List of all English words
wordlist = wordfile.read()


def filter(color: str, letter: str, index: int, words: list) -> list:
    """Takes in a list of words and filters out impossible choices based on if the letter is yellow, green, or black and the position of the letter"""
    filtered_words = []

    if color == "Y":
        for word in words:
            for i in range (0,5):
                if (word[i] == letter) and not (word[index-1] == letter):
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
    possible_words = []

    for line in wordlist.split("\n"):
        if len(line) == 5:
            possible_words.append(line.upper())

    while len(possible_words) > 1:
        info = []
        index = 1
        while index <= 5:
            color = input(f"Color of square {index} - G for green, Y for yellow, or B for black: ").upper()
            letter = input(f"Letter in square {index}: ").upper()
            print()
            info.append((color, letter, index))

            index += 1

        for entry in info:
            black_and_hit = False
            for entry2 in info:
                if (entry[0] == "B") and (entry2[0] == "G" or entry2[0] == "Y") and (entry[1] == entry2[1]) and not (entry[2]==entry2[2]):
                    black_and_hit = True
            if not black_and_hit:
                possible_words = filter(entry[0], entry[1], entry[2], possible_words)

        possible_words = sorted(possible_words)


        if len(possible_words) > 100:
            if input("You still have over 200 possible words! Would you like to show them (Y for yes)?: " ).upper() == "Y":
                print("Possible words: " + ", ".join(possible_words))
        elif len(possible_words) > 1:
            print("Possible words: " + ", ".join(possible_words))

        elif len(possible_words) == 0:
            print("Error! No words match your criteria.")

        else:
            print("The word is: " + possible_words[0])
            print("Nice job!")

    if input("\nType \"A\" to go again, or press enter to close: ").upper() == "A":
        main()


if __name__ == "__main__":
    main()
