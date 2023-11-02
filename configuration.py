
#Pygame window
screen_width = 1200
screen_height = 1200
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Habit Tracker")

BLACK = (0, 0, 0)
FPS = 60
tile_size = 55


blocks_layer = 2
ground_layer = 1
player_layer = 1
journal_layer = 3
player_steps = 4
bulletin_layer = 3
bookshelf_layer = 3


room_map = [
'BBBBBBBBBB',
'B.....S..B',
'B........B',
'B..U.....B',
'B........B',
'B.....J..B',
'B........B',
'B........B',
'B.......PB',
'BBBBBBBBBB', 
]

