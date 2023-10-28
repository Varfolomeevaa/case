import turtle


def get_color_choice():
    """
    function for selecting hexagon fill color
    :return: hexagon fill color
    """
    print('Доступные цвета заливки:')
    print('красный', 'желтый', 'синий', 'зелёный', 'серый', 'розовый', sep='\n')
    colors = {'красный': 'firebrick', 'желтый': 'gold', 'синий': 'dodger blue', 'зелёный': 'lime green',
              'серый': 'dim gray', 'розовый': 'hot pink'}
    flag = False
    while not flag:
        color = input('Пожалуйста, введите цвет: ').lower()
        if color in colors.keys():
            return colors[color]
        if not flag:
            print(color, 'не является верным значением.')


def get_num_hexagons():
    """
    function for selecting number of hexagons in the line
    :return: number of hexagons in the line
    """
    flag = 0
    num_hexagons = input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ')
    while flag == 0:
        try:
            num_hexagons = int(num_hexagons)
            if 4 <= num_hexagons <= 20:
                flag = 1
                return num_hexagons
            else:
                print('Оно должно быть от 4 до 20.')
                num_hexagons = int(input('Пожалуйста, повторите попытку: '))
        except ValueError:
            print('Оно должно быть от 4 до 20.')
            num_hexagons = input('Пожалуйста, повторите попытку: ')


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
    for j in range(0, num_hex, 2):
        for i in range(num_hex):
            if i % 2 == 0:
                draw_hexagon(-300 + i * diameter, 300 - shift * j, len_hex, color_1)
                draw_hexagon(-300 - diameter/2 + i * diameter, 300 - shift * (j + 1), len_hex, color_1)
            else:
                draw_hexagon(-300 + i * diameter, 300 - shift * j, len_hex, color_2)
                draw_hexagon(-300 - diameter / 2 + i * diameter, 300 - shift * (j + 1), len_hex, color_2)
        color_1, color_2 = color_2, color_1


main()
turtle.done()
