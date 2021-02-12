from collections import Counter

ii = 0
scc_count = 0


def solve(g):
    unvisited = -1
    n = len(g)

    ids = [0] * n
    low = [0] * n
    on_stack = [False] * n
    stack = []

    def find_sccs():
        for i in range(n):
            ids[i] = unvisited
        for i in range(n):
            if ids[i] == unvisited:
                dfs(i)
        return low

    def dfs(at):
        global ii
        global scc_count
        stack.append(at)
        on_stack[at] = True
        ids[at] = low[at] = ii
        ii += 1

        for to in g[at]:
            if ids[to] == unvisited:
                dfs(to)
            if on_stack[to]:
                low[at] = min(low[at], low[to])

        if ids[at] == low[at]:
            while len(stack):
                node = stack.pop()
                on_stack[node] = False
                low[node] = ids[at]
                if node == at:
                    break
            scc_count += 1

    ans = find_sccs()
    freq = dict(Counter(ans))
    print(n - max(freq.values()))


def main():
    n = int(input())
    g = dict()
    lang = dict()
    for i in range(n):
        inp = input().split(' ')
        lang[i] = {
            's': inp[1],
            'l': set(inp[1:])
        }

    for i in range(n):
        for j in range(n):
            if lang[i]['s'] in lang[j]['l']:
                if i in g:
                    g[i].append(j)
                else:
                    g[i] = [j]
    solve(g)


if __name__ == '__main__':
    main()
