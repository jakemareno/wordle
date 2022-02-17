import time

wordfile = open("english_words.txt", "r")
wordlist = wordfile.read()


# Initialize list with all 5 letter words
WORDS = []
for line in wordlist.split("\n"):
    if len(line) == 5:
        WORDS.append(line.upper())


# Used for crunching letter frequency/efficiency
ALPHABET = []
counter = "A"
while ord(counter) <= ord("Z"):
    ALPHABET.append(counter)
    counter = chr(ord(counter) + 1)


# Scoring constants -
GREEN_POINTS = 3
YELLOW_POINTS = 2
DUPLICATE_REDUCTION_FACTOR = 0.6 # percent multiplier in points for being a duplicate
S_REDUCTION_FACTOR = 0.5

def score_letter(letter: str, words: list) -> int:
    """Returns the amount of times a letter occurs in a given list of words."""
    score = 0
    for word in words:
        for i in range(0, len(word)):
            if word[i] == letter:
                score += 1

    return score


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


def sort_by_value(scores) -> dict:
    return dict(sorted(scores.items(), key = lambda kv: kv[1], reverse=True))


def main():
    start_time = time.time()
    letter_scores = {}
    word_scores = {}
    word_count = len(WORDS)

    for letter in ALPHABET:
        letter_scores[letter] = score_letter(letter, WORDS)
        letter_scores[letter] = float(letter_scores[letter]/word_count)

    letter_scores = sort_by_value(letter_scores)

    print("Letters by frequency:")
    for letter, score in letter_scores.items():
        print(f"{letter}: {score}")

    time1 = time.time()
    total_time = 0
    scored_words = 0
    for word in WORDS:
        word_scores[word] = score_word(word, WORDS)
        scored_words += 1
        if(word_count % 100 == 0):
            time2 = time.time()
            total_time += (time2 - time1)
            estimate = round(total_time/(scored_words/word_count), 1)
            time1 = time2
            print(f"Words remaining: {word_count}")
            print(f"Estimated time remaining: {estimate} seconds.\n")

        word_count -= 1

    word_scores = sort_by_value(word_scores)

    print("Top 20 words by score: ")
    i = 0
    for word, score in word_scores.items():
        print(f"{word}: {score}")
        i += 1
        if i >= 20:
            break


    total_time = round(time.time() - start_time, 2)
    print(f"\nTook {total_time} seconds to compute.")


if __name__ == "__main__":
    main()
    input("Press enter to close: ")
