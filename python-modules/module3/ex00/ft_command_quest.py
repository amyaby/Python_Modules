import sys

def main():
    print("=== Command Quest ===")
    c = len(sys.argv)
    if c == 1:
        print("no argument provided")
    else:
        print(f"Program name: {sys.argv[0]}")
        for i in range(1, c):
            print(f"argument {i}: {sys.argv[i]}")
        print(f"total arguments: {c}")

if __name__ == "__main__":
    main()
