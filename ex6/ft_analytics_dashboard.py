if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===\n")
    players: list = ['João', 'Pepita', 'Carol de Niterói', 'Inbonha',
    'Tulla Luana', 'Wanessa Wolf (são elas)']
    scores: list = [8000, 42, 123, 22002, 1, 122]
    lowests = [score for score in scores if score < 123]
    print(f"Lowest scores: {sorted(lowests)}")
    highests = [score for score in scores if score >= 123]
    print(f"Highest scores: {sorted(highests)}")
    doubled = [score*2 for score in scores]
    print(f"Douled scores: {doubled}")
    girlies = [name for name in players if name[len(name) - 1] == 'a']
    print(f"Girliest players: {girlies}")
    print("")

    print("=== Dict Comprehension Examples ===\n")
    scores_sort = sorted(scores, reverse = True)
    if len(players) == len(scores):
        scoreboard = {players[i]:scores_sort[i] for i in range(len(players))}
        print("Scoreboard:")
        i: int = 0
        for item in scoreboard:
            print(f"{i + 1} - {item}: {scoreboard[item]}")
            i += 1
    categories = {
        players[i]: "highest" if scores[i] >= 123 else "lowest"
        for i in range(len(players))
    }
    print("\nBest ones:", end = ' ')
    for player in categories:
        if categories[player] == "highest":
            print(f"{player}", end = ', ')
    print("and that's about it")
    print("Shame on them:", end = ' ')
    for player in categories:
        if categories[player] == "lowest":
            print(f"{player}", end = ', ')
    print("no one else\n")

    print("=== Set Comprehension Examples ===\n")

    print("=== Combined Analysis ===\n")
    print("Some Random Stuff")
    if len(players) == len(scores):
        highest = max(scores)
        print(f"- {players[0]} has the highest score: {highest} points")
        lowest = min(scores)
        print(
            f"- {players[len(players) - 1]} has the lowest: {lowest} point(s)"
            )
    print(f"- Total players: {len(players)}")
    sum_scores: int = 0
    for score in scores:
        sum_scores += score
    print(f"- Average score: {sum_scores / len(scores):.2f}")

