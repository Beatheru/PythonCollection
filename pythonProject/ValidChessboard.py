def isValidChessboard(board):
    if "bKing" not in list(board.values()) or "wKing" not in list(board.values()):
        return False

    if len(board) > 32:
        return False

    bKingCount = 0
    wKingCount = 0
    wPawnCount = 0
    bPawnCount = 0
    whiteCount = 0
    blackCount = 0

    for piece in board.values():
        if piece[0] != "w" and piece[0] != "b":
            return False
        if piece[1:] != "Pawn" and piece[1:] != "Knight" and piece[1:] != "Bishop" and piece[1:] != "Rook" and piece[1:] != "King" and piece[1:] != "Queen":
            return False

        if piece[0] == "b":
            blackCount += 1
        if piece[0] == "w":
            whiteCount += 1
        if piece == "wPawn":
            wPawnCount += 1
        if piece == "bPawn":
            bPawnCount += 1
        if piece == "bKing":
            bKingCount += 1
        if piece == "wKing":
            wKingCount += 1

    if bKingCount != 1 or wKingCount != 1 or wPawnCount > 8 or bPawnCount > 8 or whiteCount > 16 or blackCount > 16:
        return False

    for position in board.keys():
        if int(position[0]) < 1 or int(position[0]) > 8:
            return False
        if position[1] != "a" and position[1] != "b" and position[1] != "c" and position[1] != "d" and position[1] != "e" and position[1] != "f" and position[1] != "g" and position[1] != "h":
            return False

    return True


print(isValidChessboard({"1h": "bKing", "6c": "wQueen", "2g": "bBishop", "5h": "bQueen", "3e": "wKing"}))  # True
print(isValidChessboard({"1a": "bPawn", "2a": "wKing"}))  # False: no bKing
print(isValidChessboard({"1a": "wKing", "2a": "wKing", "3c": "bBishop"}))  # False: cannot have 2 white kings, no bKing
print(isValidChessboard({"1a": "bKing", "9z": "wKing"}))  # False: 9z is an invalid position

#print(isValidChessboard(chessboard))



