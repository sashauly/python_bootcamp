import asyncio
from enum import Enum, auto
from random import choice


class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


class Agent:

    def __aiter__(self, health=5):
        self.health = health
        self.actions = list(Action)
        return self

    async def __anext__(self):
        return choice(self.actions)


async def fight():
    agent = Agent()
    neo_health = 5

    async for agent_action in agent:
        neo_action = await get_neo_action()
        neo_health = await perform_actions(agent_action,
                                           neo_action,
                                           neo_health,
                                           agent)
        print(
            f"Agent: {agent_action}, Neo: {neo_action}, Agent Health: {agent.health}, Neo Health: {neo_health}")

        if neo_health == 0:
            print("Agent wins!")
            break
        elif agent.health == 0:
            print("Neo wins!")
            break
        elif neo_health == 0 and agent.health == 0:
            print("It's a tie!")
            break


async def get_neo_action():
    return choice(list(Action))


async def perform_actions(agent_action, neo_action, neo_health, agent):
    if (
        (agent_action == Action.HIGHBLOCK and neo_action == Action.LOWKICK)
        or (agent_action == Action.LOWBLOCK and neo_action == Action.HIGHKICK)
    ):
        neo_health -= 1
    elif (
        (agent_action == Action.LOWKICK and neo_action == Action.HIGHBLOCK)
        or (agent_action == Action.HIGHKICK and neo_action == Action.LOWBLOCK)
    ):
        agent.health -= 1

    return neo_health


asyncio.run(fight())
