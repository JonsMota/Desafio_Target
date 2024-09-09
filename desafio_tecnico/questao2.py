def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_in_fibonacci(n):
    sequence = fibonacci_sequence(n)
    return n in sequence

number = int(input("Informe um número: "))
if is_in_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")