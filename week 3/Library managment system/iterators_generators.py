import random

class Countdown:
    """
    An iterator class that counts down from a given number to 1.
    """
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            num = self.current
            self.current -= 1
            return num
        else:
            raise StopIteration

def fibonacci_generator(limit):
    """
    A generator function that yields Fibonacci numbers up to a specified limit.
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

def random_number_generator(start, end, count):
    """
    A generator function that yields a sequence of random numbers between a specified range.
    """
    for _ in range(count):
        yield random.randint(start, end)

def main():
    # Demonstrate the Countdown iterator
    try:
        print("Countdown from 10:")
        for number in Countdown(10):
            print(number, end=" ")
        print("\n")
    except Exception as e:
        print(f"An error occurred in Countdown: {e}")

    # Demonstrate the fibonacci_generator
    try:
        limit = 100
        print(f"Fibonacci numbers up to {limit}:")
        for fib in fibonacci_generator(limit):
            print(fib, end=" ")
        print("\n")
    except Exception as e:
        print(f"An error occurred in fibonacci_generator: {e}")

    # Demonstrate the random_number_generator
    try:
        start, end, count = 1, 100, 10
        print(f"{count} random numbers between {start} and {end}:")
        for num in random_number_generator(start, end, count):
            print(num, end=" ")
        print("\n")
    except Exception as e:
        print(f"An error occurred in random_number_generator: {e}")

if __name__ == "__main__":
    main()
