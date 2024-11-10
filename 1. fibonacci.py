# non-recursive(iterative)
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
# generate Fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

# recursive
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    fib_sequence = fibonacci(nterms)
    for num in fib_sequence:
        print(num)



'''
Iterative Method:
Time Complexity: O(n)
Space Complexity: O(1)

->Uses a for loop to generate the Fibonacci sequence.
->It starts with two numbers (0 and 1) and iteratively calculates the next number by summing the last two terms, printing each term.


Recursive Method:
Time Complexity: O(n)
Space Complexity: O(n)

->A function calls itself to generate the Fibonacci sequence.
->It builds the sequence by returning a list, appending the sum of the last two terms until the desired number of terms is reached.
'''