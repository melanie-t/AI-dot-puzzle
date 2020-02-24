

def calculate_heuristics(board, index, size_n):
    # return number_of_black_tokens(board)
    # return adjacency(board, index)
    return isolated(board, index, size_n)


def number_of_black_tokens(board):
    num_black = board.count("1")
    return int(num_black)


# TODO PATRICK
def adjacency(board, index):
    print()


# TODO GUENOLE
def isolated(board, index, size_n):
    print(board[index]+" index :"+str(index))
    print(board)
    max_index = size_n - 1
    token_above = index - size_n
    token_below = index + size_n
    token_left = index - 1
    token_right = index + 1

    value_corner = 100
    value_edge = 90
    value_center = 80
    other = 10

    if board[index] == '1':
        # Top left corner
        if index == 0 and board[token_right] == '0' and board[token_below] == '0':
            print('Top left corner isolated')
            end_value = int(value_corner)

        # Top right corner
        elif index == max_index and board[token_left] == '0' and board[token_below] == '0':
            print('Top right corner isolated')
            end_value = int(value_corner)

        # Bottom left corner
        elif index == size_n * max_index and board[token_right] == '0' and board[token_above] == '0':
            print('Bottom left corner isolated')
            end_value = int(value_center)

        # Bottom right Corner
        elif index == size_n * size_n - 1 and board[token_left] == '0' and board[token_above] == '0':
            print('Bottom right corner isolated')
            end_value = int(value_center)

        # Left edge
        elif index % size_n == 0 and board[token_right] == '0' and board[token_above] == '0' and board[token_below] == '0':
            print('Left edge isolated')
            end_value = int(value_edge)

        # Right edge
        elif (index + 1) % size_n == 0 and board[token_left] == '0' and board[token_above] == '0' and board[token_below] == '0':
            print('Index : '+str(index)+' right isolated')
            end_value = int(value_edge)

        # Top edge
        elif index < max_index and board[token_left] == '0' and board[token_below] == '0' and board[token_left] == '0':
            print('Index : '+ str(index) +' isolated top')
            end_value = int(value_edge)

        # Bottom edge
        elif int(index / size_n) == max_index and board[token_left] == '0' and board[token_above] == '0' and board[token_right] == '0':
            print('Index : ' + str(index) + ' isolated bottom')
            end_value = int(value_edge)

        # All inner tokens
        elif board[token_above] == '0' and board[token_left] == '0' and board[token_below] == '0' and board[token_right] == '0':
            print('Index :'+str(index)+' isolated center')
            end_value = int(value_center)

        else:
            print('no isolated')
            end_value = int(other)

    else:
        print('zéro 0')
        end_value = int(other)

    print("Returns : "+str(end_value))
    return end_value
