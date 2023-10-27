import turtle


def get_color_choice():
    """
    function for selecting hexagon fill color
    :return: hexagon fill color
    """
    print('Доступные цвета заливки:')
    print('красный', 'желтый', 'синий', 'зелёный', 'черный', 'розовый', sep='\n')
    colors = ['красный', 'желтый', 'синий', 'зелёный', 'черный', 'розовый']
    flag = False
    while not flag:
        color = input('Пожалуйста, введите цвет: ').lower()
        if color in colors:
            return color
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

print(get_num_hexagons())
