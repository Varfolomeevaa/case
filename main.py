"""
Group:
Varfolomeeva Viktoria 95
Sineokaya Anastasia 91
"""
import turtle
import RU_LOCAL as RU


def get_color_choice():
    """
    function for selecting hexagon fill color
    :return: hexagon fill color
    """
    print(RU.INTRODUCTION_1)
    print(RU.COLOR_1, RU.COLOR_2, RU.COLOR_3, RU.COLOR_4, RU.COLOR_5, RU.COLOR_6, sep='\n')
    colors = {RU.COLOR_1: 'firebrick', RU.COLOR_2: 'gold', RU.COLOR_3: 'dodger blue', RU.COLOR_4: 'lime green',
              RU.COLOR_5: 'dim gray', RU.COLOR_6: 'hot pink'}
    flag = False
    while not flag:
        color = input(RU.QUESTION_COLOR_1).lower()
        if color in colors.keys():
            return colors[color]
        if not flag:
            print(color, RU.QUESTION_COLOR_2)


def get_num_hexagons():
    """
    function for selecting number of hexagons in the line
    :return: number of hexagons in the line
    """
    flag = 0
    num_hexagons = input(RU.HEXAGONS_1)
    while flag == 0:
        try:
            num_hexagons = int(num_hexagons)
            if 4 <= num_hexagons <= 20:
                flag = 1
                return num_hexagons
            else:
                print(RU.HEXAGONS_2)
                num_hexagons = int(input(RU.HEXAGONS_3))
        except ValueError:
            print(RU.HEXAGONS_2)
            num_hexagons = input(RU.HEXAGONS_3)


def draw_hexagon(x, y, side_len, color):
    """
    function to draw a hexagon
    :param x: abscissa of the point from which the figure is drawn
    :param y: ordinate of the point from which the figure is drawn
    :param side_len: side length
    :param color: shape fill color
    :return: None
    """
    turtle.pu()
    turtle.goto(x, y)
    turtle.speed(40)
    turtle.color('black', color)
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.pd()
    turtle.lt(30)
    for i in range(6):
        turtle.fd(side_len)
        turtle.rt(60)
    turtle.rt(30)
    turtle.end_fill()
    turtle.pu()


def main():
    color_1 = get_color_choice()
    color_2 = get_color_choice()
    num_hex = get_num_hexagons()
    diameter = 500 / num_hex
    len_hex = (diameter / 2) / (3 ** 0.5 / 2)
    shift = len_hex + 0.5 * len_hex
    parity = 0
    if num_hex % 2 != 0:
        parity = 1

    for j in range(0, num_hex, 2):
        for i in range(num_hex):
            if i % 2 == 0:
                if parity == 1 and j == num_hex - 1:
                    draw_hexagon(-300 + i * diameter, 300 - shift * j, len_hex, color_1)
                    color_1, color_2 = color_2, color_1
                else:
                    draw_hexagon(-300 + i * diameter, 300 - shift * j, len_hex, color_1)
                    draw_hexagon(-300 - diameter / 2 + i * diameter, 300 - shift * (j + 1), len_hex, color_1)
            else:
                if parity == 1 and j == num_hex - 1:
                    draw_hexagon(-300 + i * diameter, 300 - shift * j, len_hex, color_1)
                    color_1, color_2 = color_2, color_1
                else:
                    draw_hexagon(-300 + i * diameter, 300 - shift * j, len_hex, color_2)
                    draw_hexagon(-300 - diameter / 2 + i * diameter, 300 - shift * (j + 1), len_hex, color_2)
        color_1, color_2 = color_2, color_1


main()
turtle.done()
