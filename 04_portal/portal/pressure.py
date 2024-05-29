import random
import time


def emit_gel(step):
    pressure = 50
    while True:
        step = yield pressure
        pressure += step
        if pressure < 10 or pressure > 90:
            break


def valve(step):
    gen = emit_gel(step)
    pressure = next(gen)
    while True:
        time.sleep(0.5)
        if pressure > 80 or pressure < 20:
            step = -step
        try:
            pressure = gen.send(step)
            print(f'Pressure: {pressure}, step: {step}')
        except StopIteration:
            print('Emergency break! Exit the script.')
            break


valve(random.uniform(-2, 2))
