def solve(n, arr):
    arr = [elem for elem in arr if elem.startswith('Simon says')]
    for elem in arr:
        print(elem[10:])


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    solve(n, arr)


if __name__ == '__main__':
    main()
