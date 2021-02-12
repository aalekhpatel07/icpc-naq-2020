def board():
    brd = []
    for _ in range(8):
        brd.append(list(input()))
    return brd


def neighbors(x, y, dx, dy, b):
    cx = x + dx
    cy = y + dy
    while 0 <= cx < 8 and 0 <= cy < 8:
        if b[cx][cy] == '*':
            return False
        else:
            cx += dx
            cy += dy
    return True


def search(x, y, brd):
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == b == 0:
                continue
            if not neighbors(x, y, a, b, brd):
                return False
    return True


def queens(brd):
    coords = set()
    for i in range(8):
        for j in range(8):
            if brd[i][j] == '*':
                coords |= {(i, j)}
    if len(coords) != 8:
        return False
    for sx, sy in coords:
        if not search(sx, sy, brd):
            return False
    return True


if __name__ == '__main__':
    _b = board()
    if queens(_b):
        print('valid')
    else:
        print('invalid')
