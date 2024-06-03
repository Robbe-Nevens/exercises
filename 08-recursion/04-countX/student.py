def countX(text):
    if not text:
        return 0

    if text[0] == 'x':
        first = 1 
    else: 
        first= 0

    return first + countX(text[1:])

