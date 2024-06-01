import json
import random


def load_questions(file_name: str) -> dict:
    """
        Load questions from a JSON file.

        Args:
            file_name (str): The name of the JSON file.

        Returns:
            dict: A dictionary containing the loaded questions.

        Raises:
            FileNotFoundError: If the JSON file doesn't exist.
            ValueError: If the JSON file is empty.
    """
    try:
        with open(file_name) as file:
            questions = json.load(file)
        if not questions:
            raise ValueError("The JSON file is empty.")
        return questions
    except FileNotFoundError:
        raise FileNotFoundError("The JSON file doesn't exist")


def display_question(question: dict) -> int:
    """Display question and answers, and capture user input for answer

    Args:
        question (dict): question dictionary with 1 question and 3 answers

    Raises:
        ValueError: If the user input not in range 1-3
        ValueError: If the user input not an integer

    Returns:
        int: User input for answer
    """
    print(question["question"])
    for i, answer in enumerate(question["answers"], start=1):
        print(f"{i}. {answer}")

    while True:
        try:
            response = int(input("Select your answer (1-3): "))
            if response < 1 or response > 3:
                raise ValueError
            return response - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            raise ValueError


def input_variables(prompt: str,
                    min_value: int = 0,
                    max_value: int = None) -> float:
    """Handle user input for additional indicators

    Args:
        prompt (str): Description of indicator
        min_value (int, optional): Minimal value of indicator. Defaults to 0.
        max_value (int, optional): Maximal value of indicator. Defaults to None.

    Raises:
        ValueError: If user input greater or lesser than max or min
        ValueError: If user input is not a number

    Returns:
        float: User input for according indicator
    """
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or (max_value is not None and
                                     value > max_value):
                raise ValueError
            return value
        except ValueError:
            raise ValueError(
                f"Invalid input. Please enter a number between {min_value} and {max_value}.")


def is_human_or_replicant(respiration: float,
                          heart_rate: float,
                          blushing_level: float,
                          papillary_dilation: float) -> str:
    """determines if the person being tested is a human or a replicant

    Args:
        respiration (float): Level of respiration
        heart_rate (float): Heart Rate
        blushing_level (float): Blushing level
        papillary_dilation (float): Papillary dilation

    Returns:
        str: Human or Replicant
    """
    return random.choice(["Human", "Replicant"])


def run_test():
    """
    Basically run test
    """
    file_name = "questions.json"
    questions = load_questions(file_name)
    random.shuffle(questions)

    decision_variables = []

    for question in questions:
        response = display_question(question)
        decision_variables.append(response)

    respiration = input_variables("Respiration (BPM): ", min_value=0)
    heart_rate = input_variables("Heart Rate (BPM): ", min_value=0)
    blushing_level = input_variables(
        "Blushing Level (1-6): ", min_value=1, max_value=6)
    papillary_dilation = input_variables(
        "Papillary Dilation (mm): ", min_value=0)

    result = is_human_or_replicant(
        respiration, heart_rate, blushing_level, papillary_dilation)

    print(f"\nResult: {result}")


if __name__ == "__main__":
    run_test()
