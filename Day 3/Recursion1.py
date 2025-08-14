def one_to_n(n):
    assert n>0 and int(n) == n, 'The number should be positive integer only'
    if n > 1:
        one_to_n(n-1)
    print(n, end="")
one_to_n(6)
print()
