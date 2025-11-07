def fib(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed).

    Args:
        n: non-negative integer index

    Returns:
        The nth Fibonacci number.

    Raises:
        TypeError: if n is not an int
        ValueError: if n is negative
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python main.py <n>")
        sys.exit(2)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("n must be an integer")
        sys.exit(2)
    print(fib(n))