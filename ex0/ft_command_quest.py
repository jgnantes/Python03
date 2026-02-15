""""""

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
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
