wordfile = open("english_words.txt", "r")
wordlist = wordfile.read()


# Used for crunching letter frequency/efficiency
ALPHABET = []
counter = "A"
while ord(counter) <= ord("Z"):
    ALPHABET.append(counter)
    counter = chr(ord(counter) + 1)


# Scoring constants
GREEN_POINTS = 3
YELLOW_POINTS = 2
DUPLICATE_REDUCTION_FACTOR = 0.6 # percent multiplier in points for being a duplicate
S_REDUCTION_FACTOR = 0.5 # reduce effectiveness of S due to plurals


def score_letter_position(letter: str, words: list, index: int, occurences: int) -> int:
    """Scores a letter accounting for its position in the word, giving more points for a direct hit."""
    score = 0
    for word in words:
        for i in range(0, len(word)):
            if word[i] == letter:
                if i == index:
                    if not letter == "S":
                        score += GREEN_POINTS
                else:
                    if not letter == "S":
                        score += YELLOW_POINTS
                    else:
                        score += YELLOW_POINTS*S_REDUCTION_FACTOR


    if occurences > 1:
        return int(score*DUPLICATE_REDUCTION_FACTOR)
    return score


def score_word(word: str, words: list) -> int:
    """Scores a word based on how often its letters appear in the given list of words."""
    score = 0

    for i in range(0,len(word)):
        score += score_letter_position(word[i], words, i, word.count(word[i]))

    return score


def score_words(words: list) -> dict:
    scores = {}
    for word in words:
        scores[word] = score_word(word, words)
    return scores



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


def sort_by_value(scores: dict) -> dict:
    return dict(sorted(scores.items(), key = lambda kv: kv[1], reverse=True))


def top_scores(word_dict: dict) -> dict:
    top_scores_dict = {}

    i = 0
    for word, score in sort_by_value(word_dict).items():
        top_scores_dict[word] = score
        i += 1
        if i >= 20:
            break

    return top_scores_dict


def main():
    possible_words = []

    for line in wordlist.split("\n"):
        if len(line) == 5:
            possible_words.append(line.upper())

    while len(possible_words) > 1:
        scores = {}
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
                if (entry[0] == "B") and (entry2[0] == "G" or entry2[0] == "Y") and (entry[1] == entry2[1]):
                    black_and_hit = True
            if not black_and_hit:
                possible_words = filter(entry[0], entry[1], entry[2], possible_words)


        possible_words = sorted(possible_words)


        if len(possible_words) > 1:
            if len(possible_words) > 200:
                if input("You still have over 200 possible words! Would you like to show them (Y for yes)?: " ).upper() == "Y":
                    print("Possible words: " + ", ".join(possible_words))

            else:
                print("Possible words: " + ", ".join(possible_words))

            scores = score_words(possible_words)
            scores = top_scores(scores)

            print("Top 20 best choices for next word: ")
            i = 1
            for word, score in scores.items():
                print(f"{i}) {word}")
                i += 1
            print()


        elif len(possible_words) == 0:
            print("Error! No words match your criteria.")

        else:
            print("The word is: " + possible_words[0])
            print("Nice job!")

    if input("\nType \"A\" to go again, or press enter to close: ").upper() == "A":
        main()


if __name__ == "__main__":
    main()
