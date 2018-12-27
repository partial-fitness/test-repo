from math_utils import sum

class TestSum:

    def test_when_passed_positive_integer_and_neutral_element_the_result_is_positive(self):
        positive_int = 100
        neutral_element = 0
        result = sum(positive_int, neutral_element)

        assert result == 100

    def test_when_passed_negative_integer_and_neutral_element_the_result_is_negative(self):
        negative_int = -100
        neutral_element = 0
        result = sum(negative_int, neutral_element)

        assert result == -100
