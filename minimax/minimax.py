import copy

RED = (255,0,0)
WHITE = (255,255,255)

def minimax(position, depth, playerTurn):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    playerColor = WHITE if playerTurn else RED
    value = float('-inf') if playerTurn else float('inf')
    moves = getAllMoves(position, playerColor)
    if len(getAllMoves(position, playerColor)) == 0:
        return position.evaluate(), -1
    next_position = None

    for move in moves:
        newBoards = getNewBoard(moves[move], position, move)
        for newBoard in newBoards:
            updated_value = minimax(newBoard, depth - 1, not playerTurn)[0]
            maximumValue = max(updated_value, value)
            minimumValue = min(updated_value, value)
            value = maximumValue if playerTurn else minimumValue
            if value == updated_value or next_position == None:
                next_position = newBoard
    return value, next_position


def simulateMove(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def getNewBoard(validMove, board, piece):
    newBoards = list()
    for move, skip in validMove.items():
        tempBoard = copy.deepcopy(board)
        tempPiece = tempBoard.getPiece(piece.row, piece.col)
        newBoard = simulateMove(tempPiece, move, tempBoard, skip)
        newBoards.append(newBoard)
    return newBoards


def getAllMoves(board, color):
    validMoves = dict()
    for piece in board.getAllPieces(color):
        validMoves[piece] = board.getValidMoves(piece)
    return validMoves

