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


