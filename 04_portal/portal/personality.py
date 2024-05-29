import random


def turrets_generator():
    def shoot(self):
        print("Shooting")

    def search(self):
        print("Searching")

    def talk(self):
        print("Talking")

    def generate_traits():
        traits = ["neuroticism", "openness",
                  "conscientiousness", "extraversion", "agreeableness"]
        values = []
        for i in range(4):
            values.append(random.randint(0, 100 - sum(values)))
        values.append(100 - sum(values))
        return dict(zip(traits, values))

    Turret = type("Turret", (), {
                  "shoot": shoot,
                  "search": search,
                  "talk": talk,
                  **generate_traits()
                  })

    return Turret


if __name__ == '__main__':
    turret = turrets_generator()()

    turret.shoot()
    turret.search()
    turret.talk()

    print("Neuroticism: ", turret.neuroticism)
    print("Openness: ", turret.openness)
    print("Conscientiousness: ", turret.conscientiousness)
    print("Extraversion: ", turret.extraversion)
    print("Agreeableness: ", turret.agreeableness)
