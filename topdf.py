from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_solution_sheet(matrix, solution_phrase, selected_words, solution_phrase_index=None, filename="solution_sheet.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    margin = 50
    cell_size = 25
    start_x = margin

    # Draw clues above the puzzle
    clue_x = start_x
    clue_y = height - margin
    for idx, info in enumerate(selected_words):
        c.drawString(clue_x, clue_y - idx * 20, f"{idx + 1}. {info['clue']}")

    # Extra spacing below clues
    num_clues = len(selected_words)
    spacing_below_clues = 50
    start_y = height - margin - num_clues * 20 - spacing_below_clues  # puzzle starts below clues + extra spacing

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Draw the grid with letters and row numbers
    for row_idx, row in enumerate(matrix):
        y = start_y - row_idx * cell_size

        # Find first non-dot column to place row number
        first_col = next((i for i, l in enumerate(row) if l != '.'), None)
        if first_col is not None:
            # Draw black rectangle for row number
            x_num = start_x + first_col * cell_size - cell_size
            c.setFillColorRGB(0, 0, 0)
            c.rect(x_num, y - cell_size, cell_size, cell_size, fill=True)
            # Draw white number inside
            c.setFillColorRGB(1, 1, 1)
            c.drawCentredString(x_num + cell_size / 2, y - cell_size / 2 - 4, str(row_idx + 1))
            c.setFillColorRGB(0, 0, 0)  # reset color

        for col_idx, letter in enumerate(row):
            if letter != '.':
                x = start_x + col_idx * cell_size
                # Highlight the solution column with light gray background
                if solution_phrase_index is not None and col_idx == solution_phrase_index:
                    c.setFillColor(colors.lightgrey)
                    c.rect(x, y - cell_size, cell_size, cell_size, fill=True)
                    c.setFillColorRGB(0, 0, 0)  # reset color for letters
                else:
                    c.rect(x, y - cell_size, cell_size, cell_size)
                c.drawCentredString(x + cell_size / 2, y - cell_size / 2 - 4, letter.upper())

    c.save()
    print(f"PDF saved as {filename}")

