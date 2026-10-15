
# Program 2: Fibonacci series

n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Enter a positive number of terms.")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
