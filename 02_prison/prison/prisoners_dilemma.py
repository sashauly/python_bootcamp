from collections import Counter

REWARD_BOTH_COOPERATE = 2
REWARD_ONE_CHEATS = 3
REWARD_OTHER_CHEATS = -1
REWARD_BOTH_CHEAT = 0

class Player(object):
    def __init__(self, cooperate: bool = True):
        self.cooperate = cooperate

    def play(self, previous_play):
        return self.cooperate


class Cheater(Player):
    def __init__(self):
        super().__init__(False)


class Cooperator(Player):
    def __init__(self):
        super().__init__(True)


class Copycat(Player):
    def __init__(self):
        super().__init__(True)
        self.previous_play = None

    def play(self, previous_play):
        if self.previous_play is None:
            self.previous_play = previous_play
        else:
            self.cooperate = self.previous_play
            self.previous_play = previous_play
        return self.cooperate


class Grudger(Player):
    def __init__(self):
        super().__init__(True)
        self.previous_play = None
        self.state = 0

    def play(self, previous_play):
        if self.previous_play is False:
            self.state = 1
            self.cooperate = False
        if self.state != 1:
            self.previous_play = previous_play
        return self.cooperate


class Detective(Player):
    def __init__(self):
        super().__init__(True)
        self.previous_play = None
        self.turn = 0
        self.state = 0  # 0 - Cheater, 1 - Copycat

    def play(self, previous_play):
        if self.turn < 4:
            if previous_play is False:
                self.state = 1
            if self.turn == 1:
                self.cooperate = False
            else:
                self.cooperate = True
            self.turn += 1
            return self.cooperate
        if self.state == 1:  # Copycat behavior
            self.cooperate = self.previous_play
            self.previous_play = previous_play
        else:  # Cheater behavior
            self.cooperate = False
        return self.cooperate


class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: Player, player2: Player):
        # simulate number of matches
        # equal to self.matches
        for _ in range(self.matches):
            plays = [player1.play(player2.cooperate),
                     player2.play(player1.cooperate)]
            player1.cooperate = plays[0]
            player2.cooperate = plays[1]

            if all(plays):
                self.registry[type(player1).__name__] += REWARD_BOTH_COOPERATE
                self.registry[type(player2).__name__] += REWARD_BOTH_COOPERATE
            elif not any(plays):
                self.registry[type(player1).__name__] += REWARD_BOTH_CHEAT
                self.registry[type(player2).__name__] += REWARD_BOTH_CHEAT
            else:
                if plays[0]:
                    self.registry[type(
                        player1).__name__] += REWARD_OTHER_CHEATS
                    self.registry[type(player2).__name__] += REWARD_ONE_CHEATS
                else:
                    self.registry[type(player1).__name__] += REWARD_ONE_CHEATS
                    self.registry[type(
                        player2).__name__] += REWARD_OTHER_CHEATS

    def top3(self):
        # print top three
        return self.registry.most_common(3)


if __name__ == "__main__":
    cheater = Cheater()
    cooperator = Cooperator()
    copycat = Copycat()
    grudger = Grudger()
    detective = Detective()

    game = Game()

    players = [cheater, cooperator, copycat, grudger, detective]
    for player1 in players:
        for player2 in players:
            if player1 != player2:
                game.play(player1, player2)
    print(game.top3())
