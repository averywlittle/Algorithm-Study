import PA_1, time

a = 3141592653589793238462643383279502884197169399375105820974944592

b = 2718281828459045235360287471352662497757247093699959574966967627

# Timing is heavily dependent on internet connection
# This will print the correct answer, but hopefully we can see it's slower
initA = time.perf_counter()
print(a * b)
print(f'{time.perf_counter() - initA:0.9f} seconds')

# new line
print('\n')

initB = time.perf_counter()
PA_1.karatsuba(a, b)
print(f'{time.perf_counter() - initB:0.9f} seconds')