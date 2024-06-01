from unittest import mock, TestCase
from unittest.mock import Mock, mock_open
import pytest
from blade_runner.main import (
    load_questions,
    display_question,
    input_variables
)


def test_nonexistent_json_file(monkeypatch):
    monkeypatch.setattr("builtins.open", Mock(side_effect=FileNotFoundError))
    with pytest.raises(FileNotFoundError):
        load_questions("nonexistent.json")


def test_empty_json_file(monkeypatch):
    monkeypatch.setattr("builtins.open", mock_open(read_data="{}"))
    with pytest.raises(ValueError) as exc_info:
        load_questions("./tests/empty.json")
    assert str(exc_info.value) == "The JSON file is empty."


@pytest.mark.parametrize("user_input", ["0", "4"])
def test_invalid_input_number(monkeypatch, user_input):
    monkeypatch.setattr("builtins.input", Mock(return_value=user_input))
    question = {"question": "Sample question", "answers": ["A", "B", "C"]}
    with pytest.raises(ValueError):
        display_question(question)


class InputVariablesTestCase(TestCase):
    def test_valid_input(self):
        with mock.patch('builtins.input', return_value='5'):
            result = input_variables(
                "Test Prompt: ", min_value=0, max_value=10)
            self.assertEqual(result, 5)

    def test_invalid_input(self):
        with mock.patch('builtins.input', return_value='-1'):
            with self.assertRaises(ValueError) as cm:
                input_variables("Test Prompt: ", min_value=0)
            self.assertEqual(str(
                cm.exception), "Invalid input. Please enter a number between 0 and None.")

        with mock.patch('builtins.input', return_value='11'):
            with self.assertRaises(ValueError) as cm:
                input_variables("Test Prompt: ", max_value=10)
            self.assertEqual(str(
                cm.exception), "Invalid input. Please enter a number between 0 and 10.")

        with mock.patch('builtins.input', return_value='7'):
            with self.assertRaises(ValueError) as cm:
                input_variables("Test Prompt: ", min_value=0, max_value=6)
            self.assertEqual(
                str(cm.exception), "Invalid input. Please enter a number between 0 and 6.")
