def ft_achievement_tracker(achievements: list, player: str) -> set:
    """Casts a list of achievements from a player into a set and prints it"""
    try:
        returning_set: set = set(achievements)
    except TypeError as e:
        print(f"Error detected: {e},", end=' ')
        print(
            f"{player}'s achievements must be an iterable of hashable values"
            )
        return set()

    print(f"Player {player} achievements: {returning_set}")
    return returning_set


def ft_achievement_analytics(set_1: set, set_2: set, set_3: set) -> None:
    """Compares elemens between three different sets of achievements
    and prints the results"""
    if set_1 is None or set_2 is None or set_3 is None:
        print("Error detected: one or more sets are None")
        print("Achievement analytics could not be processed")
        return

    try:
        union_set = set_1.union(set_2, set_3)
        inter_set = set_1.intersection(set_2, set_3)
        only_1 = set_1 - set_2 - set_3
        only_2 = set_2 - set_1 - set_3
        only_3 = set_3 - set_1 - set_2
        rare = only_1 | only_2 | only_3
    except (AttributeError, TypeError) as e:
        print(f"Error detected: {e}")
        print("Achievement analytics could not be processed")
        return

    print(f"All unique achievements: {union_set}")
    print(f"Total unique achievements: {len(union_set)}")
    print(f"Common to all players: {inter_set}")
    print(f"Rare achievements (1 player): {rare}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']
    alice_set = ft_achievement_tracker(alice, "alice")
    bob = ['first_kill', 'level_10', 'boss_slayer', 'collector']
    bob_set = ft_achievement_tracker(bob, "bob")
    charlie = [
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist']
    charlie_set = ft_achievement_tracker(charlie, "charlie")

    print("\n=== Achievement Analytics ===")
    ft_achievement_analytics(alice_set, bob_set, charlie_set)

    print(f"\nAlice vs Bob common: {alice_set.intersection(bob_set)}")
    print(f"Alice unique: {alice_set.difference(bob_set)}")
    print(f"Bob unique: {bob_set.difference(alice_set)}")
