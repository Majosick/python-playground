# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pytest


# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     sum = a+b
#     subs = a-b
#     prod = a*b
#     print(f'{sum}\n{subs}\n{prod}\n')
# test_example.py

def add(a, b):
    return a + b


def test_addition():
    assert add(2, 3) == 5


@pytest.fixture
def setup_data() -> float:
    return 3


def test_setup_data(setup_data):
    assert setup_data == 3. and isinstance(setup_data, int)


def square(y: float) -> float:
    return y * y


@pytest.mark.parametrize(
    ('input_n', 'expected'),
    (
        (5, 25),
        (3.0, 9.0),
    )
)
def test_square(input_n, expected) -> float:
    print(f'{input_n=}')
    assert square(input_n) == pytest.approx(expected)


class TestSquare:
    def test_square(self):
        assert square(3) == 9
