from constants import ___


def calculate_total_spent_for_users(users_ids: set[int], users_ids_to_users_map: dict[int, tuple[str, int, list[int]]]) -> int | None:
    pass
# интуитивно кажется что результат еще может быть и None

if __name__ == "__main__":
    assert calculate_total_spent_for_users(
        users_ids={3, 6, 12, 15},
        users_ids_to_users_map={
            3: ("Ilya", 32, [102, 15, 63, 12]),
        },
    ) == 192
