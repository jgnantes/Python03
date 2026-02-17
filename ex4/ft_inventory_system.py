import sys


def parse_str(arg: str) -> tuple:
    """Parses strings from sys.argv into a 'key:value' format"""
    i = 0
    while i < len(arg) and arg[i] != ":":
        i += 1
    if i == len(arg) or i == 0:
        print(f'Error: "{arg}" could not be parsed into a "key:value" format')
        print(f'"{arg[:i]}" could not be added to the inventory')
        raise TypeError

    key: str = arg[:i]
    value_str: str = arg[(i + 1):]
    try:
        value: int = int(value_str)
    except ValueError:
        print(f"Error: {value_str} is not a numeric value")
        print(f'"{key}" could not be added to the inventory')
        raise ValueError

    return key, value


def inventory_system_analysis(inventory: dict):
    """Counts total and unique items"""
    total: int = 0
    unique: int = 0
    for _, value in inventory.items():
        total += value
        unique += 1
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {unique}")


def current_inventory(inventory: dict):
    """"""
    total: int = 0
    for _, value in inventory.items():
        total += value

    for key, value in inventory.items():
        percent: float = (value * 100) / total
        print(f"{key}: {value} units ({percent:.1f}%)")


def inventory_statistic(inventory: dict):
    """"""
    highest: int = 0
    most_abundant: str = ""
    for key, value in inventory.items():
        if value > highest:
            highest = value
            most_abundant = key

    lowest: int = highest
    least_abundant: str = ""
    for key, value in inventory.items():
        if value < lowest:
            lowest = value
            least_abundant = key

    print(f"Most abundant: {most_abundant} ({highest} units)")
    print(f"Least abundant: {least_abundant} ({lowest} units)")


def item_categories(inventory: dict):
    abundant: dict = {}
    moderate: dict = {}
    scarce: dict = {}

    for key, value in inventory.items():
        if value >= 10:
            abundant.update({key:value})
        elif value >= 5 and value < 10:
            moderate.update({key:value})
        else:
            scarce.update({key:value})

    if abundant:
        print(f"Abundant: {abundant}")
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")


def management_suggestions(inventory: dict):
    restock: list = []

    for key, value in inventory.items():
        if value < 2:
            restock += [key]
    print(f"Restock needed: {restock}")


def dictionary_poperties_demo(inventory: dict, sample_key: str):
    keys: set = []
    values: list = []
    lookup: bool = False

    for key, value in inventory.items():
        keys += [key]
        if key == sample_key:
            lookup = True
        values += [value]

    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print(f"Sample lookup - '{sample_key}' in dictionary: {lookup}")


if __name__ == "__main__":
    inventory: dict = {}

    for item in sys.argv[1:]:
        try:
            key, value = parse_str(item)
            if value <= 0:
                print(f'Error: "value" cannot be zero or negative')
                print(f'"{key}" could not be added to the inventory')
                print("Try again using a value higher than zero\n")
            else:
                inventory.update({key:value})
        except (TypeError, ValueError):
            print('Try again using a valid "key:value" format\n')

    if inventory:
        print("=== Inventory System Analysis ===")
        inventory_system_analysis(inventory)

        print("\n=== Current Inventory ===")
        current_inventory(inventory)

        print("\n=== Inventory Statistics ===")
        inventory_statistic(inventory)

        print("\n=== Item Categories ===")
        item_categories(inventory)

        print("\n=== Management Suggestions ===")
        management_suggestions(inventory)

        print("\n=== Dictionary Properties Demo ===")
        dictionary_poperties_demo(inventory, "sword")
