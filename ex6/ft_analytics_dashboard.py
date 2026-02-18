if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===\n")
    players: list = [
        'João',
        'Pepita',
        'Carol de Niterói',
        'Inbonha', 'Tulla Luana',
        "Débora dos Falsetes",
        'José Arcádio Buendía',
        'Wanessa Wolf (são elas)']
    scores: list = [8000, 42, 123, 22002, 1, 122, 801, 801]
    lowests = [score for score in scores if score < 800]
    print(f"Lowest scores: {sorted(lowests)}")
    highests = [score for score in scores if score >= 800]
    print(f"Highest scores: {sorted(highests)}")
    doubled = [score*2 for score in sorted(scores)]
    print(f"Doubled scores: {doubled}")
    girlies = [name for name in players if name[len(name) - 1] == 'a']
    print(f"Girliest players: {girlies}")
    print("")

    print("=== Dict Comprehension Examples ===\n")
    scores_sort = sorted(scores, reverse=True)
    if len(players) == len(scores):
        scoreboard = {players[i]: scores_sort[i] for i in range(len(players))}
        print("Scoreboard:")
        i: int = 0
        for item in scoreboard:
            print(f"{i + 1} - {item}: {scoreboard[item]}")
            i += 1
    categories = {
        players[i]: "highest" if scores[i] > 123 else "lowest"
        for i in range(len(players))
        }
    print("\nBest ones:", end=' ')
    for player in categories:
        if categories[player] == "highest":
            print(f"{player}", end=', ')
    print("and that's about it")
    print("Shame on them:", end=' ')
    for player in categories:
        if categories[player] == "lowest":
            print(f"{player}", end=', ')
    print("no one else")
    even_scores = {
        players[i]: scores_sort[i] for i in range(len(players))
        if scores_sort[i] % 2 == 0
        }
    print(f"Even scores: {even_scores}")
    odd_scores = {
        players[i]: scores_sort[i] for i in range(len(players))
        if scores_sort[i] % 2 == 1
        }
    print(f"Odd scores: {odd_scores}\n")

    print("=== Set Comprehension Examples ===\n")
    print("Another Scoreboard Comparison")
    unique_players = {player for player in players}
    print(f"They're all uniquely weird: {unique_players}")
    not_unique_scores = {score for score in scores_sort}
    print(f"They ain't: {not_unique_scores}")
    print(f"Top performer: {players[scores_sort.index(max(scores))]} xoxo")

    print("\n=== Combined Analysis ===\n")
    print("Some Random Stuff")
    if len(players) == len(scores):
        highest = max(scores)
        print(f"- {players[0]} has the highest score: {highest} points")
        lowest = min(scores)
        print(
            f"- {players[len(players) - 1]} has the lowest: {lowest} point(s)"
            )
    print(f"- Total players: {len(players)}")
    print(f"- Average score: {sum(scores) / len(scores):.1f}")
