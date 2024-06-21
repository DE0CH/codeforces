
ms = {}
aa = []

def ans(left, right, cat):
    if (left, right, cat) in ms:
        return ms[(left, right, cat)]
    # up means has another element higher next to it and down means does not have an element higher
    # 0: left up, right up, 1: left up, right down, 2: left down, right up, 3: left down, right down
    if left + 1 == right:
        ms[(left, right, cat)] = 1 if cat == 0 else 2
        return ms[(left, right, cat)]
    mid = (left + right) // 2

    ms[(left, right, cat)] = ans(
        left,
        mid,
        cat // 2 * 2 + (0 if mid + 1 == len(aa) or aa[mid] < aa[mid+1] else 1)
    ) * ans(
        mid,
        right,
        (1 if mid + 1 == len(aa) or aa[mid] < aa[mid+1] else 0) *2 + cat % 2
    )
    return ms[(left, right, cat)]

t = int(input())
for _ in range(t):
    input()
    aa = list(map(int, input().split()))

    ms = {}
    print(ans(0, len(aa), 0))
