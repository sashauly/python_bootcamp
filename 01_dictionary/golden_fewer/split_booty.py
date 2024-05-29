from golden_fewer import purse


def split_booty(*purses: dict[str, int]) -> list[dict[str, int]]:
    total_gold: int = sum(given_purse.get("gold_ingots", 0) for given_purse in purses)
    if total_gold < 0:
        raise ValueError("Number of total_ingots cannot be less than 0")

    share, remainder = divmod(total_gold, 3)

    new_purses: list[dict[str, int]] = [purse.empty({}) for _ in range(3)]
    for i in range(3):
        for _ in range(share):
            new_purses[i] = purse.add_ingot(new_purses[i])

    for i in range(remainder):
        new_purses[i] = purse.add_ingot(new_purses[i])

    return new_purses


if __name__ == "__main__":
    purse1 = {"gold_ingots": 2}
    purse2 = {"gold_ingots": 1}
    purse3 = {"apples": 10}
    purse4 = {"gold_ingots": 1}
    purse5 = {"gold_ingots": 2}

    new_purses = split_booty(purse1, purse2, purse3, purse4, purse5)
    print(new_purses)
