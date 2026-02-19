import sys


def ft_score_analytics() -> None:
    """Process command-line scores and display basic statistics."""
    processed_score: list = []

    for score in sys.argv[1:]:
        try:
            score = int(score)
            processed_score += [score]
        except ValueError:
            print(f"'{score}' is not a numeric value")

    length: int = len(processed_score)
    if length == 0:
        print(
            f"No scores provided. Usage: {sys.argv[0]} <score1> <score2> ..."
            )
        return
    min_score: int = min(processed_score)
    max_score: int = max(processed_score)

    print(f"Scores processed: {processed_score}")
    print(f"Total players: {length}")
    print(f"Total score: {sum(processed_score)}")
    print(f"Average score: {sum(processed_score)/length}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
