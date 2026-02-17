def ft_achievement_tracker(achievements: list, player: str) -> set:
    """"""
    returning_set: set = set(achievements)
    print(f"Player {player} achievements: {returning_set}")
    return returning_set


def ft_achievement_analytics(set_1: set, set_2: set, set_3: set = None):
    """"""
    if set_3 is not None:
        union_set = set_1.union(set_2, set_3)
        inter_set = set_1.intersection(set_2, set_3)
    else:
        union_set = set_1.union(set_2)
        inter_set = set_1.intersection(set_2)

    print(f"All unique achievements: {union_set}")
    print(f"Total unique achievements: {len(union_set)}")
    print(f"Common to all players: {inter_set}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']
    alice_set = ft_achievement_tracker(alice, "alice")
    bob = ['first_kill', 'level_10', 'boss_slayer', 'collector']
    bob_set = ft_achievement_tracker(bob, "bob")
    charlie = ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist']
    charlie_set = ft_achievement_tracker(charlie, "charlie")

    print("\n=== Achievement Analytics ===\n")
    ft_achievement_analytics(alice_set, bob_set, charlie_set)
