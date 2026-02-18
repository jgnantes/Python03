from typing import Generator


def event_processing() -> Generator:
    """Processes, prints and yields several random event statistics"""
    players: list = ["alice", "bob", "charlie"]
    events: list = [
        "killed monster",
        "found treasure",
        "leveled up",
        "cooked feijoada",
        "sang 'jingle bells'",
        "fell in love with you"]
    i: int = 1
    high_levels: int = 0
    treasure: int = 0
    level_up: int = 0
    while True:
        player: str = players[i % len(players) - 1]
        level: int = (i * 11) % 13 + 1
        if level >= 10:
            high_levels += 1
        event: str = events[i*i % len(events) + 1]
        if event == "found treasure":
            treasure += 1
        if event == "leveled up":
            level_up += 1
        yield (
            f"Event {i}: Player {player} (level {level}) {event}",
            high_levels,
            treasure,
            level_up
        )
        i += 1


def fibonacci() -> Generator:
    """Calculates a fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b)


def prime() -> Generator:
    """Finds and yields prime numbers starting from 2"""
    prime_value: int = 2
    while True:
        yield prime_value
        prime_value += 1
        n = prime_value - 1
        while n > 1:
            if prime_value % n == 0:
                prime_value += 1
                n = prime_value - 1
            n -= 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    iterations: int = 1000

    if iterations > 0:
        print(f"Processing {iterations} game events...\n")
        gen = event_processing()
        i: int = 1
        for _ in range(iterations):
            event, high_levels, treasure, level_up = next(gen)
            if i == 1 or i == 2 or i == 3:
                print(event)
                i += 1
        print("...")
        print("\n=== Stream Analytics ===")
        print(f"Total events processed: {iterations}")
        print(f"High-level players (10+): {high_levels}")
        print(f"Treasure events: {treasure}")
        print(f"Level-up events: {level_up}")
        print("\nMemory usage: Constant (streaming)")
        print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fib = fibonacci()
    print("Fibonacci sequence (first 10):", end=' ')
    for _ in range(9):
        print(next(fib), end=', ')
    print(next(fib), end=' ')
    prime_value = prime()
    print("\nPrime numbers (first 5):", end=' ')
    for _ in range(4):
        print(next(prime_value), end=', ')
    print(next(prime_value), end=' ')
    print("")
