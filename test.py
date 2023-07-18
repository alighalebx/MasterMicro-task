import pytest
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLineEdit, QPushButton
from PySide2.QtTest import QTest


@pytest.fixture
def main_window(qtbot):
    from main import MainWindow
    window = MainWindow()
    qtbot.addWidget(window)
    return window


def test_valid_input(main_window, qtbot):
    main_window.function_input.setText("5*x^2 + 2*x")
    main_window.min_input.setText("-10")
    main_window.max_input.setText("10")

    qtbot.mouseClick(main_window.plot_button, Qt.LeftButton)


def test_invalid_function(main_window, qtbot):
    main_window.function_input.setText("5*x^2 + 2*x + ")
    main_window.min_input.setText("-10")
    main_window.max_input.setText("10")

    qtbot.mouseClick(main_window.plot_button, Qt.LeftButton)

    assert isinstance(main_window.plot_button.clicked, type(main_window.plot_function))


def test_invalid_range(main_window, qtbot):
    main_window.function_input.setText("5*x^2 + 2*x")
    main_window.min_input.setText("10")
    main_window.max_input.setText("-10")

    qtbot.mouseClick(main_window.plot_button, Qt.LeftButton)

    assert isinstance(main_window.plot_button.clicked, type(main_window.plot_function))


if __name__ == "__main__":
    pytest.main()