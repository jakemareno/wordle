from typing import List

wordfile = open("words.txt", "r")
wordlist = wordfile.read()

WORDS = []
ALPHABET = []

GREEN_POINTS = 2
YELLOW_POINTS = 1

letter_scores = {}
word_scores = {}


def score_letter(letter: str, words: List) -> int:
    score = 0
    for word in words:
        for i in range (0,5):
            if word[i] == letter:
                score += 1

    return score



def main():
    word_count = 0

    for line in wordlist.split("\n"):
        if len(line) == 5:
            WORDS.append(line.upper())
            word_count += 1


    counter = "A"
    while ord(counter) <= ord("Z"):
        ALPHABET.append(counter)
        counter = chr(ord(counter) + 1)

    for letter in ALPHABET:
        letter_scores[letter] = score_letter(letter, WORDS)
        letter_scores[letter] = float(letter_scores[letter]/word_count)

    for letter, score in letter_scores.items():
        print(f"{letter}: {score}")


if __name__ == "__main__":
    main()
    input("Press enter to close: ")
