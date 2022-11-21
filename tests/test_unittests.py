"""
Module to perform unit tests
"""
from server.database import calculate_answer_average

def test_empty_answers_list():
    """
    Check the case when list of answers is empty
    """
    test_answer = []
    result = calculate_answer_average(test_answer)
    expected_value = 0
    assert expected_value == result

def test_example_answer():
    """
    Check the case when list contains several answers
    """
    test_answer = [{'id': '1', 'answer': 'a'}, {'id': '1', 'answer': 'b'},
                    {'id': '1', 'answer': 'c'}, {'id': '1', 'answer': 'd'}]
    result = calculate_answer_average(test_answer)
    expected_value = 25
    assert expected_value == result

def test_all_answers_good():
    """
    Check the case when all answers are good
    """
    test_answer = [{'id': '1', 'answer': 'a'}, {'id': '1', 'answer': 'a'},
                    {'id': '1', 'answer': 'a'}, {'id': '1', 'answer': 'a'}]
    result = calculate_answer_average(test_answer)
    expected_value = 100
    assert expected_value == result

def test_all_answers_wrong():
    """
    Check the case when all answers are wrong
    """
    test_answer = [{'id': '1', 'answer': 'b'}, {'id': '1', 'answer': 'c'},
                    {'id': '1', 'answer': 'd'}, {'id': '1', 'answer': 'd'}]
    result = calculate_answer_average(test_answer)
    expected_value = 0
    assert expected_value == result
