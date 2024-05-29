from golden_fewer.squeak_decorator import squeak_decorator


@squeak_decorator
def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse.copy()
    new_purse["gold_ingots"] = new_purse.get("gold_ingots", 0) + 1
    return new_purse


@squeak_decorator
def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse.copy()
    if new_purse.get("gold_ingots", 0) > 0:
        new_purse["gold_ingots"] -= 1
    return new_purse


@squeak_decorator
def empty(purse: dict[str, int]):
    return {}


if __name__ == "__main__":
    purse = {"stones": 3, "gold_ingots": 3}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
