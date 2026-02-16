import sys


def ft_score_analytics():
    """Process command-line scores and display basic statistics."""
    argc_1: int = len(sys.argv)
    processed_score: list = []

    if argc_1 != 1:
        for score in sys.argv[1:]:
            try:
                score = int(score)
                processed_score += [score]
            except ValueError:
                print(f"'{score}' is not a numeric value")

    argc_2: int = len(processed_score)
    if argc_2 == 0:
        print(
            f"No scores provided. Usage: {sys.argv[0]} <score1> <score2> ..."
            )
        return
    min_s: int = min(processed_score)
    max_s: int = max(processed_score)

    print(f"Scores processed: {processed_score}")
    print(f"Total players: {argc_2}")
    print(f"Total score: {sum(processed_score)}")
    print(f"Average score: {sum(processed_score)/argc_2}")
    print(f"High score: {max_s}")
    print(f"Low score: {min_s}")
    print(f"Score range: {max_s - min_s}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
