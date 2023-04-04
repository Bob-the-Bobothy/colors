import random

# making random colors
def random_color():
    values = []

    for i in range(0, 3):
        color = random.randint(1, 255)
        values.append(color)

    return values

print(random_color())