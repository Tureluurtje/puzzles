from generator import select_words, build_grid

solution_phrase = "handige"

selected_words = select_words(solution_phrase)

matrix, solution_phrase_index = build_grid(solution_phrase, selected_words)

for row in matrix:
    row_str = []
    for col in range(len(row)):
        char = row[col]
        if col == solution_phrase_index:
            # Make character red
            char = f"\033[91m{char}\033[0m"
        row_str.append(char)
    print(" ".join(row_str))
