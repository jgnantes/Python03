import math


def parse_str(string: str) -> tuple:
    """Splits each string into three substrings separated by ','
    and then parses then into a three-element integer tuple"""
    try:
        values: list = string.split(",")
        x: int = int(values[0])
        y: int = int(values[1])
        z: int = int(values[2])
        parsed_data: tuple = (x, y, z)
        print(f'Parsing coordinates: "{string}"')
        print(f"Parsed position: {parsed_data}")
        return parsed_data
    except Exception as e:
        print(f'Parsing invalid coordinates: "{string}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return None


def calculate_distance(coord: tuple, origin: tuple) -> float:
    """Uses the Euclidean formul to calculate
    the distance between two 3D coordinates"""
    try:
        distance: float = math.sqrt((
            (coord[0] - origin[0])**2 +
            (coord[1] - origin[1])**2 +
            (coord[2] - origin[2])**2
            ))
        print(f"Distance between {origin} and {coord}: {distance:.2f}\n")
        return distance
    except Exception as e:
        print(f"Error detected: {e}")
        print(
            f"Could not calculate the distance between {origin} and {coord}\n"
            )
        return None


def unpack_tuple(pack: tuple):
    """Unpacks a three-element tuple and prints its values"""
    try:
        x, y, z = pack
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except (ValueError, TypeError) as e:
        print(f'Invalid unpacking : "{pack}"')
        print("Error unpacking tuple:", e)
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    origin: tuple = (0, 0, 0)

    position_1: tuple = (10, 20, 5)
    print(f"Position created: {position_1}")
    calculate_distance(position_1, origin)

    position_2: str = "3,4,0"
    parsed_pos_2: tuple = parse_str(position_2)
    calculate_distance(parsed_pos_2, origin)

    parse_str("abc,def,ghi")

    unpack_tuple(parsed_pos_2)
