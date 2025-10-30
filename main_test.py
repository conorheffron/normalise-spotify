import main
import pytest

def test_assignment2():
  try:
    main.run(["python", "main.py", "2"], capture_output=True, text=True)
  except Exception as e:
    pytest.fail(f"An error occurred: {e}")
