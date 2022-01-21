import random
from setup_global import *


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        # No self-collision simply by pressing wrong key.
        if snake_direction != "down":
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"


def game_loop():
    stamper.clearstamps()  # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] \
       > WIDTH / 2 or new_head[1] < - HEIGHT / 2 or new_head[1] \
       > HEIGHT / 2:
        main()
    else:
        # Add new head to snake body.
        snake.append(new_head)

        # Check food collision
        eat = food_collision()
        if eat is False:
            snake.pop(0)  # Keep the snake the same length unless fed.

        # Draw a snake
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh screen
        screen.title(f"Score: {score}")
        screen.onscreenclick(set_food, 1)
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score

    if get_distance(snake[-1], food_pos) < 20:
        score += 10
        food_pos = get_random_food_pos()
        setFoodOnSclick(*food_pos)
        # food.goto(food_pos)
        return True
    return False


def setFoodOnSclick(*args):
    global food_pos
    print("setFoodOnSclick() args", args)
    food_pos = args[0], args[1]
    food.goto(food_pos)


def set_food(*args):
    setFoodOnSclick(*args)


def get_random_food_pos():
    x = random.randint(VALID_WIDTH_TUPLE[0], VALID_WIDTH_TUPLE[1])
    y = random.randint(VALID_HEIGHT_TUPLE[0], VALID_HEIGHT_TUPLE[1])
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    # Pythagoras' Theorem
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


def reset():
    global snake, food_pos, snake_direction, score

    snake = list(iniSnake)
    snake_direction = iniSnake_dir
    score = iniScore
    food_pos = get_random_food_pos()

    # food.goto(food_pos)
    setFoodOnSclick(*food_pos)
    game_loop()


def main():

    # Set the dimensions of the Turtle Graphics window.
    screen.setup(WIDTH, HEIGHT)
    screen.title(f"Score: {score}")
    screen.bgcolor("black")
    screen.tracer(0)  # Turn off automatic animation.

    # Event handlers
    screen.listen()
    bind_direction_keys()

    stamper.shape("square")
    stamper.color("green")
    stamper.penup()

    # Food
    food.shape("square")
    food.color("brown")
    food.shapesize(FOOD_SIZE / 20)
    food.penup()

    # Set animation in motion
    reset()

    # Finish nicely
    turtle.done()


if __name__ == '__main__':
    main()
