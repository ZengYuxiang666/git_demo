def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print(f"moving form {a} to {c}")
        hanoi(n-1, b, a, c)
hanoi(64, 'A', 'B', 'C')