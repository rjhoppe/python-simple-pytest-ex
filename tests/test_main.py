import main
import pytest

def test_square():
  assert main.square(5) == 25

def test_square_float():
  assert main.square(3.) == pytest.approx(9.)

# Easy to make tests very unreadable if used too heavily
@pytest.mark.parametrize(
  ('input_n', 'expected'),
  (
      (5, 25),
      (3., 9.),
  )
)
def test_square2(input_n, expected):
  print(f'{input_n=}')
  assert main.square(input_n) == expected

# Class based test
class TestSquare:
  def test_square3(self):
    assert main.square(3) == 9