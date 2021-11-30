def digit_display(number: str, min_width: int = 0) -> str:
    number = str(number).zfill(min_width)

    rows = ['', '', '', '', '', '']
    for i, n in enumerate(number):
        match n:
            case '.':
                rows[0] += '   '
                rows[1] += '   '
                rows[2] += '   '
                rows[3] += '   '
                rows[4] += ' . '
                rows[5] += '   '
            case ',':
                rows[0] += '   '
                rows[1] += '   '
                rows[2] += '   '
                rows[3] += '   '
                rows[4] += ' , '
                rows[5] += '   '
            case ':':
                rows[0] += '   '
                rows[1] += '   '
                rows[2] += ' . '
                rows[3] += ' . '
                rows[4] += '   '
                rows[5] += '   '
            case '-':
                rows[0] += '     '
                rows[1] += '     '
                rows[2] += ' ___ '
                rows[3] += '     '
                rows[4] += '     '
                rows[5] += '     '
            case '0':
                rows[0] += ' ___ '
                rows[1] += '|  /|'
                rows[2] += '| / |'
                rows[3] += '|/  |'
                rows[4] += '|___|'
                rows[5] += '     '
            case '1':
                rows[0] += '  ,  '
                rows[1] += ' /|  '
                rows[2] += '  |  '
                rows[3] += '  |  '
                rows[4] += '__|__'
                rows[5] += '     '
            case '2':
                rows[0] += ' ___ '
                rows[1] += '    |'
                rows[2] += ' ___|'
                rows[3] += '|    '
                rows[4] += '|___ '
                rows[5] += '     '
            case '3':
                rows[0] += ' ___ '
                rows[1] += '    |'
                rows[2] += ' ___|'
                rows[3] += '    |'
                rows[4] += ' ___|'
                rows[5] += '     '
            case '4':
                rows[0] += '   , '
                rows[1] += '  /| '
                rows[2] += ' / | '
                rows[3] += '/__|_'
                rows[4] += '   | '
                rows[5] += '     '
            case '5':
                rows[0] += ' ___ '
                rows[1] += '|    '
                rows[2] += '|___ '
                rows[3] += '    |'
                rows[4] += ' ___|'
                rows[5] += '     '
            case '6':
                rows[0] += ' ___ '
                rows[1] += '|    '
                rows[2] += '|___ '
                rows[3] += '|   |'
                rows[4] += '|___|'
                rows[5] += '     '
            case '7':
                rows[0] += '_____'
                rows[1] += '    /'
                rows[2] += '   / '
                rows[3] += '  /  '
                rows[4] += ' /   '
                rows[5] += '     '
            case '8':
                rows[0] += ' ___ '
                rows[1] += '|   |'
                rows[2] += '|___|'
                rows[3] += '|   |'
                rows[4] += '|___|'
                rows[5] += '     '
            case '9':
                rows[0] += ' ___ '
                rows[1] += '|   |'
                rows[2] += '|___|'
                rows[3] += '    |'
                rows[4] += ' ___|'
                rows[5] += '     '

        # Add a space (for the space in between numerals) if this
        # isn't the last numeral:
        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
            rows[3] += ' '
            rows[4] += ' '

    return '\n'.join(rows)
