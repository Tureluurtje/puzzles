import json
import random

with open('words.json', 'r') as file:
    words = json.load(file)
    
puzzle_entries = words["puzzle_entries"]
solution_phrases = words["solution_phrases"]

def select_word(letter: str):
    try:
        word_pool = []
        for entry in puzzle_entries:
            if str(entry['word'])[1:-1].find(letter) != -1:
                word_pool.append(entry)
        if word_pool != []:
            chosen_word = random.choice(word_pool)
            return chosen_word
        else:
            raise ValueError("No words found containing the letter '{}'".format(letter))
    except Exception as e:
        return str(e)

def select_words(solution_phrase):
    solution_phrase = str(solution_phrase).replace(" ", "")
    selected_words = []
    used_words = set()

    for letter in solution_phrase:
        try:
            attempts = 0
            while attempts < 100:
                result = select_word(letter)
                if isinstance(result, dict) and result['word'] not in used_words:
                    used_words.add(result['word'])
                    letter_indexes = [i + 1 for i, ch in enumerate(result['word'][1:-1]) if ch == letter]
                    if len(letter_indexes) > 1:
                        letter_indexes = random.choice(letter_indexes)
                    elif letter_indexes == []:
                        pass
                    else:
                        selected_words.append({
                            'word': result['word'],
                            'clue': result['clue'],
                            'letter': letter,
                            'indexes': letter_indexes
                        })
                    break
                attempts += 1
            else:
                selected_words.append({
                    'error': f"No unused word found for letter '{letter}' after 100 attempts",
                    'letter': letter
                })
        except Exception as e:
            selected_words.append({
                'letter': letter,
                'error': str(e)
            })
    return selected_words

        
x = select_words(random.choice(solution_phrases))
for item in x:
    print(item)