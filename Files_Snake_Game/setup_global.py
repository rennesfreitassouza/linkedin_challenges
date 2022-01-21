# Define program constants
import turtle

WIDTH = 800
HEIGHT = 600
DELAY = 300  # Milliseconds
FOOD_SIZE = 20
VALID_WIDTH_TUPLE = (-WIDTH/2 + FOOD_SIZE, WIDTH/2 - FOOD_SIZE)
VALID_HEIGHT_TUPLE = (-HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)

# Start game values
iniPosition = None
iniSnake = [[0, 0], [20, 0], [40, 0], [60, 0]]
iniSnake_dir = "right"
iniScore = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


snake = iniSnake
snake_direction = iniSnake_dir
score = iniScore
food_pos = iniPosition

# Create a turtle to do your bidding
screen = turtle.Screen()
stamper = turtle.Turtle()
food = turtle.Turtle()
