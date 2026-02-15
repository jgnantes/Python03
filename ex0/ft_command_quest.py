import sys


def ft_command_quest():
    """Display command-line arguments passed to the script."""
    length: int = len(sys.argv)

    if length == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")

    if length > 1:
        i: int = 1
        while i < length:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {length}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()
