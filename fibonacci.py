"""Fibonacci numbers: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)."""

from typing import Iterator


def fib(n: int) -> int:
    """Return the n-th Fibonacci number using fast doubling in O(log n) steps."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    def _pair(k: int) -> tuple[int, int]:
        # Returns (F(k), F(k+1)).
        if k == 0:
            return 0, 1
        a, b = _pair(k >> 1)
        c = a * (2 * b - a)  # F(2m)
        d = a * a + b * b  # F(2m+1)
        return (d, c + d) if k & 1 else (c, d)

    return _pair(n)[0]


def fib_sequence() -> Iterator[int]:
    """Yield Fibonacci numbers indefinitely: 0, 1, 1, 2, 3, 5, ..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    import itertools

    print(list(itertools.islice(fib_sequence(), 15)))
    print(fib(100))
