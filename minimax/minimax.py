import copy

RED = (255,0,0)
WHITE = (255,255,255)

def minimax(position, depth, playerTurn, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    playerColor = WHITE if playerTurn else RED
    value = float('-inf') if playerTurn else float('inf')
    moves = getAllMoves(position, playerColor, game)
    if len(getAllMoves(position, playerColor, game)) == 0:
        return position.evaluate(), -1
    next_position = moves[0]

    for move in moves:
        updated_value = minimax(move, depth - 1, not playerTurn, game)[0]
        maximumValue = max(updated_value, value)
        minimumValue = min(updated_value, value)
        value = maximumValue if playerTurn else minimumValue
        if value == updated_value:
            next_position = move
    return value, next_position


def simulateMove(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def getAllMoves(board, color, game):
    moves = []
    for piece in board.getAllPieces(color):
        validMoves = board.getValidMoves(piece)
        for move, skip in validMoves.items():
            tempBoard = copy.deepcopy(board)
            tempPiece = tempBoard.getPiece(piece.row, piece.col)
            newBoard = simulateMove(tempPiece, move, tempBoard, game, skip)
            moves.append(newBoard)
    return moves
