import main
import pytest

@pytest.mark.parametrize("decimals", [1, 2, 3])
def test_assignment2(decimals):
  try:
    result = main.assignment_2(decimals)
    print(result)
  except Exception as e:
    pytest.fail(f"An error occurred: {e}")
