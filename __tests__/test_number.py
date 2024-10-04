from src.number import sum_even_numbers


def test_sum_even_numbers():
    result = sum_even_numbers([1, 2, 3, 4])
    assert result == 6
