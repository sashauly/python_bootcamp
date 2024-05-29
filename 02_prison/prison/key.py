# AssertionError: len(key) == 1337
# AssertionError: key[404] == 3
# AssertionError: key > 9000
# AssertionError: key.passphrase == "zax2rulez"
# AssertionError: str(key) == "GeneralTsoKeycard"
class Key:
    def __len__(self):
        return 1337

    def __getitem__(self, item):
        if item == 404:
            return 3
        else:
            raise IndexError

    def __gt__(self, other):
        if other == 9000:
            return True
        else:
            return False

    @property
    def passphrase(self):
        return 'zax2rulez'

    def __str__(self):
        return "GeneralTsoKeycard"


if __name__ == "__main__":
    key = Key()

    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"
