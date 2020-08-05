def isValidChessBoard(board):
    #variable initialization
    returnValue = {'check': True, 'messages': []}
    countPiece = {}
    countColor = {'white': 0, 'black': 0}

    #main loop
    for place, piece in board.items():
        countPiece.setdefault(piece, 0)
        countPiece[piece] += 1

        if piece[0] == 'w':
            countColor['white'] += 1
        else:
            countColor['black'] += 1

        if int(place[0]) not in range(1,8) or place[1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            returnValue['check'] = False
            returnValue['messages'].append('Place ' + place + ' is not a valid place. Must be between 1a and 8h.')

    #checks        
    if countPiece.get('bking',0) > 1:
        returnValue['check'] = False
        returnValue['messages'].append('More than one black king is not allowed.')
    if countPiece.get('wking', 0) > 1:
        returnValue['check'] = False
        returnValue['messages'].append('More than one white king is not allowed.')

    if countPiece.get('bpawn', 0) > 8:
        returnValue['check'] = False
        returnValue['messages'].append('More than 8 black pawns are not allowed.')
    if countPiece.get('wpawn',0) > 8:
        returnValue['check'] = False
        returnValue['messages'].append('More than 8 white pawns are not allowed.')
    
    if countColor['white'] > 16:
        returnValue['check'] = False
        returnValue['messages'].append('More than 16 white pieces are not allowed.')
    if countColor['black'] > 16:
        returnValue['check'] = False
        returnValue['messages'].append('More than 16 black pieces are not allowed.')
    
    return returnValue

exampleBoard = {'1h': 'bking', '6c': 'bking', '7i': 'bpawn', 
                  '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(exampleBoard))