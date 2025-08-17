from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_solution_sheet(matrix, solution_phrase, selected_words, solution_phrase_index=None, filename="solution_sheet_a4.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    margin = 50
    cell_size = 25
    start_x = margin
    start_y = height - margin

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Draw the grid with letters and row numbers
    for row_idx, row in enumerate(matrix):
        y = start_y - row_idx * cell_size
        # Draw row number
        c.drawString(start_x - 30, y - cell_size / 2 - 4, str(row_idx + 1))
        for col_idx, letter in enumerate(row):
            if letter != '.':
                x = start_x + col_idx * cell_size
                c.rect(x, y - cell_size, cell_size, cell_size)  # only draw box if not dot
                c.drawCentredString(x + cell_size / 2, y - cell_size / 2 - 4, letter.upper())

    # Draw vertical solution word if index provided
    if solution_phrase_index is not None:
        for i, letter in enumerate(solution_phrase):
            row_idx = i
            col_idx = solution_phrase_index
            if matrix[row_idx][col_idx] != '.':  # highlight only if there’s a letter
                y = start_y - row_idx * cell_size
                x = start_x + col_idx * cell_size
                c.setFillColorRGB(1, 0, 0)
                c.drawCentredString(x + cell_size / 2, y - cell_size / 2 - 4, letter.upper())
                c.setFillColorRGB(0, 0, 0)

    # Draw clues next to the grid
    clue_x = start_x + num_cols * cell_size + 50
    clue_y = start_y
    for idx, info in enumerate(selected_words):
        c.drawString(clue_x, clue_y - idx * 40, f"{idx + 1}. {info['clue']}")

    c.save()
    print(f"PDF saved as {filename}")
