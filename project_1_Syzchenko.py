import random


def main(cells):
    desk = f"""
            +-------+-------+-------+
            |       |       |       |
            |   {cells[0]}   |   {cells[1]}   |   {cells[2]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {cells[3]}   |   {cells[4]}   |   {cells[5]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {cells[6]}   |   {cells[7]}   |   {cells[8]}   |
            |       |       |       |
            +-------+-------+-------+         
            """
    print(desk)


def check(cells):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for pattern in win_patterns:
        if all(cells[i] == 'X' for i in pattern):
            main(cells)
            print('BOT WIN!')
            return True

        if all(cells[i] == 'O' for i in pattern):
            main(cells)
            print('YOU WIN!')
            return True

    return False


def game(cells = [1, 2, 3, 4, 'X', 6, 7, 8, 9],
         av_index = [0, 1, 2, 3, 5, 6, 7, 8]):
    main(cells)

    if not av_index:
        print('Draw!')
        return

    try:
        user_move = int(input('Enter your move: '))

        if (user_move - 1) not in av_index:
            raise TypeError

        else:
            cells[user_move - 1] = 'O'
            av_index.remove(user_move - 1)
            if check(cells):
                return

            bot_turn = random.choice(av_index)
            cells[bot_turn] = 'X'
            av_index.remove(bot_turn)
            if check(cells):
                return

            game(cells, av_index)

    except:
        print('ONLY 1-9 NUMBERS!')
        game(cells, av_index)


game()