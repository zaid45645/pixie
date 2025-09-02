from components import *
import webbrowser

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixie!~")

def create_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * pixel_sizes, i * pixel_sizes, pixel_sizes, pixel_sizes))
    
    if draw_lines:
        for i in range(rows + 1):
            pygame.draw.line(window, black_colour, (0, i * pixel_sizes), (width, i * pixel_sizes))
        for j in range(colums + 1):
            pygame.draw.line(window, black_colour, (j * pixel_sizes, 0), (j * pixel_sizes, height - toolbar_h))

def draw(window, grid, buttons):
    window.fill(bg_colour)
    draw_grid(window, grid)
    for button in buttons:
        button.draw(window)
    pygame.display.update()
    

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // pixel_sizes
    col = x // pixel_sizes

    if row >= rows:
        raise IndexError

    return row, col

run = True
clock_fps = pygame.time.Clock()
grid = create_grid(rows, colums, bg_colour)
drawing_color = black_colour
undo_stack = []
redo_stack = []
max_undo_steps = 10
button_y = height - toolbar_h/2 - 25
buttons = [
    Button(10, button_y, 50, 50, black_colour),
    Button(70, button_y, 50, 50, red_color),
    Button(130, button_y, 50, 50, green_colour),
    Button(190, button_y, 50, 50, blue_colour),
    Button(250, button_y, 50, 50, yellow_colour),
    Button(310, button_y, 50, 50, pink_colour),
    Button(370, button_y, 50, 50, brown_colour),
    Button(430, button_y, 50, 50, white_colour, "Erase", black_colour),
    Button(490, button_y, 50, 50, white_colour, "Reset", black_colour),
    Button(550, button_y, 50, 50, white_colour, ":D", black_colour)
]

while run:
    clock_fps.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color
                    if button.text == "Reset":
                        grid = create_grid(rows, colums, bg_colour)
                        drawing_color = black_colour
                    if button.text == ":D":
                        webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
                        
    draw(window, grid, buttons)

pygame.quit()
