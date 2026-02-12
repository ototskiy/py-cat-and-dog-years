from app.main import get_human_age


def test_check_number_of_arguments_that_are_returned() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_return_value_of_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_return_value_of_second_human_year_if_input_values_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_return_value_of_second_human_year_if_input_values_is_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_return_value_of_third_human_year_if_input_values_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_return_value_of_third_human_year_if_input_values_is_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_fourth_human_year_for_cat_third_human_year_for_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_return_value_of_human_year_if_input_values_is_100() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_return_none_if_input_data_is_incorrect() -> None:
    assert get_human_age(-2, -5) == [None, None]
