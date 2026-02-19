import sys


def ft_command_quest() -> None:
    """Display command-line arguments passed to the script."""
    argc: int = len(sys.argv)

    if argc == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")

    if argc > 1:
        i: int = 1
        while i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()
