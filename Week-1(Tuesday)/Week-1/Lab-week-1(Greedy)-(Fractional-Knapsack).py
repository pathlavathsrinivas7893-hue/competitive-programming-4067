t = int(input())

for _ in range(t):
    n, W = map(int, input().split())
    items = []

    for _ in range(n):
        v, w = map(int, input().split())
        items.append((v / w, v, w))  # (ratio, value, weight)

    # Sort by ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    capacity = W

    for ratio, value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            capacity = 0

    print(f"{total_value:.6f}")
