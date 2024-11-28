import pytest
from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size

def test_text_to_duration_float2():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    input_value= "10:20"
    assert text_to_duration(input_value) == pytest.approx(10.33333333)

def test_text_to_duration_float1():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durtaion 
    """
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour duration
    """
    assert text_to_duration("10:00") == 10

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result


def test_calculate_crew_size1(): # FIXME
    """
    Test that calculate_crew_size returns expected number of people from crew member list 
    for edge cases 
    """

    # Edge case 1
    actual_result =  calculate_crew_size('')
    expected_result = None
    assert actual_result == expected_result



# If the test was successful, you get nothing on your terminal