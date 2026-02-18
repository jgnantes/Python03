if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===\n")
    players: list = ['João', 'Pepita', 'Carol de Niterói', 'Inbonha',
    'Tulla Luana', 'Wanessa Wolf (são elas)']
    scores: list = [8000, 42, 123, 22002, 1, 123]
    if len(players) == len(scores):
        print("Final Scores:")
        i: int = 0
        for player in players:
            print(f"{i + 1} - {player}: {sorted(scores, reverse = True)[i]}")
            i += 1
    print("")

    print("=== Dict Comprehension Examples ===\n")
    scoreboard: dict = {}
    if len(players) == len(scores):
        j: int = 0
        for player in players:
            scoreboard[player] = sorted(scores, reverse = True)[j]
            j += 1
        print("The Same Scoreboard from Before but Now with Dicts")
        k: int = 0
        for item in scoreboard:
            print(f"{k + 1} - {item}: {scoreboard[item]} (with dicts)")
            k += 1
    print("")

    print("=== Set Comprehension Examples ===\n")
    print("You Guessed It")
    player_set = set(players)

    print("=== Combined Analysis ===\n")
    print("\nSome Random Stuff")
    highest = max(scores)
    print(f"- {players[0]} has the highest score: {highest} points")
    lowest = min(scores)
    print(
        f"- {players[len(players) - 1]} has the lowest: {lowest} point(s)"
        )
