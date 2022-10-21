from src.counter import count_ocurrences


def test_counter():
    result_lower = count_ocurrences("src/jobs.csv", "python")
    result_upper = count_ocurrences("src/jobs.csv", "PYTHON")

    assert result_lower == 1639
    assert result_upper == 1639
    assert result_upper == result_lower
