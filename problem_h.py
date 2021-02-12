
from math import inf
x, y = list(map(int, input().split(' ')))
code = list(map(int, list(input())))

grid = []
for _ in range(y):
    rows = list(map(int, list(input())))
    grid.append(rows)

grid.reverse()


def is_valid(a, b, X, Y):
    return 0 <= a < X and 0 <= b < Y


def neighbors(sx, sy, brd, seq, seq_idx):
    cds = set()
    cx, cy = sx, sy + 1
    if is_valid(cx, cy, len(brd), len(brd[0])):
        cds |= {(cx, cy, False)}
    cx, cy = sx + 1, sy
    if is_valid(cx, cy, len(brd), len(brd[0])):
        cds |= {(cx, cy, False)}
    if seq_idx < len(seq):
        fx = sx + seq[seq_idx] + 1
        fy = sy
        if is_valid(fx, fy, len(brd), len(brd[0])):
            cds |= {(fx, fy, True)}
        fx = sx
        fy = sy + seq[seq_idx] + 1
        if is_valid(fx, fy, len(brd), len(brd[0])):
            cds |= {(fx, fy, True)}

    return cds


def search(ix, iy, X, Y, board, seq, sqIdx, dp):
    if ix == X - 1 and iy == Y - 1:
        dp[ix, iy, sqIdx] = board[ix][iy]

        return board[ix][iy]
    if (ix, iy, sqIdx) in dp:
        return dp[ix, iy, sqIdx]

    nbs = neighbors(ix, iy, board, seq, sqIdx)
    for cx, cy, hop in nbs:
        search(cx, cy, X, Y, board, seq, sqIdx + 1 if hop else sqIdx, dp)

    temp = inf
    for cx, cy, hop in neighbors(ix, iy, board, seq, sqIdx):
        if hop:
            temp = min(
                temp,
                dp[cx, cy, sqIdx + 1] + board[ix][iy]
            )
        else:
            temp = min(
                temp,
                dp[cx, cy, sqIdx] + board[ix][iy]
            )
    dp[ix, iy, sqIdx] = temp

    return


if __name__ == '__main__':
    res = dict()
    search(0, 0, y, x, grid, code, 0, res)
    val = inf
    for kx, ky, kz in res:
        if kx == 0 and ky == 0:
            val = min(val, res[kx, ky, kz])
    print(val)
