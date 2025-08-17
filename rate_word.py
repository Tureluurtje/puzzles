import re
import math

def rate_word_advanced(word, common_words=None):
    word = word.lower()

    # 1. Length
    length_score = min(5, max(1, math.ceil(len(word) / 3)))

    # 2. Letter complexity
    uncommon_letters = set("qjxz")
    complexity_score = sum(1 for c in word if c in uncommon_letters)
    complexity_score = min(5, 1 + complexity_score)

    # 3. Syllables
    syllables = len(re.findall(r'[aeiouy]+', word))
    if syllables <= 1:
        syllable_score = 1
    elif syllables == 2:
        syllable_score = 2
    elif syllables == 3:
        syllable_score = 3
    elif syllables == 4:
        syllable_score = 4
    else:
        syllable_score = 5

    # 4. Morphology
    morph_score = 1
    if '-' in word or "'" in word:
        morph_score = 4
    elif re.search(r'[A-Z]', word[1:]):
        morph_score = 3

    # 5. Rarity/frequency
    if common_words and word in common_words:
        rarity_score = 1
    else:
        rarity_score = 3
        if length_score >= 4 or complexity_score >= 3 or syllable_score >= 4:
            rarity_score += 1
        if length_score >= 5 or syllable_score >= 5:
            rarity_score = 5

    # Weighted average
    difficulty = round(
        (length_score*0.2 + complexity_score*0.2 + syllable_score*0.3 + morph_score*0.1 + rarity_score*0.2)
    )

    difficulty = max(1, min(5, difficulty))
    return difficulty


print('enter for exit')
while True:
    y = input('type woord: ')
    if y == "":
        break
    x = rate_word_advanced(y)
    print(x)