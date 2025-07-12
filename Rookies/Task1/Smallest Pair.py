T = int(input())
for _ in range(T):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    best_prev = arr[0] - 1
    answer = 10**18
    for j in range(1, n):
        pair_sum = arr[j] + j + best_prev
        if pair_sum < answer:
            answer = pair_sum
        cand = arr[j] - j
        if cand < best_prev:
            best_prev = cand
    print(answer)
