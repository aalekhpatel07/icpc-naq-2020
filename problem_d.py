def solve(w, p, arr):
    ans = set()
    for i in range(1, len(arr)):
        for j in range(i):
            ans.add(arr[i] - arr[j])
    ans = list(ans)
    ans.sort()
    print(' '.join(list(map(str, ans))))


def main():
    w, p = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    arr = [0, *arr, w]
    solve(w, p, arr)


if __name__ == '__main__':
    main()