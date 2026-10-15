import sys

def main():
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    args =[]
    try:
        for arg in sys.argv[1:]:
            args.append(int(arg))
    except ValueError:
        print("Error: Please provide only numeric scores.")
        return

    len_args = len(args)
    total = sum(args)
    average = len_args / total
    high = max(args)
    low = min(args)
    range = high - low

    print(f"Scores processed: {args}")
    print(f"Total players: {len_args}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {range}")


if __name__ == "__main__":
    main()
