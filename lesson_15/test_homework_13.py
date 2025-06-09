import pytest
from lesson_15.homework_13 import Rhombus



@pytest.mark.hw13
@pytest.mark.positive
@pytest.mark.parametrize( 'side_a, angle_a, expected_result', [
    (1, 1, 'Rhombus data: Side A - 1, Angle A - 1 degrees, Angle B - 179 degrees.'),  # 1 test
    (100, 179, 'Rhombus data: Side A - 100, Angle A - 179 degrees, Angle B - 1 degrees.'),  # 2 test
    ])
def test_my_rhombus_valid(side_a, angle_a, expected_result):
    actual_result = str(Rhombus(side_a, angle_a))
    assert actual_result == expected_result


@pytest.mark.hw13
@pytest.mark.negative
@pytest.mark.parametrize( 'side_a, angle_a, expected_exception, expected_message', [
    (0, 30, AttributeError, 'Side A should be > 0'),  # 1 test
    (10, 0, AttributeError, 'Angle A should be between 0 and 180 degrees'),  # 2 test
    (10, 181, AttributeError, 'Angle A should be between 0 and 180 degrees'), # 3 test
    ('10', 30, AttributeError,  'Side A should be an integer'), # 4 test
    (30, '10', AttributeError, 'Angle A should be an integer'), # 5 test
    ])
def test_my_rhombus_invalid(side_a, angle_a, expected_exception, expected_message):
    with pytest.raises(expected_exception) as excinfo:
        Rhombus(side_a,angle_a)
    assert expected_message in str(excinfo.value)