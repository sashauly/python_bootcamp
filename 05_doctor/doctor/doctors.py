import threading
import random


class Screwdriver:
    def __init__(self):
        self.lock = threading.Lock()


class Doctor(threading.Thread):
    def __init__(self, name, left_screwdriver, right_screwdriver):
        threading.Thread.__init__(self)
        self.name = name
        self.left_screwdriver = left_screwdriver
        self.right_screwdriver = right_screwdriver

    def run(self):
        delay = random.uniform(0, 1)
        threading.Event().wait(delay)
        self.left_screwdriver.lock.acquire()
        try:
            if self.right_screwdriver.lock.acquire(False):
                try:
                    print(f'Doctor {self.name}: BLAST!')
                finally:
                    self.right_screwdriver.lock.release()
        finally:
            self.left_screwdriver.lock.release()


def main():
    names = ['9', '10', '11', '12', '13']

    screwdrivers = [Screwdriver() for _ in range(5)]

    doctors = [Doctor(names[i], screwdrivers[i], screwdrivers[(i+1) % 5])
               for i in range(5)]

    for doctor in doctors:
        doctor.start()

    for doctor in doctors:
        doctor.join()


if __name__ == "__main__":
    main()
