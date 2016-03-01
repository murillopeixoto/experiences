def validate(board):
    for y in xrange(9):
        y_list, x_list = [], []
        for x in xrange(9):
            if board[y][x] in y_list or board[x][y] in x_list:
                return False

            y_list.append(board[y][x])
            x_list.append(board[x][y])

    for y in xrange(0, 9, 3):
        for x in xrange(0, 9, 3):
            y_pos = y
            x_pos = x
            block_list = []
            for pos in xrange(9):
                if pos and pos % 3 == 0:
                    y_pos = y_pos + 1
                    x_pos = x

                if board[y_pos][x_pos] in block_list:
                    return False

                block_list.append(board[y_pos][x_pos])
                x_pos = x_pos + 1

    return True
