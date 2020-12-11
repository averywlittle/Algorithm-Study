
# Karatsuba's algorithm is an efficient way to solve integer multiplication problems O(n^1.68)
def karatsuba(a, b):

  if a < 10 or b < 10:
    return a * b;
  else:
    # Get half max length, accounting for odds
    max_len = max(len(str(a)), len(str(b)))
    half_len = max_len // 2

    # Split the inputs and shift over based on input lengths (use floor and modulo)
    n0 = a // 10**(half_len)
    n1 = a % 10**(half_len)
    n2 = b // 10**(half_len)
    n3 = b % 10**(half_len)

    # Recur on the split numbers
    z0 = karatsuba(n1, n3)
    z1 = karatsuba((n0 + n1), (n2 + n3))
    z2 = karatsuba(n0, n2)

    # Merge the equation to reduce multiplications
    return (z2 * 10**(2*half_len) + ((z1 - z2 - z0) * 10**(half_len)) + (z0))
