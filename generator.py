import json
import random
from collections import defaultdict

with open('words.json', 'r') as file:
    words = json.load(file)
    
puzzle_entries = words["puzzle_entries"]
solution_phrases = words["solution_phrases"]

def select_word(letter: str):
    try:
        word_pool = []
        for entry in puzzle_entries:
            word_content = str(entry['word'])[1:-1]  # Remove quotes
            if letter in word_content:
                word_pool.append(entry)
        if word_pool:
            return random.choice(word_pool)
        raise ValueError(f"No words found containing the letter '{letter}'")
    except Exception as e:
        return {'error': str(e)}

def select_words(solution_phrase):
    solution_phrase = str(solution_phrase).replace(" ", "")
    selected_words = []
    used_words = set()

    for letter in solution_phrase:
        try:
            attempts = 0
            found = False

            while attempts < 100:
                result = select_word(letter)
                if isinstance(result, dict) and result['word'] not in used_words:
                    used_words.add(result['word'])
                    letter_indexes = [i + 1 for i, ch in enumerate(result['word'][1:-1]) if ch == letter]
                    if letter_indexes:  # non-empty list
                        if len(letter_indexes) > 1:
                            letter_indexes = [random.choice(letter_indexes)]
                        # append regardless of single or multiple matches
                        selected_words.append({
                            'word': result['word'],
                            'clue': result['clue'],
                            'letter': letter,
                            'indexes': letter_indexes
                        })
                    # If letter_indexes is empty, skip this word
                    found = True
                    break
                attempts += 1

            if not found:
                raise ValueError(f"No suitable words found for letter '{letter}' after 100 attempts")

        except ValueError:
            raise
        
        except Exception as e:
            selected_words.append({
                'letter': letter,
                'error': str(e)
            })
    return selected_words

def build_grid(main_word, words):
    grid = defaultdict(dict)

    # Place the main word vertically in column 0
    for row, ch in enumerate(main_word):
        grid[row][0] = ch

    # Place other words horizontally
    for row, entry in enumerate(words):
        word = entry['word']
        idx = entry['indexes'][0]
        start_col = -idx
        for j, ch in enumerate(word):
            grid[row][start_col + j] = ch

    # Determine grid boundaries
    min_col = min(c for r in grid.values() for c in r.keys())
    max_col = max(c for r in grid.values() for c in r.keys())
    rows = max(grid.keys()) + 1

    # Build the matrix
    matrix = []
    for r in range(rows):
        row_data = []
        for c in range(min_col, max_col + 1):
            row_data.append(grid[r].get(c, "."))
        matrix.append(row_data)

    # Compute the main word column index in the matrix
    main_word_col_index = -min_col  # because main word is at column 0 in grid

    return matrix, main_word_col_index
